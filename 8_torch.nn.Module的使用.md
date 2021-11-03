# `torch.nn.Module`有什么用？
1. 其定义了基本的框架，我们可以继承它，来实现我们自己的训练模型

# `torch.nn.Module`怎么用？
1. 首先新建自己的训练模型，继承`torch.nn.Module`，然后重写方法
2. 怎么重写，就要看我们怎么设计我们的训练模型吧

# 别人的实例
``` python
# -*- coding: utf-8 -*-
# 作者：小土堆
# 公众号：土堆碎念
import torch
from torch import nn


class Tudui(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input):
        output = input + 1
        return output


tudui = Tudui()
x = torch.tensor(1.0)
output = tudui(x)
print(output)
```

[torch.nn.Module docs](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)
