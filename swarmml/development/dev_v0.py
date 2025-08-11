from eigenlib.utils.project_setup import ProjectSetupClass
ProjectSetupClass(project_folder='swarm-ml')

#MODULE##########################################################################################################
class MainModule:
    def __init__(self):
        pass

    def run(self, argument_1, argument_2):
        output = argument_1 + argument_2
        return output

#CONFIGURATION##########################################################################################################
config = {
    'argument_1': 1,
    'argument_2': 1,
    }

#LAUNCHER###############################################################################################################
def launcher(config):
    argument_1 = config['argument_1']
    argument_2 = config['argument_2']
    output = MainModule().run(argument_1, argument_2)
    config['output'] = output
    return config

launcher(config)
