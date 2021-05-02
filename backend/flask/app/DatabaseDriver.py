import pymongo


class DatabaseDriver:
    def __init__(self):
        self.DBConnection = pymongo.MongoClient("ec2-34-207-75-4.compute-1.amazonaws.com")
        self.DB = self.DBConnection.GitDB

    def updateCompanyCollection(self,data):
        CompanyName = data['OrgName']
        repolist = list()
        repolist.append(data['RepoList'])
        c = self.DB.Company.find_one({"OrgName": CompanyName})
        if c is None:
            c = {}
            c['OrgName'] = CompanyName
            c['RepoList'] = repolist
        else:
            c['RepoList'] = list(set(c['RepoList'] +repolist))
        result = self.DB.Company.update({"OrgName": CompanyName}, c, upsert=True)
        print(result)

    def updateLibrariesCollection(self,data):
        LibraryName = data['lib']
        OrgName = data['org']
        repoList =list()
        repoList.append(data['repo'])
        c = self.DB.Libraries.find_one({"LibName": LibraryName,"OrgName":OrgName})
        if c is None:
            c = {}
            c['LibName'] = LibraryName
            c['OrgName'] = OrgName
            c['LibRepos'] = repoList
        else:
            c['LibRepos'] = list(set(c['LibRepos'] +repoList))

        result = self.DB.Libraries.update({"LibName": LibraryName,"OrgName":OrgName}, c, upsert=True)
        print(result)

    def getCompanyList(self):
        c = self.DB.Company.distinct('OrgName')
        return c

    def getRepoList(self,company):
        org = self.DB.Company.find_one({"OrgName": company})
        listofRepos = org['RepoList']
        return listofRepos

    def upsertRepo(self,data):
        result = self.DB.Repository.update({"name": data['name']}, data, upsert=True)
        if result['updatedExisting'] is True:
            print("updated Repo: "+ data['name'])
        else:
            print("inserted Repo: "+ data['name'])
