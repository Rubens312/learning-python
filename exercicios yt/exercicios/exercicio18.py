def function():
    catetooposto = float(input('Cateto oposto: '))
    catetoadjacente = float(input('Cateto Adjacente: '))
    hipotenusa = float(input('hipotenusa: '))
    sen = catetooposto/hipotenusa
    cos = catetoadjacente/hipotenusa
    tan = catetooposto/catetoadjacente
    print(f'O seno do angulo é: {sen}')
    print(f'O cosseno do angulo é: {cos}')
    print(f'A tangente do angulo é: {tan}')