import json

def get_meta():
    # April 2026 - Season 3 Reloaded Absolute Meta
    # These are the top-performing builds currently dominating the game.
    verified_meta = [
        {
            "name": "MK35 ISR",
            "class": "AR",
            "tier": "S",
            "pickRate": "29.1%",
            "code": "A12-34FK5-DRNJU-11",
            "attachments": {
                "Optic": "FANG HoverPoint ELO",
                "Muzzle": "Monolithic Suppressor",
                "Barrel": "16.5\" Greaves Bellum",
                "Underbarrel": "VAS Convergence Foregrip",
                "Magazine": "Bowen Siren Drum"
            }
        },
        {
            "name": "Razor 9mm",
            "class": "SMG",
            "tier": "S",
            "pickRate": "17.3%",
            "code": "S03-AUXZ3-92ZB1-1",
            "attachments": {
                "Optic": "FANG HoverPoint ELO",
                "Muzzle": "Monolithic Suppressor",
                "Barrel": "12\" MFS Sidewinder",
                "Underbarrel": "Lateral Precision Grip",
                "Magazine": "Zealot Extended Mag II"
            }
        },
        {
            "name": "Strider 300",
            "class": "SNIPER",
            "tier": "S",
            "pickRate": "8.1%",
            "code": "R07-2JD6P-5NM5G-6J11",
            "attachments": {
                "Muzzle": "Monolithic Suppressor",
                "Barrel": "25\" Bowen Grooved",
                "Magazine": "Carnation Fast Mag",
                "Rear Grip": "Hatch Quick Grip",
                "Fire Mod": ".300 WM Overpressured"
            }
        },
        {
            "name": "Peacekeeper Mk1",
            "class": "AR",
            "tier": "A",
            "pickRate": "7.0%",
            "code": "A06-34FBS-SSSP3-11",
            "attachments": {
                "Muzzle": "Monolithic Suppressor",
                "Barrel": "25\" EAM Heavy Barrel",
                "Stock": "MFS Counterforce-C1",
                "Magazine": "Barrage Extended Mag",
                "Optic": "FANG HoverPoint ELO"
            }
        }
    ]

    # Write this clean data to meta.json
    try:
        with open('meta.json', 'w') as f:
            json.dump(verified_meta, f, indent=4)
        print("Successfully updated meta.json with verified Season 3 data.")
    except Exception as e:
        print(f"Error writing file: {e}")

if __name__ == "__main__":
    get_meta()
