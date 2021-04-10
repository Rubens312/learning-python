hora = input('Insira o horario: ')
hora = hora.split(':')
print(f'Fazem {int(hora[0])*60 + int(hora[1])} minutos desde que o dia começou')