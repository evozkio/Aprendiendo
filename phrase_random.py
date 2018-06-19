import random
from time import sleep


list = ["hola mundo","como estamos","adios","Fumas?"]

sentence = None

while sentence != "FIN":
    sleep(3)
    sentence = random.choice(list)
    print(sentence)