import copy
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
        print("X",[i+1],"=",X[i])
    return A, M
        
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
    print('\n','L \n','\n'.join(['\t'.join([str(cell) for cell in row]) for row in L]))
    print('Y1 =',Y[0],' Y2 =',Y[1],' Y3 =',Y[2])     
            
    for i in range(n - 1, -1, -1):
        X[i] = Y[i] / U[i][i]
        for j in range(i - 1, -1, -1):
            Y[j] -= U[j][i] * X[i]
    print('\n','U \n','\n'.join(['\t'.join([str(cell) for cell in row]) for row in U]))
    print('X1 =',X[0],' X2 =',X[1],' X3 =',X[2])
       
A = [[2,1,1],[4,4,3],[8,10,13]]
B = [-3,-3,-45]
lu(A, B)