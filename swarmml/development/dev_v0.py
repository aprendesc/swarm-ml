import os
from eigenlib.utils.project_setup import ProjectSetup
########################################################################################################################
os.environ['BASE_PATH'] = f'C:/Users/{os.environ["USERNAME"]}/Desktop/proyectos'
os.environ['REPO_FOLDER'] = 'swarm-ml'
os.environ['MODULE_NAME'] = 'swarmml'
########################################################################################################################
ps = ProjectSetup()
ps.init()
ps.coverage()
########################################################################################################################





if False:
    #TEMPLATES
    class MyClass:
        def __init__(self):
            pass

        def run(self):
            print(ps)
            print('Hola Mundo!')

    import unittest
    class TestMyClass(unittest.TestCase):
        def SetUp(self):
            pass

        def test_run(self):
            mc = MyClass()
            mc.run()

    ########################################################################################################################

