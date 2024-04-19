# Alex Felipe Barbosa 18/04/2024

faturamento = 1200 
custo = 752.38
imposto = faturamento * 0.1 # 10%

lucro = faturamento - custo - imposto


margem_lucro = round(lucro / faturamento,2)


print ("Faturamento foi de: ", faturamento)
print('Custo foi de: ', custo)
print('O lucro foi de: ', lucro)
print("O imposto foi de: ", imposto)
print("A margem de lucro foi de: ", margem_lucro)


