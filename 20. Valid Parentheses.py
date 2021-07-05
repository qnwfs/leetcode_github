def isValid(s):
    stack, match = [], {')': '(', ']': '[', '}': '{'}
    for ch in s: # проверяем каждый символ
        if ch in match: # если символ в словаре
            if not (stack and stack.pop() == match[ch]):
                """ если массив не пустой и из стэка, ключ которого закрывающая скобочка
                не выдается открытой скобки - отбой"""
                return False
        else:
            stack.append(ch)#добавляем в стэк
    return not stack

s = "()"
print(isValid(s))