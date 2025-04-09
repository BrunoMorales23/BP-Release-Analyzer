import os
import re

#0 We get Local Desktop path

#desktop = os.path.join(os.path.expanduser("~"), "Desktop")
desktop = "C:\\Users\\bmorales\\OneDrive - rmrconsultores.com\\Escritorio\\BP-Release-Analyzer"

#0 We create the function for deleting specific values from a Line. We're gonna use this quite a lot
def remove_selected_process(remove_value):
    lineas = content.splitlines()
    return [linea for linea in lineas if remove_value not in linea]

#0 This function, takes the value of the regex we put it in, and the value we're searching, and then uses the regex to search the provided value
#After that, it returns the first value obtained, which in this case, will be the ID of the process we're trying to remove from our Release.
def filter_selected_process_id(regex, content):
    processes_id = re.findall(regex, content, re.DOTALL)
    current_id = processes_id
    return current_id

#0 Lastly, this function merges the splitted lines back, so we have our main file back into one
def merge_splitted_lines(filter_lines):
    contenido_limpio = "\n".join(filter_lines)
    return contenido_limpio

#0 EXTRA - Delete Invalid Descriptions in script
def delete_content(regex, content):
     contenido_limpio = re.sub(regex, '', content, flags=re.DOTALL)
     return contenido_limpio

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
        content = archivo.read()
        print("Archivo cargado correctamente")

#4 We search for the values that are nested in between '<process name="' and 'version="'
#Turns that the name of the processes can be found in between those labels...

#4.1 We look for all the values that fulfill this condition

nombres = re.findall(r'<process name="(.*?)"\s+version="', content)

#4.2 Then we print the values and enumerate them so we can later work on selecting them as items
#We ask if our processes name's list is not equal to 'empty', if so, we continue with the instance of removing values from list
#in case our list is empty, means there're no more processes to remove from the list, and so, nothing else to work on...
validation = False

while validation == False:
    for i, nombre in enumerate(nombres, start=1):
        print(f"{i} - {nombre}")
    if nombres != []:
            remove_index = int(input("""Please, select which process you want to remove from release 
            If you're done, send '0'   """))
            if remove_index != 0: 
                    remove_index = remove_index - 1
                    print(nombres[remove_index] + " Removed")
                                            
                    #Step 1: Remove the line that contains the value of the list 'nombres' which user selected to delete
                    lineas_filtradas = remove_selected_process(nombres[remove_index])

                    #Step 2: Here, we filter the <object> ID value in order to obtain the specific <object-group> which contains our process
                    #regex = rf'<process name="{nombres[remove_index]}"\s+version="'
                    #regex = rf'<process id="(.*?)"\s+name="{nombres[remove_index]}"(.*?)(?=\s+xmlns="http://www.blueprism.co.uk/product/process">)'
                    regex = rf'<process id="(.*?)"\s+name="{nombres[remove_index]}"(.*?)(?=\s+xmlns="http://www.blueprism.co.uk/product/process">)'
                    current_id = filter_selected_process_id(regex, content)


                    regex = fr'<process[^>]*id="{re.escape(current_id[0][0])}"[^>]*name="{re.escape(nombres[remove_index])}"[^>]*>.*?</stage></process></process>'
                    #content = re.sub(regex, '', content, flags=re.DOTALL)
                    content = delete_content(regex, content)

                    #Step 3: We reutilize the def of Step 1 in order to remove all the lines that contain the ID value of the process we want to remove
                    lineas_filtradas = remove_selected_process(current_id[0][0])

                    #Step 4: Merge the splitted parts of the text back into one piece
                    content = merge_splitted_lines(lineas_filtradas)

                    del nombres[remove_index]
            else:
                validation = True
    else:
        validation = True
        pass

output_path = os.path.join(desktop, "archivo.bprelease")
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Archivo guardado en el Escritorio.")
