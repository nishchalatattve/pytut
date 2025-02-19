# %%
import numpy as np
# %%
# -------------------- Concatenate --------------------
a = np.array([
    [1, 2, 3],
    [4, 5, 6],
])

b = np.array([
    [11, 22, 33],
    [44, 55, 66],
])

c = np.vstack((a, b))
d = np.concatenate((a, b))
# %%
c
# %%
d
# %%
# -------------------- Understanding Axis --------------------
np.mean(a)
# %%
np.mean(a, axis=0)
# %%
np.mean(a, axis=1)
# %%
a = np.array([
    [
        [1, 2, 3],
        [4, 5, 6],
    ],
    [
        [11, 22, 33],
        [44, 55, 66],
    ],
])
# %%
np.mean(a)
# %%
np.mean(a, axis=0)
# %%
np.mean(a, axis=1)
# %%
np.mean(a, axis=2)
# %%
# --------------- Multiplication ----------------
# Element-wise
a * 9
# %%
# Copy arrays
e = [a] * 9
e
# %%
type(e)
# %%
e = np.concatenate(e)
e
# %%
# ------------- dot product -------------
# Refs: https://numpy.org/doc/stable/reference/generated/numpy.dot.html
# %%
common_dim = 3
a = np.full((3, 2, common_dim), 2)
b = np.full((3, common_dim, 2), 3)
# %%
a
# %%
b
# %%
c = np.dot(a, b)
c.shape
# %%
c
