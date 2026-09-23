import torch

def create_tensor(method: str, shape: list, value: float = 0.0) -> torch.Tensor:

    if method == 'zeros': A = torch.zeros(shape, dtype=torch.float32)

    elif method == 'ones': A = torch.ones(shape, dtype=torch.float32)

    else: A = torch.full(shape, value, dtype=torch.float32)

    return A
    
#    rows, columns = shape
   
    # if method == 'zeros':
    #     A = [[0.0] * columns] * rows

    # elif method == 'ones':
    #     A = [[1.0] * columns] * rows

    # else: A = [[value] * columns] * rows

    # return torch.tensor(A, dtype=torch.float32)
