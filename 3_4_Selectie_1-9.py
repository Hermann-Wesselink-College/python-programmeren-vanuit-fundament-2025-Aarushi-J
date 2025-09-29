# Opdrachten 1 tot en met 9 van paragraaf 3.4
# Opdracht 1
bedrag = 100
if bedrag > 150:
 print(bedrag * 1.19)
else:
 print(bedrag * 1.16)

# Opdracht 2
bedrag = 10
if bedrag > 150:
 print(bedrag * 1.19)
elif bedrag < 55:
 print(bedrag * 1.11)
else: 
 print(bedrag * 1.16)

# Opdracht 3
bedrag = float(input('Voer een bedrag in'))
if bedrag > 150:
 nieuwBedrag = bedrag * 1.19
 print(nieuwBedrag)
elif bedrag < 55:
 nieuwBedrag = bedrag * 1.11
 print(nieuwBedrag)
else: 
 nieuwBedrag = bedrag * 1.16
 print(nieuwBedrag)

# Opdracht 4
bedrag = float(input('Voer een bedrag in'))
if bedrag > 150:
 nieuwBedrag = bedrag * 1.19
 print('Na verhoging met 19% is de prijs: ' + str(nieuwBedrag))
elif bedrag < 55:
 nieuwBedrag = bedrag * 1.11
 print('Na verhoging met 11% is de prijs: ' + str(nieuwBedrag))
else: 
 nieuwBedrag = bedrag * 1.16
 print('Na verhoging met 16% is de prijs: ' + str(nieuwBedrag))

# Opdracht 5
spaargeld = int(input('Hoeveel spaargels heb je?'))
scooter = 1500
if scooter - spaargeld > 500:
 print('Je kunt beter een baantje gaan zoeken')
elif scooter - spaargeld <= 0:
 print('Je hebt genoeg geld om de scooter te kopen! ')
else:
 print ('Je hebt bijna genoeg geld, er is nog een klein beetje tekort')

# Opdracht 6
leeftijd = float(input('Wat is je leeftijd? '))
stempasOntvangen = input("Heb je een stempas ontvangen? (ja/nee)")

if leeftijd >= 16:
 print('Je mag praktijkexamen voor je scooterrijbewijs doen.')
else:
 print('Je mag geen praktijkexamen voor je scooterrijbewijs doen.')

if leeftijd >= 18:
 if stempasOntvangen == 'Nee.':
  print('Je mag niet stemmen, want je hebt (nog) geen stempas ontvangen!')
 else:
   print('Je mag stemmen.')
else:
 print('Je mag niet stemmen.')

# Opdracht 7
from datetime import datetime 
uur = datetime.now().hour

if uur < 6:
 print('Het is nacht')
elif uur < 12:
 print('Het is ochtend')
elif uur < 18:
 print('Het is middag')
else:
 print('Het is avond')

# Opdracht 8
from datetime import datetime
uur = datetime.now().hour
tempratuur = 25
luchtvochtigheid = 75

if uur < 8 or uur <= 17:
 print('Airco uit')
else:
 if tempratuur < 20 and luchtvochtigheid < 85:
  print('Airco uit')
 else:
  print('Airco aan')

# Opdracht 9
# ?