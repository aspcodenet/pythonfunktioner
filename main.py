def calculateVat(vara, pris):
    moms = 0.25        
    if vara == "Bok":
        moms = 0.07
    elif vara == "Restaurang":
        moms = 0.12
    momsen = pris * moms
    return momsen

# Prissättningssystemet som Admin anvädner
vara = input("Ange vara")
pris = float(input("Ange pris"))
momsen = calculateVat(vara,pris)








# Webb kunden användaren 
vara = input("Ange vara")
pris = float(input("Ange pris"))
moms = 0.25
momsen = calculateVat(vara,pris)









print("Mata in ett tal tack")
tal = int(input())

print("Mata in ett tal tack")
tal2 = int(input())

print("Mata in ett tal tack")
tal3 = int(input())

print("Mata in ett tal tack")
tal4 = int(input())


