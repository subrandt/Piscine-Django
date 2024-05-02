import requests
import json
import dewiki
import sys

def request_wikipedia(search_term):
    try:
        response = requests.get(f"https://fr.wikipedia.org/w/api.php?action=opensearch&search={search_term}&format=json")
        response.raise_for_status()
    except (requests.RequestException, ValueError):
        print("Wikipedia API request error")
        sys.exit(1)

    try:
        # Obtenir le contenu de la page
        page_content = requests.get(f"https://fr.wikipedia.org/w/api.php?action=query&prop=extracts&exintro&explaintext&format=json&titles={response.json()[1][0]}")
        page_content.raise_for_status()
    except (requests.RequestException, ValueError):
        print("Error getting page content")
        sys.exit(1)

    # Nettoyer le résultat du formatage JSON ou Wiki Markup
    cleaned_content = dewiki.from_string(json.loads(page_content.text)["query"]["pages"].popitem()[1]["extract"])

    # Écrire le résultat dans un fichier
    with open(f"{search_term.replace(' ', '_')}.wiki", "w") as file:
        file.write(cleaned_content)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: only one argument is required")
        sys.exit(1)

    request_wikipedia(sys.argv[1])