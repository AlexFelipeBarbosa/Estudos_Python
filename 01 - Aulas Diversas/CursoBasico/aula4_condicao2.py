vendas = 2100
vendas_empresa = 30000
meta_empresa = 20000
meta1 = 1300 # ganhar 10%
meta2 = 2000 # ganhar 13%

if vendas >= meta2 and vendas_empresa >= meta_empresa:
  bonus = 0.13 * vendas
elif vendas >= meta1 and vendas_empresa >= meta_empresa:
  bonus = 0.1 * vendas
else:
  bonus = 0

print("Bonus: ", bonus)
