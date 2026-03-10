import pandas as pd
import json
import webbrowser
from urllib.parse import quote


# try to load day from a JSON file, if it doesn't exist, use 1
try:
    with open('config.json', 'r') as file:
        config = json.load(file)
        day = config.get('day', 1)
except FileNotFoundError:
    config = {}
    day = 1

# try to load number_of_new_words from the config.json file, if it doesn't exist, use 6
number_of_new_words = config.get('number_of_new_words', 6)

number_of_words_to_review = config.get('number_of_words_to_review', 6)

review_pointer = config.get('review_pointer', 0)

send_url_template = config.get('send_url_template', 'https://www.google.com/search?q={prompt}')
#send_url_template = config.get('send_url_template', 'https://chatgpt.com/?q={prompt}')

# make a GUI to display and change the day, and a button to generate the prompt
import tkinter as tk

def copy_prompt():
    prompt_value = prompt_text.get('1.0', 'end-1c')
    root.clipboard_clear()
    root.clipboard_append(prompt_value)
    root.update()


def send_prompt():
    prompt_value = prompt_text.get('1.0', 'end-1c').strip()
    if not prompt_value:
        return
    send_url = send_url_template.format(prompt=quote(prompt_value))
    #print(send_url)
    webbrowser.open(send_url)

def update_prompt():
    # read in the word list and get the short list for the current day

    # read in ShortWordList.txt as a Python list of strings, one per line
    with open('ShortWordList.txt', 'r') as file:
        word_list = [line.strip() for line in file]

    #word_list = pd.read_csv('ShortWordList.csv', header=None)
    #start_index = (day - 1) * number_of_new_words
    end_index = review_pointer + number_of_new_words

    short_list = word_list[review_pointer:end_index]
    
    # make a list called review_list that contains number_of_words_to_review words
    # randomly chosen from the word_list, no repeats, from index 0 to review_pointer 
    # of the word_list
    review_list = []
    if review_pointer > 0:
        review_list = pd.Series(word_list[:review_pointer]).sample(n=min(number_of_words_to_review, review_pointer), replace=False).tolist()

    # make a string of the words in the short list, separated by commas
    short_list_string = ', '.join(short_list + review_list)
    # read in promptStart.txt and print the contents
    with open('promptStart.txt', 'r') as file:
        prompt_start = file.read()
    prompt_text_string = prompt_start + short_list_string
    prompt_text.delete('1.0', tk.END)
    prompt_text.insert(tk.END, prompt_text_string)

root = tk.Tk()
root.title("Prompt Generator")
day_frame = tk.Frame(root)
day_frame.pack()
prompt_label = tk.Label(root, text="Prompt")
prompt_label.pack()
prompt_text = tk.Text(root, height=8, width=80, wrap=tk.WORD)
prompt_text.pack()

actions_frame = tk.Frame(root)
actions_frame.pack()
copy_button = tk.Button(actions_frame, text="Copy Prompt", command=copy_prompt)
copy_button.pack(side=tk.LEFT)
send_button = tk.Button(actions_frame, text="Send Prompt", command=send_prompt)
send_button.pack(side=tk.LEFT)

update_prompt()
root.mainloop()



# save day and send_url_template to a JSON file
# config['day'] = day
config['send_url_template'] = send_url_template
config['number_of_new_words'] = number_of_new_words
config['number_of_words_to_review'] = number_of_words_to_review
config['review_pointer'] = review_pointer + number_of_new_words
with open('config.json', 'w') as file:
    json.dump(config, file)
