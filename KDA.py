list_kda =[(6.0, 5.4),
           (3.7, 3.8),
           (6.3, 5.3),
           (18.0, 5.5),
           (1.3, 5.6),
           (3.3, 5.7),
           (5.2, 4.8),
           (4.4, 5),
           (3.2, 4.6),
           (1.9, 4.8)]
question = ""
contador = 0
total_score = 0
total_minions = 0
perfect = 1


def select_two(one, two, question):
    response = input(question)
    while response != one and response != two:
        response = input(question)
    return response


def calculated_dka(result):
    if result[1] == 0:
        result[1] = 1
    kda = (result[0]+result[2])/result[1]
    return round(kda)


def mean(lista, number):
    total = 0
    for valor in lista:
        total += valor[number]

    mean = total / (len(lista)+1)

    return mean


question = select_two("", "N", "Quieres seguir? ")

while question == "":


    score = input("Cual fue el resultado de lapartida")
    score = score.split("/")
    score = list(map(int, score))

    if score[1] == 0:
        perfect += 1

    minion = int(input("minions ?"))
    minutes = int(input("minutos de la partida?"))
    minion_x_minut = round(minion/minutes)

    list_kda.append((calculated_dka(score), minion_x_minut))

    question = select_two("", "N", "Quieres seguir? ")


print(mean(list_kda, 0))
print(mean(list_kda, 1))
print(perfect)
print(list_kda)