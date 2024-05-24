def giveName(email):
  firstname = ""
  sep = 0
  lastname = ""
  if((email.count("_") >= 2) or (email.count(".") >= 2)):
    for i in range(0, len(email)):
      if((email[i] == "." or email[i] == "_") and firstname == ""):
        firstname = email[0: i]
      elif((email[i] == "." or email[i] == "_") and not (email[i + 2] == "." or email[i + 2] == "_")):
        sep = i + 1
      elif(email[i] == "@"):
        lastname = email[sep : (i)]
    return firstname + " " + lastname
  else:
    for i in range(0, len(email)):
      if((email[i] == "." or email[i] == "_") and firstname == ""):
        firstname = email[0: i]
        sep = i + 1
      elif(email[i] == "@"):
        lastname = email[sep : (i)]
    return firstname + " " + lastname

