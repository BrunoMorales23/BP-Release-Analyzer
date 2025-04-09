import os
import configparser
import re
from colorama import Fore, Style, init
init(autoreset=True)

#desktop = os.path.join(os.path.expanduser("~"), "Desktop")
desktop = "C:\\Users\\bmorales\\OneDrive - rmrconsultores.com\\Escritorio\\BP-Release-Analyzer"

config = configparser.ConfigParser()
config.read('config.ini')

def remove_selected_process(remove_value):
    lineas = content.splitlines()
    return [linea for linea in lineas if remove_value not in linea]

def filter_selected_process_id(regex, content):
    processes_id = re.findall(regex, content, re.DOTALL)
    current_id = processes_id
    return current_id

def merge_splitted_lines(filter_lines):
    contenido_limpio = "\n".join(filter_lines)
    return contenido_limpio

def delete_content(regex, content):
     contenido_limpio = re.sub(regex, '', content, flags=re.DOTALL)
     return contenido_limpio


print(Fore.GREEN + f"""Welcome to BP Release Analyzer
Please, drag the path of the '.bprelease' file you want to work on""" +
Fore.RED + """ 
Write K to Kill the process... """)
validation = False


while validation == False:
    path = input("...")

    if path.find("bprelease") != -1 :
        validation = True
    elif os.path.exists(path):
        print(Fore.RED + f"The file doesn't exists on declarated path... ")
    elif path.upper() == "K":
        exit()
    else:
        print(Fore.RED + f"Please, drag a valid path... ")


with open(path, 'r', encoding='utf-8') as archivo:
        content = archivo.read()
        print(Fore.GREEN + "Archivo cargado correctamente")

nombres = re.findall(r'<process name="(.*?)"\s+version="', content)

validation = False

while validation == False:

    for i, nombre in enumerate(nombres, start=1):
        print(Fore.YELLOW + f"{i} - "+ Fore.WHITE + f"{nombre}")
    if nombres != []:
            remove_index = int(input(Fore.YELLOW + """Please, select which Process or Object you wish to remove from release """ +
            Fore.RED + """ 
If you're done, write '0'   """))
            if remove_index != 0: 
                    remove_index = remove_index - 1
                    try:                        
                        lineas_filtradas = remove_selected_process(nombres[remove_index])

                        regex = rf'<process id="(.*?)"\s+name="{nombres[remove_index]}"(.*?)(?=\s+xmlns="http://www.blueprism.co.uk/product)'
                        current_id = filter_selected_process_id(regex, content)


                        regex = fr'<process[^>]*id="{re.escape(current_id[0][0])}"[^>]*name="{re.escape(nombres[remove_index])}"[^>]*>.*?</stage></process></process>'
                        content = delete_content(regex, content)

                        print(Fore.GREEN + "----Deleting an Process----")
                        lineas_filtradas = remove_selected_process(current_id[0][0])

                        content = merge_splitted_lines(lineas_filtradas)

                    except IndexError:
                        print(Fore.GREEN + "----Deleting an Object----")
                        lineas_filtradas = remove_selected_process(nombres[remove_index])

                        regex = rf'<object id="(.*?)"\s+name="{re.escape(nombres[remove_index])}"(.*?)(?=\s+xmlns="http://www.blueprism.co.uk/product)'
                        current_id = filter_selected_process_id(regex, content)

                        regex = fr'<object[^>]*id="{re.escape(current_id[0][0])}"[^>]*name="{re.escape(nombres[remove_index])}"[^>]*>.*?</stage></process></object>'
                        content = delete_content(regex, content)

                        lineas_filtradas = remove_selected_process(current_id[0][0])

                        content = merge_splitted_lines(lineas_filtradas)

                    print(Fore.GREEN + nombres[remove_index] + " Removed Successfully")
                    del nombres[remove_index]
            else:
                validation = True
    else:
        validation = True
        pass

output_path = os.path.join(desktop, "archivo.bprelease")
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(Fore.GREEN + "Export complete — '.BPRELEASE' file written to Desktop...")
