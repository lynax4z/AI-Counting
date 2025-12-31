# AI-Counting

REQUIREMENTS — optimize.cpp (pybind11 + OpenCV, macOS M1/M2)

1. OS
- macOS

2. C++ Toolchain
- Xcode Command Line Tools
  > xcode-select --install
- Compiler: clang++
- C++ standard: C++17

3. Python
- Python 3.11 atau 3.12
- pip
- (opsional) venv

4. Python Build Tools
- setuptools
- wheel
  > python3 -m pip install -U pip setuptools wheel

5. pybind11
- Untuk C++ (headers):
  > brew install pybind11
- Untuk Python:
  > python3 -m pip install pybind11

6. NumPy
- Untuk komunikasi array Python ↔ C++
  > python3 -m pip install numpy

7. OpenCV (Python)
- Untuk camera, display, drawing di Python
  > python3 -m pip install opencv-python

8. OpenCV (C++)
- Untuk API OpenCV di optimize.cpp
  > brew install opencv
- Path Homebrew (Apple Silicon):
  - Headers: /opt/homebrew/include/opencv4
  - Libs:    /opt/homebrew/lib

9. macOS Security (WAJIB)
- xattr
- codesign
- Setelah build modul .so:
  > xattr -d com.apple.quarantine optimize*.so
  > codesign --force --sign - optimize*.so

END