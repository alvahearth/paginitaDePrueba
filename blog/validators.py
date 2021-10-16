from django.core.exceptions import ValidationError

# def validar_rut(value):
    
#     numeroi = str(value)

#     lista_numeros = []

#     contador = 2
#     for i in numeroi[7::-1]:
#         if contador > 7:
#             contador = 2
#         numero = contador * int(i)
#         contador += 1
#         lista_numeros.append(numero)

#     sumatoria = 0
#     for j in lista_numeros:
#         sumatoria += j

#     division = int(sumatoria / 11)
#     multiplicado = division * 11
#     final = 11 - (sumatoria - multiplicado)

#     if final != int(numeroi[8]):
#         raise ValidationError('rut inválido')
    
#     return value