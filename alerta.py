import os
import json
from functools import reduce
import shutil
import sys



if __name__ == "__main__":
    
    SEARCH = ["md"]  #agregar extensiones de archivo a revisar por el programa
    nombre_carpeta_revisada = sys.argv[1]

    with open("keywords.json") as file:
        KEYWORDS = json.load(file)["keywords"] 

    root_dir = os.getcwd()

    usernames = list()
    for root, dirs, files in os.walk(root_dir, onerror=None):
        for filename in files:
            file_path = os.path.join(root, filename)
            temp_lines = list()
            extension = file_path.split(os.sep)[-1].split(".")[-1]
            if extension in SEARCH:
                try:
                    with open(file_path, "r") as f:
                        for line in f.readlines():
                            temp_lines.append(line.strip().split(" "))
                        temp_lines = reduce(lambda x, y: x + y, temp_lines, [])
                        intersection = [_ for _ in temp_lines if _ in KEYWORDS]
                        if intersection != list():
                            file_path_list = file_path.split(os.sep)
                            index = file_path_list.index(nombre_carpeta_revisada)
                            usernames.append(file_path_list[index + 1])
                except (IOError, OSError, UnicodeDecodeError):  
                    pass
            


    usernames = set(usernames)
    with open("_usernames.txt", "w") as file:
        for user in usernames:
            file.writelines(user + "\n")
    print("Encontrados", len(usernames), "casos sospechosos")