#!/usr/bin/python3


class Text(str):
    """
    A Text class to represent a text you could use with your HTML elements.

    Because directly using str class was too mainstream.
    """

    def __str__(self, level=0):
        """
        Do you really need a comment to understand this method?..
        """
        s = super().__str__()
        s = s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')
        return s
    


    def to_string(self, level=0):
        s = self.__str__()
        s = '  ' * level + s.replace('\n', '\n' + '  ' * level)
        return s

class Elem:
    """
    Elem will permit us to represent our HTML elements.
    """
    class ValidationError(Exception):
        pass

    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        """
        __init__() method.

        Obviously.
        """
        self.tag = tag
        self.attr = attr
        self.content = [] if content is None else [content]
        self.tag_type = tag_type

    def __str__(self, level=0):
        """
        The __str__() method will permit us to make a plain HTML representation
        of our elements.
        Make sure it renders everything (tag, attributes, embedded
        elements...).
        """
        if self.tag_type == 'double':
            if isinstance(self.content, list):
                content = '\n'.join(item.to_string(level + 1) if isinstance(item, (Elem, Text)) else str(item) for item in self.content)
            elif isinstance(self.content, (Elem, Text)):
                content = self.content.to_string(level + 1)
            else:
                content = str(self.content) if self.content else ''
            indent = '  ' * level
            inner_indent = '  ' * (level + 1)
            content = f'\n{inner_indent}' + content + f'\n{indent}' if content else ''
            return f"{indent}<{self.tag}>{content}{indent}</{self.tag}>"
        else:
            return f"{'  ' * level}<{self.tag} />"
        
    def to_string(self, level=0):
        return self.__str__(level)

    def __make_attr(self):
        """
        Here is a function to render our elements attributes.
        """
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        """
        Here is a method to render the content, including embedded elements.
        """

        if len(self.content) == 0:
            return ''
        result = '\n'
        for elem in self.content:
            result += str(elem) + '\n'
        return result

    def add_content(self, content):
        # if not Elem.check_type(content):
        #     raise Elem.ValidationError
        # if type(content) == list:
        #     self.content += [elem for elem in content if elem != Text('')]
        # elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        """
        Is this object a HTML-compatible Text instance or a Elem, or even a
        list of both?
        """
        return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))

def create_html_output():
    """
    This function will create the HTML output file.
    """
    elem = Elem(tag='html', attr={})
    elem.add_content(Elem(tag='head', attr={},
                          content=Elem(tag='title', attr={}, content=Text('"Hello ground!"'))))
    elem.add_content(Elem(tag='body', attr={},
                          content=[Elem(tag='h1', attr={}, content=Text('"Oh no, not again!"')),
                                   Elem(tag='img', attr={'src': 'http://i.imgur.com/pfp3T.jpg'}, tag_type='simple')]))

    print(elem)

if __name__ == '__main__':
    create_html_output()
