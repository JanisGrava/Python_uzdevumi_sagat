""" 
Iegūt ziņas, izmantojot RSS plūsmu no google.lv.

Kas ir RSS?- specials formāts datu izplatīšanai

"""


import feedparser

#URL uz RSS plūsmu
rss_url='https://news.google.com/home?hl=en-LV&gl=LV&ceid=LV:en'

#iegūsim RSS plūsmaS DATUS
kkk=feedparser.parse(rss_url)

#parāda un jānoformē

for entry in kkk.entries:
    print("Virsraksts:", entry.title)
    print("Saite:", entry.link)
    print('\n')