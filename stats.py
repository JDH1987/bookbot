def count_words(text):
        """
        Counts the number of words in a string.

        Args:
        text: The string to count words in.

        Returns:
        The number of words in the string.
        """
        words = text.split()
        return len(words)

def count_characters(text):
	"""
	Convert text to lower case.

	"""
	text = text.lower()
	char_count = {}

	"""
	Count each character

	"""
	for char in text:
		if char in char_count:
			char_count[char] += 1
		else:
			char_count[char] = 1

	return char_count

def sort_characters(char_count_dict):

	sorted_count = [
	{"character": char, "count": count}
	for char, count in char_count_dict.items() if char.isalpha()
	]

	sorted_count.sort(key=lambda x: x["count"], reverse=True)

	return sorted_count
