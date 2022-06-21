def sprialOrder(matrix):
    res = []
    rows,cols = len(matrix),len(matrix[0])
    left,right,top,bottom = 0,cols-1,0,rows-1
    while left <= right and top <= bottom:
        #top row left to right
        for col in range(left,right+1):
            res.append(matrix[top][col])
        top += 1 
        #right col top to bottom 
        for row in range(top,bottom+1):
            res.append(matrix[row][right])
        right -= 1 
        #bottom row right to left 
        for col in range(right,left-1,-1):
            res.append(matrix[bottom][col])
        bottom -= 1 
        #left col bottom to top 
        for row in range(bottom,top-1,-1):
            res.append(matrix[row][left])
        left += 1 
    return res[:rows*cols]




print(sprialOrder([[1,2,3],[4,5,6],[7,8,9]]))

