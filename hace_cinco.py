import datetime

hace_cinco = datetime.datetime.now() - datetime.timedelta(days=5)

print(hace_cinco.strftime("%d del %m de %y y el dia de la semana es %A"))