import torch

def tensor_op(x: torch.Tensor, y: torch.Tensor, op: str) -> torch.Tensor:

    if op == 'add':
        return torch.add(x,y)
    elif op == 'multiply':
        return torch.multiply(x,y)
    elif op == 'matmul':
        return torch.matmul(x,y)
    elif op == 'power':
        return torch.pow(x,y)
    elif op == 'max':
        return torch.maximum(x,y)