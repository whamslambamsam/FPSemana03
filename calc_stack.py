from collections import deque
stack = deque()

stackInput = input()
stackInput = stackInput.split(" ")

for x in stackInput:
    stack.append(x)
print(stack)

for y in list(stack):
    print(int(stack.pop())**2)