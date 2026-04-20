import requests
from bs4 import BeautifulSoup
import json

def get_meta():
    # Targeted URL for 2026 Meta Data
    url = "https://codmunity.gg/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    weapons = []
    
    # This logic finds the 'Absolute Meta' entries based on the 2026 site structure
    cards = soup.find_all('div', class_='weapon-card-meta')[:6] # Grab top 6
    
    for card in cards:
        name = card.find('h3').text.strip()
        pick = card.find('div', class_='pick-value').text.strip()
        code = card.find('div', class_='share-code').text.strip()
        
        weapons.append({
            "name": name,
            "pickRate": pick,
            "code": code,
            "class": "AR" if "Assault" in card.text else "SMG", # Simple logic
            "tier": "S"
        })
        
    with open('meta.json', 'w') as f:
        json.dump(weapons, f, indent=4)

if __name__ == "__main__":
    get_meta()