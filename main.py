from  Tiger import Tiger
import numpy as np
import  torch
IterNum = 1000
epsison = 0.1
iter = 0
t1 = Tiger(988,torch.tensor([450,50]),'1号老虎机')
t2 = Tiger(988,torch.tensor([550,100]),'2号老虎机')
while iter < IterNum:
    print("第{}轮".format(iter))
    if t1.getValue() >= t2.getValue():
        print('{}价值大于{}'.format(t1.tag,t2.tag))
        x = np.random.rand()
        if x < epsison:
            t2.update()
            print('x={}由于随机性，选择{}'.format(x,t2.tag))
        else:
            t1.update()
            print('x={},选择{}'.format(x,t1.tag))
    else:
        print('{}价值大于{}'.format(t2.tag, t1.tag))
        x = np.random.rand()
        if x < epsison:
            print('x={}由于随机性，选择{}'.format(x, t1.tag))
            t1.update()
        else:
            t2.update()
            print('x={},选择{}'.format(x, t2.tag))
    iter += 1


