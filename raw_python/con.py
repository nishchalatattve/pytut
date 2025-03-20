# %%
for i in range(9):
    print(i)
# %%
count = 0
while count < 9:
    print(count)
    count += 1
count = 0
# %%
import numpy as np

rng = np.random.default_rng()
a = rng.uniform(-10, 10)


if a < 5:
    print(f'{a} is less than 5')
elif a ==5:
    print(f'{a} is equal to 5')
else:
    print(f'{a} is greater than 5')
# %%
