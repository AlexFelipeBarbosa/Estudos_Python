from datetime import datetime

def validar_tipos(nome_produto: str,
                 quantidade_estoque: int,
                 preco_unitario: float,
                 disponivel_venda: bool,
                 data_validate: datetime):

  # Quero verificar se o nome do Produto é string
  if not isinstance(nome_produto, str):
    return False
  
  # Quero verificar se o quantidade estoque é int
  if not isinstance(quantidade_estoque, int):
    return False
  
  # Quero verificar se preco unitario é float
  if not isinstance(preco_unitario, float):
    return False
  
  # Quero verificar se o disponivel venda é boolean
  if not isinstance(disponivel_venda, bool):
    return False
  
  # Quero verificar se Data Validade é datetime
  if not isinstance(data_validate, datetime):
    return False        
  
  # Se todas as verificações estiverem corretas retorna True
  return True  