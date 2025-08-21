import unittest
from swarmml.main import MainClass
from swarmml.configs.base_config import Config

class TestMain(unittest.TestCase):
    def setUp(self):
        self.main = MainClass()
        self.cfg = Config(version='test')

    def test_initialize(self):
        self.main.initialize(self.cfg.initialize())

    def test_ETL(self):
        self.main.initialize(self.cfg.initialize())
        self.main.ETL(self.cfg.ETL())

    def test_train(self):
        self.main.initialize(self.cfg.initialize())
        self.main.train(self.cfg.train())

    def test_hparam_tuning(self):
        self.main.initialize(self.cfg.initialize())
        self.main.hparam_tuning(self.cfg.hparam_tuning())

    def test_eval(self):
        self.main.initialize(self.cfg.initialize())
        self.main.eval(self.cfg.eval())

    def test_predict(self):
        self.main.initialize(self.cfg.initialize())
        self.main.predict(self.cfg.predict())

    def test_deploy(self):
        pass

    def test_call(self):
        pass
