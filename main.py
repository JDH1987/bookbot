import sys
from stats import count_words
from stats import count_characters
from stats import sort_characters



def get_book_text(path):
	"""Reads a file and returns its content as a string"""
	with open(path, 'r') as f:
		return f.read()

def analyze_book(path):
	try:
		with open(path, 'r') as file:
			return file.read()
	except FileNotFoundError:
		print(f"Error: The file {path} does not exist.")
		sys.exit(1)

def main():

	# Check if the correct number of command line arguments are given

	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

	# The path to the book file (second argument)
	book_path = sys.argv[1]

	# analyze the book
	analyze_book(book_path)

	book_text = get_book_text(sys.argv[1])
	word_count = count_words(book_text)
	char_count = count_characters(book_text)

	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {sys.argv[1]} ...")
	print("----------- Word Count ----------")
	print(f'Found {word_count} total words')
	print("--------- Character Count -------")

	sorted_chars = sort_characters(char_count)

	for item in sorted_chars:
		print(f"{item['character']}: {item['count']}")

	print("============= END ===============")


if __name__ == "__main__":
	main()
