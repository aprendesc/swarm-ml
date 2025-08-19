import unittest
import os
from eigenlib.utils.project_setup import ProjectSetup

########################################################################################################################
base_path = f'C:/Users/{os.environ["USERNAME"]}/Desktop/proyectos'
project_folder = 'swarm-ml'
path_dirs = [
            os.path.join(base_path, 'swarm-ml'),
            #os.path.join(base_path, 'swarm-intelligence'),
            #os.path.join(base_path, 'swarm-automations'),
            #os.path.join(base_path, 'swarm-compute'),
            os.path.join(base_path, 'eigenlib')
        ]
########################################################################################################################
ps = ProjectSetup()
ps.health_check(base_path=base_path, project_folder=project_folder, path_dirs=path_dirs,)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#TEMPLATES
class MyClass:
    def __init__(self):
        pass

    def run(self):
        print(ps)
        print('Hola Mundo!')

class TestMyClass(unittest.TestCase):
    def SetUp(self):
        pass

    def test_run(self):
        mc = MyClass()
        mc.run()

import json
import os
import requests

class DatabricksJobLaunchClass:
    def __init__(self, DATABRICKS_INSTANCE=None, API_TOKEN=None, JOB_NAME=None, PARAMETERS=None):
        self.DATABRICKS_INSTANCE = DATABRICKS_INSTANCE
        self.API_TOKEN = API_TOKEN
        self.JOB_NAME = JOB_NAME
        self.PARAMETERS = PARAMETERS if PARAMETERS is not None else []

    def create_job(self, job_name, cluster_id, script_path):
        job_config = {
            "name": job_name,
            "tasks": [{
                    "task_key": "test_databricks_job_task",
                    "description": "A test job for running a Python script",
                    "existing_cluster_id": cluster_id,
                    "spark_python_task": {
                                "python_file": script_path,
                                "parameters": self.PARAMETERS
                            }
            }],
            "max_concurrent_runs": 1
        }
        headers = {'Authorization': f'Bearer {self.API_TOKEN}', 'Content-Type': 'application/json'}
        response = requests.post(f'{self.DATABRICKS_INSTANCE}/api/2.0/jobs/create', headers=headers, data=json.dumps(job_config))
        if response.status_code == 200:
            print("Job created successfully.")
            print("Job ID:", response.json()["job_id"])
            self.job_id = response.json()["job_id"]
        else:
            print("Failed to create job.")
            print("Response:", response.text)

    def launch(self, job_id=None):
        if job_id is None:
            job_id = self.job_id
        run_payload = {
            "job_id": job_id,
            "notebook_params": {
                "parameters": json.dumps(["-f", "/Volumes/catalog/schema/volume/path/to/file.csv"])
            }
        }
        headers = {'Authorization': f'Bearer {self.API_TOKEN}','Content-Type': 'application/json'}
        response = requests.post(f'{self.DATABRICKS_INSTANCE}/api/2.0/jobs/run-now', headers=headers, data=json.dumps(run_payload))

        if response.status_code == 200:
            run_id = response.json()["run_id"]
            print("Job launched successfully.")
            print("Run ID:", run_id)
        else:
            print("Failed to launch job.")
            print("Response:", response.text)

    def run_job_from_code(self, code, job_name, cluster_id):
        script_path = f'./temp/{cluster_id}.py'
        api_token = os.environ['DB_TOKEN']
        instance = os.environ['DATABRICKS_INSTANCE']
        with open(script_path, "w") as archivo:
            archivo.write(code)

        with open(f"./scripts/update_repos_template.sh", "r") as f:
            template = f.read()
        template = template.replace('<DB_REPO_ID>', os.environ['DB_REPO_ID']).replace('<PROJECT_FOLDER>', os.environ['PROJECT_FOLDER'])
        with open(f"./scripts/update_repos.sh", "w") as f:
            f.write(template)

        os.system(f"C:/Users/AlejandroPrendesCabo/Desktop/proyectos/{project_folder}/scripts/update_repos.sh")
        job_config = {"DATABRICKS_INSTANCE": instance, "API_TOKEN": api_token, "JOB_NAME": job_name, "JOB_ID": "job_id", "CLUSTER_ID": cluster_id, "SCRIPT_PATH": script_path, "PARAMETERS": []}
        self.__init__(**job_config)
        self.create_job(job_name, cluster_id, script_path)
        self.launch()



class TestDatabricksJobLaunchClass(unittest.TestCase):
    def SetUp(self):
        pass

    def test_run(self):
        job_name = 'test_job'
        cluster_id = '0715-112936-xf1o5dwg'
        code = 'print("Hola mundo!")'
        dbjl = DatabricksJobLaunchClass(DATABRICKS_INSTANCE=os.environ['DATABRICKS_INSTANCE'], API_TOKEN=os.environ['DB_TOKEN'], JOB_NAME=job_name)
        dbjl.run_job_from_code(code, job_name, cluster_id)
