# %%
import re
# %%
target = "acacac abcabc, ab98c. a9c a?c a c"
# %%
# . Wildcard: Matches any single character except \n
pattern = r"a.c"
re.findall(pattern, target)
# %%
# ? Matches the previous element zero or one time.
pattern = r"a.?c"
re.findall(pattern, target)
# %%
# * Matches the previous element zero or more times.
pattern = r"a.*c"
re.findall(pattern, target)
# %%
# + Matches one or more occurrences of the previous element
pattern = r"a.+c"
re.findall(pattern, target)
# %%
# *? Matches the previous element zero or more times, but as few times as possible.
pattern = r"a.*?c"
re.findall(pattern, target)
# %%
# +? Matches the previous element one or more times, but as few times as possible.
pattern = r"a.+?c"
re.findall(pattern, target)
# %%
