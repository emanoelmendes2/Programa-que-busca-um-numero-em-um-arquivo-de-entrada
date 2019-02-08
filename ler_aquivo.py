n=28
arq = open('dataset-1-b.csv', 'r')
arq1 = open('lista.txt', 'w')
texto = arq.readlines()
pos=0
for i in texto:
    print(i)
    if n==int(i):
        print('entrou')
        texto1='True'
        arq1.write(texto1)
        texto2=str(pos)
        arq1.write(texto2)
    pos=pos+1
texto1='False'
arq1.write(texto1)
texto2='-1'
arq1.write(texto2)
arq1.close()
arq.close()
