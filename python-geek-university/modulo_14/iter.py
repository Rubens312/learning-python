'''Não ficou exatamente claro para mim mas teentemos descrever o que entendi até agora
    Vamos lá, temos o iterable e o iterator

    O iterable retorna um objeto do tipo iterator utilizando a função iter()

    O iterator é segundo o professor um objeto que pode ser iteravel. o que isso sinifica? faço nem ideia.
    E quando é chamado pela função next() aparetemente retorna um dado por vez

    Vamos continuar e tentar entender.
'''

iteravel = 'Lasanha'
iteravel2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(iter(iteravel))
iteravel = iter(iteravel)
iteravel2 = iter(iteravel2)
print(next(iteravel))
print(next(iteravel))
print(next(iteravel))
print(next(iteravel))
print(next(iteravel))
print(next(iteravel))
print(next(iteravel))
print()
print(next(iteravel2))
print(next(iteravel2))
print(next(iteravel2))
print(next(iteravel2))
print(next(iteravel2))
print(next(iteravel2))
print(next(iteravel2))
print(next(iteravel2))
print(next(iteravel2))

'''Sendo bem sincero ele só ficou repetindo as palavras iterator e iteravel e o verbo iterar algumas vezes, então assim, explicação bem ruim. de 0 a 10 ele tirou -7

'''