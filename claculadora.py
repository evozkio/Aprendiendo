operacion = input("Que operacion quieres realizar (multiplicar/dividir/sumar/restar): ")
primer_numero = int(input("Primer numero: "))
segundo_numero = int(input("Segundo numero: "))

if operacion == "multiplicar":
    calculo = primer_numero*segundo_numero
    print("{} x {} = {}".format(primer_numero,segundo_numero,calculo))
elif operacion == "dividir":
    calculo = primer_numero/segundo_numero
    print("{} / {} = {}".format(primer_numero,segundo_numero,calculo))
elif operacion == "sumar":
    calculo = primer_numero+segundo_numero
    print("{} + {} = {}".format(primer_numero,segundo_numero,calculo))
elif operacion == "restar":
    calculo = primer_numero-segundo_numero
    print("{} - {} = {}".format(primer_numero,segundo_numero,calculo))
else:
    print("Error")