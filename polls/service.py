import re

def regular_streings(a,b):
    match = re.search(rf'{a}', rf'{b}')
    return match