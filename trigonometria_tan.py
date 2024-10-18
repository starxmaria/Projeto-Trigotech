import math

print("CÍRCULO TRIGONOMETRICO")
print("CALCULANDO A TANGENTE")

nome = input("digite seu nome: ")
angulo = float(input(f"olá {nome} digite o valor de um ângulo que deseja calcular: "))

tangente = math.tan(math.radians(angulo))
print(" A tangente de {:.0f} graus é : {:.1f} graus" .format(angulo,tangente))

