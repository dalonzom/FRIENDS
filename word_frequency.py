import pandas as pd
import numpy as np

writer = pd.ExcelWriter("word_frequency.xlsx")

characters = [ "rach",  "mon","mnca", "phoebe","phoe", "chan", "ross", "joey", "janice", "gunther", "ben", "carol", "susan", "kathy", "julie", "emily",  "richard", "burke"]
phrases = ["lobster", "coffee", "we were on a break", "smelly cat", "ugly naked guy", "ramoray","remoray", "remore", "days of our lives", "chicken", "duck", "pivot", "unagi",
           "joey doesn't share food", "share food", "phalange", "regina", "dinosaur", "paleontologist", "date"]
janiceSpecific = "god" 
chandlerSpecific= "could i be"
joeySpecific = "how you doin" 
monicaSpecific = "i know"
phoebeSpecific = "you guys"

characterCount = pd.DataFrame()
characterCount["Characters"] = characters
writer = pd.ExcelWriter("word_frequency.xlsx")

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


    seasonCounts = []
    seasonCounts2 = []
    for character in characters: 
        seasonCount = len(transcripts["Speakers"].where(transcripts["Speakers"] == character).dropna())
        seasonCount = len([s for s in transcripts["Speakers"] if character in s.lower()])

        seasonCounts.append(seasonCount)
    characterCount["Season"+str(i)] = seasonCounts
 
    
    phraseCounts = []
    for phrase in phrases:
        phraseCount = len([ s for s in transcripts["Dialogue"] if phrase in s.lower()])
        phraseCounts.append(phraseCount)

    temp = transcripts[transcripts["Dialogue"].str.contains(janiceSpecific)]
    count = 0 
    phraseCount = temp[temp["Speakers"].str.contains("Janice") | temp["Speakers"].str.contains("janice") | temp["Speakers"].str.contains("JANICE")]
    phraseCounts.append(len(phraseCount))
    
   
    
    temp = transcripts[transcripts["Dialogue"].str.contains(chandlerSpecific)]
    phraseCount = temp[temp["Speakers"].str.contains("Chandler") | temp["Speakers"].str.contains("CHAN")]
    phraseCounts.append(len(phraseCount))
    
    temp = transcripts[transcripts["Dialogue"].str.contains(joeySpecific)]
    phraseCount = temp[temp["Speakers"].str.contains("Joey") | temp["Speakers"].str.contains("JOEY") ]
    phraseCounts.append(len(phraseCount))
    
    temp = transcripts[transcripts["Dialogue"].str.contains(monicaSpecific)]
    phraseCount = temp[temp["Speakers"].str.contains("Monica") | temp["Speakers"].str.contains("MON") | temp["Speakers"].str.contains("MNCA")]
    phraseCounts.append(len(phraseCount))
    
    temp = transcripts[transcripts["Dialogue"].str.contains(phoebeSpecific)]
    phraseCount = temp[temp["Speakers"].str.contains("Phoebe") | temp["Speakers"].str.contains("PHOE") | temp["Speakers"].str.contains("PHOEBE")]
    phraseCounts.append(len(phraseCount))
    phraseCounted["Season"+str(i)] = phraseCounts

print(characterCount)
print(phraseCounted)
sheet1 = "Characters"
sheet2 = "Phrases"
characterCount.to_excel(writer, sheet1)
phraseCounted.to_excel(writer, sheet2)
writer.save()
