#20.Ma trận dưới dạng list lồng nhau
matrix = [
   [1,2,3],
   [4,5,6],
   [7,8,9]
]
n = len(matrix) 
tong_cheo_chinh = 0 
tong_cheo_phu = 0
for i in range(n):
    tong_cheo_chinh += matrix[i][i]
    tong_cheo_phu += matrix[i][n - 1 - i]
    tuple_of_tuples = tuple(tuple(row) for row in matrix)
print(f"Tổng đường chéo chính: {tong_cheo_chinh}")
print(f"Tổng đường chéo phụ: {tong_cheo_phu}")
print("Ma trận dưới dạng tuple of tuples:",tuple_of_tuples)