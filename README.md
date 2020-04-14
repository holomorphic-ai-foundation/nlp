# Natural Language Processing
> A Holomorphic AI Foundation collaborative project

## Running locally

### Install python requirements
`pip3 install -r requirements.txt`

### Run full scraper/analyzer
`python3 run_scrapers.py`

### Load the analyzer manually
```
python3
from sentiment.analyzer import Analyzer
analyzer = Analyzer()
```
Then you can use `analyzer.sentiment()` to get the sentiment of any string:

`analyzer.sentiment('This is pretty cool!')`
> 'pos'

`analyzer.sentiment("this isn't that cool")`
> 'neg`
