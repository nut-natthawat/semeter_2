def gauss(A, B):
    n = len(A)
    M = [[1,0,0],[0,1,0],[0,0,1]]
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
        
A = [[2, 6, 1], [1, 2, -1], [5, 7, -4]]
B = [7, -1, 9]
gauss(A, B)