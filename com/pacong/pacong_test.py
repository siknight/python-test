import requests
import re
class Zhenghun(object):
    url="http://www.zhenai.com/zhenghun/"
    def __init__(self,city):
        self.newUrl=self.url+city+"/nv";
    def getHtml(self):
        return requests.get(self.newUrl).content;
    def prase(self):
        html = self.getHtml()
        rex = '<a href="http://album.zhenai.com/u/[0-9]+"[^>]*[^<]+</a>'
        list = re.findall(rex,html)
        return list
def main():
    cityList=["sanya","hainan"];
    for city in cityList:
        zhenghun=Zhenghun("city");
        print(zhenghun.getHtml());
        #aaaaaaaaaaaaaaaaaaaa
        list = zhenghun.prase()
        for l in list:
            u = l.split('"')
            #print(u[1])
            n = l[l.rfind('"')+2:l.rfind("<")]
            print(n+"\t\t\t"+u[1])



if __name__=="__main__":
    main();