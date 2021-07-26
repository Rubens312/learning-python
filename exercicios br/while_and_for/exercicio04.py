A = 80000
B = 200000
i = 0

while B > A:
    i += 1
    A = A + A*3/100
    B = B + B*1.5/100

print(f'{A}, {B}, {i}anos')