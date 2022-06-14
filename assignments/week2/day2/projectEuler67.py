def get_triangle(filename):
	#creates 2D array from input
	triangle = [[int(number) for number in row.split()] for row in open(filename)]
	return triangle


tri_array = get_triangle('./triangle.txt')

print(tri_array)

def maximize_triangle(triangle, start_idx=-1):
	#first element at -len(triangle)
    if start_idx == -len(triangle):
    	return triangle[0][0]
    for index in range(len(triangle[start_idx]) - 1):
        maximum = max(triangle[start_idx][index], triangle[start_idx][index + 1])
        triangle[start_idx - 1][index] += maximum
    return maximize_triangle(triangle, start_idx - 1)

x = maximize_triangle(tri_array)
print(x)
