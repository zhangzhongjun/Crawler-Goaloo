# coding=utf-8
import codecs
import HtmlDownloader
baseUrl = 'http://info.goaloo.com/jsData/LeagueSeason/sea%s.js'
f = codecs.open(u'F:\\PythonDev\\codes\\SCALWER\\goaloo\\0.所有的赛事.txt','r','utf-8')
f1 = codecs.open(u'F:\\goaloo\\1.赛季.txt','w','utf-8')
content = f.read()
content = content.split('\r\n')

for line in content:
    if line.find('^')!=-1:
        datas = line.split('^')
        leagueNo = datas[0]
        url = baseUrl %(leagueNo)
        print url
        seasons =  HtmlDownloader.getCon(url)
        seasons = seasons[seasons.find('['):seasons.rfind(']')+1:1]
        f1.write(datas[0]+u"^"+datas[1]+u"^"+datas[2]+u"^"+datas[3].strip('\r\n')+u"^"+seasons+u"\r\n")
    else:
        f1.write(line+u'\r\n')
