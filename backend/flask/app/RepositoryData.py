import requests
import json
from dateutil import parser
import datetime


class RepositoryData:
    api_token = 'c08e4ed955919d9d346ec205496ce3b4a657511b'
    session = None
    url = None

    def __init__(self):
        self.session = requests.session()
        self.session.headers['Authorization'] = 'token %s' % self.api_token
        self.session.headers['Content-type'] = 'application/json'
        self.url = "https://api.github.com/"

    def getPullData(self, repo, i, name):
        openreq = 0
        closereq = 0
        url = self.url + "repos/" + i + "/" + name + "/pulls"
        response = self.session.get(url, params={'state': 'open'})
        data = json.loads(response.text)
        openreq = len(data)

        url = self.url + "repos/" + i + "/" + name + "/pulls"
        response = self.session.get(url, params={'state': 'closed'})
        data = json.loads(response.text)
        closereq = len(data)
        repo['name'] = name
        repo['openpullrequests'] = openreq
        repo['closepullrequest'] = closereq

    def getIssueData(self, repo, i, name):
        openIssues = 0
        closedIssues = 0
        url = self.url + "repos/" + i + "/" + name + "/issues"
        response = self.session.get(url, params={'state': 'open'})
        data = json.loads(response.text)
        openIssues = len(data)

        url = self.url + "repos/" + i + "/" + name + "/issues"
        response = self.session.get(url, params={'state': 'closed'})
        data = json.loads(response.text)
        closedIssues = len(data)
        repo['openissues'] = openIssues
        repo["closeissues"] = closedIssues

    def calculateHealth(self, repo):
        openIssues = repo['openissues']
        closedIssues = repo["closeissues"]
        openreq = repo['openpullrequests']
        closereq = repo['closepullrequest']
        reqeffective = 0
        issueEffective = 0
        if (openreq == 0 or closereq == 0):
            reqeffective = 0
        else:
            reqeffective = openreq / closereq
        if (openIssues == 0 or closedIssues == 0):
            ratio = 0
        else:
            ratio = closedIssues / openIssues
        issueEffective = 10 * (ratio / 1 + ratio)

        health = ((0.66 * reqeffective) + (0.34 * issueEffective))
        repo["health"] = int(health * 100)

    def getForkData(self, repo, i, name):
        url = self.url + "repos/" + i + "/" + name + "/forks"
        response = self.session.get(url)
        data = json.loads(response.text)
        forks = len(data)

        url = self.url + "repos/" + i + "/" + name + "/forks"
        response = self.session.get(url)
        forkDates = []
        x = datetime.datetime(2019, 1, 1)
        x = x.replace(tzinfo=None)
        while 'next' in response.links:
            data = json.loads(response.text)
            for fork in data:

                created = parser.parse(fork['created_at'])
                created = created.replace(tzinfo=None)
                if (created > x):
                    forkDates.append(created)
            url = response.links['next']['url']
            # print(url)
            response = self.session.get(url)
        data = json.loads(response.text)

        # last page
        try:
            for fork in data:
                created = parser.parse(fork['created_at'])
                created = created.replace(tzinfo=None)
                if (created > x):
                    forkDates.append(created)
        except Exception:
            pass

        repo["forks"] = forks
        repo["forkdates"] = forkDates

    def getCommitData(self, repo, i, name):
        url = self.url + "repos/" + i + "/" + name + "/commits"
        response = self.session.get(url)
        data = json.loads(response.text)
        commits = len(data)

        url = self.url + "repos/" + i + "/" + name + "/issues"
        response = self.session.get(url, params={'state': 'closed'})

        responseTime = []
        while 'next' in response.links:
            data = json.loads(response.text)
            for issue in data:
                opend = parser.parse(issue['created_at'])
                close = parser.parse(issue['closed_at'])
                responseTime.append(int((close - opend).days))

            url = response.links['next']['url']
            # print(url)
            response = self.session.get(url)
        data = json.loads(response.text)

        # last page
        try:
            for issue in data:
                opend = parser.parse(issue['created_at'])
                close = parser.parse(issue['closed_at'])
                responseTime.append(int((close - opend).days))
        except Exception:
            pass

        repo["commits"] = commits
        repo["responsetime"] = responseTime

    def getAttributes(self, CompanyName, name):
        repo = {}
        self.getPullData(repo, CompanyName, name)
        self.getIssueData(repo, CompanyName, name)
        self.calculateHealth(repo)
        self.getForkData(repo, CompanyName, name)
        self.getCommitData(repo, CompanyName, name)
        return repo
