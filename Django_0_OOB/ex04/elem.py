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
        return super().__str__().replace('\n', '\n<br />\n')


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
        self.content = []
        if content:
            self.add_content(content)
        self.tag_type = tag_type
    
    def add_content(self, content):
        """
        Add a content to the element.
        """
        if isinstance(content, Elem) or isinstance(content, Text):
            self.content.append(content)
        else:
            raise self.ValidationError("Content must be an instance of Elem or Text")


    def __str__(self):
        """
        The __str__() method will permit us to make a plain HTML representation
        of our elements.
        Make sure it renders everything (tag, attributes, embedded
        elements...).
        """
        if self.tag_type == 'double':
            content = escape_html(self.__make_content())
            result = f"<{self.tag}{self.__make_attr()}>{content}</{self.tag}>"
        elif self.tag_type == 'simple':
            result = f"<{self.tag}{self.__make_attr()} />"
        return result

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
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
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
                          content=Elem(tag='title', attr={}, content=Text('Hello ground!'))))
    elem.add_content(Elem(tag='body', attr={},
                          content=[Elem(tag='h1', attr={}, content=Text('Oh no, not again!')),
                                   Elem(tag='img', attr={'src': 'http://i.imgur.com/pfp3T.jpg'}, tag_type='simple')]))
    
    with open('test.html', 'w') as file:
        file.write(str(elem))
    print(elem)

def escape_html(text):
    """
    Escape special characters in text to their HTML entities.
    """
    return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace("'", '&#39;')



if __name__ == '__main__':
    create_html_output()