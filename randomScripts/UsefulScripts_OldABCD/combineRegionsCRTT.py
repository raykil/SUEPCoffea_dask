import os

output    = "RunII_CRTT"
cardList  = [] 

if not(os.path.isdir(output)): os.mkdir(output)


for f in os.listdir("RunII"):
  if not ("txt" in f): continue
  if not ("CombinedSR_" in f): continue
  cardList.append(f)

os.chdir("RunII_CRTT")
for card in cardList:
  if os.path.isfile("RunII_CRTT/%s"%card.replace("SR","SRTT")): continue
  print("combineCards.py SR=%s CRTT=%s >> %s"%('../RunII/'+card, '../RunII/'+card.replace("SR", "CRTT"), card.replace("SR","SRTT")))
  os.system("combineCards.py SR=%s CRTT=%s >> %s"%('../RunII/'+card, '../RunII/'+card.replace("SR", "CRTT"), card.replace("SR","SRTT")))