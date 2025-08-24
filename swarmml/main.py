from eigenlib.utils.project_setup import ProjectSetup

class Main:
    def __init__(self):
        ProjectSetup().init()

    def initialize(self, config):
        self.model = config['model_class']

    def ETL(self, config):
        config = self.model(config).ETL(config)
        return config

    def train(self, config):
        config = self.model(config).train(config)
        return config

    def hparam_tuning(self, config):
        config = self.model(config).hparam_tuning(config)
        return config

    def eval(self, config):
        config = self.model(config).eval(config)
        return config

    def predict(self, config):
        config = self.model(config).predict(config)
        return config

    def serving(self, config):
        from swarmcompute.main import Main
        def aux(method, config):
            return getattr(self, method)(config)
        config['node_method'] = aux
        Main().launch_node(config)
        return config

    def deploy(self, config):
        from swarmml.modules.databricks_utils import DatabricksJobLaunchClass
        code = """
from swarmml.main import Main
from swarmml.configs.base_config import Config
main = Main()
main.initialize(Config().initialize())
main.serving(Config().serving())
"""
        job_name = config['job_name']
        cluster_id = config['cluster_id']
        DatabricksJobLaunchClass().run_job_from_code(code, job_name, cluster_id)

    def call(self, config):
        from swarmcompute.main import Main as SCMain
        ################################################################################################################
        config = SCMain().launch_client(config)
        return config
