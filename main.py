def count_words(book_contents):
  words = list(book_contents.split())
  return len(words)
def count_characters(book_contents):
  chars_dict = dict()
  for char in book_contents:
    char = char.lower()
    if char != ' ' and char != '.' and char != '#':
      if char not in chars_dict:
        chars_dict[char] = 1
      else:
        chars_dict[char] += 1
  return chars_dict

def report(book_contents):
  words = count_words(book_contents)
  chars_freq = count_characters(book_contents)

  print("--- Begin report of books/frankenstein.txt ---")
  print(f"{words} words found in the document")

  for char, count in chars_freq.items():
    print(f"The '{char}' character was found {count} times")

  print("--- End report ---")

def main():
  with open("./books/frankenstein.txt") as f:
    file_contents = f.read()
  report(file_contents)

main()