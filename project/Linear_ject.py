def display(A):
    n = len(A)
    for i in range(n):
        print('X',[i+1],'=',A[i])

def jordan(A,B):
    n = len(A)
    for i in range(n): 
        pivot = A[i][i]
        for j in range(n): 
             A[i][j] /= pivot
        B[i] /= pivot
        for k in range(n):
            if k != i:
                factor = A[k][i]
                for j in range(n):
                    A[k][j] -= factor * A[i][j]
                B[k] -= factor * B[i]

    X = [0] * n
    for i in range(n-1,-1,-1):
        X[i] = B[i]
    display(X)

def gauss(A, B):
    n = len(A)
    M = [[0]*n for i in range(n)]
    for i in range(n):
        M[i][i] = 1
    for i in range(n - 1):
        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]
            M[j][i] = factor
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
            B[j] -= factor * B[i]
            
    X = [0] * n
    for i in range(n - 1, -1, -1):
        X[i] = B[i] / A[i][i]
        for j in range(i - 1, -1, -1):
            B[j] -= A[j][i] * X[i]
    display(X)
    return A, M
        
import copy
def lu(A, B):
    n = len(A)
    Y = [0] * n
    X = [0] * n
    b_copy = copy.deepcopy(B)
    U, L = gauss(A, B)
    for i in range(n):
        Y[i] = b_copy[i]/L[i][i]
        for j in range(n):
            b_copy[j] -= (L[j][i]*Y[i])
    print('\n','L :\n','\n'.join(['\t'.join([str(cell) for cell in row]) for row in L]))
    print('\nY1 =',Y[0],' Y2 =',Y[1],' Y3 =',Y[2])     
            
    for i in range(n - 1, -1, -1):
        X[i] = Y[i] / U[i][i]
        for j in range(i - 1, -1, -1):
            Y[j] -= U[j][i] * X[i]
    print('\n','U :\n','\n'.join(['\t'.join([str(cell) for cell in row]) for row in U]))
    print('\nX1 =',X[0],' X2 =',X[1],' X3 =',X[2])
    
def inverse(A):
    n = len(A)
    B = [[1,0,0],[0,1,0],[0,0,1]]
    for i in range(n): 
        pivot = A[i][i]
        for j in range(n): 
            A[i][j] /= pivot
            B[i][j] /= pivot
        for k in range(n):
            if k != i:
                factor = A[k][i]
                for j in range(n):
                    A[k][j] -= factor * A[i][j]
                    B[k][j] -= factor * B[i][j]
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in B]))
     
    
row = int(input('Input size M:'))
col = int(input('Input size N:'))
A = []
B = []
for i in range(row):
    row = []
    for k in range(col):
        x = int(input(f'A[{i}][{k}] :'))
        row.append(x)
    y = int(input(f'input B[{i}] :'))
    B.append(y)
    A.append(row)
print(A,B)
print()
    
print('1)Gauss Elimination\n2)Gauss-Jordan Elimination\n3)ALU Method\n4)Inverse Matrix')
chioce = int(input('\nChoice Method 1-4 :'))
print()
if chioce == 1:
    print('Gauss Elinimation')
    gauss(A,B)
elif chioce == 2:
    print('Gauss-Jordan Elimination')
    jordan(A,B)
elif chioce == 3:
    print('ALU')
    lu(A,B)
elif chioce == 4:
    print('Inverse Matrix')
    inverse(A)
else:
    print('Erorrrrrrrrrrrrrrrrr')