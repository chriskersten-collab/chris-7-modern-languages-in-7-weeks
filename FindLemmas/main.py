import requests
import json

# read in ShortWordList.csv and create a list of words
with open('ShortWordList.csv', 'r') as f:
    words = f.read().splitlines()

# read num_words_to_check and start_pointer from config.json.
# If num_words_to_check is not set, set it to 5. If start_pointer is not set, set it to 0.
with open('config.json', 'r') as f:
    config = json.load(f)

num_words_to_check = config.get('num_words_to_check', 5)
start_pointer = config.get('start_pointer', 0)

if start_pointer + num_words_to_check >= len(words):
    num_words_to_check = len(words) - start_pointer

# iterate through words, num_words_to_check at a time, and print them out
for i in range(start_pointer, start_pointer + num_words_to_check):
    print(words[i])
    # query an online dictionary API for the word and print the lemma of the word
    
    response = requests.get(f'https://freedictionaryapi.com/api/v1/entries/es/{words[i]}')
    # print(response)
    if response.status_code == 200:
        data = response.json()
        # print(data)
        # extract the definition to a variable named def
        definition = None
        if data.get('entries') and data['entries'][0].get('senses'):
            definition = data['entries'][0]['senses'][0].get('definition')

        # make a new variable named def_minus_commas, which is the definition with all commas removed
        def_minus_commas = definition.replace(',', '') if definition else ''
        def_minus_commas = def_minus_commas.replace(';', '') if def_minus_commas else ''
        def_minus_commas = def_minus_commas.replace(')', '') if def_minus_commas else ''
        def_minus_commas = def_minus_commas.replace(':', '') if def_minus_commas else ''
        def_minus_commas = def_minus_commas.replace('.', '') if def_minus_commas else ''

        split_def = def_minus_commas.split() if def_minus_commas else []
        # look for the index of the word 'of' in split_def. If it exists, the lemma is the word after 'of'. If it doesn't exist, the lemma is the original word.
        if 'of' in split_def:
            of_index = split_def.index('of')
            if of_index + 1 < len(split_def):
                lemma = split_def[of_index + 1]
            else:
                lemma = words[i]
        else:
            lemma = words[i]

        print(i)
        print(def_minus_commas)
        print(f'lemma: {lemma}')
        print()

        if lemma != words[i]:
            upd = 'updated'
        else: upd = ''

        with open('Lemmas.csv', 'a') as of:
            of.write(f'{words[i]},{def_minus_commas},{lemma},{upd}\n')

# write start_pointer back to config.json
config['start_pointer'] = start_pointer + num_words_to_check
with open('config.json', 'w') as f:
    json.dump(config, f)
