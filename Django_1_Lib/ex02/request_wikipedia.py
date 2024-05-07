import requests
import json
import dewiki
import sys

# Dependency Installation:
    # activate venv: source venv/bin/activate
    # pip install -r requirements.txt



# Comment obtenir la reponse json de la page comme dans l'exemple du sujet ?
# Comment faire une recherche mal orthographiée ?

def request_wikipedia(search_term):
    try:
        response = requests.get(f"https://fr.wikipedia.org/w/api.php?action=opensearch&search={search_term}&format=json")
        response.raise_for_status()
        print("Response JSON:", response.json())
    except (requests.RequestException, ValueError):
        print("Wikipedia API request error")
        sys.exit(1)

    try:
        page_content = requests.get(f"https://fr.wikipedia.org/w/api.php?action=query&prop=extracts&exintro&explaintext&format=json&titles={response.json()[1][0]}")
        page_content.raise_for_status()
    except (requests.RequestException, ValueError):
        print("Error getting page content")
        sys.exit(1)

    # Step 1: Load the page content as JSON
    page_content_json = json.loads(page_content.text)

    # Step 2: Access the "query" key
    query_content = page_content_json["query"]
    print("Query content:", query_content)

    # Step 3: Access the "pages" key
    pages_content = query_content["pages"]
    print("Pages content:", pages_content)

    # Step 4: Use popitem() to get the last item from the dictionary
    last_item_key, last_item_value = pages_content.popitem()
    print("Last item key:", last_item_key)
    print("Last item value:", last_item_value)

    # Step 5: Access the "extract" key in the item's value
    extract_content = last_item_value["extract"]
    print("Extract content:", extract_content)

    # Step 6: Use dewiki to clean the content
    cleaned_content = dewiki.from_string(extract_content)
    print("Cleaned content:", cleaned_content)

    # # Écrire le résultat dans un fichier
    # with open(f"{search_term.replace(' ', '_')}.wiki", "w") as file:
    #     file.write(cleaned_content)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: only one argument is required")
        sys.exit(1)

    request_wikipedia(sys.argv[1])