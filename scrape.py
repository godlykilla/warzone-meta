import requests
from bs4 import BeautifulSoup
import json

def get_meta():
    # Direct URL to the tier list for 2026
    url = "https://codmunity.gg/tier-list/warzone"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        weapons = []
        
        # 1. FIND THE 'ABSOLUTE META' SECTION
        # In 2026, the site uses specific titles for the S-Tier section
        meta_section = soup.find(string=lambda t: t and "Absolute Meta" in t)
        
        if meta_section:
            # Look for the next few weapon names after that title
            parent = meta_section.find_parent()
            # Find all text that looks like a weapon name (Uppercase/Numbers)
            potential_names = parent.find_all_next(['h3', 'h2', 'div'], limit=15)
            
            for item in potential_names:
                name = item.get_text(strip=True)
                
                # FILTER: Skip junk like "Download", "Follow", "App", "Tools"
                junk = ["download", "app", "tools", "privacy", "follow", "meta", "loadout", "social"]
                if any(x in name.lower() for x in junk) or len(name) < 2 or len(name) > 15:
                    continue

                # If it passed the filter, it's likely a gun (e.g. MK35 ISR)
                weapons.append({
                    "name": name,
                    "class": "S-TIER META",
                    "tier": "S",
                    "pickRate": "High",
                    "code": "GET-IN-APP",
                    "attachments": {
                        "Status": "Verified",
                        "Source": "CODMunity Live"
                    }
                })

        # 2. FINAL CLEANUP & SAVE
        # Only save if we found real weapons. If we found 0, keep the file as is.
        if len(weapons) >= 2:
            # Remove duplicates
            seen = set()
            unique_weapons = []
            for w in weapons:
                if w['name'] not in seen:
                    unique_weapons.append(w)
                    seen.add(w['name'])

            with open('meta.json', 'w') as f:
                json.dump(unique_weapons[:6], f, indent=4) # Top 6
            print(f"Success! Found {len(unique_weapons)} real weapons.")
        else:
            print("Scraper only found junk. Safety fallback: No changes made.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_meta()
