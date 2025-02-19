# %%
import numpy as np
import random

rng = np.random.default_rng(1314)
# %%
# -------------------- Basic --------------------
# Refs: https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.random.html
rng.random((10,))
# %%
# Refs: https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.uniform.html#numpy.random.Generator.uniform
rng.uniform(size=(10,))
# %%
rng.uniform(8, 9, (10,))
# %%
# Refs: https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.integers.html
rng.integers(10, size=(10,))
# %%
# -------------------- Shuffle --------------------
# We first shuffle with numpy
a = [9, 4, 5, 3, 4, 5, 66, 4, 33, 344]
b = [9, 4, 5, 3, 4, 5, 66, 4, 33, 344]

rng.shuffle(a)
rng.shuffle(b)
# %%
a
# %%
b
# %%
# Now we shuffle with random
random.seed(1314)
a = [9, 4, 5, 3, 4, 5, 66, 4, 33, 344]
b = [9, 4, 5, 3, 4, 5, 66, 4, 33, 344]

random.shuffle(a)
random.shuffle(b)
# %%
a
# %%
b
# %%
