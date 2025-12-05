from setuptools import setup, Extension
import pybind11

opencv_include = "/opt/homebrew/include/opencv4"
opencv_lib = "/opt/homebrew/lib"

ext = Extension(
    "optimize",
    sources=["optimize.cpp"],
    include_dirs=[
        pybind11.get_include(),
        opencv_include,
    ],
    library_dirs=[opencv_lib],
    libraries=[
        "opencv_core",
        "opencv_imgproc",
        "opencv_objdetect",
    ],
    language="c++",
    extra_compile_args=["-std=c++17"],
)

setup(
    name="optimize",
    version="1.0",
    ext_modules=[ext],
)
