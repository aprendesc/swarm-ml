from eigenlib.utils.project_setup import ProjectSetup

class MainClass:
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

    def deploy(self):
        pass

    def call(self, config):
        from swarmcompute.main import MainClass as SCMainClass
        ################################################################################################################
        sc_main = SCMainClass(config)
        response = sc_main.launch_personal_net(config)
        config['response'] = response
        return config

    def project_dev_server(self, **kwargs):
        import os
        from swarmautomations.main import MainClass as SAMainClass
        config = {
            'launch_master': False,
            'node_name': os.environ['MODULE_NAME'],
            'node_delay': 1
        }
        sa_main = SAMainClass(config)
        sa_main.dev_tools_server(config)
