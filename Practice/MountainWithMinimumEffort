def evalute(triangle):

    for row in range(len(triangle)-2,-1,-1):
        for col in range(len(triangle[row])):
            triangle[row][col] += min(triangle[row+1][col],triangle[row+1][col+1])
    return triangle[0][0]


def main():
    triangle = eval(input())
    result = evalute(triangle)
    print(result)
main()