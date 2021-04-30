from math import factorial

def generate(rows: int):
    triangle = []
    for i in range(rows):
        temp = []
        for j in range(i+1):
            temp.append(int(factorial(i)/(factorial(j)*factorial(i-j))))
        triangle.append(temp)
    return triangle

rows = 5
print(generate(rows))