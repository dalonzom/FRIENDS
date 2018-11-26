import pandas as pd
import numpy as np

#List all of season2's episodes
writer = pd.ExcelWriter("test.xlsx")
season2 = map(str, range(1, 12, 1))
season2 = season2 + ["12-13"] + map(str, range(14,25))

#Read in all the lines
new = []
for season in season2: 
    words = pd.read_excel(season+'.xlsx').dropna()
    new.append(words.iloc[:,0].str.split(":", n = 1, expand = True))
  
results = pd.concat(new)

#Break into speakers and dialogue
transcripts = pd.DataFrame()
transcripts["Speakers"] = results[0].replace(np.nan, '', regex=True)
transcripts["Dialogue"] = results[1].replace(np.nan, '', regex=True)
transcripts["Dialogue"] = transcripts["Dialogue"].str.lower()
print(transcripts)

#List of all characters and common phrases
characters = [ "rach",  "mon","mnca", "phoebe","phoe", "chan", "ross", "joey", "janice", "gunther", "ben", "carol", "susan", "kathy", "julie", "emily",  "richard", "burke"]
phrases = ["lobster", "coffee", "we were on a break", "smelly cat", "ugly naked guy", "ramoray","remoray", "remore", "days of our lives", "chicken", "duck", "pivot", "unagi",
           "joey doesn't share food", "share food", "phalange", "regina", "dinosaur", "paleontologist", "date"]
janiceSpecific = "god" 
chandlerSpecific= "could i be"
joeySpecific = "how you doin" 
monicaSpecific = "i know"
phoebeSpecific = "you guys"

#Create dataframes to store info
characterCount = pd.DataFrame()
characterCount["Characters"] = characters
phraseCounted = pd.DataFrame()
overallPhrases = phrases + [janiceSpecific, chandlerSpecific, joeySpecific, monicaSpecific, phoebeSpecific]
phraseCounted["Phrases"] = overallPhrases

#Count number of lines of each character
seasonCounts = []
for character in characters: 
    seasonCount = len(transcripts["Speakers"].where(transcripts["Speakers"] == character).dropna())
    seasonCount = len([s for s in transcripts["Speakers"] if character in s.lower()])
    seasonCounts.append(seasonCount)
characterCount["Season2"] = seasonCounts
 

#Count number of times phrase is said by any character    
phraseCounts = []
for phrase in phrases:
    phraseCount = len([ s for s in transcripts["Dialogue"] if phrase in s.lower()])
    phraseCounts.append(phraseCount)

#Count number of times phrase is said by Janice
temp = transcripts[transcripts["Dialogue"].str.contains(janiceSpecific)]
count = 0 
phraseCount = temp[temp["Speakers"].str.contains("Janice") | temp["Speakers"].str.contains("janice") | temp["Speakers"].str.contains("JANICE")]
phraseCounts.append(len(phraseCount))
    
   
 #Count number of times phrase is said by Chandler   
temp = transcripts[transcripts["Dialogue"].str.contains(chandlerSpecific)]
phraseCount = temp[temp["Speakers"].str.contains("Chandler") | temp["Speakers"].str.contains("CHAN")]
phraseCounts.append(len(phraseCount))
    
#Count number of times phrase is said by Joey
temp = transcripts[transcripts["Dialogue"].str.contains(joeySpecific)]
phraseCount = temp[temp["Speakers"].str.contains("Joey") | temp["Speakers"].str.contains("JOEY") ]
phraseCounts.append(len(phraseCount))
 
#Count number of times phrase is said by Monica   
temp = transcripts[transcripts["Dialogue"].str.contains(monicaSpecific)]
phraseCount = temp[temp["Speakers"].str.contains("Monica") | temp["Speakers"].str.contains("MON") | temp["Speakers"].str.contains("MNCA")]
phraseCounts.append(len(phraseCount))

#Count number of times phrase is said by Phoebe 
temp = transcripts[transcripts["Dialogue"].str.contains(phoebeSpecific)]
phraseCount = temp[temp["Speakers"].str.contains("Phoebe") | temp["Speakers"].str.contains("PHOE") | temp["Speakers"].str.contains("PHOEBE")]
phraseCounts.append(len(phraseCount))
phraseCounted["Season2"] = phraseCounts

#Print
print(characterCount)
print(phraseCounted)
sheet1 = "Characters"
sheet2 = "Phrases"

#Write to Excel
characterCount.to_excel(writer,sheet1)
phraseCounted.to_excel(writer, sheet2)
writer.save()
