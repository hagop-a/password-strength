# Module pwalgorithms

# get words from password dictionary file
def get_dictionary():
  words = []
  dictionary_file = open("dictionary.txt")
  for line in dictionary_file:
    # store word, ommitting trailing new-line
    words.append(line[:-1])
  dictionary_file.close()
  return words
 
def get_digits():
  digits = []
  digits_file = open("finddigits.txt")
  for line in digits_file:
    digits.apeend(line[:-1])
  digits_file.close()
  return words

# analyze a one-word password
def one_word(password):
  words = get_dictionary()
  guesses = 0
  # get each word from the dictionary file
  for w in words:
    guesses += 1
    if (w == password):
      return True, guesses
  return False, guesses

# analyze a two-word password
def two_word(password):
  words = get_dictionary()
  guesses = 0
  # get each word from the dictionary file
  for w1 in words:
    for w2 in words:
      phrase = w1 + w2
      guesses += 1
      if (phrase == password):
        return True, guesses
  return False, guesses
'''
def two_words_and_digit(password):
  words = get_dictionary()
  digits = get_digits()
  guesses = 0
  # get each word from the dictionary file
  for w1 in words:
    for w2 in words:
      for w3 in digits:
        phrase = w1 + w2 + w3
        guesses += 1
        if (phrase == password):
          return True, guesses
  return False, guesses'''