import os

for x in range(10):
    print(x)
def new_gen():
    gen = []
    for x in range(10):
        gen[x].append([])
        for y in range(10):
            gen[x][y].append(0)
    print(gen)

new_gen()