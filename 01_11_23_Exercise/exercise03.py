text = "Python is amazing. Python is powerful. Python is easy to learn. Programming with Python is fun."

# Part A: Word Extraction
print("\n--- Part A: Word Extraction ---")
words = text.lower().split()
clean_words = [word.strip(" ") for word in words]
clean_words = [word.replace(".", "") for word in words]
clean_words = [word.replace("!", "") for word in words]
print("Clean words:", clean_words)
print(f"Total words: {len(clean_words)}")

# Part B: Word Frequency Counter
print("\n--- Part B: Word Frequency Counter ---")
word_count = {}
for word in clean_words:
    word_count[word] = word_count.get(word, 0) + 1

print("Word frequencies (sorted by count):")
sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
for word, count in sorted_words:
    print(f"{word}: {count}")


# Part C: Word Filtering
print("\n--- Part C: Word Filtering ---")
long_words = [word for word in clean_words if len(word) > 4]
unique_long_words = set(long_words)
print(f"Long words (>4 chars): {unique_long_words}")

p_words = [word for word in clean_words if word.startswith('p')]
print(f"Words starting with 'p': {set(p_words)}")


# Part D: Word Length Analysis
print("\n--- Part D: Word Length Analysis ---")
unique_words = set(clean_words)
word_lengths = {word: len(word) for word in unique_words}
print("Word lengths:", word_lengths)

max_length = max(word_lengths.values())
longest_words = [word for word, length in word_lengths.items() if length == max_length]
print(f"Longest words ({max_length} chars): {longest_words}")

print()
min_length = min(word_lengths.values())
shortest_words = [word for word, length in word_lengths.items() if length == min_length]
print(f"Shortest words ({min_length} chars): {shortest_words}")

# Part E: Statistics
print("\n--- Part E: Statistics ---")
print(f"Total words (including duplicates): {len(clean_words)}")
print(f"Number of unique words: {len(unique_words)}")

avg_length = sum(len(word) for word in clean_words) / len(clean_words)
print(f"Average word length: {avg_length:.2f}")

print("\n--- Part F: Most Repeated Word ---")
most_repeated_number = max(word_count.values())
most_repeated_words = [word for word, count in word_count.items() if count == most_repeated_number]
print(f"Most repeated word(s) (appeared {most_repeated_number} times): {most_repeated_words}")
