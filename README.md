# Vector Add GPU

This Python package provides a simple implementation of vector addition using CUDA for GPU acceleration. The package uses `nvcc` to compile the CUDA code in `.cu` files and provides a Python interface for calling the CUDA functions.

## Prerequisites

Before installing the package, please make sure you have the following software installed on your system:

- CUDA Toolkit (version 10.x or later)
- A supported version of Python (3.6 or later)
- NumPy

Additionally, make sure that the environment variable `OPENMM_CUDA_COMPILER` is set to the path of your `nvcc` binary, or that `nvcc` is available in your `PATH`.

## Installation

To install the package, follow these steps:

1. Clone the repository:

```
git clone https://github.com/yourusername/vector_add_gpu.git
```


2. Navigate to the cloned directory:

```
cd vector_add_gpu
```

3. Install the package using `pip`:

```
pip install .
```
Or install it in editable mode:
```
pip install -e .
```


## Usage

To use the `vector_add` package in your Python code, simply import the desired function from the package:

```python
from vector_add import some_function

# Use the function
result = some_function(...)
```