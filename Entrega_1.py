#uri 1001
a = int(input())
b = int(input())
x = (a+b)
print("X =", x)

#uri 1015

#ler primeiro ponto
ponto1 = input().split()
x1 = float(ponto1[0])
y1 = float(ponto1[1])

#ler o segundo ponto
ponto2 = input().split()
x2 = float(ponto2[0])
y2 = float(ponto2[1])

#Calculo da distancia
distancia = ((x2 - x1)**(2) + (y2 - y1)**(2))**(1/2)

print('{:.4f}'.format(distancia))


#uri 1069

qte = int(input())

for i in range(qte):
	linha = input()
	total = 0
	menor = 0
	for j in range(len(linha)):
		if(linha[j] == "<"):
			menor += 1
		if(linha[j] == ">" and menor > 0):
			total += 1
			menor -= 1

	print(total)


#uri 1078

n = int(input())

for i in range(1, 11):
    print('{} x {} = {}'.format(i, n, i*n))

