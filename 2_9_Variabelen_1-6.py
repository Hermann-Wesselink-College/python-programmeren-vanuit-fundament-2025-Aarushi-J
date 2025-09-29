# opdrachten 1 tot en met 6 van paragraaf 2.9
# opdracht 1
totaalprijs = 30.99
kortingbon = 10.99
nieuwprijs = totaalprijs - kortingsbon
print(nieuwprijs)

# opdracht 2
cijfer1 = 9.5
cijfer2 = 7.5
gemiddelde = (cijfer1 + cijfer2)/2
print(gemiddelde)

# opdracht 3
totaalprijs = float(input('Totaalprijs van de producten:'))
verzendkosten = 3.95
teBetalen = totaalprijs + verzendkosten
print('Totaalprijs: ' + str(totaalprijs) + 'EUR.')
print('verzendkosten: ' + str(verzendkosten) + 'EUR.')
print('Totaal: ' + str(teBetalen) + 'EUR.')

#opdracht 4
totaalprijs = float(input('Totaalprijs van de producten:'))
verzendkosten = 3.95
teBetalen = totaalprijs + verzendkosten
print('Totaalprijs: ' + str(totaalprijs) + 'EUR.')
print('verzendkosten: ' + str(verzendkosten) + 'EUR.')
print('Totaal: ' + str(teBetalen) + 'EUR.')

# opdracht 5
bedrag = float(input('Voer een bedrag in euros '))
wisselkoers = 1.1746
prijsDollar = bedrag * wisselkoers
print('$' + str(prijsDollar))

# opdracht 6
totaalPrijs = float(input('Geef een totaalprijs: '))
kortingsPercentage = float(input('Geef een kortingspercentage: '))
nieuwprijs = (1 - (kortingsPercentage/100)) * totaalPrijs
print(nieuwprijs)