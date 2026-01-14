# String Utility Functions
# Common string manipulation functions for quick use

def reverse_string(s):
    """Reverse a string."""
    return s[::-1]

def is_palindrome(s):
    """Check if string is palindrome (ignoring spaces and case)."""
    clean = s.replace(' ', '').lower()
    return clean == clean[::-1]

def count_vowels(s):
    """Count the number of vowels in a string."""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

def capitalize_words(s):
    """Capitalize first letter of each word."""
    return ' '.join(word.capitalize() for word in s.split())

def remove_duplicates(s):
    """Remove duplicate characters from string."""
    seen = set()
    return ''.join(char for char in s if not (char in seen or seen.add(char)))

if __name__ == '__main__':
    # Test cases
    print(reverse_string('hello'))  # olleh
    print(is_palindrome('racecar'))  # True
    print(count_vowels('hello world'))  # 3
    print(capitalize_words('hello world python'))  # Hello World Python
    print(remove_duplicates('programming'))  # progamin
