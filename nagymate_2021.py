lista = []
jovalaszok = ['BCCCDBBBBCDAAA']
f = open("valaszok.txt","r",encoding = "UTF-8")
megoldas = f.readline().rstrip()
for sor in f:
    sor = sor.strip().split()
    lista.append(sor)
f.close()
#print(lista)
print("1.feladat: fájl beolvasva eltárolva")
print("2.feladat: A versenyen",len(lista),"versenyző indult.")
try:
    azonosito = input('A versenyző azonosítója =')
except ValueError:
    print("Nincs ilyen kód!")
else:

    for sor in lista:
        if sor[0] == azonosito:
            valaszok = sor[1]
            print(sor[1], 'válaszok')

print('4. feladat:')
ki = ""
print(megoldas, ('(a helyes megoldás)'), )

for index in range(0, len(megoldas)):
    if valaszok[index] == megoldas[index]:
        ki = ki + '+'
    else:
        ki = ki + ' '
print(ki, '(a versenyző helyes válaszai)')

print('5. feladat:')
feladat = int(input('A feladat sorszáma ='))
jovalaszok = 0
for sor in lista:
    if sor[1][feladat - 1] == megoldas[feladat - 1]:
        jovalaszok = jovalaszok + 1
osszversenyzo = len(lista)
print('A feladatra', jovalaszok, 'fő, a versenyzők', round((jovalaszok / osszversenyzo) * 100, 2),
      '%-a adott helyes választ')

print('6.feladat: A versenyzők pontszámának meghatározása!')

f = open("pontok.txt", 'w', encoding='UTF-8')
pontok = []

for sor in lista:
    pontszamitas = 0
    for index in range(0, len(megoldas)):
        if sor[1][index] == megoldas[index] and index < 5:
            pontszamitas = pontszamitas + 3
        if sor[1][index] == megoldas[index] and index >= 5 and index < 10:
            pontszamitas = pontszamitas + 4
        if sor[1][index] == megoldas[index] and index >= 10 and index < 13:
            pontszamitas = pontszamitas + 5
        if sor[1][index] == megoldas[index] and index == 13:
            pontszamitas = pontszamitas + 6

    f.write(sor[0] + " " + str(pontszamitas) + '\n')

f.close()

print('7.feladat:')
pontozas = []
f = open('pontok.txt', 'r', encoding='UTF-8')
for sor in f:
    sor = sor.strip().split(' ')
    sor[1] = int(sor[1])
    pontozas.append(sor)
f.close()

# print(pontozas)

elso = 0
masodik = 0
harmadik = 0

szum = []

for sor in pontozas:
    if sor[1] > elso:
        elso = sor[1]

for sor in pontozas:
    if sor[1] < elso and sor[1] > masodik:
        masodik = sor[1]
for sor in pontozas:
    if sor[1] < elso and sor[1] < masodik and sor[1] > harmadik:
        harmadik = sor[1]

for sor in pontozas:  # 1. díj (56 pont): JO001
    if sor[1] == elso:
        print('1. díj ', '(', sor[1], ' pont): ', sor[0])

for sor in pontozas:
    if sor[1] == masodik:
        print('2. díj ', '(', sor[1], 'pont): ', sor[0])

for sor in pontozas:
    if sor[1] == harmadik:
        print('3. díj ', '(', sor[1], ' pont): ', sor[0])