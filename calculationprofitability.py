#Valor inicial aplicado
vi=float(input("Valor inicial: "))

#Rentabilidade Mensa, em %
i=float(input("Rentabilidade mensal: "))

#Transformar porcentagem em valor numérico
i=i/100

#Tempo de investimento
m=int(input("Meses que vai deixar rendendo: "))

vf = vi * (1+i)**m

print('Valor após' ,m, 'meses: R$' , round(vf, 2))