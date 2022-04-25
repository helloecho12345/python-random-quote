import random

def primary():
  # print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = 13 # holds the highest index for the array
  # last = len(quotes) - 1   # change the last variable to update automatically if quotes are added or removed from text file
  rnd = random.randint(0, last)   # random number is stored in rnd
  
  print(quotes[rnd])   # prints random quote
  # print(quotes[-1]) # prints last array value

if __name__== "__main__":
  primary()
