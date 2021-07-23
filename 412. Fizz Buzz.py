def fizzBuzz(n: int):
    answer = []
    for i in range(1, n+1):
        three = False
        five = False
        if (int(i) % 10) % 5 == 0:
            five = True
        summa = 0
        for j in str(i):
            summa += int(j)
        if summa % 3 == 0:
            three = True
        if three and five:
            answer.append("FizzBuzz")
        elif three:
            answer.append("Fizz")
        elif five:
            answer.append("Buzz")
        elif not three and not five:
            answer.append(str(i))
    return answer


n = 3
print(fizzBuzz(n))
