# Alex Felipe Barbosa 18/04/2024

# 04 - 3 Estruturas Básicas de Python em Menos de 10 Minutos

vendas = 1000
meta = 1500

if vendas > meta:
  print("Vendedor bateu a Meta!")
else: 
  print("Vendedor NÃO bateu a Meta!")  
  
  
  
 # For  
vendas = [1500, 1600, 1700, 1278, 1274, 4494, 9996]


for venda in vendas:
  if venda > meta:
    print("Vendedor BATEU A META!", venda, meta)
  else: 
    print("Vendedor NÃO BATEU A META!!!", venda, meta)
 
 
# Funções
def analisar_meta_vendas(lista_vendas, meta):
  quantidade_bateu_meta = 0
  for venda in lista_vendas:
    if venda > meta:
      print(' - Vendedor bateu a meta!')
      quantidade_bateu_meta += 1
    else:
      print(" - Vendedor NÃO bateu a meta!")
  
  return quantidade_bateu_meta    
  
 
# Chamando a função
analisar_meta_vendas(vendas, meta)
 
qtde_bateu_meta = analisar_meta_vendas(vendas,meta)
print(qtde_bateu_meta)