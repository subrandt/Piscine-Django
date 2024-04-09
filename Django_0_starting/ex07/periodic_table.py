import sys

def create_periodic_table():
    
    try:
        # read in txt file
        file = open("periodic_table.txt", "r", encoding="utf8")
        # periodic_table = file.read()

        
        # create html file
        create_html = open("periodic_table.html", "w")

        # write in html file:
        create_html.write("<!DOCTYPE html>\n<html lang=\"en\">\n")
        create_html.write("<body>\n")
        create_html.write("<table>\n")
        
        while(1):
            create_html.write("<tr>\n")
            create_html.write("<td style=\"border: 1px solid black; padding:10px\">\n")
            
            periodic_table_element = file.readline()
            if(periodic_table_element == ''):
                break
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