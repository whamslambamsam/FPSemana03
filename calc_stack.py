from collections import deque
stack = deque()

stackInput = input()
stackInput = stackInput.split(" ")

for x in stackInput:
    stack.appendleft(x)
print(stack)

for y in stack:
    print(int(y)**2)