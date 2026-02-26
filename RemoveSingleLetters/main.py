# import pandas as pd

# read in DupesRemoved.txt as a Python list
with open('DupesRemoved.txt', 'r') as f:
    lines = f.readlines()


# remove single-letter lines from lines
lines = [line for line in lines if len(line.strip()) > 1]

# save lines to SingleLettersRemoved.txt
with open('SingleLettersRemoved.txt', 'w') as f:
    f.writelines(lines)