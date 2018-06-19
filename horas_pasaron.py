import datetime

dia = int(input("Dia :"))
mes = int(input("Mes :"))
ano = int(input("Año :"))

fecha = datetime.datetime(year=ano, month=mes, day=dia)

tiempo_paso = datetime.datetime.now() - fecha

print(tiempo_paso.days*24)