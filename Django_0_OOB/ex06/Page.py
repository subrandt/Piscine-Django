from elem import Elem
from elem import Text
from elements import Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br

class Page(Elem):

    def __init__(self, root):
        self.root = root
    
    # Html must contain exactly one Head and then one Body
    def check_html(self, elem):
        if elem.content is None:
            return False
        if len(elem.content) != 2 or not isinstance(elem.content[0], Head) or not isinstance(elem.content[1], Body):
            return False
        if not self.is_valid(elem.content[0]) or not self.is_valid(elem.content[1]):
            return False
        return True

    # Head must contain exactly one Title
    def check_head(self, elem):
        if not elem.content:
            return True
        if len(elem.content) != 1 or not isinstance(elem.content[0], Title):
            return False
        if not self.is_valid(elem.content[0]):
            return False
        return True
        
    # Body and Div must contain only H1, H2, Div, Table, Ul, Ol, Span, or Text elements
    def check_body_and_div(self, elem):
        if elem.content is None:
            return True
        for child in elem.content:
            if not isinstance(child, (H1, H2, Div, Table, Ul, Ol, Span, Text)):
                return False
            if not self.is_valid(child):
                return False
        return True

    # Title, H1, H2, Li, Th, Td must only contain one Text and only this Text.
    def check_only_text(self, elem):
        if elem.content is None or len(elem.content) == 0:
            return True
        if len(elem.content) != 1:
            return False
        if isinstance(elem.content[0], Text):
            if hasattr(elem.content[0], 'content') and not isinstance(elem.content[0].content, str):
                return False
            return True
        return False

    # P must only contain Text.
    def check_p(self, elem):
        if elem.content is None:
            return True
        for child in elem.content:
            if not isinstance(child, Text):
                return False
            if not self.is_valid(child):
                return False
        return True

    # Span must only contain Text or P.
    def check_span(self, elem):
        if not elem.content:
            return True
        for child in elem.content:
            if not isinstance(child, (Text, P)):
                return False
            if not self.is_valid(child):
                return False
        return True

    # Ul and Ol must contain at least one Li and only Li.
    def check_ul_ol(self, elem):
        if not elem.content:
            return False
        for child in elem.content:
            if not isinstance(child, Li):
                return False
            if not self.is_valid(child):
                return False
        return True

    # Tr must contain at least one Th or Td and only Th or Td. The Th and the Td must be mutually exclusive.
    def check_tr(self, elem):
        th = False
        td = False
        for child in elem.content:
            if isinstance(child, Th):
                th = True
                if not self.is_valid(child):
                    return False
            elif isinstance(child, Td):
                td = True
                if not self.is_valid(child):
                    return False
            else:
                return False
        return th or td

    # Table must contain at least one Tr and only Tr.
    def check_table(self, elem):
        for child in elem.content:
            if not isinstance(child, Tr):
                return False
            if not self.is_valid(child):
                return False
        return True


    def is_valid(self, elem=None):
        if elem is None:
            elem = self.root

        if isinstance(elem, Html) and not self.check_html(elem):
            return False
        elif isinstance(elem, Head) and not self.check_head(elem):
            return False
        elif isinstance(elem, (Body, Div)) and not self.check_body_and_div(elem):
            return False
        elif isinstance(elem, (Title, H1, H2, Li, Th, Td)) and not self.check_only_text(elem):
            return False
        elif isinstance(elem, Table) and not self.check_table(elem):
            return False
        elif isinstance(elem, Tr) and not self.check_tr(elem):
            return False
        elif isinstance(elem, (Ul, Ol)) and not self.check_ul_ol(elem):
            return False
        elif isinstance(elem, P) and not self.check_p(elem):
            return False
        elif isinstance(elem, Span) and not self.check_span(elem):
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
        simple_page = Page(Html([
            Head(
                Title(Text('Simple Title')),
            ),
            Body([
                H1(Text('Simple Heading')),
                P(Text('Simple paragraph.'))
            ])
        ]))

        # simple_page.write_to_file('simple_test.html')
        print(simple_page)
        print('-->Test passed')


        # create a more complex page
        print('\n-------------------')
        print('Creating a complex page')
        complex_page = Page(Html([
            Head([
                Title(Text("Complex Title")),
                Meta(attr={'charset': 'UTF-8'})
            ]),
            Body([
                H1(Text("Complex Heading")),
                P(Text("Complex paragraph.")),
                Img(attr={'src': 'image.jpg', 'alt': 'image'})
            ])
        ]))
        complex_page.write_to_file('complex_test.html')
        print(complex_page)
        print('--> Test passed')

        # other tests
        print('\n-------------------')
        page = Page(P())
        assert page.is_valid()
        page = Page(Html([Head(Title(Text("toto"))), Body()]))
        assert page.is_valid()
        print("Test Basic Page Passed!")
        page = Page(Html())
        assert not page.is_valid()
        page = Page(Html(Head()))
        assert not page.is_valid()
        page = Page(Html(Body()))
        assert not page.is_valid()
        page = Page(Html(P()))
        assert not page.is_valid()
        page = Page(Html([Head(), P()]))
        assert not page.is_valid()
        page = Page(Html([Body(), Head()]))
        assert not page.is_valid()
        page = Page(Html([Head(Title()), Body()]))
        assert page.is_valid()
        print("Test Html Passed!")
        page = Page(Head())
        assert page.is_valid()
        page = Page(Head(P()))
        assert not page.is_valid()
        page = Page(Head(Title()))
        assert page.is_valid()
        page = Page(Head([Title(), Title()]))
        assert not page.is_valid()
        print("Test Head Passed!")
        page = Page(Div())
        assert page.is_valid()
        page = Page(Div(H1()))
        assert page.is_valid()
        page = Page(Div([H1(), H2(), Div(), Table(), Ul(Li()), Ol(Li()), Span(), Text("toto")]))
        assert page.is_valid()
        page = Page(Div(Li()))
        assert not page.is_valid()
        page = Page(Div([H1(), Head()]))
        assert not page.is_valid()
        print("Test Div Passed!")
        page = Page(Body())
        assert page.is_valid()
        page = Page(Body(H1()))
        assert page.is_valid()
        page = Page(Body([H1(), H2(), Div(), Table(),
                     Ul(Li()), Ol(Li()), Span(), Text("toto")]))
        assert page.is_valid()
        page = Page(Body(Li()))
        assert not page.is_valid()
        page = Page(Body([H1(), Body()]))
        assert not page.is_valid()
        print("Test Body Passed!")
        page = Page(Title())
        assert page.is_valid()
        page = Page(Title(P()))
        assert not page.is_valid()
        page = Page(Title(Text("toto")))
        assert page.is_valid()
        page = Page(Title([Text("toto"), Text("toto")]))
        assert not page.is_valid()
        print("Test Title Passed!")
        page = Page(H1())
        assert page.is_valid()
        page = Page(H1(P()))
        assert not page.is_valid()
        page = Page(H1(Text("toto")))
        assert page.is_valid()
        page = Page(H1([Text("toto"), Text("toto")]))
        assert not page.is_valid()
        print("Test H1 Passed!")
        page = Page(H2())
        assert page.is_valid()
        page = Page(H2(P()))
        assert not page.is_valid()
        page = Page(H2(Text("toto")))
        assert page.is_valid()
        page = Page(H2([Text("toto"), Text("toto")]))
        assert not page.is_valid()
        print("Test H2 Passed!")
        page = Page(Li())
        assert page.is_valid()
        page = Page(Li(P()))
        assert not page.is_valid()
        page = Page(Li(Text("toto")))
        assert page.is_valid()
        page = Page(Li([Text("toto"), Text("toto")]))
        assert not page.is_valid()
        print("Test Li Passed!")
        page = Page(Th())
        assert page.is_valid()
        page = Page(Th(P()))
        assert not page.is_valid()
        page = Page(Th(Text("toto")))
        assert page.is_valid()
        page = Page(Th([Text("toto"), Text("toto")]))
        assert not page.is_valid()
        print("Test Th Passed!")
        page = Page(Td())
        assert page.is_valid()
        page = Page(Td(P()))
        assert not page.is_valid()
        page = Page(Td(Text("toto")))
        assert page.is_valid()
        page = Page(Td([Text("toto"), Text("toto")]))
        assert not page.is_valid()
        print("Test Td Passed!")
        page = Page(P())
        assert page.is_valid()
        page = Page(P(Div()))
        assert not page.is_valid()
        page = Page(P(Text("toto")))
        assert page.is_valid()
        page = Page(P([Text("toto"), Text("toto")]))
        assert page.is_valid()
        print("Test P Passed!")
        page = Page(Span())
        assert page.is_valid()
        page = Page(Span(Div()))
        assert not page.is_valid()
        page = Page(Span(P()))
        assert page.is_valid()
        page = Page(Span(Text("toto")))
        assert page.is_valid()
        page = Page(Span([Text("toto"), Text("toto")]))
        assert page.is_valid()
        page = Page(Span([Text("toto"), P(), Text("toto")]))
        assert page.is_valid()
        page = Page(Span([Text("toto"), Span()]))
        assert not page.is_valid()
        print("Test Span Passed!")
        page = Page(Ul())
        assert not page.is_valid()
        page = Page(Ul(Li()))
        assert page.is_valid()
        page = Page(Ul(P()))
        assert not page.is_valid()
        page = Page(Ul([Li(), Li()]))
        assert page.is_valid()
        page = Page(Ul([Li(), Span(), Li()]))
        assert not page.is_valid()
        print("Test Ul Passed!")
        page = Page(Ol())
        assert not page.is_valid()
        page = Page(Ol(Li()))
        assert page.is_valid()
        page = Page(Ol(P()))
        assert not page.is_valid()
        page = Page(Ol([Li(), Li()]))
        assert page.is_valid()
        page = Page(Ol([Li(), Span(), Li()]))
        assert not page.is_valid()
        print("Test Ol Passed!")
        page = Page(Tr())
        assert not page.is_valid()
        page = Page(Tr(Th()))
        assert page.is_valid()
        page = Page(Tr(Td()))
        assert page.is_valid()
        page = Page(Tr(Span()))
        assert not page.is_valid()
        page = Page(Tr([Th(), Td()]))
        assert page.is_valid()
        page = Page(Tr([Th(), Span(), Td()]))
        assert not page.is_valid()
        page = Page(Tr([Th(), Td(), Td()]))
        assert page.is_valid()
        page = Page(Tr([Th(), Td(), Th()]))
        assert page.is_valid()
        print("Test Tr Passed!")
        page = Page(Table())
        assert page.is_valid()
        page = Page(Table(H1()))
        assert not page.is_valid()
        page = Page(Table(Text("toto")))
        assert not page.is_valid()
        page = Page(Table(Tr(Th())))
        assert page.is_valid()
        page = Page(Table([Tr(Th()), Tr(Th())]))
        assert page.is_valid()
        page = Page(Table([Tr(Th()), Span(), Tr(Th())]))
        assert not page.is_valid()
        print("Test Table Passed!")

        print("Additionnal Tests:")
        page = Page(Html([Head(), Body()]))
        assert page.is_valid()
        page = Page(Html([Head(Title(Text('title'))), Body()]))
        assert page.is_valid()
        page.write_to_file('additionnal.html')
        
        page = Page(Html([Head(Title(Text('title'))), Body(Ol(Li(Text('foo'))))]))
        assert page.is_valid()
        page = Page(Html([Head(Title([Text('title')])), Body(Li())]))
        assert not page.is_valid()        
        page = Page(Html([Head(Title(Text(Html))), Body(Ol(Li(Head('foo'))))]))
        assert not page.is_valid() 
        print("Additionnal Tests passed!")

        print('--> All tests passed!')

    except Exception as e:
        print('Test failed: ', e)


if __name__ == '__main__':
    testing_page_class()