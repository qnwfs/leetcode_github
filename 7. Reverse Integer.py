def reverse(x):
    total = ''
    x = str(x)
    if '-' in x:
        total += '-'
    for i in x[::-1]:
        if i != '-':
            total += i
    if total[0] == '0' and len(total) != 1:
        return int(total[1::]) if -2147483648 <= int(total[1::]) <= 2147483647 else 0
    else:
        return int(total) if -2147483648 <= int(total) <= 2147483647 else 0

x = 1534236469
print(reverse(x))