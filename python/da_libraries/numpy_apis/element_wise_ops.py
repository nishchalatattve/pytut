# %%
import numpy as np

rng = np.random.default_rng()
# %%
N = 200

a = np.zeros((N,)),
b = np.full((N,), 9)
c = np.full((N,), 3)
d = 7
e = rng.random((N,))
# %%
b + d
# %%
b * c
# %%
b * d
# %%
b * e
# %%
(b * e).shape
# %%
# Let's write our own broadcast add function
b = rng.random((10,))
a = rng.random((32, 10))


def broadcast_add(x, y):
    assert x.ndim == 2
    assert y.ndim == 1
    assert x.shape[-1] == y.shape[0]

    z = []
    for i in range(x.shape[0]):
        z.append(x[i] + y)
    return np.array(z)


c = broadcast_add(a, b)
c