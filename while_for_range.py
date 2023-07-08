criando_lista_com_range = list(range(10, 100, 20))# Aqui começa em dez, vai até 100 e vai de 20 em 20
print(criando_lista_com_range)
#criando_lista_com_range1 = list(range(10))
#print(criando_lista_com_range1)

carat = ["David"]
for caractere in carat:
    print(caractere)
      
pares = ([n for n in range(11) if n % 2 == 0])      # conseguindo uma lista de pares
print(pares)      

impares = ([n for n in range(11) if n % 2 == 1])  # conseguindo uma lista de impares
print(impares) 


