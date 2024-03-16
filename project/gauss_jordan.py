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
    for i in range(n):
        X[i] = B[i]
        print("X",[i+1],"=",X[i])
        
A = [[1,-1,-1,-1],[-2,4,3,0],[0,-4,2,3],[2,2,0,-5]]
B = [2,-3,-1,5]
jordan(A,B)