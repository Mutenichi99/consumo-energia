# Valor fixo da energia (R$ por kWh)
preco_kwh = 0.75

# Solicita os dados ao usuário
nome = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho (em watts): "))
horas_dia = float(input("Digite o tempo médio de uso diário (em horas): "))

# Calcula o consumo mensal em kWh
consumo_mensal = (potencia * horas_dia * 30) / 1000

# Calcula o custo estimado
custo_estimado = consumo_mensal * preco_kwh

# Exibe o resultado
print("\n--- Resultado ---")
print(f"Aparelho: {nome}")
print(f"Consumo mensal: {consumo_mensal:.2f} kWh")
print(f"Custo estimado: R$ {custo_estimado:.2f}")