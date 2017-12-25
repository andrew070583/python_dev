def max(*args):
    res = args[0]
    for val in args[1:]:
        if val > res:
            res = val
    return res

def mnim(*args):
    res = args[0]
    for val in args[1:]:
        if val < res:
            res = val
    return res

print(max(3, 5, 4))
print(min(3, 5, 4))
