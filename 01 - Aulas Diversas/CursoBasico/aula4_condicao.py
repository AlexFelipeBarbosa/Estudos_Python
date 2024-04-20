vendas = 1500
meta = 1300

# Comparadores no Python
# > maior que 
# < menor que 
# >= maior ou igual
# <= menor ou igual
# == igual
# != diferente


if vendas > meta:
  print("Vendedor ganha bonus")
  print("Bateu a meta de vendas")
  bonus = 0.1 * vendas
  print("Bonus do Vendedor: ", bonus)
else: 
  print("Vendedor não ganha bonus")  
  print("Não bateu a meta de vendas")
  
print("Acabou o programa")  


# 2º Cenario
vendas = 2500
meta1 = 1300 # ganhar 10%
meta2 = 2000 # ganhar 13%

if vendas >= meta2:
  bonus = 0.13 * vendas
else:
  if vendas >= meta1:
    bonus = 0.1 * vendas
  else:
    bonus = 0
    
print("Bonus: ", bonus)    


# Segunda forma 
if vendas >= meta2:
  bonus = 0.13 * vendas
elif vendas >= meta1:
  bonus = 0.1 * vendas
else:
  bonus = 0
  
print("Segunda forma - Bonus: ", bonus)
  
  
lista_produtos = ["airpod", "ipad", "iphone", "macbook"]  
produto_procurado = input("Informe o produto: ")
produto_procurado = produto_procurado.lower()

if produto_procurado in lista_produtos:
  print("Produto no estoque")
else: 
  print("Não temos esse produto")
  
