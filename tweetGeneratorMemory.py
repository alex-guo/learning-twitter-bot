import json
import re
from random import randint

class TweetGeneratorMemory:
    def __init__(self):
        self.initialStates = []
        self.rawTweets = []
        self.markovDictionary = {}

    def loadTweets(self, fileName):
        self.rawTweets = self.loadJSON(fileName)

    def updateDictionary(self, priorWord, word):
        if priorWord in self.markovDictionary:
            self.markovDictionary[priorWord].append(word)
        else:
            self.markovDictionary.update({priorWord:[word]})

    def processTweets(self):
        endingCharacters = [".", "?", "!"]
        for tweet in self.rawTweets:
            
            priorWord = None
            for word in tweet.split() + [None]:
                if priorWord == None and word != None: #start of sentence
                    self.initialStates.append(word)
                    priorWord = word
                elif word == None: #end of sentence
                    self.updateDictionary(priorWord, "END_OF_SENTENCE")
                    priorWord = None
                elif word[-1] in endingCharacters:
                    self.updateDictionary(priorWord, word)
                    self.updateDictionary(word, "END_OF_SENTENCE")
                    priorWord = None
                else:
                    self.updateDictionary(priorWord, word)
                    priorWord = word


    def loadTweetGen(self, fileName):
        pass

    def saveTweetGen(self, fileName):
        pass

    def generateTweet(self):
        word = self.initialStates[randint(0, len(self.initialStates) - 1)]
        tweet = [word]
        while word is not "END_OF_SENTENCE":
            randomIndex = randint(0,len(self.markovDictionary[word]) - 1)
            word = self.markovDictionary[word][randomIndex]
            if not word == "END_OF_SENTENCE":
                tweet.append(word)
        return " ".join(tweet)


    def loadJSON(self, fileName):
        with open(fileName, 'r') as fileHandler:
            jsonData = json.load(fileHandler)
        return jsonData

    def saveJSON(self, jsonData, fileName):
        with open(fileName, 'w') as fileHandler:
            json.dump(jsonData, fileHandler)
        print("Successfully Saved as json in {}".format(fileName))

def main():
    t = TweetGeneratorMemory()
    t.loadTweets("officialjadenTweets2")
    t.processTweets()
    print(t.generateTweet())

if __name__ == '__main__':
    main()