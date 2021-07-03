from random import randint

alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '*', '_', '+', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '_', '°', '<', '>', '£', '¢', '|')

password = input('Password: ')
values = []
for i in range(len(password)):
    index = randint(0, 76)
    values.append((password, alphabet[index]))

print('Criptographed password:', end=' ')
for char in values:
    print(char[1], end='')
print()

# Pensei agora como terminar essa ideia. Seguem notas abaixo
# Posso utilizar o pyautogui para modificar o texto em tela
# Preciso de alguma forma criar um gatilho com hotkey
# O pyautogui pega o texto, criptografa e substitui
# Devo alterar o código que fiz a fim de reutilizar
# Posso gerar sempre o mesmo output pro mesmo input
# Cada letra recebe um valor numérico
# Valor esse que passa por um conjunto de calculos
# após esses calculos são colocados todos os resultados em uma sequencia
# Essa sequência será dividida em partes com dois caracteres
# Ou seja uma sequência de vários pares
# Pares esses que podem ser números de 10 a 86
# Portanto itens maiores que 86 serão transformados na parte inteira de sua divisão por 3
# Assim definindo seu novo valor
# Após tudo isso os números seráo substituídos por caracteres presentes em uma lista.
# Esses números substituidos serão a senha criptografada
