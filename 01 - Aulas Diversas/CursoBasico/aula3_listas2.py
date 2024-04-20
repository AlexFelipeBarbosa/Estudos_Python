lista_produtos = ['iphone', 'airpod', 'ipad', 'macbook']


# adicionando um item na lista
lista_produtos.append("apple watch")
print(lista_produtos)

# remover um item da lista
lista_produtos.remove("apple watch")
print(lista_produtos)

# outra forma de remover (agora passando a posicao na lista)
lista_produtos.pop(0)
print(lista_produtos)

# editar um item
precos = [1000, 1500, 3500]
precos[0] = 6000
print(precos)

# pode ser uma valor calculado (neste exemplo aumento em 50%)
precos[0] = precos[0] * 1.5
print(precos)

# Contar quantas vezes um produto aparece na lista
lista_produtos = ['iphone', 'airpod', 'ipad', 'macbook', 'iphone']
print(lista_produtos.count('iphone'))
print(lista_produtos.count('ipad'))
print(lista_produtos.count('apple watch'))

# Ordenando a lista 
lista_produtos.sort() # ordem alfabetica
print(lista_produtos)

lista_produtos.sort(reverse=True) # ordem alfabetica "inversa"
print(lista_produtos)
