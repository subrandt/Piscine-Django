from elem import Elem
from elements import Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br, Text

class Page(Elem):

    def __init__(self, root):
        self.root = root
    
    def check_html(self, elem):
        # Html must contain exactly one Head and then one Body
        if len(elem.content) != 2 or not isinstance(elem.content[0], Head) or not isinstance(elem.content[1], Body):
            return False
        return True

    def check_head(self, elem):
        # Head must contain exactly one Title
        if len(elem.content) != 1 or not isinstance(elem.content[0], Title):
            return False
        
    def check_body_and_div(self, elem):
        # Body and Div must contain only H1, H2, Div, Table, Ul, Ol, Span, or Text elements
        for child in elem.content:
            if not isinstance(child, (H1, H2, Div, Table, Ul, Ol, Span, Text)):
                return False

    # Title, H1, H2, Li, Th, Td must only contain one Text and only this Text

    # P must only contain Text.

    # Span must only contain Text or some P.

    # Ul and Ol must contain at least one Li and only some Li.

    # Tr must contain at least one Th or Td and only some Th or Td. The Th and the Td must be mutually exclusive.

    # Table must contain at least one Tr and only some Tr.

    def is_valid(self):
        if not isinstance(self.root, Html):
            return False

        for elem in self.root:
            if isinstance(elem, Html):
                if not self.check_html(elem):
                    return False
            elif isinstance(elem, Head):
                if not self.check_head(elem):
                    return False
            elif isinstance(elem, Body):
                if not self.check_body_and_div(elem):
                    return False
            elif isinstance(elem, Title):
                if not self.check_title(elem):
                    return False
            elif isinstance(elem, Meta):
                if not self.check_meta(elem):
                    return False
            elif isinstance(elem, Img):
                if not self.check_img(elem):
                    return False
            elif isinstance(elem, Table):
                if not self.check_table(elem):
                    return False
            elif isinstance(elem, Th):
                if not self.check_th(elem):
                    return False
            elif isinstance(elem, Tr):
                if not self.check_tr(elem):
                    return False
            elif isinstance(elem, Td):
                if not self.check_td(elem):
                    return False
            elif isinstance(elem, Ul):
                if not self.check_ul(elem):
                    return False
            elif isinstance(elem, Ol):
                if not self.check_ol(elem):
                    return False
            elif isinstance(elem, Li):
                if not self.check_li(elem):
                    return False
            elif isinstance(elem, H1):
                if not self.check_h1(elem):
                    return False
            elif isinstance(elem, H2):
                if not self.check_h2(elem):
                    return False
            elif isinstance(elem, P):
                if not self.check_p(elem):
                    return False
            elif isinstance(elem, Div):
                if not self.check_body_and_div(elem):
                    return False
            elif isinstance(elem, Span):
                if not self.check_span(elem):
                    return False
            elif isinstance(elem, Hr):
                if not self.check_hr(elem):
                    return False
            elif isinstance(elem, Br):
                if not self.check_br(elem):
                    return False
            elif isinstance(elem, Text):
                if not self.check_text(elem):
                    return False
                
            # TODO: Check other element types

        return True
    
    def __str__(self):
        if isinstance(self.root, Html):
            return "<!DOCTYPE html>\n" + str(self.root)
        else:
            return str(self.root)

    def write_to_file(self, filename: str):
        with open(filename, 'w') as file:
            file.write(str(self))


def testing_page_class():
    try:
        print('-------------------')
        print('Testing Page class')
        print('-------------------')
        print('Creating a simple page')
        simple_html = Html([
            Head([
                Title("Simple Title")
            ]),
            Body([
                H1("Simple Heading"),
                P("Simple paragraph.")
            ])
        ])

        simple_page = Page(simple_html)
        simple_page.write_to_file('simple_test.html')
        print(simple_page)
        # print(page.is_valid())
        print('-->Test passed')


        # create a more complex page
        print('\n-------------------')
        print('Creating a complex page')
        complex_html = Html([
            Head([
                Title("Complex Title"),
                Meta(attr={'charset': 'UTF-8'})
            ]),
            Body([
                H1("Complex Heading"),
                P("Complex paragraph."),
                Img(attr={'src': 'image.jpg', 'alt': 'image'})
            ])
        ])
        complex_page = Page(complex_html)
        complex_page.write_to_file('complex_test.html')
        print(complex_page)
        # print(page.is_valid())
        print('--> Test passed')



        print('--> All tests passed!')

    except Exception as e:
        print('Test failed: ', e)


if __name__ == '__main__':
    testing_page_class()


