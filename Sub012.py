#Conversor de Temperatura
#Solicite ao usuário uma temperatura em graus Celsius e converta-a para graus Fahrenheit (e vice-versa).

celsius = float(input('Digite a temperatura em graus Celsius: '))

def fahrenheit(a):
    b = (a * 9/5) + 32
    return b

print(f'\n{celsius}ºCelsius foi convertido para {fahrenheit(celsius)} ºFahrenheit')