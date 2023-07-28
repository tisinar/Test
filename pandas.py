import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

S=[5,6,7,8]
S



J=pd.Series(['A','V','F','K'])
p=(pd.Series([8,6,9,7,6,5]))
p
p1=pd.DataFrame(
  {
    'A':pd.date_range("20230101",periods=6,freq='M'),
    'B':pd.Series([8,6,9,7,6,5,])
    }
  )
p1

dt=pd.date_range("20230101",periods=6,freq='M')
dt
dx=pd.DataFrame(np.arange(12).reshape(4,3),columns=tuple('ABC'),index=list(range(5,9)))
dx

df2 = pd.DataFrame(
  { 
    "A": 1.0,
    "B": pd.Timestamp("20130102"),
    "C": pd.Series(1, index=list(range(4)), dtype="float32"),
    "D": np.array([3] * 4, dtype="int32"),
    "E": pd.Categorical(["test", "train", "test", "train"]),
    "F": "foo",
    }
  )
   
df2
tf= pd.DataFrame(np.random.randn(10, 4))    
tf     
     


ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))
ts 
ts = ts.cumsum()
ts
ts.plot(cmap='magma');
plt.show()
plt.plot(ts)
plt.show()

p1.plot();
plt.show()


pd.Series(p)


fy=r['iris']
fy
