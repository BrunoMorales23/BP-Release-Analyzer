import os
import re

#1 At first instance, we show all the main presentation in console.

print(f"""Welcome to BP Release Analyzer
Please, drag the path of the '.bprelease' file you want to work on
Write K to Kill the process... """)
validation = False

#2 We ask the user for Input, in this case, we ask for an specific kind of file ('bprelease')
#and we ask to input 'K' in case user wants to exit

while validation == False:
    path = input("...")

    if path.find("bprelease") != -1 :
        validation = True
    elif os.path.exists(path):
        print(f"The file doesn't exists on declarated path... ")
    elif path.upper() == "K":
        exit()
    else:
        print(f"Please, drag a valid path... ")

#3 We take the XML value of uploaded file and save it in memory into 'content' variable

with open(path, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()
        print("Archivo cargado correctamente")

#4 We search for the values that are nested in between '<process name="' and 'version="'
#Turns that the name of the processes can be found in between those labels...

#4.1 We look for all the values that fulfill this condition
nombres = re.findall(r'<process name="(.*?)"\s+version="', contenido)

#4.2 Then we print the values and enumerate them so we can later work on selecting them as items
for i, nombre in enumerate(nombres, start=1):
    print(f"{i} - {nombre}")

total = i
print(total)
