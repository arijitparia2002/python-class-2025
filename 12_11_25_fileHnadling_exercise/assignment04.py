import json

def analyze_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print("File not found. Please check the filename and try again.\n")
        return

    # Split text into words
    words = text.split()
    total_words = len(words)
    unique_words = len(set(words))

    # Find the longest word
    longest_word = ""
    if words:
        for w in words:
            if len(w) > len(longest_word):
                longest_word = w

    # Find the most common word manually (no collections)
    word_freq = {}
    for w in words:
        word_freq[w] = word_freq.get(w, 0) + 1

    most_common_word = ""
    highest_count = 0
    for word, count in word_freq.items():
        if count > highest_count:
            most_common_word = word
            highest_count = count

    # Prepare analysis data
    analysis = {
        "file_name": filename,
        "total_words": total_words,
        "unique_words": unique_words,
        "longest_word": longest_word,
        "most_common_word": most_common_word,
        "most_common_word_frequency": highest_count
    }

    # Save analysis to JSON file
    save_analysis_json(analysis)
    print("\n===== File Analysis Report =====")
    for key, value in analysis.items():
        print(f"{key}: {value}")
    print("\nAnalysis saved to 'file_analysis_report.json'\n")

def save_analysis_json(data):
    with open("file_analysis_report.json", "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4)

def main():
    while True:
        print("===== File Analyzer =====")
        print("1. Analyze a File")
        print("2. Exit")

        choice = input("Enter choice (1-2): ").strip()

        if choice == "1":
            filename = input("Enter the file name to analyze: ").strip()
            analyze_file(filename)
        elif choice == "2":
            print("Exiting File Analyzer. Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")

if __name__ == "__main__":
    main()
