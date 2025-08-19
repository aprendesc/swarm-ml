import unittest
import os
from eigenlib.utils.project_setup import ProjectSetup

########################################################################################################################
base_path = f'C:/Users/{os.environ["USERNAME"]}/Desktop/proyectos'
project_folder = 'swarm-ml'
path_dirs = [
            os.path.join(base_path, 'swarm-ml'),
            #os.path.join(base_path, 'swarm-intelligence'),
            #os.path.join(base_path, 'swarm-automations'),
            #os.path.join(base_path, 'swarm-compute'),
            os.path.join(base_path, 'eigenlib')
        ]
########################################################################################################################
ps = ProjectSetup()
ps.health_check(base_path=base_path, project_folder=project_folder, path_dirs=path_dirs,)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#TEMPLATES
class MyClass:
    def __init__(self):
        pass

    def run(self):
        print(ps)
        print('Hola Mundo!')

class TestMyClass(unittest.TestCase):
    def SetUp(self):
        pass

    def test_run(self):
        mc = MyClass()
        mc.run()

