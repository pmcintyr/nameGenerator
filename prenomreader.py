# importing modlue
from pandas import *

data = read_csv("patronymes.csv")
month = data['patronyme'].tolist()
print('Noms:', month)
textfile = open("prenomsList.txt", "w")
for element in month:
	try:
    		textfile.write(element + ", ")
	except Exception as e2:
		pass
textfile.close()
