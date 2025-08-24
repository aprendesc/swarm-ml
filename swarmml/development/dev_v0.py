import unittest
from swarmml.main import Main
from swarmml.configs.base_config import Config

class TestDev(unittest.TestCase):
    def setUp(self):
        self.main = Main()
        self.cfg = Config(version='test')

    def test_under_development(self):
        print('Development  test')


