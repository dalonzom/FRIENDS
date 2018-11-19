import pandas as pd
import numpy as np

writer = pd.ExcelWriter("word_frequency.xlsx")

characters = ["Rachel", "Monica", "Phoebe", "Chandler", "Ross", "Joey", "Janice", "Gunther", "Ben", "Carol", "Susan", "Kathy", "Julie", "Emily", "Julie", "Richard"]
phrases = ["lobster", "coffee", "we were on a break", "smelly cat", "ugly naked guy", "drake ramoray", "days of our lives", "chicken", "duck", "pivot", "unagi"]
janiceSpecific = "oh my god"
chandlerSpecific= "could i be"
joeySpecific = "how you doin" 
monicaSpecific = "i know"
phoebeSpecific = "you guys"

characterCount = pd.DataFrame()
characterCount["Characters"] = characters

phraseCounted = pd.DataFrame()
overallPhrases = phrases + [janiceSpecific, chandlerSpecific, joeySpecific, monicaSpecific, phoebeSpecific]
phraseCounted["Phrases"] = overallPhrases

for i in range(1,11):
    words = pd.read_excel('data.xlsx', sheet_name='Season'+ str(i))
    new = words.iloc[:,0].str.split(":", n = 1, expand = True) 

    transcripts = pd.DataFrame()
    transcripts["Speakers"] = new[0].replace(np.nan, '', regex=True)
    transcripts["Dialogue"] = new[1].replace(np.nan, '', regex=True)
    transcripts["Dialogue"] = transcripts["Dialogue"].str.lower()
  #  print(transcripts)

    seasonCounts = []
    for character in characters: 
        seasonCount = len(transcripts["Speakers"].where(transcripts["Speakers"] == character).dropna())
        seasonCounts.append(seasonCount)
    characterCount["Season"+str(i)] = seasonCounts
    
    phraseCounts = []
    for phrase in phrases:
        phraseCount = len([ s for s in transcripts["Dialogue"] if phrase in s.lower()])
        phraseCounts.append(phraseCount)

    temp = transcripts[transcripts["Dialogue"].str.contains(janiceSpecific)]
    phraseCount = temp[temp["Speakers"].str.contains("Janice")]
    phraseCounts.append(len(phraseCount))
    
    temp = transcripts[transcripts["Dialogue"].str.contains(chandlerSpecific)]
    phraseCount = temp[temp["Speakers"].str.contains("Chandler")]
    phraseCounts.append(len(phraseCount))
    
    temp = transcripts[transcripts["Dialogue"].str.contains(joeySpecific)]
    phraseCount = temp[temp["Speakers"].str.contains("Joey")]
    phraseCounts.append(len(phraseCount))
    
    temp = transcripts[transcripts["Dialogue"].str.contains(monicaSpecific)]
    phraseCount = temp[temp["Speakers"].str.contains("Monica")]
    phraseCounts.append(len(phraseCount))
    
    temp = transcripts[transcripts["Dialogue"].str.contains(phoebeSpecific)]
    phraseCount = temp[temp["Speakers"].str.contains("Phoebe")]
    phraseCounts.append(len(phraseCount))
    phraseCounted["Season"+str(i)] = phraseCounts

print(characterCount)
print(phraseCounted)