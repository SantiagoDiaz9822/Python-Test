import re
from collections import Counter

def is_valid_string(s: str) -> bool:
    if len(s) < 6:
        return False
    
    numbers = re.findall(r'\d', s)
    if not (2 <= len(numbers) <= 3):
        return False
    
    if re.search(r'\d{2,}', s):
        return False
    
    return True

def word_frequency(text: str):
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text.lower()) 
    words = text.split()
    freq = Counter(words)
    
    print("Word Frequencies:")
    for word, count in sorted(freq.items(), key=lambda x: x[1], reverse=True):
        print(f"{word}: {count}")


#testing
text = "Hello world! This is a test. Hello, this test is only a test."
word_frequency(text)

test_strings = ["abc12d", "1a2b3c", "abc123", "ab1c2d", "12ab34"]
for s in test_strings:
    print(f"'{s}' es válido? {is_valid_string(s)}")