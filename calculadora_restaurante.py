# Nome: Jeniffer Sousa
# Atividade: Calculadora de Conta de Restaurante

# Preços
hamburguer = 20.00
refrigerante = 6.00
batata = 12.00

# Quantidades
qtd_hamburguer = 2
qtd_refrigerante = 3
qtd_batata = 1

# Subtotais
subtotal_hamburguer = qtd_hamburguer * hamburguer
subtotal_refrigerante = qtd_refrigerante * refrigerante
subtotal_batata = qtd_batata * batata

# Total
total = subtotal_hamburguer + subtotal_refrigerante + subtotal_batata

# Taxa de serviço
taxa_servico = total * 0.10
total += taxa_servico

# Gorjeta extra
gorjeta = "sim"

if gorjeta == "sim":
    valor_gorjeta = 10.00
    total += valor_gorjeta

# Divisão da conta
pessoas = 5

# Desconto
if pessoas > 4:
    desconto = total * 0.05
    total -= desconto
    print(f"Desconto aplicado: R$ {desconto:.2f}")

# Mensagem
if total > 200:
    print("Conta acima de R$ 200,00!")
else:
    print("Conta abaixo de R$ 200,00!")

valor_por_pessoa = total / pessoas

print("\n----- RESUMO DA CONTA -----")
print(f"Hambúrgueres: R$ {subtotal_hamburguer:.2f}")
print(f"Refrigerantes: R$ {subtotal_refrigerante:.2f}")
print(f"Batatas: R$ {subtotal_batata:.2f}")
print(f"Taxa de serviço: R$ {taxa_servico:.2f}")
print(f"Total da conta: R$ {total:.2f}")
print(f"Valor por pessoa: R$ {valor_por_pessoa:.2f}")
