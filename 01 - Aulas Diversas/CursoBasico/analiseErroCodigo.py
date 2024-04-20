nome = "Alex"

if nome == "João" or "Paulo" or "Marcos":
  print("Acesso Liberado!")
else:
  print("Acesso Negado!")
  

# Corrigindo 
# 1º Forma
if nome == "João" or nome == "Paulo" or nome =="Marcos":
  print("Parte 1 - Acesso Liberado!")
else:
  print("Parte 1 - Acesso Negado!")  
  
# 2º Forma - utilizando uma lista
if nome in ["João", "Paulo", "Marcus"]:
  print("Parte 2 - Acesso Liberado!")
else:
  print("Parte 2 - Acesso Negado!")   