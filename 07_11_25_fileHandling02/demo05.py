import json

def save_settings(settings):
    """Save settings to JSON"""
    with open("config.json", "w") as file:
        json.dump(settings, file, indent=4)
    print("Settings saved!")

def load_settings():
    """Load settings from JSON"""
    try:
        with open("config.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Usage
settings = {
    "theme": "dark",
    "language": "English",
    "font_size": 14
}

save_settings(settings)
loaded = load_settings()

print("\nCurrent Settings:")
for key, value in loaded.items():
    print(f"{key}: {value}")