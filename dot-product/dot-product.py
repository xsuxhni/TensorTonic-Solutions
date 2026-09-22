import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """

    if len(x) != len(y):
        raise ValueError("Vectors must have the same length.")

    return float(np.dot(x,y))

    pass