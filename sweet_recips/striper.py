def striper(texte):
    word = []    
    for letter in texte:
        if letter != "\n" and letter != "\t":
            word.append(letter)
    return "".join(word).strip()

a = '3\n\n\ng de sucre\n\n\n gg'
t = striper(a)
print(t)
