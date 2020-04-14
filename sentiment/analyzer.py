from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

class Analyzer:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def sentiment(self, article):
        vs = self.analyzer.polarity_scores(article)

        # Below utilizes customizable sentiment ratings. Currently tuned to default.

        if vs['compound'] >= 0.05:
            return { "num_value": vs['compound'], "rating": "pos" }
        elif vs['compound'] <= -0.05:
            return { "num_value": vs['compound'], "rating": "neg" }
        else:
            return { "num_value": vs['compound'], "rating": "neu" }

        # Below utilizes built-in sentiment ratings

        # if vs['pos'] > vs['neu'] and vs['pos'] > vs['neg']:
        #     return 'pos'
        # if vs['neu'] > vs['neg']:
        #     return 'neu'
        # return 'neg'