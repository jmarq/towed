import json;

dc=json.JSONDecoder();
f=open("./towData.json");
d=f.read();
f.close();
d=dc.decode(d);
d=d['data'];
colorCounts={};
colorList=map( lambda(x): x[12], d);
for color in colorList:
  if(color in colorCounts):
    colorCounts[color]+=1;
  else:
    colorCounts[color]=1;
print colorCounts;
