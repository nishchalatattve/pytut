"""Variable types"""
# %%
# ---------------- Simple ----------------
a: int = 99
a
# %%
b: float = 99.99
b
# %%
c: bool = True
c
# %%
d: str = 'h'
d
# %%
a: str = "hi"
a
# %%
e: complex = 1 + 2j
e
# %%
# ---------------- Composite ----------------
f = (9)
type(f)
# %%
f = (9,)
type(f)
# %%
g = [1, '1', 1.0, True]
g
# %%
a = {"hi": 99, "pussy": 88, "adiyogi": 128}
print(a.get("hii", '?'))
# %%
b = {"bhairavi": 9 == 11}
b.get("bhairavi", '?')