import requests;
import re;
class pacong:
    url="http://www.lisi.work:8090/";
    def getHtml(self):
        return requests.get(self.url).content.decode("UTF-8");
    def parse(self):
        html=self.getHtml();
        rex='<a +[^>]*[^<]+</a>'
        print("****")
        # list=re.findall('<small class="block">© 2019. 李思版权所有,盗版必究</small> ',html);
        list=re.findall(rex,html)
        return list;


def main():
    pac=pacong();
    print(pac.getHtml())
    print(pac.parse())




if __name__ == '__main__':
   main();
