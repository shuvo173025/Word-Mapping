import csv

sentence_list = []
sentence_list_3 = []
x = 0

with open('depression_dataset_2.txt', encoding='utf8') as f:
    for line in f:
        sentence_list.append(line.strip())


def getting_sentence():
    for sentence in sentence_list:
        cleaning_sentence(sentence)
    save_to_csv()


def cleaning_sentence(sentence):
    sentence_list_2 = []
    temp = str(sentence)
    temp2 = temp.replace("\"", " ")
    temp3 = temp2.replace("!", " ")
    temp4 = temp3.replace(",", " ")
    temp5 = temp4.replace("Emaz", "")
    temp6 = temp5.replace("Uddin", "")
    temp7 = temp6.replace("neutral", " ")
    temp8 = temp7.replace("sim_negative", " ")
    clean_sentence = temp8

    sentence_list_2.append(clean_sentence)
    list_of_list(sentence_list_2)


def list_of_list(sentence_list_2):
    sentence_list_3.append(sentence_list_2)


def save_to_csv():
    global x
    with open('test4.csv', 'w', encoding='UTF8') as data:
        writer = csv.writer(data)
        writer.writerows(sentence_list_3)


getting_sentence()
