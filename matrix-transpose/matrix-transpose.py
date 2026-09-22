import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    rows = len(A)
    cols = len(A[0])

    B = []

    for j in range(cols):
        new_rows = []
        for i in range(rows):
            new_rows.append(A[i][j])
        B.append(new_rows)

    return np.array(B, dtype=float)
    pass
