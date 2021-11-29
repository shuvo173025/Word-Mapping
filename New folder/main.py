import csv

# word data
csv_file_for_word = open('test.csv', encoding="utf8")
csv_word_file_reader = csv.reader(csv_file_for_word)

# moderate data
csv_file_for_data = open('test3.csv', encoding="utf8")
csv_data_file_reader = csv.reader(csv_file_for_data)

all_word_csv = []
all_moderate_word_csv = []
all_rural_word_csv = []
unchanged_word_dummy_list = []
unchanged_word_dummy_list_temp = []
unchanged_word_dummy_list_2 = []
unchanged_word_dummy_list_temp_2 = []
unchanged_word_final_list = []
expected_rural_text = ""
re_run_expected_rural_text = ""
test = ""
counter = 0


# test2 file 2 te moderate and rural word gulake alada kora hobe
def separete_csv_word_list():
    for info in csv_word_file_reader:
        all_word_csv.append(info)

    for a in range(len(all_word_csv)):
        all_moderate_word_csv.append(all_word_csv[a][0])
        all_rural_word_csv.append(all_word_csv[a][1])
    getting_dummy_modetare_data()


def getting_dummy_modetare_data():
    global counter
    for info in csv_data_file_reader:
        if not info:
            pass
        else:
            dummy_moderate_text = info
            print("\n")
            x = input("\t\t\t\t\t\t To procceed the mapping, press y : ->  ")
            print("\n\n\n")
            if x == "y" or "ইয়":
                counter += 1
                processing(dummy_moderate_text)


def processing(dummy_moderate_text):
    temp = str(dummy_moderate_text)
    temp1 = temp.replace('।', " ")
    temp2 = temp1.replace(',', " ")
    temp3 = temp2.replace('\'', " ")
    temp4 = temp3.replace('\"', " ")
    temp5 = temp4.replace('-', "")
    temp6 = temp5.replace('?', " ")
    processed_moderate_data = temp6

    print(processed_moderate_data)

    build_word_list(processed_moderate_data)
    processed_moderate_data = ""


def build_word_list(processed_moderate_data):
    processed_moderate_data_word_list = list(processed_moderate_data.split(" "))
    processed_moderate_data_word_list.remove('[')
    processed_moderate_data_word_list.remove(']')
    matching_and_changing(processed_moderate_data_word_list)


def matching_and_changing(processed_moderate_data_word_list):
    for c in range(len(processed_moderate_data_word_list)):
        unchanged_word_dummy_list_temp_2.append(processed_moderate_data_word_list[c])
        for d in range(len(all_moderate_word_csv)):
            if processed_moderate_data_word_list[c] == all_moderate_word_csv[d]:
                unchanged_word_dummy_list_temp.append(processed_moderate_data_word_list[c])
                processed_moderate_data_word_list[c] = all_rural_word_csv[d]

    back_to_text(processed_moderate_data_word_list)
    processed_moderate_data_word_list.clear()


def back_to_text(processed_moderate_data_word_list):
    for i in processed_moderate_data_word_list:
        global expected_rural_text
        expected_rural_text = expected_rural_text + str(i) + " "

    print(expected_rural_text)
    global test
    test = expected_rural_text
    expected_rural_text = ""
    unchanged_word()


def unchanged_word():
    global counter
    accuracy = 0
    for ele in unchanged_word_dummy_list_temp:
        if ele.strip():
            unchanged_word_dummy_list.append(ele)

    for ele in unchanged_word_dummy_list_temp_2:
        if ele.strip():
            unchanged_word_dummy_list_2.append(ele)

    print("\n")
    accuracy = ((len(unchanged_word_dummy_list) / len(unchanged_word_dummy_list_2)) * 100)
    print("\t\t\t\t\t\t At sentence ",counter," Here we got ", int(accuracy), "% accuracy from this mapping")
    print("\n")
    unchanged_word_final_list = set(unchanged_word_dummy_list_2) - set(unchanged_word_dummy_list)
    print(unchanged_word_final_list)
    unchanged_word_dummy_list.clear()
    unchanged_word_dummy_list_2.clear()
    unchanged_word_dummy_list_temp.clear()
    unchanged_word_dummy_list_temp_2.clear()
    unchanged_word_final_list.clear()
    print("\n")

separete_csv_word_list()
