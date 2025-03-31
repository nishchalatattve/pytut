# %%
import pandas as pd

df = pd.DataFrame({
    "name": ["John", "Lewis", "Chloe", "Steve"],
    "age": [23, 45, 31, 55],
    "score": [90, 88, 85, 90],
})
df
# %%
df["age"].mean()
# %%
df["score"].max()
# %%
df["score"].std()
# %%
df.to_csv("student_info.csv")
# %%
df = pd.read_csv("diffraction.csv")
df

# %%
import matplotlib.pyplot as plt

x = df.iloc[:, 0]
y = df.iloc[:, 1]
plt.plot(x, y)
plt.show()
# %%
