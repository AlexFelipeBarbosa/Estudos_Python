faturamento = 1200
custo = 712
lucro = faturamento - custo
margem_lucro = lucro / faturamento

print(faturamento)
print(custo)
print(lucro)

print("Faturamento da empresa: {}, Custo: {}, Lucro {} ".format(faturamento, custo, lucro))
print(f"Faturamento da empresa: {faturamento}, Custo: {custo}, Lucro {lucro}")


### Manipulando TEXTOS
email_cliente = "qualquercoisaaleatoria@gmail.com"

# Maiuscula
email_cliente = email_cliente.upper()
print(email_cliente)

#Minuscula
email_cliente = email_cliente.lower()
print(email_cliente)

# Encontrando o "@"
print(email_cliente.find("@")) # retorna -1 quando não encontrado

# Tamanho do texto
print(len(email_cliente))

# Pegar um caractere
print(email_cliente[0])

# pegar o ultimo caractere
print(email_cliente[-1])

# pegar um "pedaco" do texto
print(email_cliente[:10]) # até o 10

# pegar o pedaço antes do "@"
caractere = email_cliente.find("@")
print(email_cliente[:caractere])
# pegar o pedaço depois do "@"
print(email_cliente[caractere:])

# Trocar um pedaço do texto  - neste exemplo trocar o provedor do email
novo_email = email_cliente.replace("gmail.com", "yahoo.com.br")
print(novo_email)


nome = "alex barbosa"
print(nome.capitalize()) # somente a primeira letra maiuscula 
print(nome.title())  # deixa a primeira letra da palavra em maiuscula


# Pegar o servidor do email
servidor_email = email_cliente[email_cliente.find('@') + 1:]
print(servidor_email)

# Pegar o primeiro nome
primeiro_nome = nome[:nome.find(" ")]
print(primeiro_nome)

# Pegar o sobrenome
sobrenome = nome[nome.find(" ") + 1:]
print(sobrenome)

# Casos especiais - formatações numéricas em texto
margem_lucro = round(margem_lucro,2)
print(f"Faturamento da empresa: R$ {faturamento:.2f}, Custo: R$ {custo:.2f}, Lucro: R$ {lucro:.2f}, Margem: {margem_lucro:.1%}")