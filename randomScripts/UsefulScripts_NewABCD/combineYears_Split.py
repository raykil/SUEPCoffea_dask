import os

years     = ["2016", "2016APV", "2017", "2018"]
output    = "RunII"
cardList  = {i:[] for i in years}

if not(os.path.isdir(output)): os.mkdir(output)


for y in years:
  for f in os.listdir(y):
    if not ("txt" in f): continue
    if not ("Combined" in f): continue
    if not("Split" in f): continue 
    cardList[y].append(f)

combinable = list(set(cardList["2016"]).intersection(cardList["2016APV"]).intersection(cardList["2017"]).intersection(cardList["2018"]))
os.chdir("RunII")
for card in combinable:
  #if not("CombinedCRDY_SUEP_leptonic_mS125_mD4.00_T8.00.txt" in card): continue
  if os.path.isfile("RunII/%s"%card): continue
  
  print("combineCards.py UL16=../%s/%s UL16APV=../%s/%s UL17=../%s/%s UL18=../%s/%s >> %s"%("2016", card, "2016APV", card, "2017", card, "2018", card, card))
  os.system("combineCards.py UL16=../%s/%s UL16APV=../%s/%s UL17=../%s/%s UL18=../%s/%s >> %s"%("2016", card, "2016APV", card, "2017", card, "2018", card, card))
  #os.system("combineCards.py UL16=%s/%s UL16APV=%s/%s UL17=%s/%s UL18=%s/%s >> RunII/%s"%("2016", card, "2016APV", card, "2017", card, "2018", card, card))
