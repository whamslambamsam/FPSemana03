from collections import deque

palavras = input()
palavras = palavras.split()

queue = deque()
for palavra in palavras:
    queue.append(palavra)

print(queue)

for word in queue:
        if "o" in word:
            print(word)
        else:
            continue