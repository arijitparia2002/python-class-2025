import json
import os

SETTINGS_FILE = "settings.json"

# Default settings
DEFAULT_SETTINGS = {
    "theme": "light",
    "language": "en",
    "font_size": 14,
    "notifications": True
}

def load_settings():
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "r", encoding="utf-8") as file:
            try:
                settings = json.load(file)
                print("Settings loaded successfully.\n")
                return settings
            except json.JSONDecodeError:
                print("Error reading settings file. Resetting to default.\n")
                return DEFAULT_SETTINGS.copy()
    else:
        print("No settings file found. Using default settings.\n")
        return DEFAULT_SETTINGS.copy()

def save_settings(settings):
    with open(SETTINGS_FILE, "w", encoding="utf-8") as file:
        json.dump(settings, file, indent=4)
    print("Settings saved successfully.\n")

def display_settings(settings):
    print("===== Current Settings =====")
    for key, value in settings.items():
        print(f"{key}: {value}")
    print()

def update_settings(settings):
    print("Enter new settings (press Enter to keep current value):")
    theme = input(f"Theme (current: {settings['theme']}): ").strip() or settings['theme']
    language = input(f"Language (current: {settings['language']}): ").strip() or settings['language']
    font_size_input = input(f"Font Size (current: {settings['font_size']}): ").strip()
    font_size = int(font_size_input) if font_size_input.isdigit() else settings['font_size']
    notifications_input = input(f"Notifications (on/off, current: {'on' if settings['notifications'] else 'off'}): ").strip().lower()

    if notifications_input == "on":
        notifications = True
    elif notifications_input == "off":
        notifications = False
    else:
        notifications = settings['notifications']

    settings.update({
        "theme": theme,
        "language": language,
        "font_size": font_size,
        "notifications": notifications
    })

    save_settings(settings)
    print("Settings updated.\n")

def reset_settings():
    save_settings(DEFAULT_SETTINGS.copy())
    print("Settings reset to default.\n")
    return DEFAULT_SETTINGS.copy()

def main():
    settings = load_settings()

    while True:
        print("===== Settings Manager =====")
        print("1. Display Current Settings")
        print("2. Update Settings")
        print("3. Reset to Default")
        print("4. Save Settings")
        print("5. Exit")

        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            display_settings(settings)
        elif choice == "2":
            update_settings(settings)
        elif choice == "3":
            settings = reset_settings()
        elif choice == "4":
            save_settings(settings)
        elif choice == "5":
            print("Exiting Settings Manager. Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")

if __name__ == "__main__":
    main()
