# %%
import numpy as np
import pandas as pd
# %%
rng = np.random.default_rng()
# %%
# ------------------------------ Index and DataFrames -------------------
# Basic DataFrame creation
df = pd.DataFrame({
    "time" : pd.date_range("2024-12-12 11:53:00", periods=10, freq="min"),
    "voltage": rng.integers(10, size=(10,)),
    "current": rng.integers(10, size=(10,))**2,
})
df
# %%
# DataFrame with index
df2 = pd.DataFrame({
    "voltage": rng.integers(10, size=(10,)),
    "current": rng.integers(10, size=(10,))**2,
}, index=pd.date_range("2024-12-12 11:53:00", periods=10, freq="min"))
df2
# %%
# Different ways to set index
df.set_index("time", inplace=True)
df
# %%
# Setting index name
df2.index.name = "time"
df2
# %%
# Multi index
array = [
    ["Falcon", "Falcon", "Parrot", "Parrot"],
    ["Captive", "Wild", "Captive", "Wild"]
]
index = pd.MultiIndex.from_arrays(array, names=("Animal", "Type"))
df = pd.DataFrame({
    "Max Speed": [390., 350, 30., 20.],
}, index=index)
df
# %%
# ---------------------------------- Access -------------------
df["voltage"]
# %%
df.voltage
# %%
df.iloc[0]
# %%
df.iloc[0, 0]
# %%
# ---------------------------------- Renaming -------------------
df.rename(columns={"voltage": 'V', "current": 'I'}, inplace=True)
df
# %%
df.columns = ["Voltage", "Current"]
df
# %%
# ---------------------------------- Timeseries ----------------------------------
N = 50
data_range = pd.date_range("2015-04-06", periods=N, freq="ME")
data_range
# %%
df = pd.DataFrame({
    "count": rng.integers(10, size=(N,)),
}, index=data_range)
df
# %%
df.resample('Y', origin="epoch").sum()













# %%
df.loc["2015-04-09", "count"] = 100
df.resample('Y').sum()
# %%
df.loc["2016-04-09", "count"] = 100
df.resample('Y').sum()
# %%
df.loc["2016-04-06", "count"] = 100
df.resample('Y').sum()
# %%
df.loc["2016-04-05", "count"] = 100
df.resample('Y').sum()
# %%
df.loc["2016-01-05", "count"] = 100
df.resample('Y').sum()
# %%
df.resample(pd.Grouper(freq='Y'), origin=pd.Timestamp("04-06")).sum()
# %%
