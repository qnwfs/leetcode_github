def toGoatLatin(s):
    words = s.split()
    final = ''
    vowel = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    for i in range(len(words)):
        if words[i].startswith(vowel):
            words[i] += 'ma'
        else:
            words[i] += (words[i][0])
            words[i] += 'ma'
            words[i] = words[i][1::]
        words[i] += 'a' * (i+1)


    for i in words:
        final += i
        final += ' '

    return final[:-1]



s = "I speak Goat Latin"
print(toGoatLatin(s))
