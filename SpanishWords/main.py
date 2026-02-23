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

# try to load num_words from the config.json file, if it doesn't exist, use 12
num_words = config.get('num_words', 12)

#send_url_template = config.get('send_url_template', 'https://www.google.com/search?q={prompt}')
send_url_template = config.get('send_url_template', 'https://chatgpt.com/?q={prompt}')

# make a GUI to display and change the day, and a button to generate the prompt
import tkinter as tk


def sync_day_from_entry():
    global day
    try:
        parsed_day = int(day_var.get())
        if parsed_day < 1:
            raise ValueError
        day = parsed_day
    except ValueError:
        day_var.set(str(day))


def generate_prompt():
    global day
    sync_day_from_entry()
    day_var.set(str(day))
    # save day to a JSON file
    config['day'] = day
    with open('config.json', 'w') as file:
        json.dump(config, file)
    # update the prompt
    update_prompt()


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
    word_list = pd.read_csv('ShortWordList.csv', header=None)
    start_index = (day - 1) * num_words
    end_index = start_index + num_words
    short_list = word_list.iloc[start_index:end_index]
    # make a string of the words in the short list, separated by commas
    short_list_string = ', '.join(short_list[0])
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
day += 1
day_label = tk.Label(day_frame, text="Day:")
day_label.pack(side=tk.LEFT)
day_var = tk.StringVar(value=str(day))
day_entry = tk.Entry(day_frame, textvariable=day_var, width=6)
day_entry.pack(side=tk.LEFT)
day_entry.bind('<Return>', lambda event: sync_day_from_entry())
day_entry.bind('<FocusOut>', lambda event: sync_day_from_entry())
generate_button = tk.Button(root, text="Generate Prompt", command=generate_prompt)
generate_button.pack()

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
config['day'] = day
config['send_url_template'] = send_url_template
config['num_words'] = num_words
with open('config.json', 'w') as file:
    json.dump(config, file)
