def checkAnagram(str1, str2):
    letras_str1 = list(str1)
    letras_str2 = list(str2)
    letras_str1.sort()
    letras_str2.sort()
    i = 0
    for letra in letras_str1:
        if letra is not letras_str2[i]:
            return False
        i = i + 1
    return True

print('Ingresar primer palabra: ')
str1=input()
print('Ingresar segunda palabra: ')
str2=input()
if checkAnagram(str1, str2):
    print('La palabra '+str1+' es un anagrama de '+str2)
else:
    print('La palabra '+str1+' no es un anagrama de '+str2)
