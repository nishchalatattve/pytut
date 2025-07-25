# %%
import re
# %%
target = "ID A1.3"
# %%
pattern = r"\w"
re.findall(pattern, target)
# %%
pattern = r"\W"
re.findall(pattern, target)
# %%
pattern = r"\d"
re.findall(pattern, target)