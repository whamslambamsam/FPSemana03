from collections import deque
stack = deque()
repeated = []

stackInput = input()
stackInput = stackInput.split(" ")

for x in stackInput:
    stack.append(x)
print(stack)

for y in list(stack):
    for z in y:
        if z == "o":
            if y in repeated:
                continue
            else:
                repeated.append(y)
                print(y)

# Conjunto de palavras, print ao queue; print palavras apenas com "o".