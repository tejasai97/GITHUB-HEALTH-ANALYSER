import requests
import json
import pymongo
from dateutil import parser
import datetime

class GitHub:
    api_token = 'c08e4ed955919d9d346ec205496ce3b4a657511b'
    session = None
    url = None

    username = None
    def __init__(self):
        self.session = requests.session()
        self.session.headers['Authorization'] = 'token %s' % self.api_token
        self.session.headers['Content-type'] = 'application/json'
        self.session.headers['Accept'] ='application/vnd.github.machine-man-preview'
        self.url="https://api.github.com/"
        self.DBConnection = pymongo.MongoClient("ec2-34-207-75-4.compute-1.amazonaws.com")
        self.DB = self.DBConnection.GitDB


    def getgoogleRepr(self):
        url = self.url+"orgs/google/repos"
        response = self.session.get(url)
        print(response.links)
        data = json.loads(response.text)
        repo_list =[]
        for repo in data:
            repo_list.append(repo['name'])
        c =self.DB.company.find_one({"name":'google'})
        c['repos'] = repo_list
        result = self.DB.company.update({'name':'google'},c,upsert= True)
        print(result)
        print(response.links)

    def getissueData(self):
        url = self.url +"repos/google/googletest/issues"
        response =self.session.get(url,params={'state':'closed'})

        l =[]
        while 'next' in response.links:
            data = json.loads(response.text)
            for issue in data:
                opend = parser.parse(issue['created_at'])
                close = parser.parse(issue['closed_at'])
                l.append(int((close - opend).days))
            url = response.links['next']['url']
            print(url)
            response = self.session.get(url)
        data = json.loads(response.text)

        #last page
        for issue in data:
            opend = parser.parse(issue['created_at'])
            close = parser.parse(issue['closed_at'])
            l.append(int((close - opend).days))


        c = self.DB.repository.find_one({"name": 'test'})
        c['responsetime'] = l
        result = self.DB.repository.update({'name': 'test'}, c, upsert=True)
        print(result)

    def getforkData(self):
        url = self.url + "repos/google/googletest/forks"
        response = self.session.get(url)

        l = []
        x = datetime.datetime(2019,1,1)
        x = x.replace(tzinfo=None)
        while 'next' in response.links:
            data = json.loads(response.text)
            for fork in data:

                created = parser.parse(fork['created_at'])
                created = created.replace(tzinfo=None)
                if(created>x):
                    l.append(created)
            url = response.links['next']['url']
            print(url)
            response = self.session.get(url)
        data = json.loads(response.text)

        # last page
        for fork in data:
            created = parser.parse(fork['created_at'])
            created = created.replace(tzinfo=None)
            if(created>x):
                l.append(created)

        c = self.DB.repository.find_one({"name": 'test'})
        c['forkdates'] = l
        result = self.DB.repository.update({'name': 'test'}, c, upsert=True)
        print(result)


