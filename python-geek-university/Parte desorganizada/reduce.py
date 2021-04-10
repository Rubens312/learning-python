import functools

test = [1,2,3,4]

res = functools.reduce(lambda x, y: x * y, test)

print(res)