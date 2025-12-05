#include <pybind11/pybind11.h>
#include <opencv2/opencv.hpp>
#include <pybind11/numpy.h>

namespace py = pybind11;

static cv::CascadeClassifier file;

bool loadCascade(const std::string& path){
    return file.load(path);
}

py::list detect(py::array_t<uint8_t> frameArray){
    if(file.empty()) throw std::runtime_error("drop your file xml");
    auto buf = frameArray.request();
    if(buf.ndim != 3 || buf.shape[2] != 3) throw std::runtime_error("expected format HxWx3(channels)");
    int h = buf.shape[0], w = buf.shape[1];
    cv::Mat frame(h, w, CV_8UC3, (unsigned char*)buf.ptr), gray;
    cv::cvtColor(frame, gray, cv::COLOR_BGR2GRAY);
    std::vector<cv::Rect> faces;
    file.detectMultiScale(gray, faces, 1.1, 7, 0, cv::Size(50, 50));
    for(const auto& face : faces) cv::rectangle(frame, face, cv::Scalar(0, 255, 0), 5);
    py::list out;
    py::dict d;
    for(const auto& face : faces){
        d["x1"] = face.x;
        d["y1"] = face.y;
        d["x2"] = face.x + face.width;
        d["y2"] = face.y + face.height;
        out.append(d);
    }
    return out;
}

PYBIND11_MODULE(optimize, m){
    m.doc() = "A highly efficient frame-receiving function for better performance.";
    m.def("detect", &detect, "Draw boxes if objects are found");
    m.def("loadCascade", &loadCascade, "load a pre-trained AI model", py::arg("path"));
}
