def caseSwitch(phrase):
  str(phrase)
  letters = []
  startsplit = 0
  endsplit = startsplit + 1
  newphrase = []
  for letter in range(len(phrase)):
    
    # Create split up phrase
    s = phrase[startsplit:endsplit]
    letters.append(s)
    startsplit += 1
    endsplit += 1

    if s.isupper():
        newletter = s.lower()
        newphrase.append(newletter)
    elif s.islower():
      newletter = s.upper()
      newphrase.append(newletter)
    else:
      newphrase.append(s)
  print(newphrase)
