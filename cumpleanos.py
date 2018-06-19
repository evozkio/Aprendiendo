import datetime

dia = int(input("Dia nacimiento :"))
mes = int(input("Mes naciemiento :"))
ano = int(input("Año nacimiento :"))

cumpleanos = datetime.datetime(year=ano, month=mes, day=dia)

falta= cumpleanos - datetime.datetime.now()

print ("Falta {} dias para tu cumpleaños y sera {}".format(falta.days, cumpleanos.strftime("%A")))