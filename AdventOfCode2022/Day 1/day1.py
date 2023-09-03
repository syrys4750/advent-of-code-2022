
file = open('adventofcode.com_2022_day_1_input.txt', 'r')
lista = file.readlines()
elfos = []
contador = 0
calorias_actuales = 0
max_calorias_lista = [0, 0, 0]
for calorias in lista:
    if(calorias == "\n"):
        contador += 1
        elfos.append(calorias_actuales)
        calorias_actuales = 0
    else:
        calorias_actuales += int(calorias)
elfos.append(calorias_actuales)
print(elfos)
elfos.sort(reverse=True)
print(elfos)
print(sum(elfos[:3]))