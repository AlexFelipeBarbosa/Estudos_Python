## Alex Felipe Barbosa 18/04/2024
## 01 - Diferença Entre Lista, Tupla e Conjunto no Python


lista_produtos = ["iphone", "ipad", "airpod", "macbook"] # lista de informações
tupla_produtos = ("iphone", "ipad", "airpod", "macbook") # imutavel (não é possivel adicionar itens)
set_produtos   = {"iphone", "ipad", "airpod", "macbook"} # conjuntos (não tem uma ordem definida e não tem duplicados)


# Exemplo - Pegar o primeiro produto de cada item
print(lista_produtos[0])
print(tupla_produtos[0])
# print(set_produtos["iphone"]) (não é possivel, pois não tem uma ordem definida)
# Transformando o set em uma lista para poder pegar o item (lembrando que não tem ordem definida)
print(list(set_produtos)[0])


# Exemplo  - Adicionando valores
lista_produtos.append("apple watch")
set_produtos.add("apple watch")
print(lista_produtos)
print(set_produtos)
# A tupla é IMUTAVEL então não tem como adicionar valores 
print(tupla_produtos)


# Exemplo - Valores repetidos 
lista_produtos = ["iphone", "ipad", "airpod", "macbook", "macbook"] 
tupla_produtos = ("iphone", "ipad", "airpod", "macbook", "macbook") 
set_produtos   = {"iphone", "ipad", "airpod", "macbook", "macbook"} # aqui não vai duplicar
print('Verificando os duplicados!')
print(lista_produtos)
print(tupla_produtos)
print(set_produtos)


# Se eu quiser retirar os duplicados da minha lista é só transformar ela em um set
lista_produtos = list(set(lista_produtos))
print ('Nova lista de Produtos')
print(lista_produtos)
