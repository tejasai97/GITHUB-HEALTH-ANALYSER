from .LibraryExtractor import LibraryExtractor
from .DatabaseDriver import DatabaseDriver
from .RepositoryData import RepositoryData
from apscheduler.schedulers.background import BackgroundScheduler

def addToDb(data, company):
    d = DatabaseDriver()
    result = {}
    for repo in data:
        result['OrgName'] = company
        result['RepoList'] = repo
        d.updateCompanyCollection(result)
        for library in data[repo]:
            Libdata = {}
            Libdata['lib'] = library
            Libdata['org'] = company
            Libdata['repo'] = repo
            d.updateLibrariesCollection(Libdata)


def updateRepo(company):
    d = DatabaseDriver()
    r = RepositoryData()
    listofRepos = d.getRepoList(company)
    for name in listofRepos:
        data = r.getAttributes(company, name)
        d.upsertRepo(data)


def schedUpdate():
    L = LibraryExtractor()
    d = DatabaseDriver()
    companyList = d.getCompanyList()
    for com in companyList:
        L.setCompany(com)
        data = L.getPom()
        addToDb(data, L.company)
        data = L.getPython()
        addToDb(data, L.company)
        data = L.getJavaScript()
        addToDb(data, L.company)
        updateRepo(com)

sched = BackgroundScheduler(daemon=True)
sched.add_job(schedUpdate,'interval',hours=24)
sched.start()

