import sys
import requests
from bs4 import BeautifulSoup


# Dependency Installation:
    # activate venv: source venv/bin/activate
    # pip install -r requirements.txt


# HTML Parsing using BeautifulSoup
def get_wikipedia_url(search_term):
    return f"https://en.wikipedia.org/wiki/{search_term}"

def get_first_link(page_content):
    soup = BeautifulSoup(page_content, 'html.parser')
    content_div = soup.find(id='mw-content-text').find(class_='mw-parser-output')

    for element in content_div.find_all(['p', 'ul'], recursive=False):
        if element.name == 'p':
            links = element.find_all('a', recursive=False)
        else:  # 'ul'
            links = [li.find('a') for li in element.find_all('li')]

        for link in links:
            if link:
                parents = [parent.name for parent in link.parents]
                if 'span' not in parents and 'small' not in parents:
                    if link.find_parent(['s', 'i', 'sup']):
                        continue
                    # Check if link is inside parentheses
                    text = str(element)
                    start = text.find(str(link))
                    if text.rfind('(', 0, start) > text.rfind(')', 0, start):
                        continue
                    return link.get('href')
    return None

def get_wikipedia_page(search_term):
    url = get_wikipedia_url(search_term)
    response = requests.get(url)
    page_content = response.text
    first_link = get_first_link(page_content)
    return first_link

def get_page_title_from_content(page_content):
    soup = BeautifulSoup(page_content, 'html.parser')
    return soup.find('h1').get_text()

def find_philosophy(search_term):
    if search_term.lower() == 'philosophy':
        print("0 roads from philosophy to philosophy")
        return

    visited_pages = set()
    url = get_wikipedia_url(search_term)

    # Main Loop: Create a loop until one of the following cases occurs:
        # The link leads to the "Philosophy" page.
        # The page contains no valid link.
        # The link leads to a page already visited.
    while True:
        response = requests.get(url)
        if response.status_code == 404:
            print("Http Error 404: Page not found")
            print("It leads to a dead end!")
            break
        try:
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            sys.exit(1)
        page_content = response.text
        title = get_page_title_from_content(page_content)
        if title in visited_pages:
            print("It leads to an infinite loop!")
            break
        visited_pages.add(title)
        print(title)
        if title.lower() == 'philosophy':
            print(f"{len(visited_pages)} roads from {search_term} to philosophy")
            break
        first_link = get_first_link(page_content)
        if not first_link:
            print("It leads to a dead end!")
            break
        next_url = get_wikipedia_url(first_link.lstrip('/wiki/'))
        url = next_url

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 roads_to_philosophy.py \"<search_term>\"")
        sys.exit(1)
    search_term = sys.argv[1]
    find_philosophy(search_term)

if __name__ == "__main__":
    main()