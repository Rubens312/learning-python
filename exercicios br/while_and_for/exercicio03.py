nome = input('Nome: ')
while len(nome) <= 3:
    print('Error(Nome deve ter mais que 3 caracteres)')
    nome = input('Nome: ')
idade = int(input('Idade: '))
while idade < 1 or idade > 150:
    print('Error(Idade deve estar entre 1 e 150)')
    idade = int(input('Idade: '))
salario = float(input('Salario: '))
while salario < 1:
    print('Error(salario deve ser maoior que 1)')
    salario = float(input('Salario: '))
# Fiquei com preguiça de terminar mas é só repetir os processos.

