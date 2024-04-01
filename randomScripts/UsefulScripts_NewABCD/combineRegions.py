import os

output    = "RunII"
cardList  = [] 

if not(os.path.isdir(output)): os.mkdir(output)


for f in os.listdir("RunII"):
  if not ("txt" in f): continue
  if not ("CombinedSR" in f): continue
  cardList.append(f)

os.chdir("RunII")
for card in cardList:
  if os.path.isfile("RunII/%s"%card): continue
  print("combineCards.py SR=%s CRDY=%s CRTT=%s >> %s"%(card, card.replace("SR", "CRDY"), card.replace("SR", "CRTT"), card.replace("SR","SRCR")))
  os.system("combineCards.py SR=%s CRDY=%s CRTT=%s >> %s"%(card, card.replace("SR", "CRDY"), card.replace("SR", "CRTT"), card.replace("SR","SRCR")))