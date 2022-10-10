import sys 

def mat_mul(N,mat,mat2):
    matrix = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N): 
                matrix[i][j] += mat[i][k] * mat2[k][j]
            matrix[i][j] %= 1000
    return matrix

def devide(N,B,mat): 
    if B == 1 :
        matrix = [[m%1000 for m in ma] for ma in mat]
        return matrix
    elif B == 2: 
        return mat_mul(N,mat,mat)
    else : 
        temp_mat = devide(N, B//2, mat)
        if B%2 == 0 :
            return mat_mul(N,temp_mat,temp_mat)
        else : 
            return mat_mul(N,mat_mul(N,temp_mat,temp_mat), mat)


if __name__ == "__main__" :
    N,B = map(int,sys.stdin.readline().split())
    matrix= [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    answer = devide(N,B,matrix)
    for a in answer:
        print(*a)


"""
2 1
1000 1000
1000 1000
30 36 42
66 81 96
102 126 150

400 232 64
822 617 412
244 2 760

3 3 
1 2 3
4 5 6
7 8 9

5 10
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1

2개 
30 36 42
66 81 96
102 126 150

4개
560 288 16
118 33 948
676 778 880
"""