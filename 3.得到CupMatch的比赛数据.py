# coding=utf-8
import json
import requests
import re
import CsvUtils

import codecs
f = codecs.open(u'F:\\goaloo\\3.客户要求的赛事.txt','r','utf-8')
lines = f.readlines()
f2 = codecs.open(u"F:\\goaloo\\4.错误的.txt",'a','utf-8')
baseUrl = 'http://info.goaloo.com/jsData/matchResult/%s/c%s.js'
requireSeasons = {'2009-2010','2010-2011','2011-2012','2012-2013','2013-2014','2014-2015','2015-2016','2016-2017'}
requireSeasons2 = {'2009','2010','2011','2012','2013','2014','2015','2016','2017'}

for s in lines:
    if s.find('^')==-1:
        continue
    words = s.split('^')
    if words[3] != u'2':
        continue
    path = 'F://goaloo//ju_CupMatch//'+words[0]+u"_"+words[2]+'.csv'
    cu = CsvUtils.CsvUtils(path)
    leagueNo = words[0]
    seasons = json.loads(words[4].replace('\'','\"'))
    for season in seasons:
        if season in requireSeasons or season in requireSeasons2:
            url = baseUrl %(season,leagueNo)
            
            res = requests.get(url)
            print url,res.status_code
            content = res.text
            #print content
            if content.find('arrCupKind')==-1:
                print 'error',s
                f2.write(s)
                f2.write(url)
                continue
            content = content.split('\n')
            
            #{子杯赛ID,子杯赛Name}
            subCups = {}
            #{团队ID,团队Name}
            teams={}
            #[杯赛ID,杯赛全称,杯赛简称]
            cup=[]
            for line in content:
                if(line.find('arrCup')!=-1):
                    line = line[line.find('['):line.rfind(']')+1:1]
                    line = line.replace('\'','\"')
                    line = json.loads(line)
                    cup.append(line[0])
                    cup.append(line[3])
                    cup.append(line[6])
                    break
            for line in content:
                if (line.find('arrCupKind')!=-1):
                    line = line[line.find('['):line.rfind(']')+1:1]
                    line = line.replace('\'','\"')
                    line = json.loads(line)
                    for lineline in line:
                        subCups[lineline[0]] = lineline[4]
                        
            for line in content:
                if(line.find('arrTeam')!=-1):
                    line = line[line.find('['):line.rfind(']')+1:1]
                    line = line.replace('\'','\"')
                    line = json.loads(line)
                    for lineline in line:
                        teams[lineline[0]] = lineline[3]
                        
            for line in content:
                if(line.find('jh')!=-1):
                    subCup = line[line.find('[')+1:line.find(']'):1]
                    if subCup.find('S')!=-1:
                        print u'什么情况'
                        continue
                    subCup = subCup.replace('\"','')
                    subCup1 = re.sub('\D','',subCup)
                
                    jh = line[line.find('=')+1:line.rfind(']')+1:1]
                    jh = jh.replace('\'','\"')
                    while jh.find(',,')!=-1:
                        jh = jh.replace(',,',',1,')
                    jh = re.sub('<a .*?</a>', '',jh)
                    try:
                        data = json.loads(jh)
                    except:
                        print u"不能加载成list",s
                    #print data
                    for d in data:
                        if str(type(d[4]))=="<type 'list'>":
                            for i in range(4,len(d)):
                                bisai = d[i]
                                #子赛 主场 客场 时间 比分
                                try:
                                    if bisai[6].find('-')!=-1:
                                        res=[words[0],words[1],words[2],words[3],season,subCups[int(subCup1)],u"",bisai[3],teams[bisai[4]],teams[bisai[5]],bisai[6].split('-')[0],bisai[6].split('-')[1]]
                                    else:
                                        res=[words[0],words[1],words[2],words[3],season,subCups[int(subCup1)],u"",bisai[3],teams[bisai[4]],teams[bisai[5]],u'cancel',u'cancel']
                                    cu.collect(res)
                                except Exception as e:
                                    print subCup,u'获取信息错误',e
                                    print bisai 
                        else:
                            for d in data:
                                #子赛 主场 客场 时间 比分
                                try:
                                    if d[6].find('-')!=-1:
                                        res=[words[0],words[1],words[2],words[3],season,subCups[int(subCup1)],u"",d[3],teams[d[4]],teams[d[5]],d[6].split('-')[0],d[6].split('-')[1]]
                                    else:
                                        res=[words[0],words[1],words[2],words[3],season,subCups[int(subCup1)],u"",d[3],teams[d[4]],teams[d[5]],u'cancel',u'cancel']
                                    cu.collect(res)
                                except Exception as e:
                                    print subCup,u'获取信息错误2',e
                                    print d
    cu.write()