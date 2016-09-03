from tweetGenerator import *

def main():
    t = TrumpTweetGenerator()
    t.loadTweets("realDonaldTrumpTweets2")
    t.processTweets()
    print(t.generateTrumpTweet())

if __name__ == "__main__":
    main()