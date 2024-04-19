#!/usr/bin/python3


class Text(str):
    """
    A Text class to represent a text you could use with your HTML elements.

    Because directly using str class was too mainstream.
    """

    def __str__(self):
        """
        Do you really need a comment to understand this method?..
        """
        s = super().__str__()
        if s == '"':
            return '&quot;'
        s = s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('\n', '\n<br />\n').replace('&quot;', '"')
        return s
    

class Elem:
    """
    Elem will permit us to represent our HTML elements.
    """
    class ValidationError(Exception):
        def __init__(self, message):
            self.message = message

    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        """
        __init__() method.

        Obviously.
        """
        if isinstance(content, str) and content == '' and not isinstance(content, (Elem, Text)):
            raise self.ValidationError("Content cannot be an empty string")
        self.tag = tag
        self.attr = attr
        self.content = content if isinstance(content, list) else [content] if content else []
        self.tag_type = tag_type

    def __str__(self):
        """
        The __str__() method will permit us to make a plain HTML representation
        of our elements.
        Make sure it renders everything (tag, attributes, embedded
        elements...).
        """
        attrs = self.__make_attr()
        if self.tag_type == 'double':
            inner = self.__make_content()
            return f"<{self.tag}{attrs}>{inner}</{self.tag}>"
        else:
            return f"<{self.tag}{attrs} />"


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
        empty = True
        result = ''
        if self.check_type(self.content):
            if isinstance(self.content, list):
                if len(self.content) == 0:
                    return ''
                for element in self.content:
                    if element != '':
                        empty = False
                if empty is False:
                    result = '\n'
                for elem in self.content:
                    if elem != '':
                        result += "  " + str(elem).replace("\n", "\n  ") + "\n"
            else:
                result = "  " + str(self.content).replace("\n", "\n  ") + "\n"
        return result

    def add_content(self, content):
        if not isinstance(content, (Elem, Text)):
            raise self.ValidationError("Invalid content type")
        if isinstance(self.content, list):
            self.content.append(content)
        else:
            self.content = [self.content, content]

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
    try:
        html = Elem('html', {}, [
            Elem('head', {}, [
                Elem('title', {}, [Text('"Hello ground!"')])
            ]),
            Elem('body', {}, [
                Elem('h1', {}, [Text('"Oh no, not again!"')]),
                Elem('img', {'src': "http://i.imgur.com/pfp3T.jpg"}, tag_type='simple')
            ])
        ])

        print(html)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    create_html_output()
