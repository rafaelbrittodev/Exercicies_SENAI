#Calculadora de Distância
#Solicite ao usuário as coordenadas de dois pontos(x1, y1, x2, y2) e calcule a distância entre eles.
import  math

x0 = float(input('Digite o valor da posição X¹: '))
y0 = float(input('Digite o valor da posição Y¹: '))
x1 = float(input('Digite o valor da posição X²: '))
y1 = float(input('Digite o valor da posição X²: '))

def dist (x0, y0, x1, y1):
    a = (x1 - x0)**2 + (y1 - y0)**2
    b = math.sqrt(a)
    return b

print(f'A distância entre os pontos é {dist(x0, y0, x1, y1):.4f}')
