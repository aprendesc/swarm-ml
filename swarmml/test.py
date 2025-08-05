import unittest
from swarmml.main import MainClass
from swarmml.config import test_config as config
from eigenlib.utils.project_setup import ProjectSetupClass
ProjectSetupClass(project_folder='swarm-ml', test_environ=True)

class TestUtilsClass(unittest.TestCase):

    def setUp(self):
        self.main = MainClass(config)
        self.config = config

    def test_ETL(self):
        self.main.ETL(self.config)

    def test_train(self):
        self.main.train(self.config)

    def test_hparam_tuning(self):
        self.main.hparam_tuning(self.config)

    def test_eval(self):
        self.main.eval(self.config)

    def test_predict(self):
        self.main.predict(self.config)
