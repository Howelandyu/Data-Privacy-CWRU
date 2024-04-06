import pickle


def read_file():
    # Opening file
    file = open('user-ct-test-collection-02.txt', 'r')
    file_list = []
    # Using for loop
    used_query_list = []
    for line_str in file:
        item_list = []
        line_str = line_str.strip()
        # print(line_str)
        line_list = line_str.split()
        # print(line_list)
        item_list.append(line_list[0])
        contain_web = None
        for count, value in enumerate(line_list):
            contain_web = False
            if '2006' in value:
                query_str = " "
                for i in range(1, count):
                    query_str += line_list[i]
                    query_str += ' '
                query_str = query_str.strip()
                item_list.append(query_str)
            if 'http' in value:
                contain_web = True
        assert contain_web is not None
        if contain_web:
            """ don't consider 0"""
            item_list.append(line_list[-2])
            if item_list[1] != '-' and 'www' not in item_list[1]:
                if item_list[1] not in used_query_list:
                    file_list.append(item_list)
                    used_query_list.append(item_list[1])
        else:
            item_list.append('0')
        # file_list.append(item_list)
        print(item_list)
        # print(file_list)
    with open('file_list.pkl', 'wb') as f:
        pickle.dump(file_list, f)

    # print("{}".format(file_list))
    # print("{}".format(len(file_list)))

    # Closing files
    file.close()


def get_query_pair_list():
    with open('file_list.pkl', 'rb') as f:
        file_list = pickle.load(f)
    # print("{}".format(file_list))
    # print("{}".format(len(file_list)))

    id_stat_dict = {}
    for query in file_list:
        if query[0] in id_stat_dict.keys():
            id_stat_dict[query[0]] += 1
        else:
            id_stat_dict[query[0]] = 1
    # print(id_stat_dict)
    filtered_id_stat_dict = {}
    for id_str in id_stat_dict.keys():
        if 20 <= id_stat_dict[id_str] <= 30:
            filtered_id_stat_dict[id_str] = id_stat_dict[id_str]
    # print(len(filtered_id_stat_dict))

    query_pair_list = []
    file_num = len(file_list)
    for count, value in enumerate(file_list):
        if value[0] not in filtered_id_stat_dict.keys():
            continue
        print(count, file_num)
        zero_label_num = 0
        for i in range(count + 1, file_num):
            if zero_label_num == 12:  # Control how many 0 and 1
                break
            pair_item = [value[1], file_list[i][1]]  # Get query string pair
            if value[0] == file_list[i][0]:  # Get labels
                pair_item.append(1)
            else:
                pair_item.append(0)
                zero_label_num += 1
            query_pair_list.append(pair_item)
    # print("{}".format(query_pair_list))
    # print("{}".format(len(query_pair_list)))
    with open('query_pair_list.pkl', 'wb') as f:
        pickle.dump(query_pair_list, f)
    label_dict = {0: 0, 1: 0}
    for query_pair in query_pair_list:
        label_dict[query_pair[2]] += 1
    # print(label_dict)


def main():
    read_file()
    # get_query_pair_list()
    # with open('query_pair_list.pkl', 'rb') as f:
    #     query_pair_list = pickle.load(f)
    # print(query_pair_list)
    # label_dict = {0: 0, 1: 0}
    # for query_pair in query_pair_list:
    #     label_dict[query_pair[2]] += 1
    # print(label_dict)


if __name__ == '__main__':
    main()
