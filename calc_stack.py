# calc stack.py: Solicita um conjunto de números inteiros separados por um espaço e, em seguida, 
# imprime um stack com os números.
# 
# Depois, imprime os elementos um a um elevados a dois. Implemente a pilha utilizando a biblioteca deque.

from collections import deque

numeros = input()
numeros = numeros.split()

stack = deque()
for numero in numeros:
    stack.append(int(numero))

print(stack)

for _ in range(len(stack)):
    num = stack.pop()
    print(num**2)

    