import tkinter as tk   #pycharmde pencere kütüphanesi
import nltk # doğal dil işlemeye yönelik bir kitaplıklar ve programlar paketidir. Sınıflandırma, tokenizasyon, kök çıkarma, etiketleme, ayrıştırma ve anlamsal akıl yürütme işlevlerini destekler.
from textblob import TextBlob   #metin verilerini işlemek için kullanılan bir Python kütüphanesidir , duygu analizi için kullanılır.
from newspaper import Article   # makaleleri çıkarmak ayrıştırmak ve özet çıkarmak için kullanılır.
import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize
url = "https://tr.wikipedia.org/wiki/Bill_Gates"


article= Article(url)
article.download()
article.parse()
article.nlp()
key = article.keywords
print(f"Title = {article.title}")
print(f"Text publication date = {article.publish_date}")
print(f"Text summarize = {article.summary}")
print(f"text  keyword = {article.keywords}")
dataframe = pd.read_csv('tr-stopwords.txt',sep=';')
