
import json

config = {}

config['start_pointer'] = 0
config['num_words_to_check'] = 5
with open('config.json', 'w') as f:
    json.dump(config, f)
