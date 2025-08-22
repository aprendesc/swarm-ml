from swarmml.modules.titanic_model import TitanicModelClass

class Config:
    def __init__(self, version='v0', hypothesis=None):
        self.version = version
        self.hypothesis = hypothesis or 'Pruebas basicas con el dataset de Titanic'

    def initialize(self, update=None):
        base_cfg = {
            'hypothesis': self.hypothesis,
            'version': self.version,
            'model_class': TitanicModelClass,
        }
        return base_cfg | (update or {})

    def ETL(self, update=None):
        base_cfg = {
            'n_shards': 1,
            'cloud': False,
            'selected_dataset': 'titanic_dataset',
            'output_dataset_name': 'titanic_dataset_' + self.version,
        }
        return base_cfg | (update or {})

    def train(self, update=None):
        model_id = f'titanic_test_{self.version}'
        Catboost_params_dict = {
            'iterations': 1000,
            'learning_rate': 0.01,
            'depth': 6,
            'loss_function': 'Logloss',
            'eval_metric': 'Accuracy',
            'cat_features': [],
            'random_state': 42,
            'logging_level': 'Silent',
            'early_stopping_rounds': 20,
            'subsample': 0.8,
            'colsample_bylevel': 0.8,
            'l2_leaf_reg': 3,
            'border_count': 32,
            'thread_count': -1,
        }
        LGBM_params_dict = {
            'boosting_type': 'gbdt',
            'objective': 'binary',
            'metric': 'accuracy',
            'n_estimators': 1000,
            'learning_rate': 0.01,
            'num_leaves': 32,
            'max_depth': 6,
            'min_child_samples': 20,
            'subsample': 0.8,
            'subsample_freq': 1,
            'colsample_bytree': 0.8,
            'reg_alpha': 0.1,
            'reg_lambda': 0.1,
            'random_state': 42,
            'n_jobs': -1,
            'verbosity': -1,
        }
        XGB_params_dict = {
            'objective': 'binary:logistic',
            'eval_metric': 'logloss',
            'booster': 'gbtree',
            'max_depth': 4,
            'min_child_weight': 1,
            'gamma': 0.1,
            'learning_rate': 0.05,
            'subsample': 0.8,
            'colsample_bytree': 0.8,
            'reg_alpha': 0.01,
            'reg_lambda': 1.0,
            'num_boost_round': 500,
            'early_stopping_rounds': 20,
        }
        base_cfg = {
            'model_id': model_id,
            'to_cloud': False,
            'checkpoint': 1,
            'hparams_grid': {'num_boost_round': 0.001},
            'main_metric': 'accuracy',
            'Catboost_params_dict': Catboost_params_dict,
            'LGBM_params_dict': LGBM_params_dict,
            'XGB_params_dict': XGB_params_dict,
            'dataset_name': 'titanic_dataset_' + self.version,
        }
        return base_cfg | (update or {})

    def hparam_tuning(self, update=None):
        base_cfg = {
            'tuning_direction': 'maximize',
            'tuning_trials': 2,
        }
        return self.train() | base_cfg | (update or {})

    def eval(self, update=None):
        model_id = f'titanic_test_{self.version}'
        base_cfg = {
            'model_id': model_id,
            'cloud': False,
        }
        return base_cfg | (update or {})

    def predict(self, update=None):
        model_id = f'titanic_test_{self.version}'
        base_cfg = {
            'model_id': model_id,
        }
        return base_cfg | (update or {})

    def serving(self, update=None):
        base_cfg = {
                'master_address': 'tcp://localhost:5005',
                'password': 'internal_pass',
                'node_name': 'swarm-ml_node',
                'node_method': None,
                'delay': 1,
                'wait': True
                      }
        return base_cfg | (update or {})

    def deploy(self, update=None):
        base_cfg = {
            'cluster_id': '0715-112936-xf1o5dwg',
            'job_name': 'deployment'
        }
        return base_cfg | (update or {})

    def call(self, update=None):
        base_cfg = {
            'master_address': 'tcp://localhost:5005',
            'password': 'internal_pass',
            'node_name': 'swarm-ml_client',
            'address_node': 'swarm-ml_node',
            'payload': {'method':'train', 'config': self.train()},
            'delay': 0.1,
            'wait': False,
        }
        return base_cfg | (update or {})
