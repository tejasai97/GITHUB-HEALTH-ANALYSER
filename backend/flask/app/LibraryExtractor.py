import requests
import json
import urllib3
import requirements
from xml.etree import ElementTree as ET
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class LibraryExtractor:
    api_token = 'c08e4ed955919d9d346ec205496ce3b4a657511b'
    session = None
    url = None
    company = None
    
    def __init__(self):
        self.session = requests.session()
        self.session.headers['Authorization'] = 'token %s' % self.api_token
        self.session.headers['Content-type'] = 'application/json'
        self.url="https://api.github.com/"

    def setCompany(self,name):
        self.company=name

    def getPom(self):
        url = self.url + "orgs/"+self.company+"/repos"
        response = self.session.get(url,params={'type':'public'})
        count=0
        outdata ={}
        while 'next' in response.links:
            data = json.loads(response.content)
            for rep in data:
                # count+=1
                u = "https://raw.githubusercontent.com/"+self.company+"/"+rep['name']+"/master/pom.xml"
                l =self.getModules(u)
                li=[]
                for module in l:
                    ur = "https://raw.githubusercontent.com/"+self.company+"/"+rep['name']+"/master/"+module+"/pom.xml"
                    li +=self.getLibraries(ur)
                li = set(li)
                li = list(li)
                if len(l) !=0:
                    count += 1

                    print(li)
                    print("xxxxx--"+rep['name']+"--xxxxx")
                    print(count)
                    outdata[rep['name']] = li
            url = response.links['next']['url']
            response = self.session.get(url)
        return outdata

    def getLibraries(self,url):
        http = urllib3.PoolManager()
        r = http.request('GET', url)
        libraryList = []
        if r.status != 404:
            f = ET.XML(r.data)
            for element in f:
                if "dependencies" in element.tag:
                    for i in range(0,len(element)):
                        libraryList.append(element[i][0].text)
        return libraryList

    def getModules(self,url):
        http = urllib3.PoolManager()
        r = http.request('GET', url)
        l =[]
        if r.status != 404:
            f = ET.XML(r.data)
            for element in f:
                # print(element)
                if "modules" in element.tag:
                    for i in range(0, len(element)):
                        if '$' not in element[i].text:
                            l.append(element[i].text)
        return l

    def getPython(self):
        url = self.url + "orgs/"+self.company+"/repos"
        response = self.session.get(url,params={'type':'public'})
        count = 0
        outdata = {}
        while 'next' in response.links:
            data = json.loads(response.content)
            for rep in data:
                u = "https://raw.githubusercontent.com/" + self.company + "/" + rep['name'] + "/master/requirements.txt"
                l = self.getRequirement(u)
                if(len(l)!=0):
                    outdata[rep['name']] = l
                    print(rep['name'])
                    print(l)
                    count+=1
                    print(count)
            url = response.links['next']['url']
            response = self.session.get(url)
        return outdata

    def getRequirement(self,url):
        http = urllib3.PoolManager()
        r = http.request('GET', url)
        l=[]
        if r.status != 404:
            file = r.data.decode("utf-8")
            try:
                for req in requirements.parse(file):
                    if req.name != None:
                        l.append(req.name)
            except Exception:
                pass
        return l

    def getJavaScript(self):
        url = self.url + "orgs/" + self.company + "/repos"
        response = self.session.get(url, params={'type': 'public'})
        count = 0
        outdata = {}
        while 'next' in response.links:
            data = json.loads(response.content)
            for rep in data:
                u = "https://raw.githubusercontent.com/" + self.company + "/" + rep['name'] + "/master/package.json"
                l = self.getPackages(u)
                if (len(l) != 0):
                    outdata[rep['name']] = l
                    print(rep['name'])
                    print(l)
                    count += 1
                    print(count)
            url = response.links['next']['url']
            response = self.session.get(url)
        return outdata

    def getPackages(self,url):
        http = urllib3.PoolManager()
        r = http.request('GET', url)
        l = []
        if r.status != 404:
            file = r.data.decode("utf-8")
            try:
                data  = json.loads(file)
                if 'dependencies' in data:
                    for d in data['dependencies']:
                        if "@" not in d:
                            l.append(d)
            except Exception:
                pass
        return l



