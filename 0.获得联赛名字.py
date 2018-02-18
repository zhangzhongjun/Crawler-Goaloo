# coding=utf-8
import urllib2
import urllib
url = 'http://info.goaloo.com/en/CupMatch/103.html'

s='''
var arrArea = new Array();
arrArea[0] = [['国际赛事','國際賽事','International',0,[],[[75,'世界杯','世界盃','World Cup',2],[650,'欧洲预选','歐洲預選','WCPEU',2],[648,'亚洲预选','亞洲預選','FIFA WCQL',2],[652,'南美预选','南美預選','WCPSA',2],[651,'非洲预选','非洲預選','WCPAF',2],[653,'北美预选','北美預選','WCPCA',2],[88,'洲际杯','洲際盃','FICC',2],[649,'大洋预选','大洋預選','WCPO',2],[892,'世界杯附','世界盃附','WCP-PO',2],[304,'世俱杯','世俱盃','FCWC',2],[44,'奥运男足','奧運男足','MOFT',2],[185,'奥运女足','奧運女足','WOFT',2],[388,'女世界杯','女世界盃','WWC',2],[76,'世青杯','世青盃','FIFAWYC',2],[222,'土伦杯','土倫杯','TOUT',2],[434,'加夫杯','加夫盃','ALGC',2],[349,'球迷杯','球迷盃','FANSC',2],[387,'世女杯U20','世女盃U20','FIFA WU20',2],[261,'世青U17','世青U17','WCU17',2],[609,'世五足','世五足','Fut W5',2],[730,'女世杯U17','女世盃U17','WCWU17',2],[768,'世室內足','世室內足','F.D.D.H',2],[329,'LG杯','LG盃','LG Cup',2],[41,'球会友谊','球會友誼','INT CF',2],[300,'法语运','法語運','FRGFB',2],[845,'世挑赛','世挑賽','WFC',2],[1180,'大运女足','大運女足','WWUFT',2],[1181,'大运男足','大運男足','MWUFT',2],[1294,'蒙太古U16','蒙太古U16','TM U16',2],[1336,'阿卡斯杯','阿卡斯盃','INT Kass',2],[1322,'OSN杯','OSN盃','OSN Cup',2],[1299,'吉尼斯杯','吉尼斯盃','ICC',2],[1279,'女室世锦','女室世錦','Futsal WTW',2],[1726,'中国杯','中國杯','China Cup',2],[1489,'COTIF杯','COTIF盃','COTIF',2],[1366,'国际友谊','國際友誼','INT FRL',2],[1223,'格雷纳杯','格雷納盃','GMC U18',2],[1218,'世室欧预','世室歐預','Futsal WCPEU',2]]],['沙滩赛事','沙灘賽事','Beach Soccer',0,[],[[1315,'欧沙联','歐沙聯','Europe BSWCP',2],[1310,'沙亚洲杯','沙亞洲盃','BSAC',2],[1307,'沙滩世杯','沙滩世盃','BSWC',2],[1280,'沙世亚预','沙世亞預','WCA S',2],[1679,'亚沙运','亞沙運','ASI BGS',2],[1244,'沙足赛','沙足賽','MCBS',2],[1232,'沙美杯','沙美盃','CABS',2],[1229,'沙滩洲际','沙灘洲際','BSIC',2],[1219,'拉各斯杯','拉各斯盃','Lagos Cup',2]]]];
arrArea[1] = [['欧洲赛事','歐洲賽事','Europe',1,[],[[67,'欧洲杯','歐洲盃','EURO  Cup',2],[103,'欧冠杯','歐冠盃','UEFA CL',2],[113,'欧罗巴杯','歐霸盃','UEFA EL',2],[79,'图图杯','圖圖盃','TOTO',2],[109,'超霸杯','超霸盃','UEFA SC',2],[223,'女欧国杯','女歐國盃','UEFACW',2],[114,'欧青U21外','欧青U21外','UEFA  U21Q',2],[1164,'欧青U21','歐青U21','UEFA U21',2],[215,'欧青U19','歐青U19','UEFA U19',2],[210,'欧青U17','歐青U17','UEFA U17',2],[534,'欧女杯','歐女盃','UEFA WUC',2],[256,'女欧U19','女歐U19','UEFA-W U19',2],[498,'酋长杯','酋長盃','Emirates S',2],[382,'阿姆杯','阿姆盃','AMST',2],[526,'女欧U17','女歐U17','EU-WU17',2],[668,'波罗杯','波羅盃','Baltic Cup',2],[561,'欧室锦标','歐室錦標','UFC',2],[690,'女北欧U23','女北歐U23','NTW U23',2],[697,'北欧U17','北歐U17','NT U17',2],[605,'CIS杯','CIS盃','CIS Cup',2],[741,'欧室U21','歐室U21','UEFA U21FC',2],[617,'波罗联','波羅聯','INT BL',2],[418,'TIP杯','TIP盃','TIP CUP',2],[608,'CO杯','CO盃','CO Cup',2],[147,'北欧联','北歐聯','ROYAL',2],[755,'斯堪彩杯','斯堪彩杯','SCA CLY Cup',2],[806,'温布利杯','溫布利盃','Wembley Cup',2],[834,'奥迪杯','奧迪盃','Audi Cup',2],[836,'北欧女U16','北歐女U16','ONW Cup',2],[844,'GF锦U19','GF錦U19','GF CUP U19',2],[875,'世女欧预','世女歐預','WWCPE',2],[1178,'都柏林杯','都柏林盃','Dublin SC',2],[1327,'欧联U19','歐聯U19','UEFA YL U19',2],[1306,'地中运','地中運','MGF',2],[1469,'多塞纳杯','多塞納杯','TDC',2],[1711,'欧联U23','歐聯U23','UEFASL U23',2],[1230,'不列颠杯','不列顛盃','CNCup',2],[1225,'太阳杯','太陽盃','Copa del Sol',2]]],['英格兰','英格蘭','England',1,[[36,'英超','英超','ENG PR',1],[37,'英冠','英冠','ENG LCH',0],[39,'英甲','英甲','ENG L1',0],[35,'英乙','英乙','ENG L2',0],[146,'英议联','英議聯','ENG Conf',0],[298,'英议南','英議南','ENG CS',0],[297,'英议北','英議北','ENG CN',0],[336,'英南超','英南超','ENG-S PR',0],[713,'英北超','英北超','ENG-N PR',0],[566,'英依超','英依超','ENG RYM',0],[1147,'英女足','英女足','ENG WSL',1],[861,'英女南','英女南','EWSL',1],[1016,'英女北','英女北','ENG WNPL',1],[285,'英女超','英女超','ENG WPR',0],[1260,'英U21','英U21','ENG U21',0],[1599,'英乙U23','英乙U23','ENG U23 D1',0],[1583,'英U23','英U23','ENG PU23',0],[1264,'英乙U21','英乙U21','ENG U21D2',0]],[[90,'英足总杯','英足總盃','ENG FAC',2],[84,'英联杯','英聯盃','ENG LC',2],[144,'英锦赛','英錦賽','ENG JPT',2],[177,'英挑杯','英挑盃','ENG FAT',2],[207,'英青杯','英青盃','ENG YFAC',2],[385,'英社盾','英社盾','ENG FACS',2],[586,'英斯盾','英斯盾','ENG CLC',2],[452,'英女足总','英女足總','ENG FA WC',2],[585,'英女联杯','英女聯盃','ENG WPR LC',2],[1209,'英女杯','英女盃','ENG FA WC',2],[1617,'英U23杯','英U23盃','ENG U23LC',2]]],['意大利','意大利','Italy',1,[[34,'意甲','意甲','ITA D1',1],[40,'意乙','意乙','ITA D2',0],[142,'意丙1','意丙1','ITA C1',0],[743,'意丙2','意丙2','ITA C2',0],[677,'意青联','意青聯','ITA YTHL',0],[1217,'意女甲','意女甲','IWD1',0]],[[83,'意杯','意盃','ITA Cup',2],[252,'TIM杯','TIM盃','TIM Cup',2],[346,'维亚杯','維亞盃','VIAT',2],[264,'意超杯','意超盃','ITA SC',2],[219,'意丙杯','意丙盃','ITA PRO LC',2],[736,'意青杯','意青盃','ITA YCup',2]]],['西班牙','西班牙','Spain',1,[[31,'西甲','西甲','SPA D1',1],[33,'西乙','西乙','SPA D2',0],[1413,'西丙','西丙','SPA D3',0],[587,'西室内足','西室內足','SPA FDH',0],[1186,'西女超','西女超','SPA WD1',0]],[[81,'西杯','西盃','SPA CUP',2],[704,'西超杯','西超杯','SPA SC',2],[684,'皇后杯','皇后盃','S Q C',2],[1126,'西联杯','西聯杯','SPA FC',2]]],['德国','德國','Germany',1,[[8,'德甲','德甲','GER D1',1],[9,'德乙','德乙','GER D2',0],[693,'德丙','德丙','GER D3',1],[1416,'德地区','德地區','GER Reg',0],[1415,'德U19','德U19','GER U19',0],[1412,'德U17','德U17','GER U17',0],[441,'德女联','德女聯','GER WD1',1]],[[51,'德国杯','德國盃','GERC',2],[529,'德青杯','德青盃','GERJBC',2],[462,'德女杯','德女盃','GERWC',2],[842,'德超杯','德超盃','GER SC',2],[1151,'德女联杯','德女联杯','GER WBC',2],[1312,'德电信杯','德電信盃','Ger LTC',2]]],['法国','法國','France',1,[[11,'法甲','法甲','FRA D1',1],[12,'法乙','法乙','FRA D2',0],[203,'法丙','法丙','FRA D3',0],[1421,'法丁','法丁','FRA D4',0],[440,'法女甲','法女甲','FRA WD1',1],[1414,'法U19','法U19','FRA U19',0]],[[54,'法国杯','法國盃','FRAC',2],[55,'法联杯','法聯盃','FRA LC',2],[698,'法超杯','法超杯','FRA SC',2]]],['葡萄牙','葡萄牙','Portugal',1,[[23,'葡超','葡超','POR D1',0],[157,'葡甲','葡甲','POR D2',0],[1429,'葡青A1','葡青A1','PORJA1',0],[1419,'葡青U17','葡青U17','POR JB',0]],[[70,'葡杯','葡盃','POR CN',2],[505,'葡联杯','葡聯盃','PORLC',2],[69,'葡超杯','葡超盃','POR SC',2]]],['苏格兰','蘇格蘭','Scotland',1,[[29,'苏超','蘇超','SCO PR',1],[150,'苏冠','蘇冠','SCO CH',0],[151,'苏甲','蘇甲','SCO L1',0],[152,'苏乙','蘇乙','SCO L2',0],[337,'苏高联','蘇高聯','SCO HL',1],[523,'苏青联','蘇青聯','SCO U20',0],[1092,'苏女超','蘇女超','SCO WPL',0]],[[78,'苏总杯','蘇總盃','SCOFAC',2],[77,'苏联杯','蘇聯盃','SCO LC',2],[145,'苏挑杯','蘇挑盃','SCO BC',2]]],['荷兰','荷蘭','Netherlands',1,[[16,'荷甲','荷甲','HOL D1',0],[17,'荷乙','荷乙','HOL D2',0],[573,'荷女甲','荷女甲','HOL WD1',0],[604,'荷青甲','荷青甲','HOL BD1',0],[767,'荷青乙','荷青乙','HOL BD2',1]],[[59,'荷兰杯','荷蘭盃','HOLC',2],[58,'荷超杯','荷超盃','DSC',2]]],['比利时','比利時','Belgium',1,[[5,'比甲','比甲','BEL D1',0],[138,'比乙','比乙','BEL D2',0],[1418,'比丙','比丙','BEL D3',0],[1405,'比女超','比女超','BPL (W)',0],[575,'比女甲','比女甲','BEL WD1',0],[1524,'比业余','比業餘','BEL FAD',0],[1270,'比荷女联','比荷女聯','BENL BNL',0]],[[108,'比利时杯','比利時盃','BEL Cup',2],[110,'比超杯','比超盃','BEL SC',2]]],['瑞典','瑞典','Sweden',1,[[26,'瑞典超','瑞典超','SWE D1',0],[122,'瑞典甲','瑞典甲','SWE D2',0],[218,'瑞典乙','瑞典乙','SWE D1 SN',0],[1436,'瑞典丙','瑞典丙','SWE D3',0],[447,'瑞青超','瑞青超','SWE U21AS',0],[1291,'瑞青甲','瑞青甲','SWE U21',0],[443,'瑞典女超','瑞典女超','SWE WD1',1],[1430,'瑞典女甲','瑞典女甲','SW D1',0]],[[73,'瑞典杯','瑞典盃','SWE Cup',2],[625,'瑞超杯','瑞超盃','SWESC',2],[464,'女瑞典杯','女瑞典盃','SWEC-W',2]]],['芬兰','芬蘭','Finland',1,[[13,'芬超','芬超','FIN D1',0],[212,'芬甲','芬甲','FIN D2',0],[1417,'芬乙','芬乙','FIN D3 A',0],[475,'芬女超','芬女超','FIN WD1',0]],[[226,'芬兰杯','芬蘭盃','FIN CUP',2],[189,'芬联杯','芬聯盃','FIN LC',2]]],['挪威','挪威','Norway',1,[[22,'挪超','挪超','NOR D1',1],[123,'挪甲','挪甲','NOR AL',0],[1428,'挪乙','挪乙','NOR D2',0],[473,'挪女超','挪女超','NORW',0]],[[64,'挪威杯','挪威盃','NORC',2],[508,'女挪威杯','女挪威盃','NOR WCUP',2],[775,'挪超杯','挪超盃','NSC',2],[786,'挪青英赛','挪青英賽','NOR JET',2]]],['丹麦','丹麥','Denmark',1,[[7,'丹麦超','丹麥超','DEN SASL',0],[127,'丹麦甲','丹麥甲','DEN D1',0],[1427,'丹麦乙','丹麥乙','DEN D2',0],[461,'丹女甲','丹女甲','DEN WD2',0],[720,'丹女超','丹女超','DEN WD1',0],[816,'丹麦U19','丹麥U19','DAN U19',1],[1085,'丹后备','丹後備','DEN RL',0]],[[378,'丹维杯','丹維盃','DMVC',2],[50,'丹麦杯','丹麥盃','DAN Cup',2],[540,'丹女杯','丹女盃','DWLWC',2]]],['奥地利','奧地利','Austria',1,[[3,'奥甲','奧甲','AUT D1',1],[128,'奥乙','奧乙','AUT D2',1],[1426,'奥丙','奧丙','AUS D3',0],[1249,'奥女甲','奥女甲','AFB',1]],[[96,'奥地利杯','奧地利盃','AUT CUP',2]]],['瑞士','瑞士','Switzerland',1,[[27,'瑞士超','瑞士超','SUI Sl',1],[121,'瑞士甲','瑞士甲','SUI D1',0],[1425,'瑞士乙','瑞士乙','SUI D2',0]],[[74,'瑞士杯','瑞士盃','SUI Cup',2]]],['爱尔兰','愛爾蘭','Ireland',1,[[1,'爱超','愛超','IRE PR',0],[139,'爱甲','愛甲','IRE D1',0]],[[231,'爱联杯','愛聯盃','IRE LC',2],[195,'爱足杯','愛足盃','IRFAIC',2],[200,'斯坦杯','斯坦盃','IRE SC',2]]],['北爱尔兰','北愛爾蘭','Northern Ireland',1,[[165,'北爱超','北愛超','NIR D1',0],[748,'北爱冠','北愛冠','NIR CH',0]],[[365,'北爱联杯','北愛聯盃','NIR LC',2],[501,'牛奶杯','牛奶盃','Milk Cup',2],[757,'北爱杯','北愛盃','NIR CUP',2]]],['俄罗斯','俄羅斯','Russia',1,[[10,'俄超','俄超','RUS PR',0],[235,'俄甲','俄甲','RUS D1',0],[1433,'俄乙','俄乙','RUS D2',0],[476,'俄青联','俄青聯','RUS YthC',0],[1049,'俄女超','俄女超','RUS WPL',0]],[[153,'俄杯','俄盃','RUS Cup',2],[191,'俄超杯','俄超盃','RUS SC',2],[1739,'俄FNL杯','俄FNL盃','RUS FC',2]]],['波兰','波蘭','Poland',1,[[6,'波兰超','波蘭超','POL D1',0],[221,'波兰甲','波蘭甲','POL D2',0],[1355,'波兰丙','波蘭丙','POL D4',0],[1159,'波女超','波女超','POL WD1',0],[500,'波青联','波青聯','POL ME',0]],[[115,'波兰杯','波蘭盃','POL Cup',2],[402,'波联杯','波聯盃','POL LC',2],[491,'波超杯','波超盃','Poland Super Cup',2]]],['乌克兰','烏克蘭','Ukraine',1,[[119,'乌克超','烏克超','UKR D1',0],[872,'乌克甲','烏克甲','UKR D2',0]],[[154,'乌克兰杯','烏克蘭盃','UKRC',2],[485,'乌超杯','烏超盃','UKR SC',2]]],['捷克','捷克','Czech Repoublic',1,[[137,'捷甲','捷甲','CZE D1',1],[290,'捷乙','捷乙','CZE D2',1],[706,'捷丙','捷丙','CZE CFL',0],[1258,'捷U21','捷U21','CZE U21',1],[1191,'捷女甲','捷女甲','CZE W1',0],[807,'捷U19','捷U19','CZE U19',0]],[[116,'捷克杯','捷克盃','CZEC',2],[1080,'捷超杯','捷超杯','CZE SC',2]]],['希腊','希臘','Greece',1,[[32,'希腊超','希臘超','GRE D1',0],[170,'希腊甲','希臘甲','GRE D2',0]],[[163,'希腊杯','希臘盃','GRE Cup',2]]],['罗马尼亚','羅馬尼亞','Romania',1,[[124,'罗甲','羅甲','ROM D1',0],[1423,'罗乙','羅乙','ROM D2',0]],[[197,'罗杯','羅盃','ROMC',2],[494,'罗超杯','羅超盃','Rom SC',2],[1351,'罗联杯','羅聯盃','ROMCL',2]]],['斯洛伐克','斯洛伐克','Slovakia',1,[[132,'斯伐超','斯伐超','SVK D1',1],[351,'斯伐甲','斯伐甲','SVK D2',0]],[[143,'斯伐杯','斯伐盃','SVK Cup',2],[654,'斯伐杯U18','斯伐盃U18','SVKCU18',2]]],['冰岛','冰島','Iceland',1,[[166,'冰岛超','冰島超','ICE PR',0],[381,'冰岛甲','冰島甲','ICE D1',1],[1047,'冰女超','冰女超','ICE WPR',1],[1083,'冰岛乙','冰島乙','ICE D2',1],[1251,'冰女甲','冰女甲','ICE LD1',0]],[[246,'冰岛杯','冰島盃','ICE CUP',2],[773,'冰联杯','冰聯盃','ICE LC',2],[1009,'冰女联杯','冰女聯盃','ICE WLC',2],[1074,'冰女杯','冰女杯','ICE WC',2],[1132,'冰岛锦','冰島錦','ICE CH',2],[1148,'冰超杯','冰超盃','ICE SC',2],[1334,'雷克锦标','雷克錦標','REYT',2],[1438,'雷克女锦','雷克女錦','REWT',2],[1439,'冰岛锦B','冰島錦B','ICE CH B',2]]],['拉脱维亚','拉脫維亞','Latvia',1,[[214,'拉脱超','拉脫超','LAT D1',1],[1070,'拉脱甲','拉脫甲','LAT D2',0]],[[243,'拉脱杯','拉脫盃','LAT Cup',2],[1730,'拉冬联杯','拉冬聯杯','LAT VWC',2]]],['白俄罗斯','白俄羅斯','Belarus',1,[[230,'白俄超','白俄超','BLR D1',0],[1046,'白俄甲','白俄甲','BLR D2',0],[1086,'白俄女超','白俄女超','BWPL',0]],[[638,'白俄杯','白俄盃','BLR CUP',2]]],['立陶宛','立陶宛','Lithuania',1,[[217,'立陶甲','立陶甲','LIT D1',0],[897,'立陶乙','立陶乙','LIT D2',0]],[[558,'立陶杯','立陶盃','LIT Cup',2]]],['威尔士','威爾士','Wales',1,[[135,'威超','威超','WAL PR',0],[1104,'威联','威聯','WAL CA',0],[1115,'威甲','威甲','WAL D1',1]],[[190,'威杯','威盃','WALC',2],[518,'威挑杯','威挑盃','WAL CLC',2]]],['匈牙利','匈牙利','Hungary',1,[[136,'匈甲','匈甲','HUN D1',1],[703,'匈乙','匈乙','HUN D2E',0],[893,'匈U19','匈U19','HUN U19A',0],[1056,'匈女甲','匈女甲','HUN WD1',0],[1319,'匈U21','匈U21','HUN U21',0]],[[155,'匈杯','匈盃','HUN Cup',2],[249,'匈超杯','匈超盃','HUN SC',2],[513,'匈联杯','匈聯盃','HUN LC',2]]],['土耳其','土耳其','Turkey',1,[[30,'土超','土超','TUR D1',0],[130,'土甲','土甲','TUR D2',0],[1431,'土乙','土乙','TUR D3',0],[1432,'土丙','土丙','TUR 3B',0],[1192,'土A2联','土A2聯','TUR A2',0],[1053,'土A2冠','土A2冠','TUR A2LPO',0],[1365,'土U21超','土U21超','Turk U21 SL',1],[750,'土女甲','土女甲','TUR WD1',0],[922,'土女乙','土女乙','TUR WD2',1]],[[167,'土杯','土盃','TUR Cup',2],[495,'土比杯','土比盃','Tur BC',2],[497,'土卡杯','土卡盃','TUR CAPC',2],[705,'土超杯','土超盃','TUR SC',2],[1236,'土冠杯','土冠盃','TUR STC',2]]],['克罗地亚','克羅地亞','Croatia',1,[[133,'克亚甲','克亞甲','CRO D1',0]],[[62,'克亚杯','克亞盃','CRO Cup',2]]],['保加利亚','保加利亞','Bulgaria',1,[[131,'保超','保超','BUL D1',0],[1262,'保乙','保乙','BUL D2',0]],[[196,'保杯','保盃','BUL Cup',2],[496,'保超杯','保超盃','Bulg SC',2]]],['斯洛文尼亚','斯洛文尼亞','Slovenia',1,[[247,'斯亚甲','斯亞甲','SLO D1',0],[120,'斯亚乙','斯亞乙','SLO D2',1]],[[208,'斯亚杯','斯亞盃','SLOC',2],[688,'斯尼超杯','斯尼超盃','SLO SC',2]]],['塞浦路斯','塞浦路斯','Cyprus',1,[[159,'塞浦甲','塞浦甲','CYP D1',0],[915,'塞浦乙','塞浦乙','CYP D2',0]],[[168,'塞浦杯','塞浦盃','CYP Cup',2],[710,'塞浦超杯','塞浦超杯','CYP SCUP',2]]],['塞尔维亚','塞爾維亞','Serbia',1,[[129,'塞尔超','塞爾超','SER D1',0],[1061,'塞尔甲','塞爾甲','SER D2',0]],[[211,'塞尔杯','塞爾盃','SER CUP',2]]],['以色列','以色列','Israel',1,[[118,'以超','以超','ISR D1',0],[160,'以甲','以甲','ISR D2',0],[783,'以乙','以乙','ISR D3',0],[947,'以女甲','以女甲','ISR W1',0]],[[205,'以杯','以盃','ISR CUP',2],[711,'以超杯','以超盃','ISR LATTC',2],[858,'以图杯','以圖盃','ISR LLTTC',2]]],['阿尔巴尼亚','阿爾巴尼亞','Albania',1,[[315,'阿尔巴超','阿爾巴超','ALB D1',0]],[[634,'阿尔巴杯','阿爾巴盃','ALB Cup',2]]],['哈萨克斯坦','哈薩克斯坦','Kazakhstan',1,[[466,'哈萨超','哈薩超','KAZ PR',0],[1077,'哈萨甲','哈薩甲','KAZ D1',0]],[[527,'哈萨杯','哈薩盃','KAZ C',2]]],['波黑','波黑','Bosnia',1,[[352,'波斯甲','波斯甲','BOS PL',0]],[[355,'波斯杯','波斯盃','BOS Cup',2]]],['爱沙尼亚','愛沙尼亞','Estonia',1,[[353,'爱沙甲','愛沙甲','EST D1',1],[1043,'爱沙乙','愛沙乙','EST D2',0],[1154,'爱沙丙','愛沙丙','EST D3',0],[1079,'爱沙女甲','愛沙女甲','EST WD2',0]],[[646,'爱沙杯','愛沙盃','EST CUP',2],[1437,'爱沙冬锦','愛沙冬錦','Estonia WT',2]]],['摩尔多瓦','摩爾多瓦','Moldova',1,[[389,'摩尔甲','摩爾甲','MOL D1',1],[1014,'摩尔乙','摩爾乙','MOL D2',1]],[[549,'摩尔杯','摩爾盃','MOL Cup',2]]],['阿美尼亚','阿美尼亞','Armenia',1,[[469,'阿美超','阿美超','ARM D1',1],[1062,'阿美甲','阿美甲','ARM D2',1]],[[794,'阿美杯','阿美盃','ARM CUP',2]]],['黑山','黑山','Montenegro',1,[[562,'黑山甲','黑山甲','MNE D1',0],[1520,'黑山乙','黑山乙','MNE D2',1]],[[639,'黑山杯','黑山盃','MNE CUP',2]]],['马耳他','馬爾他','Malta',1,[[533,'马尔甲','馬爾甲','MAL D1',0],[994,'马尔女甲','馬爾女甲','MWD1',0],[1000,'马尔乙','馬爾乙','MAL D2',1]],[[701,'马尔超杯','馬爾超盃','MAL SC',2],[657,'马耳他杯','馬爾他盃','MAL Cup',2],[1285,'AME杯','AME盃','AMEC',2]]],['卢森堡','盧森堡','Luxembourg',1,[[514,'卢森甲','盧森甲','LUX D1',0]],[[1328,'卢森杯','盧森盃','LUX Cup',2]]],['法罗群岛','法羅群島','Faroe Islands',1,[[576,'法罗甲','法羅甲','FAR D1',1]],[[1050,'法罗杯','法羅盃','FAR Cup',2]]],['格鲁吉亚','格魯吉亞','Georgia',1,[[563,'格鲁甲','格魯甲','GEO D1',0],[1116,'格鲁乙','格魯乙','GEO D2',0]],[[647,'格鲁杯','格魯盃','GEO C',2]]],['阿塞拜疆','阿塞拜疆','Azerbaijan',1,[[613,'阿塞超','阿塞超','AZE D1',0]],[[620,'阿塞杯','阿塞盃','AZE CUP',2]]],['马其顿','馬其頓','FYR Macedonia',1,[[392,'马其甲','馬其甲','MKD D1',0],[1242,'马其乙','馬其乙','MKD D2',0]],[[569,'马其杯','馬其盃','MKD CUP',2]]],['圣马力诺','聖馬力諾','San Marino',1,[[1662,'圣马甲','聖馬甲','SAN L',0]],[]],['安道尔','安道爾','Andorra',1,[[880,'安道超','安道超','ANDSL',0]],[[1224,'安道杯','安道盃','And Cup',2]]]];
arrArea[2] = [['美洲赛事','美洲賽事','Americas',2,[],[[224,'美洲杯','美洲盃','AMEC',2],[89,'自由杯','自由盃','CON CLA',2],[232,'美金杯','美洲金盃','CGC',2],[263,'南球杯','南球盃','CON CSA',2],[344,'美冠杯','美冠盃','CNCF CHL',2],[424,'中美杯','中美盃','UNCAFNC',2],[270,'南美超杯','南美超盃','RESU',2],[175,'美青杯','美青盃','CNCF U20Q',2],[489,'泛美男足','泛美男足','PAGM',2],[487,'泛美女足','泛美女足','PAGW',2],[213,'南美U20','南美U20','CSU20',2],[429,'南美U17','南美U17','CNCF U17',2],[621,'女南冠U20','女南冠U20','CON WU20',2],[188,'美加杯','美加盃','CGC CZ',2],[679,'女北美U20','女北美U20','CNCF WU20',2],[682,'南美室內','南美室內','CONMEBOLFC',2],[691,'女北美U17','女北美U17','CNCF W U17',2],[734,'美青U17','美青U17','CNCF U17',2],[673,'北美室內足','北美室內足','CONCACAFFC',2],[889,'女自由杯','女自由盃','LIB CF',2],[974,'女南冠U17','女南冠U17','CON WU17',2],[1121,'世女美预','世女美預','WWCQ CONC',2],[1123,'女南冠','女南冠','CON W',2],[1167,'自由杯U20','自由盃U20','LIBC U20',2],[1171,'女奥北美','女奥北美','NCAOW',2],[1211,'南冠U15','南冠U15','CS U15',2],[1177,'奥北选','奧北選','NCAO',2],[1212,'南运U17','南運U17','SAG U17',2],[1289,'中美运女','中美運女','WAG',2],[1290,'中美运男','中美運男','CAG',2],[1282,'沙南美预','沙南美預','CONMEBOL Qualifier',2],[1719,'巴皮青杯','巴皮青盃','BRA Cup',2],[1368,'美女金杯','美女金盃','CNCF WGC',2],[1371,'女美加杯','女美加盃','CNCF WCAC',2],[1345,'南美女运','南美女運','SAme GF',2]]],['阿根廷','阿根廷','Argentina',2,[[2,'阿甲','阿甲','ARG D1',0],[423,'阿乙','阿乙','ARG D2',0],[917,'阿乙曼特','阿乙曼特','ARG B M',0],[1461,'阿丙曼特','阿丙曼特','ACT  M',0],[1462,'阿丁曼特','阿丁曼特','ADT M',0]],[[340,'阿夏赛','阿夏賽','ARG TPV',2],[1277,'阿超杯','阿超盃','ARG SC',2],[1183,'阿根廷杯','阿根廷盃','ARG C',2]]],['巴西','巴西','Brazil',2,[[4,'巴西甲','巴西甲','BRA D1',1],[358,'巴西乙','巴西乙','BRA D2',1],[181,'里约锦标','里約錦標','BRA RJ',0],[178,'巴圣锦标','巴聖錦標','BRA SP',0],[957,'巴塞阿甲','巴塞阿甲','BRA CE',0],[960,'巴帕联','巴帕聯','Bra CaP',0],[961,'巴国诺联','巴國諾聯','BRA CGD',0],[962,'巴卡德联','巴卡德聯','BRA CCD1',0],[963,'巴伯联','巴伯聯','BRA PE',0],[964,'巴高联','巴高聯','BRA CGD1',0],[971,'巴米联','巴米聯','BRA MG',0],[973,'巴巴亚联','巴巴亞聯','BRA CBD',0],[987,'巴波联','巴波聯','BRA CP',0],[998,'巴伊联','巴伊聯','BRA PB',0],[1373,'巴圣甲','巴聖甲','BRA SPB',0]],[[186,'巴西杯','巴西盃','BRA CUP',2],[751,'圣青杯','聖青盃','CSP YC',2],[930,'巴青锦','巴青錦','Bra YL',2],[1065,'巴东北超','巴東北超','BRA CNF',2],[1358,'巴圣杯','巴聖盃','BRA SPC',2],[1441,'巴超联杯','巴超聯盃','BLP',2],[1448,'巴维杯','巴維杯','BRA CV',2],[1275,'巴青杯','巴青盃','BRA YCup',2]]],['美国','美國','United States',2,[[21,'美职业','美職業','MLS',0],[448,'美乙','美乙','USL D1',0],[802,'美女职','美女職','USA WD1',0],[1145,'北美联','北美聯','NAL',0]],[[483,'美公开赛','美公開賽','USA CUP',2],[1740,'卡罗挑杯','卡羅挑盃','Car Cup',2]]],['智利','智利','Chile',2,[[415,'智利甲','智利甲','CHI D1',0],[611,'智利乙','智利乙','CHI D2',0]],[[714,'智利杯','智利盃','Chile Cup',2],[1309,'智超杯','智超盃','CHI SC',2]]],['墨西哥','墨西哥','Mexico',2,[[140,'墨西联','墨西聯','MEX D1',0],[847,'墨西乙','墨西乙','MEX D2',0]],[[173,'墨西哥杯','墨西哥盃','MEX IL',2],[1350,'墨超杯','墨超盃','MEX SC',2]]],['巴拉圭','巴拉圭','PARA',2,[[354,'巴拉甲','巴拉甲','PAR D1',0],[1076,'巴拉乙','巴拉乙','PAR D2',0]],[]],['秘魯','秘鲁','Peru',2,[[242,'秘鲁甲','秘魯甲','PER D1',0]],[[1162,'秘印加杯','秘印加盃','Peru Copa Inca',2]]],['乌拉圭','烏拉圭','Uruguay',2,[[240,'乌拉甲','烏拉甲','URU D1',0]],[[1231,'乌拉锦标','烏拉錦標','Uruguay Torneo Preparacion',2]]],['哥伦比亚','哥倫比亞','Colombia',2,[[250,'哥伦甲','哥倫甲','COL D1',0],[1169,'哥伦乙','哥倫乙','COL D2',0]],[[635,'哥伦杯','哥倫盃','COL Cup',2]]],['厄瓜多尔','厄瓜多爾','Ecuador',2,[[596,'厄瓜甲','厄瓜甲','ECU D1',0]],[]],['委內瑞拉','委內瑞拉','Venezuela',2,[[391,'委內超','委內超','VEN D1',0]],[[1184,'委内杯','委內盃','VEN CUP',2]]],['玻利维亚','玻利維亞','Bolivia',2,[[593,'玻利甲','玻利甲','BOL D1',0]],[[1484,'玻日比杯','玻日比盃','BCCC',2]]],['洪都拉斯','洪都拉斯','Honduras',2,[[577,'洪都甲','洪都甲','HON D1',0]],[]],['加拿大','加拿大','Canadian',2,[[460,'加拿超','加拿超','CAN CSL',0]],[[664,'加拿冠','加拿冠','CAN CHL',2]]],['哥斯达黎加','哥斯達黎加','Costa',2,[[504,'哥斯甲','哥斯甲','CRC D1',0]],[[1308,'哥斯杯','哥斯盃','CRC C',2]]],['危地马拉','危地馬拉','Guatemala',2,[[579,'危地甲','危地甲','GUA D1',0]],[]],['萨尔瓦多','薩爾瓦多','El Salvador',2,[[511,'萨尔超','薩爾超','SLV D1',0]],[]],['特立尼达','特立尼達','Republic of Trinidad',2,[[1684,'千里甲','千里甲','TRI PL',0]],[]]];
arrArea[3] = [['亚洲赛事','亞洲賽事','Asian',3,[],[[95,'亚洲杯','亞洲盃','AFC',2],[192,'亚冠杯','亞冠盃','AFC CL',2],[350,'亚协杯','亞協盃','AFC Cup',2],[251,'亚挑杯','亞挑盃','AFC CC',2],[53,'东亚杯','東亞盃','EASTC',2],[979,'南亚运','南亞運','SAGA',2],[291,'东亚运','東亞運','EAG',2],[293,'东南运','東南運','SEAG',2],[1124,'东南锦','東南錦','AFF Cup',2],[470,'西亚锦','西亞錦','WAFFC',2],[1044,'亚总杯','亞總盃','AFC PC',2],[655,'亚室锦标','亞室錦標','AFC FC',2],[220,'麒麟杯','麒麟盃','KIR Cup',2],[187,'A3冠军杯','A3冠軍盃','A3CC',2],[182,'阿拉冠','阿拉冠','ARCL',2],[1252,'阿拉伯杯','阿拉伯盃','ARAB CUP',2],[161,'海湾运','海灣運','GC',2],[401,'亚运男足','亞運男足','AGS',2],[405,'亚运女足','亞運女足','AGSW',2],[515,'独立杯','獨立盃','MC',2],[432,'东南青冠','東南青冠','ASEANYC',2],[307,'黄金杯','黄金盃','SAFF',2],[560,'阿拉运','阿拉運','Pan Arab',2],[520,'海湾锦标','海灣錦标','GCC',2],[851,'内鲁盃','內魯盃','ONC',2],[477,'和平杯','和平盃','PEACE Cup',2],[600,'海湾奥杯','海灣奧盃','GOT Cup',2],[629,'女亚杯','女亞盃','AFC W',2],[725,'女东南锦','女東南錦','AFFWC',2],[992,'西亚女锦','西亞女錦','WAWC',2],[731,'女亚青冠','女亞青冠','AFC WU19',2],[396,'女和平杯','女和平盃','WPEA Cup',2],[564,'东亚女足','東亞女足','EFFC',2],[1331,'东亚女运','東亞女運','WEAG',2],[798,'女亚杯预','女亞盃預','Asian CQW',2],[1136,'女奥亚预','女奥亞預','OPAW',2],[295,'亚青U16','亞青U16','AFAYC',2],[435,'女亚冠U16','女亞冠U16','AFC WU16',2],[689,'东南亚U16','東南亞U16','AFF U16',2],[516,'东南亚U17','東南亞U17','AFF U17',2],[1253,'阿拉青U17','阿拉青U17','Arab U17',2],[699,'海湾U17','海灣U17','GF C U17',2],[399,'亚青U19','亞青U19','AFC U19',2],[726,'东南亚U19','東南亞U19','AFF U19',2],[1385,'亚青U23','亞青U23','AFC U23',2],[1638,'海湾U19','海灣U19','GF C U19',2],[1725,'中超跨年杯','中超跨年盃','CSL NYCup',2],[1444,'女南亚运','女南亞運','AFC WSAG',2],[1408,'西亚青锦','西亞青錦','WAFF U23',2],[1625,'亚协预选','亞協預選','Asian Cup',2],[1792,'亚五足','亞五足','Asian F',2],[1403,'西亚U16','西亞U16','WAFF-U16',2],[1404,'南亚杯U19','南亞盃U19','SAFF U19',2],[1370,'南亚女杯','南亞女盃','South A G',2],[503,'东南亚U20','東南亞U20','AFF U20',2],[1254,'阿拉杯U20','阿拉盃U20','Arab Cup U20',2],[1220,'海湾运U20','海灣運U20','Gulf Cup U20',2]]],['中国','中國','China',3,[[60,'中超','中超','CHA CSL',1],[61,'中甲','中甲','CHA D1',1],[686,'中乙','中乙','CHA D2',0],[311,'香港超','香港超','HK PR',0],[645,'中女超','中女超','CWPL',0],[1363,'香港甲','香港甲','HK D1',1],[1378,'澳门甲','澳門甲','MAC D1',1]],[[1278,'甲A明星','甲A明星','A.D.tor',2],[1303,'上海锦标','上海錦標','SH IT',2],[831,'全运U16','全運U16','CSGU16',2],[1320,'全运男U18','全運男U18','CSGU18',2],[1321,'全运女U18','全運女U18','CSGU18',2],[86,'中超杯','中超盃','China Lea',2],[87,'中协杯','中協盃','CFC',2],[202,'全运男足','全運男足','CHN NGFM',2],[796,'全运女足','全運女足','CHN NGFW',2],[735,'高级银牌','高級銀牌','HK SS',2],[1286,'梅贺岁杯','梅賀歲盃','NYCup',2],[420,'港联杯','港聯盃','HK LC',2],[458,'港足总杯','港足總盃','HKFA CUP',2],[631,'港主席杯','港主席盃','HK CC',2],[499,'潍坊杯','濰坊盃','WFC',2],[413,'省港杯','省港盃','GDHKCUP',2],[610,'贺岁杯','賀歲盃','LNY CUP',2],[1690,'京津冀杯','京津冀盃','BTH Cup',2],[1399,'潍坊女杯','濰坊女盃','WFW',2]]],['日本','日本','Japan',3,[[25,'日职联','日職聯','JPN D1',0],[284,'日职乙','日職乙','JPN D2',0],[780,'日足联','日足聯','JPN JFL',0],[459,'日职女甲','日職女甲','JPN WD1',0],[455,'日职女乙','日職女乙','JWD2',0],[1346,'日丙','日丙','JPN D3',1]],[[695,'日青锦','日青錦','JCYF',2],[393,'日卫星赛','日衛星賽','JPN SL',2],[72,'日联杯','日聯盃','JPN LC',2],[71,'日超杯','日超盃','JPN SC',2],[162,'日皇杯','日皇盃','JE Cup',2],[517,'日撒杯','日撒盃','J.S Cup',2],[525,'女日联杯','女日聯盃','WJLC',2],[744,'日女锦标','日女錦標','JWFC',2],[1581,'SBS杯','SBS盃','SBS CUP',2],[1731,'日新杯','日新盃','JPN NYC',2],[1795,'日女杯乙','日女盃乙','Japanese W C 2',2]]],['南韩','南韓','Korea Republic',3,[[15,'韩K联','韓K聯','KOR D1',0],[1292,'韩挑K联','韓挑K聯','KOR D2',0],[456,'韩联盟','韓聯盟','KOR D3',0],[630,'韩挑赛','韓挑賽','KCL',0],[827,'韩女联','韓女聯','KOR WD1',0]],[[685,'韩锦赛','韓錦賽','KOR NCH',2],[468,'韩足总','韓足總','KFAC',2],[437,'韩联杯','韓聯盃','K-LC',2]]],['澳洲','澳洲','Australia',3,[[273,'澳洲甲','澳洲甲','AUS D1',0],[616,'澳威超','澳威超','AUS NSW',0],[436,'澳维超','澳維超','AUS VPL',0],[1073,'澳维甲','澳維甲','Aus VD1',0],[774,'澳布超','澳布超','AUS BPL',0],[1029,'澳南超','澳南超','AUS SASL',0],[481,'澳西超','澳西超','WAUS D1',0],[1063,'澳首超','澳首超','AUS CGP',0],[1068,'澳昆超','澳昆超','AUS QSL',0],[722,'澳青联','澳青聯','AUS YTH',0],[1072,'澳南甲','澳南甲','FFSA PL',0],[453,'澳维女超','澳維女超','AUS WPL',0],[729,'澳女联','澳女聯','AUS WAL',0],[619,'澳维U21','澳維U21','Aus VPL U21',0],[1450,'澳塔超','澳塔超','TSA TPL',0],[1382,'澳布甲','澳布甲','AUS BPL1',0]],[[383,'澳前赛','澳前賽','AUS FWD1',2],[612,'澳西前赛','澳西前賽','MFNSPD',2],[977,'澳西甲前','澳西甲前','AUS FWD1',2],[978,'澳西夜赛','澳西夜賽','AUS PLNS',2],[1064,'澳威杯','澳威盃','AUS NSWC',2],[1069,'澳南杯','澳南盃','SAUS FCup',2],[1135,'澳西杯','澳西盃','WAUS LC',2],[1301,'澳维杯','澳維盃','FFV Cup',2],[1356,'澳足总','澳足總','A FFA Cup',2]]],['沙地阿拉伯','沙地阿拉伯','Saudi Arabia',3,[[292,'沙地联','沙地聯','KSA PR',0],[745,'沙地甲','沙地甲','KSA D1',0],[950,'沙地乙','沙地乙','KSA D2',0],[749,'沙地青','沙地青','KSA YTH',0],[1118,'亲王杯U21','親王盃U21','PFBFC',1]],[[891,'沙杯U17','沙盃U17','KSA FC U17',2],[640,'沙王冠','沙王冠','KSA CC',2],[339,'沙王杯','沙王盃','KSA CC',2],[884,'沙青杯','沙青盃','SAYC',2]]],['伊朗','伊朗','Iran',3,[[279,'伊朗超','伊朗超','IRN PR',0],[898,'伊朗甲','伊朗甲','IRN D1',0]],[[618,'伊朗杯','伊朗盃','Iran Cup',2],[1488,'伊朗超杯','伊朗超盃','ISC',2]]],['阿联酋','阿聯酋','UAE',3,[[301,'阿联酋超','阿聯酋超','UAE LP',0],[1706,'阿联酋乙','阿聯酋乙','UAE D2',1]],[[331,'阿联酋杯','阿聯酋杯','UAE C',2],[733,'阿联杯','阿聯盃','UAE',2],[899,'阿联合杯','阿聯合盃','UAE F C',2]]],['新加坡','新加坡','Singapore',3,[[194,'新加坡联','新加坡聯','SIN D1',0]],[[245,'新加坡杯','新加坡盃','SIN CUP',2],[603,'新电信杯','新電信盃','STLC',2]]],['马来西亚','馬來西亞','Malaysia',3,[[316,'马来超','馬來超','MAS SL',0],[317,'马来甲','馬來甲','MAS PL',0]],[[280,'马足总','馬足總','MAS FAC',2],[426,'马来杯','馬來盃','MALAC',2],[822,'马洲际杯','馬洲際杯','INT Cup',2],[1187,'马后杯','馬後盃','MAS RESC',2]]],['巴林','巴林','Bahrain',3,[[318,'巴林超','巴林超','BHR D1',0]],[[721,'巴王杯','巴王盃','BHR Cup',2],[747,'巴林杯','巴林盃','BHR FAC',2],[839,'巴王子杯','巴王子盃','BHR CPC',2]]],['卡塔尔','卡塔爾','Qatar',3,[[313,'卡塔尔联','卡塔爾聯','QAT D1',0]],[[1028,'卡亲王杯','卡亲王盃','QAT PC',2],[1031,'卡王储杯','卡王儲盃','QCP Cup',2],[1102,'贾西姆杯','賈西姆盃','QSJC',2]]],['也门','也門','Yemen',3,[[465,'也门甲','也門甲','YEM D1',0],[976,'也门乙','也門乙','YEM D2',0]],[[1058,'也统杯','也總盃','YEM FAC',2]]],['约旦','約旦','Jordan',3,[[309,'约超联','約超聯','JOR D1',0]],[[330,'约旦杯','約旦盃','JORC',2],[687,'约盾杯','約盾盃','JOR ShC',2]]],['泰国','泰國','Thailand',3,[[700,'泰超','泰超','THA PR',0],[1048,'泰甲','泰甲','THA D1',1]],[[758,'泰王杯','泰王盃','KCTH',2],[882,'泰足总','泰足總','TH FC',2],[1119,'泰联杯','泰聯盃','THA LC',2]]],['科威特','科威特','Kuwaiti',3,[[322,'科威特联','科威特聯','KUW D1',0],[923,'科威甲','科威甲','KUW D2',1]],[[471,'科元首杯','科元首盃','KUW Cup',2],[559,'科王杯','科王盃','KUWCPC',2],[592,'科威杯','科威盃','Kuw FC',2],[1008,'科青杯','科青盃','KUW FeC',2]]],['阿曼','阿曼','Omani',3,[[332,'阿曼联','阿曼聯','OMA D1',0]],[[925,'阿曼苏杯','阿曼蘇盃','OMA Cup',2],[1318,'阿曼杯','阿曼盃','OMA FA Cup',2]]],['乌兹别克','烏茲別克','Uzbekistan',3,[[772,'乌兹超','烏茲超','UZB D1',1],[1160,'乌兹甲','烏茲甲','UZB D2',0]],[[823,'乌兹杯','烏茲盃','UzbC',2],[1342,'乌兹联杯','烏茲聯盃','Uzbekistan PFL Cup',2],[1383,'乌兹超杯','烏茲超盃','Uzbekistan Su',2]]],['黎巴嫩','黎巴嫩','Lebanon',3,[[325,'黎巴嫩联','黎巴嫩聯','LBN D1',1]],[[474,'黎巴杯','黎巴盃','LIB',2],[1273,'黎精英杯','黎精英盃','Lbn EC',2]]],['伊拉克','伊拉克','Iraq',3,[[1054,'伊拉联','伊拉聯','IRQ D1',0]],[]],['印度','印度','India',3,[[1367,'印度超','印度超','ISL',0],[763,'印度甲','印度甲','IND D1',1]],[[937,'印联杯','印聯盃','IND FC',2],[1340,'印度盾','印度盾','IFA ST',2]]],['越南','越南','Vietnam',3,[[766,'越南联','越南聯','VIE D1',1],[1248,'越南甲','越南甲','VIE D2',0]],[[1379,'越青锦','越青錦','VIE U19',2],[1265,'越南杯','越南盃','VIE Cup',2]]],['印度尼西亚','印度尼西亞','Indonesia',3,[[1122,'印尼超','印尼超','IDN ISL',0]],[[1335,'印国岛杯','印國島盃','IDN IIC',2],[1240,'印尼杯','印尼盃','IDN C',2]]],['缅甸','緬甸','Myanmar',3,[[1443,'缅甸联','緬甸聯','MYA D1',0]],[]]];
arrArea[4] = [['大洋洲赛事','大洋洲賽事','Oceania',4,[],[[543,'大冠杯','大冠盃','Oce CL',2],[968,'大洋女U20','大洋女U20','OFC W U20',2],[1025,'大洋女U17','大洋女U17','OFC W U17',2],[1128,'大洋冠U17','大洋冠U17','OFC U17',2],[1149,'大洋冠U20','大洋冠U20','OFCCU20',2],[1332,'奥大洋预','奥大洋預','OP OFC',2],[1372,'大洋统杯','大洋統盃','OFC PC',2]]],['新西兰','新西蘭','New Zealand',4,[[341,'新西兰联','新西蘭聯','NZFC',0]],[]]];
arrArea[5] = [['非洲赛事','非洲賽事','Africa',5,[],[[93,'非洲杯','非洲盃','CAF NC',2],[239,'非冠杯','非冠盃','CAF CL',2],[262,'非联杯','非聯盃','CAF Cup',2],[176,'非青杯','非青盃','CAFYC',2],[581,'中东非杯','中東非盃','CECAFA Cup',2],[738,'北非冠','北非冠','NAFCUP',2],[765,'非超杯','非超盃','Non-Cup',2],[781,'非青U17','非青U17','AYC U17',2],[1051,'女非国杯','女非國盃','CAF WNC',2],[1052,'非国锦标','非國錦標','CAF SC',2],[1133,'非洲运','非洲運','All Africa Soccer',2],[1138,'奥非预','奧非預','OPAF',2],[1333,'非青杯外','非青盃外','CAF YCQ',2],[1311,'南非洲杯','南非洲盃','SACC',2],[1387,'非运女足','非運女足','AAS WNC',2],[1722,'南联杯U20','南聯盃U20','CAF CoC20',2],[1666,'非女挑杯','非女挑盃','CAF WCC',2],[1806,'大洋女U19','大洋女U19','BQC',2],[1226,'非女锦U20','非女錦U20','CAN W-U20',2]]],['南非','南非','South Africa',5,[[308,'南非超','南非超','SAPL D1',0],[907,'南非甲','南非甲','SAFL',0]],[[779,'南联杯','南聯盃','SALC',2],[1010,'南非联杯','南非聯盃','SAPL  CUP',2]]],['尼日利亚','尼日利亞','Nigeria',5,[[949,'尼日超','尼日超','NGA PR',1]],[]],['摩洛哥','摩洛哥','Morocco',5,[[321,'摩洛超','摩洛超','MAR D1',1],[953,'摩洛乙','摩洛乙','MAR D2',1]],[[467,'摩洛杯','摩洛盃','MOLE Cup',2]]],['突尼斯','突尼西亞','Tunisia',5,[[326,'突尼甲','突尼甲','TUN D1',0],[1222,'突尼乙','突尼乙','TTLd',0]],[[636,'突尼杯','突尼盃','T C',2]]],['阿尔及利亚','阿爾及利亞','Algeria',5,[[193,'阿尔甲','阿爾甲','ALG D1',1],[863,'阿尔乙','阿爾乙','ALG D2',1]],[[333,'阿尔杯','阿爾杯','ALG CUP',2]]],['埃及','埃及','Egypt',5,[[303,'埃及超','埃及超','EGY D1',0]],[[451,'埃及杯','埃及盃','EGYCup',2]]],['利比亚','利比亞','Libya',5,[[324,'利比亚甲','利比亞甲','LIBD1L',0]],[]],['安哥拉','安哥拉','Angola',5,[[1471,'安哥甲','安哥甲','AGB LE',0]],[]],['加纳','加納','Ghana',5,[[1393,'加纳超','加納超','GHA D1',1]],[]],['苏丹','蘇丹','Sudan',5,[[1487,'苏丹超','蘇丹超','SUD PR',1]],[]]];
'''
s = unicode(s,'utf-8')
lines = s.split('\n')
s =  lines[3]
s = s[s.find('=')+1::1]
s = s[s.find('['):s.rfind(']')+1:1]
s = s.replace('\'','\"')
import json
my_datas = json.loads(s)

import codecs
f = codecs.open(u'f:\\PythonDev\\codes\\SCALWER\\goaloo\\0.获得联赛名字.txt','w','utf-8')
for i in range(0,len(my_datas),1):
    country = my_datas[i][0]
    print country
    f.write(country+u'\r\n')
    datas1 =  my_datas[i][4]
    for data in datas1:
        print data[0],data[1],data[3],data[4]
        f.write(unicode(str(data[0]),'utf-8')+u"^"+data[1]+u'^'+data[3]+u"^"+unicode(str(data[4]),'utf-8')+u'\r\n')
    datas2 =  my_datas[i][5]
    for data in datas2:
        print data[0],data[1],data[3],data[4]
        f.write(unicode(str(data[0]),'utf-8')+u"^"+data[1]+u'^'+data[3]+u"^"+unicode(str(data[4]),'utf-8')+u'\r\n')
