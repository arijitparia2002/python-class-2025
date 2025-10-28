# String Filter Operations

# Filter words starting with specific letter
words = ["apple", "banana", "apricot", "cherry", "avocado"]

a_words = [word for word in words if word.startswith('a')]
print("Words starting with 'a':", a_words)
# Output: ['apple', 'apricot', 'avocado']

# Get words with specific length
five_letter_words = [word for word in words if len(word) == 5]
print("5-letter words:", five_letter_words)
# Output: ['apple']

# Filter and capitalize
sentences = ["hello world", "python is great", "ai", "machine learning"]
long_caps = [s.upper() for s in sentences if len(s) > 5]
print(long_caps)
# Output: ['HELLO WORLD', 'PYTHON IS GREAT', 'MACHINE LEARNING']