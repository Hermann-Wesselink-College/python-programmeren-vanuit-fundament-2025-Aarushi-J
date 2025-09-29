# Opdracht 1 tot en met 7 van pragraaf 2.10
# Opdracht 1
from datetime import datetime
datum = datetime.now()
maand = datum.month
print(str(maand))

# Opdracht 2
from datetime import datetime
datum = datetime.now()
dag = datum.day
print(str(dag))

# Opdracht 3
from datetime import datetime
datum = datetime.now()
dag = datum.day
maand = datum.month
jaar = datum.year
print(str(dag) + '-' + str(maand) + '-' + str(jaar))

# Opdracht 4
from datetime import datetime
datumtijd = datetime.now()
minuut = datumtijd.minute
print(str(minuut))

# Opdracht 5
from datetime import datetime
datumtijd = datetime.now()
minuut = datumtijd.minute
uur = datumtijd.hour
print(str(uur) + ':' + str(minuut))

# Opdracht 6
from datetime import datetime
datuntijd = datetime.now()
minuut = datetime.minute
uur = datetime.hour
dag = datetime.day
maand = datumtijd.month
jaar = datumtijd.year
datum = str(dag) + '-' + str(maand) + '-' + str(jaar)
tijd = str(uur) + ':' + str(minuut)
print('De datum van vandaag is  ' + datum + '. Het is nu '' + tijd + '.')

# opdracht 7
#a
