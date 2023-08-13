name = input('Escreva seu nome: ')
age = input('Escreva sua idade: ')
height = input('Escreva sua altura: ')

print('-----------------')

print(name, 'tem', age, 'anos e', height, 'm de altura')
print(name + ' tem ' + str(age) + ' anos e ' + str(height) + 'm de altura')

print('-----------------')

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

sum = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2

print(f'Ao somar {num1} e {num2}, o resultado é {sum}')
print(f'Ao subtrair {num1} e {num2}, o resultado é {sub}')
print(f'Ao multiplicar {num1} e {num2}, o resultado é {mult}')
print(f'Ao dividir {num1} e {num2}, o resultado é {div}')