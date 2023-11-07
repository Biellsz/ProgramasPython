# 1° Questão

for x in range(1000,2001):
    y = x % 11 
    if y == 5:
        print(x,"->", y)

# 2° Questão 

n = int(input('Digite o número:'))
if n <= 0:
    print('Por favor digite um valor positivo.')
else:
    s = 0 
    for i in range(1, n+1):
        s += 1 / i
    
    print('A soma é:', s)


# 3° Questão

for x in range (1,10+1):
    for i in range (1, 10+1):
        tabuada = x * i
        print(x, "->", tabuada)


# 4° Questao
# 5° Questao

# 6° Questao

preco_ingresso = 5.00

preco_final = 1.00

passo = 0.50

despesas = 200.00

lucro_maximo = 0
preco_lucro_maximo = 0
qtd_vendidos_lucro_maximo = 0

while preco_ingresso >= preco_final:

    qtd_vendidos = 120 + (26 * (5.00 - preco_ingresso) / 0.50) 

    lucro = (preco_ingresso * qtd_vendidos) - despesas
    
    if lucro > lucro_maximo:
        lucro_maximo = lucro
        preco_lucro_maximo = preco_ingresso
        qtd_vendidos_lucro_maximo = qtd_vendidos
    print(f"Preço do Ingresso: R$ {preco_ingresso:.2f}, Quantidade Vendida: {qtd_vendidos}, Lucro: R$ {lucro:.2f}")
    
    preco_ingresso -= passo

print(f"\nLucro Máximo Esperado: R$ {lucro_maximo:.2f}")
print(f"Preço do Ingresso para o Lucro Máximo: R$ {preco_lucro_maximo:.2f}")
print(f"Quantidade de Ingressos Vendidos para o Lucro Máximo: {qtd_vendidos_lucro_maximo}")


# 7° Questao

idades = []
for x in range(10):
    ida = int(input('Digite a idade:'))
    if ida  >= 18:
        idades.append(ida)
print(len(idades))


# 8° Questao

faixa1 = []
faixa2 = []
faixa3 = []
faixa4 = []
faixa5 = []
idade = []

# Função de faixa etária
def faixa_etaria():
    for x in idade:
        if 0 < x <= 15:
            faixa1.append(x)
        elif 16 < x <= 30:
            faixa2.append(x)
        elif 31 < x <= 45:
            faixa3.append(x)
        elif 46 < x <= 60:
            faixa4.append(x)
        else:
            faixa5.append(x)
# Inserindo idades
for x in range(5):
    num = int(input(f'Digite a idade da pessoa {x+1}°:'))
    idade.append(num)
# Chamando a função
faixa_etaria()
# Percentual
p_f1 = len(faixa1)
p_f5 = len(faixa5)
total = len(idade)
calc = ((p_f1 + p_f5) / total) * 100
print(f'\nFaixa etária 1°: {faixa1}')
print(f'Faixa etária 2°: {faixa2}')
print(f'Faixa etária 3°: {faixa3}')
print(f'Faixa etária 4°: {faixa4}')
print(f'Faixa etária 5°: {faixa5}')
print(f'Percentual entre a 1° e a 5° Faixa etária em relação ao total: {calc:.2f}')

# 9° Questão

x = int(input('Digite o numero para tabuada: '))
for i in range(11):
    print(f'{i} -> {x * i}')

# 10° Questão

for x in range (1,10+1):
    for i in range (1, 10+1):
        tabuada = x * i
        print(x, "->", tabuada)

# 11° Questão

l_vista = []
l_prazo = []
v_total = []
def pagamento():
    for x in range(3):
        valor = float(input('Digite o valor da sua compra: R$ '))
        cod = input("Insira o código de pagamento: ")
        print('')
        v_total.append(valor)
        if cod == 'V' or cod == 'v': 
            l_vista.append(valor)
        elif cod == 'P' or cod == 'p':
            l_prazo.append(valor)

pagamento()
# Valor a vista
x = 0
for valor in l_vista:
    x += valor 
print(f'Total dos pagamentos à vista: R$ {x:.2f}')
# Valor a prazo
m = 0
for valor in l_prazo:
    m += valor
print(f'Total dos pagamentos á prazo: R$ {m:.2f}')
# Valor total
n = 0
for valor in v_total:
    n += valor
print(f'Total dos pagamentos: R$ {n:.2f}')
# Valor da 1° prestação
h = 0
for valor in l_prazo:
    h += valor
    calc = h / 3
    print(f'O valor da primeira parcela da compra R$ {valor:.2f} é R$ {calc:.2f}')

# 12° Questão


# 13° Questão

idade = []
peso = []
for x in range(7):
    ida = int(input(f'Digite a idade da {x+1}° pessoa: '))
    pes = float(input(f'Digite a quantidade de Kg da {x+1}° Pessoa: '))
    idade.append(ida)
    if pes > 90:
        peso.append(pes)
media = sum(idade) / len(idade)
print(f'Essa é a quantidade de pessoas acima de 90 Kg: {len(peso)}')
print(f'Essa é a media de idade das pessoas: {media}')

# 14° Questão

    