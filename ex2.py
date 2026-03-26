import time
import os

contador = 10

while contador > 0:
    print(contador)
    time.sleep(1)
    contador -= 1;

os.system('cls' if os.name == 'nt' else 'clear')

print("Fogo")