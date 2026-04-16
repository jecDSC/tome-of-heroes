# fetch_fandom_html handles fetching pages from fandom.com.
import requests
from urllib.parse import unquote

def fetch_fandom_html(page_url):
    title = unquote(page_url.split('/wiki/', 1)[1]).split('?', 1)[0]
    try:
        response = requests.get(
            'https://feheroes.fandom.com/api.php',
            params={
                'action': 'parse',
                'page': title,
                'prop': 'text',
                'formatversion': '2',
                'format': 'json',
            },
            timeout=30,
        )
        response.raise_for_status()
        return response.json()['parse']['text']
    except requests.RequestException as e:
        print(f"Request failed for {title}: {e}")
        return None