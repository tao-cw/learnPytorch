import torch
import torchvision
from torch import nn

vgg16 = torchvision.models.vgg16(pretrained=False)
torch.save(vgg16.state_dict, "vgg16_method2.pth")