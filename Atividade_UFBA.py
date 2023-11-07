# 1° Questão
'''
lista = []
for num in range(10):
    num = int(input('Numeros a serem adicionados: '))
    lista.append(num)
print(lista[:])
'''

# 2° Questão
'''
lista = []
for num in range(10):
    num = int(input('Numeros a serem adicionados: '))
    lista.append(num)
per = int(input('Número perguntado: '))
if per in lista:
    print(per)
else:
    print('Nuemro selecionado não presente na lista.')
'''

# 3° Questão 
'''
lista = [1,2,3,4,5]
media = 5
print(media)
'''

# 4° Questão
'''
soma = 0
maior = float('-inf')
menor = float('inf')
positivos = 0
negativos = 0
# Entrada de dados
for i in range(10):
    num = float(input(f'Digite o {i + 1}° número real: '))
    # Soma para média posterior
    soma += num
    # Condição para números maior e menor
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    # Condição para números positivos e negativos    
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
# Média
media = soma / 10

print(f'Media é igual: {media}')
print(f'Maior é igual: {maior}')
print(f'Menor é igual: {menor}')
print(f'O número de positivos são: {positivos}')
print(f'O número de negarivos são: {negativos}')
'''
# 5° Questão
'''
import math

# Função para calcular a norma de um vetor
def calcular_norma(vetor):
    norma = math.sqrt(sum(x ** 2 for x in vetor))
    return norma

# Função para calcular o vetor soma de três vetores
def vetor_soma(vetor1, vetor2, vetor3):
    soma = [x + y + z for x, y, z in zip(vetor1, vetor2, vetor3)]
    return soma

# Pedir ao usuário o tamanho dos vetores (N)
N = int(input("Digite o tamanho dos vetores: "))

# Inicializar os três vetores
vetor1 = []
vetor2 = []
vetor3 = []

# Pedir ao usuário os valores dos vetores
print("Digite os elementos do primeiro vetor:")
for i in range(N):
    elemento = float(input("Elemento {}: ".format(i + 1)))
    vetor1.append(elemento)

print("Digite os elementos do segundo vetor:")
for i in range(N):
    elemento = float(input("Elemento {}: ".format(i + 1)))
    vetor2.append(elemento)

print("Digite os elementos do terceiro vetor:")
for i in range(N):
    elemento = float(input("Elemento {}: ".format(i + 1)))
    vetor3.append(elemento)

# Calcular as normas dos três vetores
norma_vetor1 = calcular_norma(vetor1)
norma_vetor2 = calcular_norma(vetor2)
norma_vetor3 = calcular_norma(vetor3)

# Encontrar o vetor com a maior norma
vetor_maior_norma = None
maior_norma = 0

if norma_vetor1 > norma_vetor2 and norma_vetor1 > norma_vetor3:
    vetor_maior_norma = vetor1
    maior_norma = norma_vetor1
elif norma_vetor2 > norma_vetor1 and norma_vetor2 > norma_vetor3:
    vetor_maior_norma = vetor2
    maior_norma = norma_vetor2
else:
    vetor_maior_norma = vetor3
    maior_norma = norma_vetor3

print("O vetor com a maior norma é:", vetor_maior_norma)
print("A maior norma é:", maior_norma)

# Calcular o vetor soma dos três vetores
vetor_soma_resultado = vetor_soma(vetor1, vetor2, vetor3)

print("O vetor soma dos três vetores é:", vetor_soma_resultado)
'''
# 6° Questão
'''
clientes = []
while True:
    nome = input("Digite o nome completo do cliente: ")
    rg = input("Digite o RG do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    cliente = [nome, rg, cpf, telefone]
    clientes.append(cliente)
    continuar = input("Deseja cadastrar outro cliente? (s/n): ")
    if continuar.lower() != 's':
        break
print("Dados dos clientes cadastrados:")
for cliente in clientes:
    print("Nome: ", cliente[0])
    print("RG: ", cliente[1])
    print("CPF: ", cliente[2])
    print("Telefone: ", cliente[3])
    print()
'''
# 7° Questão
'''
lista = []
pares = []
for x in range(10):
    num = int(input('Digite o numero: '))
    if num % 2 == 0:
        pares.append(num)
        lista.append(num)
    else:
        lista.append(num)
print(lista[:])
print(len(pares))
'''
# 8° Questão
'''
def exibir_listas(pares, impares):
    print("Números Pares:", pares)
    print("Números Ímpares:", impares)
pares = []
impares = []

# Tamanho máximo de cada lista
tamanho_maximo = 5

while True:
    try:
        numero = int(input("Digite um número inteiro (ou qualquer outro valor para encerrar): "))
        
        if numero % 2 == 0:
            pares.append(numero)
            if len(pares) == tamanho_maximo:
                exibir_listas(pares, impares)
                pares = []  
        else:
            impares.append(numero)
        if len(impares) == tamanho_maximo:
            exibir_listas(pares, impares)
            impares = []  
    except ValueError:
        break
exibir_listas(pares, impares)
'''
# 9° Questão
'''
def calcular_nota(gabarito, respostas):
    nota = 0
    for i in range(len(gabarito)):
        if gabarito[i] == respostas[i]:
            nota += 0.5
    return nota
gabarito = ['A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B', 'C', 'D']
resultados = []

for _ in range(50):
    nome = input("Nome do aluno: ")
    respostas_aluno = []
    
    
    for i in range(20):
        resposta = input(f"Resposta da questão {i + 1}: ")
        respostas_aluno.append(resposta)
    
    nota_aluno = calcular_nota(gabarito, respostas_aluno)
    
    if nota_aluno >= 6.0:
        resultado = f"{nome} - APROVADO"
    else:
        resultado = f"{nome} - REPROVADO"
    
    resultados.append(f"{resultado} - Nota: {nota_aluno}")

for resultado in resultados:
    print(resultado)
'''
# 10° Questão
'''
def calcular_nota(gabarito, respostas):
    nota = 0
    for i in range(len(gabarito)):
        if gabarito[i] == respostas[i]:
            nota += 0.5
    return nota
gabarito = ['A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B', 'C', 'D']
resultados = []

for _ in range(50):
    nome = input("Nome do aluno: ")
    respostas_aluno = []
    
    
    for i in range(20):
        resposta = input(f"Resposta da questão {i + 1}: ")
        respostas_aluno.append(resposta)
    
    nota_aluno = calcular_nota(gabarito, respostas_aluno)
    
    if nota_aluno >= 6.0:
        resultado = f"{nome} - APROVADO"
    else:
        resultado = f"{nome} - REPROVADO"
    
    resultados.append(f"{resultado} - Nota: {nota_aluno}")

for resultado in resultados:
    print(resultado)
'''
# 11° Questão
'''
import sys
codigos = []
for x in range(15):
    num = int(input(f'Digite o codigo a ser adicionado {x + 1} : '))
    codigos.append(num)
process = int(input('Digite 0 para terminar o programa, Digite 1 para visualizar a lista na ordem direta ou Digite 2 para visualizar a lista na ordem inversa: '))
if process == 0:
    sys.exit
elif process == 1:
    print(codigos[:])
elif process == 2:
    for item in codigos[::-1]:
        print(item)
else:
    print("Houve um erro na execução do programa ")
'''
# 12° Questão
'''
def contar_elementos_no_intervalo(lista, a, b):
    contagem = 0
    for elemento in lista:
        if a <= elemento <= b:
            contagem += 1
    return contagem


a = int(input("Digite o valor de 'a': "))
b = int(input("Digite o valor de 'b': "))


N = int(input("Digite o tamanho da lista: "))
lista = []
for i in range(N):
    elemento = int(input(f"Digite o elemento {i+1}: "))
    lista.append(elemento)

quantidade_no_intervalo = contar_elementos_no_intervalo(lista, a, b)

print(f"A quantidade de elementos no intervalo [{a}, {b}] é: {quantidade_no_intervalo}")
'''