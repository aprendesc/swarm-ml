from eigenlib.utils.testing_utils import TestUtils
TestUtils().get_coverage('./swarmml')

#MODULE##########################################################################################################
class MainModule:
    def __init__(self):
        pass

    def run(self, argument_1, argument_2):
        output = argument_1 + argument_2
        return output

#LAUNCHER###############################################################################################################
import unittest
class TestMainModule(unittest.TestCase):
    def setUp(self):
        pass

    def testrun(self):
        ################################################################################################################
        config = {
            'argument_1': 1,
            'argument_2': 1,
        }
        ################################################################################################################
        argument_1 = config['argument_1']
        argument_2 = config['argument_2']
        output = MainModule().run(argument_1, argument_2)
        config['output'] = output
        return config

if __name__ == "__main__":
    unittest.main()