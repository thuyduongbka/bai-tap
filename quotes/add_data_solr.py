import pysolr
import json


with open('authors.json', 'r') as author:
    authors = json.load(author)
with open('quotes.json', 'r') as quote:
    quotes = json.load(quote)    

dataQuotes = []
for quote in quotes: 
     tags = " ".join(quote['tags'])
     text = quote['text'] + " " + tags + " " + quote['author']
     res = {
         'text' : text
     }
     dataQuotes.append(res)

solr = pysolr.Solr('http://localhost:8983/solr/nhom-5-quotes/')
solr.ping()
solr.add(dataQuotes)
solr.commit()


dataAuthors = []
for author in authors: 
     authorDetail = author['name'] + " " + author['birthdate'] + " " + author['bio']
     res = {
         'text' : authorDetail
     }
     dataAuthors.append(res)

solr = pysolr.Solr('http://localhost:8983/solr/nhom-5-authors/')
solr.ping()
solr.add(dataAuthors)
solr.commit()