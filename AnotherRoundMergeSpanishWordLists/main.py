import csv
import unicodedata


def read_word_list(file_path):
    for encoding in ('utf-8', 'cp1252', 'latin-1'):
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                return [line.strip() for line in file]
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError('codec', b'', 0, 1, f'Unable to decode {file_path}')


def read_csv_with_fallback(file_path):
    for encoding in ('utf-8', 'cp1252', 'latin-1'):
        try:
            with open(file_path, 'r', encoding=encoding, newline='') as file:
                return list(csv.reader(file))
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError('codec', b'', 0, 1, f'Unable to decode {file_path}')


def remove_accents(text):
    normalized = unicodedata.normalize('NFD', text)
    return ''.join(ch for ch in normalized if unicodedata.category(ch) != 'Mn')

def main():
    word_list = read_word_list('WordList.txt')
    words_list = [word.split() for word in word_list]
    another_list = words_list[0]

    # iterate through another_list. 
    # If the item isinteger, append it to a new list called int_list
    # If the item is not integer, append it to a new list called alpha_list
    int_list = []
    alpha_list = []
    for item in another_list:
        if item.isdigit():
            int_list.append(item)
        else:
            alpha_list.append(item)
    
    # zip the two lists together 
    zipped_list = list(zip(int_list, alpha_list))

    # output the zipped list to a new csv file called ZippedList.csv
    with open('ZippedList.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(zipped_list)

    # remove accented characters from the second column of the zipped list 
    # and replace them with their unaccented counterparts, 
    # as a new list called unaccented_list
    unaccented_list = []
    for i in range(len(zipped_list)):
        unaccented_item = (zipped_list[i][0], remove_accents(zipped_list[i][1]))
        unaccented_list.append(unaccented_item)

    # output the unaccented list to a new csv file called UnaccentedList.csv
    with open('UnaccentedList.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(unaccented_list)

    # load in Lemmas.csv 
    lemmas = read_csv_with_fallback('Lemmas.csv')

    # remove accented characters from the  lemmas list, store it in a new list called unaccented_lemmas
    unaccented_lemmas = []
    for lemma in lemmas:
        unaccented_lemma = (remove_accents(lemma[0]), remove_accents(lemma[1]), remove_accents(lemma[2]))
        unaccented_lemmas.append(unaccented_lemma)

    #outer join the two lists on the second column of the zipped list and the first column of the lemmas list
    joined_list = []
    for item in unaccented_list:
        matched = False
        for lemma in unaccented_lemmas:
            if item[1] == lemma[0]:
                joined_list.append((item[0], item[1], lemma[2]))
                matched = True
                break
        if not matched:
            joined_list.append((item[0], item[1], item[1]))

    # output the joined list to a new csv file called JoinedList.csv
    with open('JoinedList.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(joined_list)

    # check for duplicates in the third column of the joined list. 
    # When a duplicate is found, add the numbers in the first column together 
    # and keep the value in the third column.
    dupe_check = []
    seen = {}
    for item in joined_list:
        if item[2] in seen:
            seen[item[2]] = (seen[item[2]][0] + int(item[0]), item[2])
        else:
            seen[item[2]] = (int(item[0]), item[2])
    dupe_check = list(seen.values())

    # sort the dupe check list by the first column in descending order
    dupe_check.sort(key=lambda x: x[0], reverse=True)

    # output the dupe check list to a new csv file called DupeCheckList.csv
    with open('DupeCheckList.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(dupe_check)

    # Remove single letter lines from the dupe check list and save it to a new file called SingleLettersRemoved.txt
    # The new file should contain only the second column of the dupe check list, which is the lemma
    with open('SingleLettersRemoved.txt', 'w', encoding='utf-8') as file:
        for item in dupe_check:
            if len(item[1]) > 1:
                file.write(item[1] + '\n')
    
if __name__ == "__main__":    main()