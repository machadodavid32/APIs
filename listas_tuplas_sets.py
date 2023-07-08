listas = [2, 5, 6, "oi"]
listas.append("David")
print(listas)
# listas podem ser modificadas.


tuplas = (3, 4, 6)
# tuplas não podem ser modificadas. Não funciona, por exemplo, a função append.
# ao adicionar um elemento a tupla usando como exemplo: tupla = +=(4, ) você estará criando uma nova tupla com os elementos adicionados.


set = {1, 3, 5, 7, 9}
# Não comporta valores repetidos e os valores são desodernados.
# podemos usar pra adicionar coisas a função add() > set.add(11)
set.add("David")
print(set)
