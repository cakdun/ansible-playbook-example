import requests
from requests.auth import HTTPBasicAuth

awx_url = 'http://192.168.1.100/api/v2/'

templateId = 18
awx_username = 'nofrisdan'
awx_password = 'N03d0600'

def launch_job():
    awx_job_url = awx_url+"workflow_job_templates/"+str(templateId)+"/launch/"
    headers = {
        'Content-Type': 'application/json'
    }

    # launch
    response = requests.post(awx_job_url,auth=HTTPBasicAuth(awx_username,awx_password)).json()

    print(response)

    # JobId = response.get("id")

    # print("Job Success run in ID:",JobId)



if __name__ == "__main__":
    launch_job()