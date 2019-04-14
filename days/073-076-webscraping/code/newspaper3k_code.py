import newspaper

from newspaper import Article

URL = 'https://www.news.com.au/travel/travel-updates/the-sultan-of-brunei-created-a-30-million-gold-coast-real-estate-nightmare/news-story/8e4a4e1ee4137a9b014ce73563fda376'

article = Article(URL)

article.download()

article.html

article.parse()

article.authors

article.publish_date

article.text

article.top_image

article.movies

article.summary
