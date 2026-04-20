import requests
from bs4 import BeautifulSoup
import json

def get_meta():
    # Use a direct link to the Warzone meta page for better accuracy
    url = "https://codmunity.gg/warzone-meta"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        weapons = []
        
        # Updated selectors for 2026 site structure
        # We look for common patterns in meta cards
        cards = soup.select('div[class*="weapon"], div[class*="loadout-card"]')
        
        if not cards:
            print("No cards found with primary selector. Trying backup...")
            cards = soup.find_all('div', recursive=True)
            cards = [c for c in cards if c.find('h3') or c.find('h2')]

        for card in cards[:8]:  # Limit to top 8
            try:
                name_tag = card.find(['h2', 'h3', 'span'], class_=True) or card.find(['h2', 'h3'])
                if not name_tag: continue
                
                name = name_tag.get_text(strip=True)
                # Skip generic titles
                if len(name) < 2 or "Meta" in name: continue
                
                # Get pick rate or tier if available
                pick = "Meta"
                pick_tag = card.find(string=lambda t: "%" in t)
                if pick_tag:
                    pick = pick_tag.strip()

                weapons.append({
                    "name": name,
                    "class": "AR/SMG",
                    "tier": "S",
                    "pickRate": pick,
                    "code": "BUILD-IN-APP",
                    "attachments": {
                        "Note": "See App for full build",
                        "Build": "Verified Meta"
                    }
                })
            except Exception as e:
                continue

        # SAFETY CHECK: Only overwrite if we actually found something
        if len(weapons) > 0:
            with open('meta.json', 'w') as f:
                json.dump(weapons, f, indent=4)
            print(f"Successfully updated with {len(weapons)} weapons.")
        else:
            print("Scraper found 0 weapons. Keeping old data to avoid empty site.")
            
    except Exception as e:
        print(f"Error during scrape: {e}")

if __name__ == "__main__":
    get_meta()
