#Exemplo de Estrutura de decisão. Programa que identifica o valor do frete para o cliente.

Tipo_de_cliente = input("Você é usuário premium, ou comum?")
if Tipo_de_cliente == 'premium':
    print("O frete é grátis!")
else:
    valor = float(input)("Qual o valor do produto?") 
if valor < 50:
    print("O valor do frete, é R$ 40.00 ")
elif valor >= 50 and valor < 149:
    print("Frete = R$ 20.00")

