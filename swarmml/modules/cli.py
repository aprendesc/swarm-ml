from swarmml.main import MainClass
from swarmml.configs.test_config import config

class CLI:
    def __init__(self):
        print("""

██████╗░██████╗░░█████╗░░░░░░██╗███████╗░█████╗░████████╗  ░█████╗░██╗░░░░░██╗
██╔══██╗██╔══██╗██╔══██╗░░░░░██║██╔════╝██╔══██╗╚══██╔══╝  ██╔══██╗██║░░░░░██║
██████╔╝██████╔╝██║░░██║░░░░░██║█████╗░░██║░░╚═╝░░░██║░░░  ██║░░╚═╝██║░░░░░██║
██╔═══╝░██╔══██╗██║░░██║██╗░░██║██╔══╝░░██║░░██╗░░░██║░░░  ██║░░██╗██║░░░░░██║
██║░░░░░██║░░██║╚█████╔╝╚█████╔╝███████╗╚█████╔╝░░░██║░░░  ╚█████╔╝███████╗██║
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░╚════╝░╚══════╝░╚════╝░░░░╚═╝░░░  ░╚════╝░╚══════╝╚═╝
░╚════╝░╚══════╝╚═╝ 
                    """)
        self.main = MainClass(config)

    def run(self):
        while True:
            print("""
========================================================================================================================
""")

            #MENU
            menu_1 = """
1- ETL
2- Train
3- Hyperparameters tuning
4- Eval
5- Predict

Select a method: """
            method = input(menu_1)

            print("""

█▀█ █▀▀ █▀ █▀█ █▀█ █▄░█ █▀ █▀▀
█▀▄ ██▄ ▄█ █▀▀ █▄█ █░▀█ ▄█ ██▄
========================================================================================================================
""")

            # TREE
            if method == '1':
                self.main.ETL(config)
                print('ETL Finished.')
            elif method == '2':
                self.main.train(config)
                print('Training finished')
            elif method == '3':
                self.main.hparam_tuning(config)
                print('Hyperparameter tuning finished.')
            elif method == '4':
                self.main.eval(config)
                print('Eval finished.')
            elif method == '5':
                self.main.predict(config)

if __name__ == "__main__":
    CLI().run()
