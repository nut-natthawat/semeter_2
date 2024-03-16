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
    print(B)
    
A = [[1,2,3],[2,5,3],[1,0,8]]
inverse(A)