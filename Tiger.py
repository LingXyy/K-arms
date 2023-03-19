import torch
import  numpy as np

class Tiger:
    def __init__(self,initValue,distribution:torch.Tensor,nickName,time = 1,) -> None:
        super().__init__()
        self.value = initValue
        self.distribution = distribution
        self.time = time
        self.tag = nickName
    def update(self):

        reward = np.random.normal(self.distribution[0].item(),self.distribution[1].item(),1)
        self.value = (float)(self.time*self.value+reward)/(self.time+1)
        self.time += 1
        print("第 {} 次选择{}的奖励为{}，价值更新为{}".format(self.time,self.tag,reward,self.value))
    def getValue(self):
        return self.value