import json
import os
import requests

class DatabricksJobLaunchClass:
    def __init__(self, DATABRICKS_INSTANCE=None, API_TOKEN=None, PARAMETERS=None, task_key=None, task_description=None):
        self.DATABRICKS_INSTANCE = DATABRICKS_INSTANCE or os.environ.get('DATABRICKS_INSTANCE')
        self.API_TOKEN = API_TOKEN or os.environ.get('DB_TOKEN')
        self.PARAMETERS = PARAMETERS if PARAMETERS is not None else []
        self.task_key = task_key or 'generic_task'
        self.task_description = task_description or 'Generic Task'

    def create_job(self, job_name, cluster_id, script_path):
        job_config = {
            "name": job_name,
            "tasks": [{
                "task_key": self.task_key,
                "description": self.task_description,
                "existing_cluster_id": cluster_id,
                "spark_python_task": {"python_file": script_path, "parameters": self.PARAMETERS}}],
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
        headers = {'Authorization': f'Bearer {self.API_TOKEN}', 'Content-Type': 'application/json'}
        response = requests.post(f'{self.DATABRICKS_INSTANCE}/api/2.0/jobs/run-now', headers=headers, data=json.dumps(run_payload))

        if response.status_code == 200:
            run_id = response.json()["run_id"]
            print("Job launched successfully.")
            print("Run ID:", run_id)
        else:
            print("Failed to launch job.")
            print("Response:", response.text)

    def run_job_from_code(self, code, job_name, cluster_id):
        import tempfile
        import os
        from eigenlib.utils.databricks_storage_utils import DatabricksStorageUtilsClass

        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write(code)
            temp_full_path = f.name

        temp_dir = os.path.dirname(temp_full_path)
        filename = os.path.basename(temp_full_path)
        DatabricksStorageUtilsClass().cloud_upload_file(temp_dir, "/tmp/", filename)
        os.unlink(temp_full_path)
        self.create_job(job_name, cluster_id, os.path.join('dbfs:/tmp', filename).replace('\\','/'))
        self.launch()

import unittest
class TestDatabricksJobLaunchClass(unittest.TestCase):
    def SetUp(self):
        pass

    def test_run(self):
        job_name = 'test_job'
        cluster_id = '0715-112936-xf1o5dwg'
        code = 'print("Hola mundo!")'
        dbjl = DatabricksJobLaunchClass(DATABRICKS_INSTANCE=os.environ['DATABRICKS_INSTANCE'],
                                        API_TOKEN=os.environ['DB_TOKEN'], JOB_NAME=job_name)
        dbjl.run_job_from_code(code, job_name, cluster_id)
