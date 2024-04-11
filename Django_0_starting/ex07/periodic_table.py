import sys

def extract_info(line):
    
    # separate name and the rest
    parts = line.split("=")
    if len(parts) != 2:
        return None
    
    # extract name
    name = parts[0].strip()    

    # extract variables
    attributes = parts[1].split(",")
    
    position = None
    number = None
    molar = None
    electron = None
    
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
    
    return (
        name,
        position,
        number,
        molar,
        electron
    )


def create_periodic_table():
    
    try:
        # read in txt file
        file = open("periodic_table.txt", "r", encoding="utf8")
        
        # create html file
        create_html = open("periodic_table.html", "w")

        # write in html file:
        create_html.write("<!DOCTYPE html>\n<html lang=\"en\">\n")
        create_html.write("<head>\n<meta charset=\"UTF-8\"><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"><title>PeriodicTable</title>")
        create_html.write("<style>\n.elem_cells {\nborder: 1px solid black; padding:10px\n}\n\n</style>\n</head>\n")
        create_html.write("<body>\n")
        create_html.write("<table>\n")
        create_html.write("<tr>\n")
        last_position = 0
        while(1):
            
            
            periodic_table_element = file.readline()
            if(periodic_table_element == ''):
                break
            
            # get element information
            (name, position, number, molar, electron) = extract_info(periodic_table_element)

            if position < last_position:
                create_html.write("</tr><tr>\n")
            
            # create_empty_boxes()
            if (position - last_position > 1):
                for _ in range(0, (position - last_position - 1)):
                    create_html.write("<td>\n</td>\n")
                
       
            # write element boxes            
            create_html.write("<td class=\"elem_cells\">\n")
            
            create_html.write("<h4>")
            create_html.write(name)
            create_html.write("</h4>\n")
            
            create_html.write("<ul>\n")
            create_html.write("<li>")
            create_html.write("n°:")
            create_html.write(str(number))
            create_html.write("</li>\n")
            
            create_html.write("<li>")
            create_html.write("mol:")
            create_html.write(str(molar))
            create_html.write("</li>\n")

            
            create_html.write("<li>")
            create_html.write("el:")
            create_html.write(electron)
            create_html.write("</li>\n")
            create_html.write("</ul>\n")
            
                
            
            create_html.write("</td>\n")
            
            
            last_position = position
            


        create_html.write("</table>\n")
        create_html.write("</body>\n")
        create_html.write("</html>")
        
        create_html.close()
    
    except Exception as e:
        print(e)
 
if __name__ == '__main__':
    create_periodic_table()