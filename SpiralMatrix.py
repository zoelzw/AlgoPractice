from numpy import outer


def sprialOrder(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    res = []
    while len(matrix[0]) > 0:
        res.append(matrix[0])
        
    # for i in range(rows):
    #     for j in range(columns):
    #         res.append(matrix[i][j])



sprialOrder([[1,2,3],[4,5,6],[7,8,9]])

