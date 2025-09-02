from eigenlib.utils.setup import Setup

class Main:
    def __init__(self):
        Setup().init()

    def initialize(self, config):
        self.model = config['model_class']
        return config

    def ETL(self, config):
        config = self.model(config).ETL(config)
        return config

    def train(self, config):
        config = self.initialize(config)
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
        from eigenlib.utils.network_io import NetworkIO
        import os
        import time
        ################################################################################################################
        def serving_method(method, config):
            return getattr(self, method)(config)
        MASTER_ADDRESS = "localhost:9000"
        NetworkIO().launch_master(address=MASTER_ADDRESS)
        NetworkIO(verbose=True).launch_node(node_name=os.environ['PACKAGE_NAME'] + '_node', master_address=MASTER_ADDRESS, node_method=serving_method, delay=1)
        while True:
            time.sleep(10)
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
        from eigenlib.utils.network_io import NetworkIO
        ################################################################################################################
        MASTER_ADDRESS = config['master_address']
        client_name = config['client_name']
        delay = config['delay']
        password = config['password']
        target_node = config['target_node']
        payload = config['payload']
        ################################################################################################################
        client = NetworkIO()
        client.launch_node(node_name=client_name, master_address=MASTER_ADDRESS, node_method=lambda: "OK", delay=delay, password=password)
        resultado = client.call(target_node=target_node, payload=payload)
        client.stop()
        config['result'] = resultado
        print(resultado)
        return config


if __name__ == "__main__":
    import os
    from swarmml.configs.base_config import Config
    os.environ['REPO_FOLDER'] = 'swarm-ml'
    main = Main()
    cfg = Config()
    #main.initialize(cfg.initialize())
    #main.ETL(cfg.ETL())
    #main.train(cfg.train())
    #main.hparam_tuning(cfg.hparam_tuning())
    #main.eval(cfg.eval())
    #main.predict(cfg.predict())
    #main.serving(cfg.serving())
    #main.deploy(cfg.deploy())
    #main.call(cfg.predict())