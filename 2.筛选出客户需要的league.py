# coding=utf-8
import requests
import json
from bs4 import BeautifulSoup
import re
import codecs

f = codecs.open(u'F:\\goaloo\\2.客户要求的赛事.txt','r','utf-8')
f1 = codecs.open(u'F:\\goaloo\\1.赛季.txt','r','utf-8')
f2 = codecs.open(u"F:\\goaloo\\3.客户要求的赛事.txt",'w','utf-8')
S =set()
lines = f.readlines()
for line in lines:
    if line is None or line =="":
        continue
    if line.find(',')==-1:
        continue
    words = line.split(',')
    S.add(words[0])

lines = f1.readlines()
for line in lines:
    if line.find(u'^')==-1:
        f2.write(line)
        continue
    leagueNo = line.split('^')[0]
    if leagueNo in S:
        f2.write(line)
