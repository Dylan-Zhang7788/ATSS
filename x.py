import torch
import numpy as np

pred = torch.tensor([[1,2,3,4],[5,6,7,8]])
x,y=pred.max(dim=1)
print(x)