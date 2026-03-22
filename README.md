#  Calculadora de Consumo de Energia


##  Este projeto tem como objetivo calcular o consumo mensal de energia elétrica de um aparelho e estimar o custo com base no valor do kWh.

##  Linguagem utilizada
-  Python


##  Fórmula utilizada
O consumo mensal é calculado utilizando a fórmula:
    consumoMensal = (potencia * horasDia * 30) / 1000

Onde:
- **potência** = valor em watts (W)
- **horasDia** = tempo de uso diário
- **30** = dias do mês
- **1000** = conversão de W para kWh

O custo estimado é calculado por:
    custo = consumoMensal * preço_kWh


##  Exemplo de uso
  - Aparelho: Geladeira  
  - Potência: 150 W  
  - Uso diário: 10 horas  

Resultado:
  - Consumo mensal: ~45 kWh  
  - Custo estimado: R$ 33,75  


##  Badges

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![GitHub](https://img.shields.io/badge/GitHub-Repository-black?logo=github)
![Energia](https://img.shields.io/badge/Energia-Consumo-yellow)
