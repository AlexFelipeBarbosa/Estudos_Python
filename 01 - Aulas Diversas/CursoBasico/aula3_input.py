# input
email = input('Escreva seu e-mail: ')
nome = input("Informe seu nome: ")
print(nome, email)

print(f"{nome}, verifique seu email: {email} que enviamos um link de confirmacao")


# O input sempre traz o valor no formato texto, quando for um numero será necessario converter para int ou float
faturamento = float(input("Informe o Faturamento: "))
imposto = faturamento * 0.1
print(imposto)

