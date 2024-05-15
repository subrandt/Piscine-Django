import requests
import json
import dewiki
import sys

# Dependency Installation:
    # activate venv: source venv/bin/activate
    # pip install -r requirements.txt

def request_wikipedia(search_term):

    # Get the page title from the search term
    params = {
            'action': 'query',
            'format': 'json',
            'titles': search_term,
            'prop': 'revisions',
            'rvprop': 'content',
            'rvslots': '*',
            'formatversion': '2',
            'redirects': '',
        }

    response = requests.get('https://fr.wikipedia.org/w/api.php', params=params, headers={'User-Agent': 'MyUserAgent/1.0'})

    try:
        response.raise_for_status()
    except (requests.RequestException, ValueError):
        print("Wikipedia API request error")
        sys.exit(1)

    # Get the page title
    data = response.json()
    page_title = data['query']['pages'][0]['title']
    print(page_title)


    try:
        page_content = requests.get(f"https://fr.wikipedia.org/w/api.php?action=query&prop=extracts&exintro&explaintext&format=json&titles={page_title}")
        page_content.raise_for_status()
    except (requests.RequestException, ValueError):
        print("Error getting page content")
        sys.exit(1)

    # Load the page content as JSON
    page_content_json = json.loads(page_content.text)

    # Access the "query" key
    query_content = page_content_json["query"]

    # Access the "pages" key
    pages_content = query_content["pages"]

    # Get the last item from the dictionary
    last_item_key, last_item_value = pages_content.popitem()
    extract_content = last_item_value["extract"]

    # Use dewiki to clean the content
    cleaned_content = dewiki.from_string(extract_content)
    print(cleaned_content)

    # Write the cleaned content to a file
    with open(f"{search_term.replace(' ', '_')}.wiki", "w") as file:
        file.write(cleaned_content)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python request_wikipedia.py <search_term>")
        sys.exit(1)

    request_wikipedia(sys.argv[1])