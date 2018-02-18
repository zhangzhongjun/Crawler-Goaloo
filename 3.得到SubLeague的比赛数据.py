# coding=utf-8
import json
import requests
import re
import CsvUtils
from bs4 import BeautifulSoup

import codecs
f = codecs.open(u'F:\\goaloo\\3.客户要求的赛事.txt','r','utf-8')
lines = f.readlines()
f2 = codecs.open(u"F:\\goaloo\\4.错误的.txt",'a','utf-8')
baseUrl = 'http://info.goaloo.com/en/SubLeague/%s/%s.html'
baseUrl2 = "http://info.goaloo.com/jsData/matchResult/%s/s%s_%s.js"
requireSeasons = {'2009-2010','2010-2011','2011-2012','2012-2013','2013-2014','2014-2015','2015-2016','2016-2017'}
requireSeasons2 = {'2009','2010','2011','2012','2013','2014','2015','2016','2017'}

for s in lines[::1]:
    if s.find('^')==-1:
        continue
    words = s.split('^')
    if words[3] != u'0':
        continue
    path = 'F://goaloo//ju_SubLeague//'+words[0]+u"_"+words[2]+'.csv'
    cu = CsvUtils.CsvUtils(path)
    leagueNo = words[0]
    seasons = json.loads(words[4].replace('\'','\"'))
    for season in seasons:
        if season in requireSeasons or season in requireSeasons2:
            url = baseUrl %(season,leagueNo)
            
            res = requests.get(url)
            print url,res.status_code
            content = res.text
            soup = BeautifulSoup(content,'html.parser',from_encoding='utf-8')
            firstUrl = soup.find('script',src=re.compile('/jsData/matchResult/.*'))[u'src']
            firstUrl = u'http://info.goaloo.com'+firstUrl

            res = requests.get(firstUrl)
            content = res.text
            if content.find('var arrSubLeague')!=-1:
                content = content.split('\n')
                #{子联赛No:子联赛Name}
                subLeagues = {}
                #[联赛No 联赛Name]
                league=[]
                
                for line in content:
                    if(line.find('arrLeague')!=-1):
                        line = line[line.find('['):line.rfind(']')+1:1]
                        line = line.replace('\'','\"')
                        line = json.loads(line)
                        league.append(line[0])
                        league.append(line[3])
                        break
                
                for line in content:
                    if (line.find('arrSubLeague')!=-1):
                        line = line[line.find('['):line.rfind(']')+1:1]
                        line = line.replace('\'','\"')
                        line = json.loads(line)
                        for lineline in line:
                            subLeagues[lineline[0]] = lineline[3]
                
                for subLeagueNo,subLeagueName in subLeagues.items():
                    needUrl = baseUrl2 %(season,leagueNo,str(subLeagueNo))
                    res = requests.get(needUrl)
                    print needUrl,res.status_code
                    content = res.text
                    content = content.split('\n')
                    #{队伍No:队伍Name}
                    teams={}
                    for line in content:
                        if(line.find('arrTeam')!=-1):
                            line = line[line.find('['):line.rfind(']')+1:1]
                            line = line.replace('\'','\"')
                            line = json.loads(line)
                            for lineline in line:
                                teams[lineline[0]] = lineline[3]
                            break
                    for line in content:
                        if(line.find('jh')!=-1):
                            #轮次
                            round = line[line.find('[')+1:line.find(']'):1]
                            round = round.replace('\"','')
                        
                            jh = line[line.find('=')+1:line.rfind(']')+1:1]
                            jh = jh.replace('\'','\"')
                            while jh.find(',,')!=-1:
                                jh = jh.replace(',,',',1,')
                            jh = re.sub('<a .*?</a>', '',jh)
                            try:
                                data = json.loads(jh)
                            except:
                                print round,u"不能加载成list",jh
                            for d in data:
                                if str(type(d[4]))=="<type 'list'>":
                                    for i in range(4,len(d)):
                                        bisai = d[i]
                                        #子赛 主场 客场 时间 比分
                                        try:
                                            if bisai[6].find('-')!=-1:
                                                try:
                                                    res=[unicode(words[0],'utf-8'),unicode(words[1],'utf-8'),unicode(words[2],'utf-8'),unicode(words[3],'utf-8'),season,subLeagueName,round,bisai[3],teams[bisai[4]],teams[bisai[5]],bisai[6].split('-')[0],bisai[6].split('-')[1]]
                                                except:
                                                    res=[words[0],words[1],words[2],words[3],season,subLeagueName,round,bisai[3],teams[bisai[4]],teams[bisai[5]],bisai[6].split('-')[0],bisai[6].split('-')[1]]
                                            else:
                                                try:
                                                    res=[unicode(words[0],'utf-8'),unicode(words[1],'utf-8'),unicode(words[2],'utf-8'),unicode(words[3],'utf-8'),season,subLeagueName,round,bisai[3],teams[bisai[4]],teams[bisai[5]],u'cancel',u'cancel']
                                                except:
                                                    res=[words[0],words[1],words[2],words[3],season,subLeagueName,round,bisai[3],teams[bisai[4]],teams[bisai[5]],u'cancel',u'cancel']
                                            cu.collect(res)
                                        except Exception as e:
                                            print round,u'获取信息错误',e
                                            print bisai 
                                else:
                                    for d in data:
                                        #子赛 主场 客场 时间 比分
                                        try:
                                            if d[6].find('-')!=-1:
                                                try:
                                                    res=[unicode(words[0],'utf-8'),unicode(words[1],'utf-8'),unicode(words[2],'utf-8'),unicode(words[3],'utf-8'),season,subLeagueName,round,d[3],teams[d[4]],teams[d[5]],d[6].split('-')[0],d[6].split('-')[1]]
                                                except:
                                                    res=[words[0],words[1],words[2],words[3],season,subLeagueName,round,d[3],teams[d[4]],teams[d[5]],d[6].split('-')[0],d[6].split('-')[1]]
                                            else:
                                                try:
                                                    res=[unicode(words[0],'utf-8'),unicode(words[1],'utf-8'),unicode(words[2],'utf-8'),unicode(words[3],'utf-8'),season,subLeagueName,round,d[3],teams[d[4]],teams[d[5]],u'cancel',u'cancel']
                                                except:
                                                    res=[words[0],words[1],words[2],words[3],season,subLeagueName,round,d[3],teams[d[4]],teams[d[5]],u'cancel',u'cancel']
                                            cu.collect(res)
                                        except Exception as e:
                                            print round,u'获取信息错误2',e
                                            print d
                cu.write()
            else:
                print "ERROR" , s
                f2.write(s+u"\r\n")

