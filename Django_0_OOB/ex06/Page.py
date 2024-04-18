from elem import Elem
from elements import Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br, Text

class Page(Elem):

    def __init__(self, root):
        self.root = root
    
    # Html must contain exactly one Head and then one Body
    def check_html(self, elem):
        if len(elem.content) != 2 or not isinstance(elem.content[0], Head) or not isinstance(elem.content[1], Body):
            return False
        return True

    # Head must contain exactly one Title
    def check_head(self, elem):
        if len(elem.content) != 1 or not isinstance(elem.content[0], Title):
            return False
        
    # Body and Div must contain only H1, H2, Div, Table, Ul, Ol, Span, or Text elements
    def check_body_and_div(self, elem):
        for child in elem.content:
            if not isinstance(child, (H1, H2, Div, Table, Ul, Ol, Span, Text)):
                return False

    # Title, H1, H2, Li, Th, Td must only contain one Text and only this Text.
    def check_only_text(self, elem):
        return len(elem.content) == 1 and isinstance(elem.content[0], Text)


    # P must only contain Text.
    def check_p(self, elem):
        for child in elem.content:
            if not isinstance(child, Text):
                return False
        return True

    # Span must only contain Text or P.
    def check_span(self, elem):
        for child in elem.content:
            if not isinstance(child, (Text, P)):
                return False
        return True

    # Ul and Ol must contain at least one Li and only Li.
    def check_ul_ol(self, elem):
        for child in elem.content:
            if not isinstance(child, Li):
                return False
        return True

    # Tr must contain at least one Th or Td and only Th or Td. The Th and the Td must be mutually exclusive.
    def check_tr(self, elem):
        th = False
        td = False
        for child in elem.content:
            if isinstance(child, Th):
                if td:
                    return False
                th = True
            elif isinstance(child, Td):
                if th:
                    return False
                td = True
            else:
                return False
        return th or td

    # Table must contain at least one Tr and only Tr.
    def check_table(self, elem):
        for child in elem.content:
            if not isinstance(child, Tr):
                return False
        return True


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
            elif isinstance(elem, Body, Div):
                if not self.check_body_and_div(elem):
                    return False
            elif isinstance(elem, (Title, H1, H2, Li, Th, Td)):
                if not self.check_only_text(elem):
                    return False
            elif isinstance(elem, Table):
                if not self.check_table(elem):
                    return False
            elif isinstance(elem, Tr):
                if not self.check_tr(elem):
                    return False
            elif isinstance(elem, Ul, Ol):
                if not self.check_ul_ol(elem):
                    return False
            elif isinstance(elem, P):
                if not self.check_p(elem):
                    return False
            elif isinstance(elem, Span):
                if not self.check_span(elem):
                    return False
                

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
        # simple_page.write_to_file('simple_test.html')
        print(simple_page)
        # print(simple_page.is_valid())
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

        # other tests
        print('\n-------------------')
        assert not Page(Elem()).is_valid()
        page = Page(P())
        assert page.is_valid()
        page = Page(Elem())
        assert not page.is_valid()
        page = Page(Html())
        assert not page.is_valid()
        page = Page(Html([Head(Title(Text("toto"))), Body()]))
        assert page.is_valid()
        print("Test Basic Page Passed!")
        elem = Html()
        assert not elem.is_valid()
        elem = Html(Head())
        assert not elem.is_valid()
        elem = Html(Body())
        assert not elem.is_valid()
        elem = Html(P())
        assert not elem.is_valid()
        elem = Html([Head(), P()])
        assert not elem.is_valid()
        elem = Html([Body(), Head()])
        assert not elem.is_valid()
        elem = Html([Head(Title()), Body()])
        assert elem.is_valid()
        print("Test Html Passed!")
        elem = Head()
        assert elem.is_valid()
        elem = Head(P())
        assert not elem.is_valid()
        elem = Head(Title())
        assert elem.is_valid()
        elem = Head([Title(), Title()])
        assert not elem.is_valid()
        print("Test Head Passed!")
        elem = Div()
        assert elem.is_valid()
        elem = Div(H1())
        assert elem.is_valid()
        elem = Div([H1(), H2(), Div(), Table(), Ul(Li()), Ol(Li()), Span(), Text("toto")])
        assert elem.is_valid()
        elem = Div(Li())
        assert not elem.is_valid()
        elem = Div([H1(), Head()])
        assert not elem.is_valid()
        print("Test Div Passed!")
        elem = Body()
        assert elem.is_valid()
        elem = Body(H1())
        assert elem.is_valid()
        elem = Body([H1(), H2(), Div(), Table(),
                     Ul(Li()), Ol(Li()), Span(), Text("toto")])
        assert elem.is_valid()
        elem = Body(Li())
        assert not elem.is_valid()
        elem = Body([H1(), Body()])
        assert not elem.is_valid()
        print("Test Body Passed!")
        elem = Title()
        assert elem.is_valid()
        elem = Title(P())
        assert not elem.is_valid()
        elem = Title(Text("toto"))
        assert elem.is_valid()
        elem = Title([Text("toto"), Text("toto")])
        assert not elem.is_valid()
        print("Test Title Passed!")
        elem = H1()
        assert elem.is_valid()
        elem = H1(P())
        assert not elem.is_valid()
        elem = H1(Text("toto"))
        assert elem.is_valid()
        elem = H1([Text("toto"), Text("toto")])
        assert not elem.is_valid()
        print("Test H1 Passed!")
        elem = H2()
        assert elem.is_valid()
        elem = H2(P())
        assert not elem.is_valid()
        elem = H2(Text("toto"))
        assert elem.is_valid()
        elem = H2([Text("toto"), Text("toto")])
        assert not elem.is_valid()
        print("Test H2 Passed!")
        elem = Li()
        assert elem.is_valid()
        elem = Li(P())
        assert not elem.is_valid()
        elem = Li(Text("toto"))
        assert elem.is_valid()
        elem = Li([Text("toto"), Text("toto")])
        assert not elem.is_valid()
        print("Test Li Passed!")
        elem = Th()
        assert elem.is_valid()
        elem = Th(P())
        assert not elem.is_valid()
        elem = Th(Text("toto"))
        assert elem.is_valid()
        elem = Th([Text("toto"), Text("toto")])
        assert not elem.is_valid()
        print("Test Th Passed!")
        elem = Td()
        assert elem.is_valid()
        elem = Td(P())
        assert not elem.is_valid()
        elem = Td(Text("toto"))
        assert elem.is_valid()
        elem = Td([Text("toto"), Text("toto")])
        assert not elem.is_valid()
        print("Test Td Passed!")
        elem = P()
        assert elem.is_valid()
        elem = P(Div())
        assert not elem.is_valid()
        elem = P(Text("toto"))
        assert elem.is_valid()
        elem = P([Text("toto"), Text("toto")])
        assert elem.is_valid()
        print("Test P Passed!")
        elem = Span()
        assert elem.is_valid()
        elem = Span(Div())
        assert not elem.is_valid()
        elem = Span(P())
        assert elem.is_valid()
        elem = Span(Text("toto"))
        assert elem.is_valid()
        elem = Span([Text("toto"), Text("toto")])
        assert elem.is_valid()
        elem = Span([Text("toto"), P(), Text("toto")])
        assert elem.is_valid()
        elem = Span([Text("toto"), Span()])
        assert not elem.is_valid()
        print("Test Span Passed!")
        elem = Ul()
        assert not elem.is_valid()
        elem = Ul(Li())
        assert elem.is_valid()
        elem = Ul(P())
        assert not elem.is_valid()
        elem = Ul([Li(), Li()])
        assert elem.is_valid()
        elem = Ul([Li(), Span(), Li()])
        assert not elem.is_valid()
        print("Test Ul Passed!")
        elem = Ol()
        assert not elem.is_valid()
        elem = Ol(Li())
        assert elem.is_valid()
        elem = Ol(P())
        assert not elem.is_valid()
        elem = Ol([Li(), Li()])
        assert elem.is_valid()
        elem = Ol([Li(), Span(), Li()])
        assert not elem.is_valid()
        print("Test Ol Passed!")
        elem = Tr()
        assert not elem.is_valid()
        elem = Tr(Th())
        assert elem.is_valid()
        elem = Tr(Td())
        assert elem.is_valid()
        elem = Tr(Span())
        assert not elem.is_valid()
        elem = Tr([Th(), Td()])
        assert elem.is_valid()
        elem = Tr([Th(), Span(), Td()])
        assert not elem.is_valid()
        elem = Tr([Th(), Td(), Td()])
        assert not elem.is_valid()
        elem = Tr([Th(), Td(), Th()])
        assert elem.is_valid()
        print("Test Tr Passed!")
        elem = Table()
        assert elem.is_valid()
        elem = Table(H1())
        assert not elem.is_valid()
        elem = Table(Text("toto"))
        assert not elem.is_valid()
        elem = Table(Tr(Th()))
        assert elem.is_valid()
        elem = Table([Tr(Th()), Tr(Th())])
        assert elem.is_valid()
        elem = Table([Tr(Th()), Span(), Tr(Th())])
        assert not elem.is_valid()
        print("Test Table Passed!")
        print("All Test Passed!")
        page = Page(Html([
            Head(Title(Text("My CV"))),
            Body([
                H1(Text("My CV")),
                H2(Text("FirstName: Michel")),
                H2(Text("LastName: Dubois")),
                Br(),
                H2(Text("Experiences:")),
                Ul([
                    Li(Text("42")),
                    Li(Text("Toto Industry")),
                    Li(Text("Tutu company")),
                    ]),
                Br(),
                H2(Text("Skills:")),
                Table([
                    Tr([Th(Text("First"),
                           {"style": "background-color: red;"}),
                        Td(Text("1")),
                        Th(Text("Yes"),
                           {"style": "background-color: green;"}),
                        Td(Text("y"))]),
                    Tr([Th(Text("Second"),
                           {"style": "background-color: blue;"}),
                        Td(Text("2")),
                        Th(Text("No")), Td(Text("n"))]),
                    Tr([Th(Text("Third")), Td(Text("3")),
                        Th(Text("Maybe")), Td(Text("m"))]),
                ])
            ])
            ]))
        

        print('--> All tests passed!')

    except Exception as e:
        print('Test failed: ', e)


if __name__ == '__main__':
    testing_page_class()


