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
git clone https://github.com/MingtianZ/vector_add.git
```


2. Navigate to the cloned directory:

```
cd vector_add
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
from vector_add import add_test

# Use the test function
add_test()
```

To use the `vector_add.gpu` package in your Python code, simply import the desired function from the package:

```python
from vector_add.gpu import vector_add
import numpy as np

vector_a = np.array([1.0, 2.0, 3.0, 4.0, 5.0], dtype=np.float32)
vector_b = np.array([5.0, 4.0, 3.0, 2.0, 1.0], dtype=np.float32)
result = np.empty_like(vector_a)

vector_add(vector_a, vector_b, result)

print("Vector A:", vector_a)
print("Vector B:", vector_b)
print("Result:", result)
```