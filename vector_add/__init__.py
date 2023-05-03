import numpy as np
from .gpu import vector_add

def print_add(a,b):
    print(a-b)

def add_test():
    vector_a = np.array([1.0, 2.0, 3.0, 4.0, 5.0], dtype=np.float32)
    vector_b = np.array([5.0, 4.0, 3.0, 2.0, 1.0], dtype=np.float32)
    result = np.empty_like(vector_a)

    gpu.vector_add(vector_a, vector_b, result)

    print("Vector A:", vector_a)
    print("Vector B:", vector_b)
    print("A+B Result:", result)

def sub_test():
    vector_a = np.array([1.0, 2.0, 3.0, 4.0, 5.0], dtype=np.float32)
    vector_b = np.array([5.0, 4.0, 3.0, 2.0, 1.0], dtype=np.float32)
    result = np.empty_like(vector_a)

    gpu.vector_sub(vector_a, vector_b, result)

    print("Vector A:", vector_a)
    print("Vector B:", vector_b)
    print("A-B Result:", result)