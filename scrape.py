import requests
from bs4 import BeautifulSoup
import json

def get_meta():
    url = "https://codmunity.gg/warzone-meta"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    
    try:
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        
        found_weapons = []
        # We look specifically for <h3> tags which are usually weapon names
        all_titles = soup.find_all(['h3', 'h2'])

        for title in all_titles:
            name = title.get_text(strip=True)
            
            # THE FILTER: Only accept names that look like actual weapons
            # (e.g., skip "Download our app", "Follow us", etc.)
            blacklisted_words = ["download", "app", "tools", "privacy", "follow", "meta", "loadout"]
            if any(word in name.lower() for word in blacklisted_words) or len(name) > 20:
                continue

            found_weapons.append({
                "name": name,
                "class": "Meta Choice",
                "tier": "S",
                "pickRate": "Trending",
                "code": "CHECK-SITE",
                "attachments": {"Status": "Live Scraped", "Build": "Check Source"}
            })

        # Final check: If we found at least 3 real-looking weapons, save them.
        # Otherwise, don't touch the file (keep the hard-coded ones).
        if len(found_weapons) >= 3:
            with open('meta.json', 'w') as f:
                json.dump(found_weapons[:10], f, indent=4)
            print(f"Success! Found {len(found_weapons)} weapons.")
        else:
            print("Scraper failed to find real weapons. Keeping fallback data.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_meta()
