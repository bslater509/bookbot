from stats import count_num_words, count_num_characters, sort_char_count_dict
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

char_count_dict = count_num_characters(book_path)
word_count =count_num_words(book_path)
sorted_char_count =sort_char_count_dict(book_path)
print("""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------""")
print(f"Found {word_count} total words")
print("--------- Character Count -------")
for item in sorted_char_count:
    print(f"{item['char']}: {item['num']}")
print("============= END ===============")
print()