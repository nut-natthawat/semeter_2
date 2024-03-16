row = int(input('Input size M:'))
col = int(input('Input size N:'))

A = []
B = []
for i in range(row):
    row = []
    for k in range(col):
        x = int(input(f'A[{i}][{k}] :'))
        row.append(x)
    y = int(input(f'input B{[i]} :'))
    B.append(y)
    A.append(row)
    