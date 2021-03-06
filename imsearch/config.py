import os
import copy

default_config = {
    'MONGO_URI': 'mongodb://localhost:27017/',
    'REDIS_URI': 'redis://localhost:6379/0',
    'DETECTOR_MODE': 'local'
}


def config_init(config):
    final_config = copy.deepcopy(default_config)
    for k, v in config.items():
        final_config[k] = v
    os.environ.update(final_config)
