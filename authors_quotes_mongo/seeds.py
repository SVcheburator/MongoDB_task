from models import Authors, Quotes
from datetime import datetime
import connect
import json

with open('json_files/quotes.json', 'r') as quotes_file:
    quotes = json.load(quotes_file)

with open('json_files/authors.json', 'r') as authors_file:
    authors = json.load(authors_file)

def get_date(date_str):
    date_splt_lst = date_str.split()
    month_str = date_splt_lst[0]
    month = datetime.strptime(month_str, "%B").month
    day = int(date_splt_lst[1].rstrip(','))
    year = int(date_splt_lst[2]) 
    date = datetime(year=year, month=month, day=day).date()
    return date

def get_author(author_name):
    for auth_from_lst in authors_list:
        if auth_from_lst.fullname == author_name:
            return auth_from_lst

authors_list = []
for author in authors:
    a = Authors(fullname=author['fullname'], born_date=get_date(author['born_date']), \
             born_location=author['born_location'], description=author['description']).save()
    
    authors_list.append(a)

quotes_list = []
for quote in quotes:
    q = Quotes(tags=quote['tags'], author=get_author(quote['author']), quote=quote['quote']).save()

    quotes_list.append(q)