import requests

owner = 'YOUR_GITHUB_USERNAME'
access_token = 'YOUR_ACCESS_TOKEN' 


def managed_projects(count=3):
    headers = {'Authorization':"Token "+access_token}

    repositories=[]

    url=f"https://api.github.com/users/{owner}/repos"
    response=requests.get(url, headers=headers).json()
    
    for repository in response:
        try:
            repositories.append({"name":repository['name'], "link":repository["svn_url"]})
        except:
            pass
 
    return {"managed_projects":repositories[:count]}

if __name__=='__main__':
    managed_projects()
