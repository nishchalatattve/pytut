# %%
# loop over 2d list
a = [
    [2, 3, 4],
    [22, 33, 44],
]

for i in a:
    print(i)

len(a)
# %%
import numpy as np
a = np.arange(12, 1, -1)

for (i, val) in enumerate(a):
    print(i, val)
# %%
