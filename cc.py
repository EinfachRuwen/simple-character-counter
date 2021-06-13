import pyperclip

def repeat():
  # Starting
  print('This Python script tells you how many characters your entered text has. Thank you for using this script.')
  print('Made by byZero')
  print("\n")

  # Enter some text
  x = input("Enter your Text... | ")

  # Printing the Number of Characters
  ch = len(x)
  print("\n")
  print(f'Your entered text is {ch} characters long')
  pyperclip.copy(ch)
  
  # Asking again
  print("\n")

  # Repeating
  repeat()

# Run the script
repeat()