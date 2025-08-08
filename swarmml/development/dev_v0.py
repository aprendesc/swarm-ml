from eigenlib.utils.project_setup import ProjectSetupClass
ProjectSetupClass(project_folder='swarm-ml')


from eigenlib.utils.nano_net import NanoNetClass

class OSLLMClientClass:
    def __init__(self, master_address='tcp://95.18.166.44:5005'):
        password = 'youshallnotpass'
        ################################################################################################################
        self.client_node = NanoNetClass()
        self.client_node.launch_node(node_name='client_node', node_method=None, master_address=master_address, password=password, delay=1)

    def run(self, history):
        result = self.client_node.call(address_node="phi_4_node", payload={'history': history})
        return result

LLM = OSLLMClientClass()
answer = LLM.run([{'role': 'user', 'content': 'Actua como un simulador de fisicas: si tengo una caja con pelotas, una de adhesivo, otra de helio otra de plomo y otra de neutronio, en t0 la caja esta dada la vuelta y con las pelotas en el fondo, cual es el estado en t10 segundos? '}])
print(answer)