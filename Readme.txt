


							***------------Introduction----------****

This example code extracts news from two websites:
1 - The Times of India
2 - India Today
And computes the virality score from the keywords extracted from following news article.

                                                        ***-------------Process-------------****

The Code uses following Libraries:
1 - pandas
2 - Newspaper3k
3 - requests
4 - BeautifulSoup
  
  ## Also need punkt from nltk module if any device doesn't have it

1. The code counts every unique keywords for all the news article in the dataframe.
2. The score for a particular news article is determined by counting the frequencies of the keywords for the particular news.
3. The score is then normalised between 0 and 1 by MinMax scaling.

                                                       ***------------------Output-----------------***

1. The output is in the form of csv format.
2. It contain 3 columns (Title, keywords, scores)

