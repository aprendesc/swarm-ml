from eigenlib.utils.project_setup import ProjectSetup

class MainClass:
    def __init__(self, config):
        ProjectSetup().init()
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