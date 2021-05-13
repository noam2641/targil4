import requests
text = open('dests.txt', 'r', encoding='utf-8')
origins = 'תל אביב'
key = 'enter your api key'
response = dict()
distan = dict()
summery = dict()

for line in text:
 try:
    url_dest = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=%s&key=%s&destinations=%s"% (origins,key,line.strip())
    url_gec = "https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" % (line.strip(),key) 
    response[line] = requests.get(url_dest).json(),requests.get(url_gec).json()
    summery[line]=(response[line][0]['rows'][0]['elements'][0]['distance']['text'],
                    response[line][0]['rows'][0]['elements'][0]['duration']['value']/3600,
                    response[line][1]['results'][0]['geometry']['location']['lng'],
                    response[line][1]['results'][0]['geometry']['location']['lat'])
    print("city",line.strip(),
          '\n distance from tel aviv = ',summery[line][0],
          '\n duration from tel aviv= ',int(summery[line][1])," hours and ",int(summery[line][1]%1*60)," Minutes",
          '\n longitude = ',summery[line][2],
          '\n Latitude = ',summery[line][3],'\n')
    distan[line]=(response[line][0]['rows'][0]['elements'][0]['distance']['value'])
 except:
     print("There is a problem with the destination address("+line.strip()+") it does not exist\n")
order=list(distan.values())
order.sort(reverse=True) 
for i in range(0,len(order)):
 if i<3:
  for key in distan:
   if distan[key]==order[i]:
    print("city ",key.strip()," is number ",i+1," city with most distance from tel-aviv \n")
