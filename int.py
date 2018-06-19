score = input("Cual fue el resultado de lapartida")

score = score.split("/")
score = list(map(int, score))

print(score)
