from swarmml.main import MainClass
from swarmml.configs.test_config import test_config as config
import unittest

class TestMainClass(unittest.TestCase):
    def setUp(self):
        self.main = MainClass(config)

    def test_ETL(self):
        self.main.ETL(config)

    def test_train(self):
        self.main.train(config)

    def test_hparam_tuning(self):
        self.main.hparam_tuning(config)

    def test_eval(self):
        self.main.eval(config)

    def test_predict(self):
        self.main.predict(config)