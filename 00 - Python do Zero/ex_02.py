from datetime import datetime

nome_produto: str = 'Mesa de Escritório'
quantidade_estoque: int = 10
preco_unitario: float = 450.0
disponivel_venda: bool = True
data_validade: datetime = datetime(2024,12,31)

print(data_validade)
print(type(data_validade))


for dia in range(1,11): # Criar o dia [1,2,3,4,5,6,7,8,9,10]
  print(f" Dia: {dia}")
  quantidade_estoque = quantidade_estoque -1
  print(f"Quantidade de estoque: {quantidade_estoque}")
  
  
  if quantidade_estoque <= 5:
    print('Estoque BAIXO! - Comprar mais Estoque')
  else:
    print('Estoque suficiente!')
    
print('Esse bloco')


# Tempo do video: 1:17:36