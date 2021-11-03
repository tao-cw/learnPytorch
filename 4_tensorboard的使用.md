# 一、`tensorboard`有什么用？
1. 可以很好的展示训练过程中的数据情况。

# 二、`tensorboard`怎么用？
1. 首先肯定得有`tensorboard`这个包，可以使用`pip`获取
2. 需要利用`torch.utils.tensorboard`里得`SummeryWriter`类
3. 实例一个`SummeryWriter`的对象，可以给一些参数进行设置，可以参考这个类的文档字符串，例如设置事件日志的目录`writer = SummeryWriter('logs')`
4. 主要就是利用`writer`对象的`add_image`和`add_scalar`方法，一个可以处理图像，一个处理标量，对这两个方法的使用，可以参考他们的文档字符串，来进行参数的设置
5. 在前面都完成后，即正常生成了事件日志。可以在命令行进入项目目录，然后执行命令`tensorboard --logdir=logs --port=6007`，它会给我们运行一个本地服务器的样子，我们<kbd>ctrl</kbd>+单击，就会进入tensorboard给我们准备好的界面

# 三、别人写的示例
``` python
from torch.utils.tensorboard import SummaryWriter
import numpy as np
from PIL import Image

writer = SummaryWriter("logs")
image_path = "data/train/ants_image/6240329_72c01e663e.jpg"
img_PIL = Image.open(image_path)
img_array = np.array(img_PIL)
print(type(img_array))
print(img_array.shape)

writer.add_image("train", img_array, 1, dataformats='HWC')
# y = 2x
for i in range(100):
    writer.add_scalar("y=2x", 3*i, i)

writer.close()
```