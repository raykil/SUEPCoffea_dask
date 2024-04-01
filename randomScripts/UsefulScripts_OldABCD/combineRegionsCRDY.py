import os

output    = "RunII_CRDY"
cardList  = [] 

if not(os.path.isdir(output)): os.mkdir(output)


for f in os.listdir("RunII"):
  if not ("txt" in f): continue
  if not ("CombinedSR_" in f): continue
  cardList.append(f)

os.chdir("RunII_CRDY")
for card in cardList:
  if os.path.isfile("RunII_CRDY/%s"%card.replace("SR","SRDY")): continue
  print("combineCards.py SR=%s CRDY=%s >> %s"%('../RunII/'+card, '../RunII/'+card.replace("SR", "CRDY"), card.replace("SR","SRDY")))
  os.system("combineCards.py SR=%s CRDY=%s >> %s"%('../RunII/'+card, '../RunII/'+card.replace("SR", "CRDY"), card.replace("SR","SRDY")))