import os
import unittest
from eigenlib.utils.project_setup import ProjectSetup

"""Environments activation"""
project_folder = 'swarm-ml'
if True:
    ########################################################################################################################
    #project_folder = 'swarm-compute'
    #project_folder = 'swarm-automations'
    #project_folder = 'swarm-intelligence'
    #project_folder = 'eigenlib'ç
    base_path = f'C:/Users/{os.environ["USERNAME"]}/Desktop/proyectos'
    project_folder = 'swarm-ml'
    path_dirs = [
                os.path.join(base_path, 'swarm-ml'),
                os.path.join(base_path, 'swarm-intelligence'),
                os.path.join(base_path, 'swarm-automations'),
                os.path.join(base_path, 'swarm-compute'),
                os.path.join(base_path, 'eigenlib')
            ]
    ########################################################################################################################
    ps = ProjectSetup()
    ps.init(path_dirs=path_dirs, working_dir=os.path.join(base_path, project_folder), project_folder=project_folder)
    test_df, modules_df = ps.coverage()
    print('COPY###############################################################################################################')
    print('test_paths = ' + str(list(test_df['tests'])).replace(',', ',\n\t#').replace(']', '\n]').replace('[', '[\n\t#'))
    print('###################################################################################################################')


class MyClass:
    def __init__(self):
        pass

    def run(self):
        print('Hola Mundo!')

class TestMyClass(unittest.TestCase):
    def SetUp(self):
        import sys
        sys.path.extend([f'C:/Users/{os.environ["USERNAME"]}/Desktop/proyectos/eigenlib'])
        pass

    def test_run(self):
        mc = MyClass()
        mc.run()



