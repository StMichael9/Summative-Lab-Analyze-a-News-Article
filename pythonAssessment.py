def count_specific_word(text, word):
    """
    Return how many times 'word' appears in the text.
    - Convert text to lowercase
    - Remove punctuation
    - Split into words
    - Count matches of the target word
    """
    # convert to lower case
    text_lower = text.lower()
    word_lower = word.lower()

    # remove punctuation
    for p in ".,!?;:\"'()":
        text_lower = text_lower.replace(p, "")

    # split into words
    word_list = text_lower.split()

    # count matches
    return word_list.count(word_lower)


def identify_most_common_word(text):
    """
    Return the single most common word in the text.
    - Clean text (lowercase, remove punctuation)
    - Split into words
    - Use a dictionary to count occurrences
    - Return the word with the highest count
    """

    # lowercase
    text_lower = text.lower()

    # remove punctuation
    for p in ".,!?;:\"'()":
        text_lower = text_lower.replace(p, "")

    # split into words
    text_list = text_lower.split()

    # count words
    word_count = {}

    for word in text_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # find the most common word
    most_common = None
    highest_count = 0

    for word in word_count:
        if word_count[word] > highest_count:
            most_common = word
            highest_count = word_count[word]

    return most_common



# 3. Calculate the average word length

def calculate_average_word_length(text):
    """
    Return the average length of all words as a float.
    - Clean text
    - Split into words
    - Add up total characters
    - Divide by number of words
    """
    pass  # TODO: implement



# 4. Count the number of paragraphs

def count_paragraphs(text):
    """
    Return the number of paragraphs.
    - Paragraphs are separated by blank lines
    - Split text by '\n\n'
    - Count non-empty sections
    """
    pass  # TODO: implement



# 5. Count the number of sentences

def count_sentences(text):
    """
    Return the number of sentences.
    - Sentences end with '.', '?', or '!'
    - Loop through characters and count sentence-ending punctuation
    """
    pass  # TODO: implement
