# Module pwalgorithms

# get words from password dictionary file
def get_dictionary():
  words = []
  dictionary_file = open("dictionary.txt")
  for line in dictionary_file:
    # store word, omitting trailing new-line
    words.append(line[:-1])
  dictionary_file.close()
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

def two_word(password):
  words = get_dictionary()
  guesses = 0
  for w in words:
    for x in words:
      guesses += 1
      if (str(w + x) == password):
        return True, guesses
  return False, guesses

def two_word_number(password):
  words = get_dictionary()
  guesses = 0
  for w in words:
    for x in words:
      for i in range(0, 9):
        guesses += 1
        if (str(w + x + str(i)) == password):
          return True, guesses
  return False, guesses

def two_word_number_symbol(password):
  words = get_dictionary()
  guesses = 0
  symbols = "!@#$%^&*()"
  for w in words:
    for x in words:
      for i in range(0, 9):
        for s in symbols:
          guesses += 1
          if (str(w + x + str(i) + s) == password):
            return True, guesses
  return False, guesses

def hacking(password):
  words = get_dictionary()
  guesses = 0
  symbols = "!@#$%^&*()"
  numbers = "0123456789"
  for w1 in words:
    for w2 in words:
      for n in numbers:
        for s in symbols:
          guesses += 1
          if (str(w1 + w2 + n + s) == password):
            return True, guesses
  return False, guesses