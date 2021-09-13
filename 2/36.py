casa = float(input("Valor da casa :€"))
salário =float(input("Salário do comprador:€"))
anos= int(input("Quantos anos de financiamento?"))
prestação= casa / (anos * 12)
mínimo = salário * 30 / 100
print ("Para pagar uma casa de €{:.2f} em {} anos".format(casa,anos), end="")
print(" a prestação será de €{:.2f}".format(prestação))
if prestação <= mínimo :
    print("Empréstimo pode ser ACEITE!")
else:
    print("Empréstimo NEGADO!")

