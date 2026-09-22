import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)

    A = np.linalg.norm(a)
    B = np.linalg.norm(b)

    if A == 0.0 or B == 0:
        return 0.0

    else:
        return float(np.dot(a,b) / (A*B))
    
    pass