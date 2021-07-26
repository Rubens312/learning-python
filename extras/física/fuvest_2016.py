'''
Eu tenho 3 velocidades médias em três trechos de mesmo tamanho
No primeiro trecho ele percorre com a velocidade de 60km/h
No segundo com 40km/h
No terceiro com 20km/h

Um jeito de solucionar isso é definir um valor default para uma função que calcula velocidade média
'''


first_speed = 60
second_speed = 40
third_speed = 20
distance = 60

def return_time(distance, speed):

    return distance/speed

total_time = return_time(distance, first_speed) + return_time(distance, second_speed) + return_time(distance, third_speed)
final_speed = 3 * distance / total_time
print(f'A velocidade média de todo o percuso foi de {final_speed}')