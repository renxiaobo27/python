import numpy as np
import pandas as pd
from pandas import Series,DataFrame

df = DataFrame(np.arange(16).reshape(4,4))

blender = np.random.permutation(4)
print blender

print df.take(blender)

box = np.array([1,2,3])

shaker = np.random.randint(0,len(box),size=10)

hand_grabs = box.take(shaker)

print hand_grabs