a = {"a" : 1 , "b":2}

print(ord("A"))


sentence = "Ali ata bak"

def func(sentence) :
  result = ""
  for i in sentence :
    if i.isalpha() :
      result += str(ord(i.upper()) - 64 ) + " "
  return result.strip()

func(sentence)
