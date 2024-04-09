import sys


def extract_info(line):
    # Divise la ligne en fonction du signe égal
    parts = line.split("=")
    if len(parts) != 2:
        return None
    
    # Extraire le nom de l'élément (première partie)
    name = parts[0].strip()
    
    # Diviser la deuxième partie en fonction des virgules
    attributes = parts[1].split(",")
    
    # Initialisation des variables
    position = None
    number = None
    molar = None
    electron = None
    
    # Parcourir les attributs pour extraire les valeurs pertinentes
    for attr in attributes:
        attr_parts = attr.strip().split(":")
        if len(attr_parts) == 2:
            key = attr_parts[0].strip()
            value = attr_parts[1].strip()
            if key == "position":
                position = int(value)
            elif key == "number":
                number = int(value)
            elif key == "molar":
                molar = float(value)
            elif key == "electron":
                electron = value
    
    return {
        "name": name,
        "position": position,
        "number": number,
        "molar": molar,
        "electron": electron
    }

# Exemple d'utilisation
line = "Hydrogen = position:0, number:1, small: H, molar:1.00794, electron:1"
info = extract_info(line)
if info:
    print(info)
else:
    print("Erreur lors de l'extraction des informations")


def create_periodic_table():
    
    try:
        # read in txt file
        file = open("periodic_table.txt", "r", encoding="utf8")
        # periodic_table = file.read()

        
        # create html file
        create_html = open("periodic_table.html", "w")

        # write in html file:
        create_html.write("<!DOCTYPE html>\n<html lang=\"en\">\n")
        # ajouter un head avec les styles
        create_html.write("<body>\n")
        create_html.write("<table>\n")
        
        while(1):
            
            
            periodic_table_element = file.readline()
            if(periodic_table_element == ''):
                break
            create_html.write("<tr>\n")
            create_html.write("<td style=\"border: 1px solid black; padding:10px\">\n")
            create_html.write(periodic_table_element)
            
            
            create_html.write("</td>\n")
            create_html.write("</tr>\n")


        create_html.write("</table>\n")
        create_html.write("</body>\n")
        create_html.write("</html>")
        
        create_html.close()
    
    except Exception as e:
        print(e)
 
if __name__ == '__main__':
    create_periodic_table()