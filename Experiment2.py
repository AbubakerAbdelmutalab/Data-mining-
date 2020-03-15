import pprint
from Message import Message


def k_grams(message_type_list, k):
    message_type_grams = []
    for item in message_type_list.items():
        message_type_stream = item[1]
        message_type_gram = set()
        for i in range(len(message_type_stream) - k + 1):
            k_gram = ""
            for j in range(i, i + k):
                k_gram = k_gram + str(message_type_stream[j])
            # print(k_gram)
            message_type_gram.update(set([k_gram]))
        message_type_grams.append(message_type_gram)
    # pprint.pprint(message_type_grams)
    return message_type_grams


def node_target(messages):
    message_type_list = {}
    for message in messages:
        if message.nodeID in message_type_list:
            message_type_list[message.nodeID].append(message.messagetype)
        else:
            message_type_list[message.nodeID] = [message.messagetype]
    # pprint.pprint(message_type_list)
    return k_grams(message_type_list, 4)


def calculate_js(set1, set2):
    if len(set1.union(set2)) == 0:
        return 0
    return float(len(set1.intersection(set2))) / float(len(set1.union(set2)))


def main():
    messages = Message.dataparser("data.csv")
    k_message_type_grams_list = node_target(messages)
    JSlist = []
    for i in range(len(k_message_type_grams_list)-1):
        for j in range(i+1, len(k_message_type_grams_list)):
            JSlist.append(calculate_js(k_message_type_grams_list[i], k_message_type_grams_list[j]))
    print(len(JSlist))
    pprint.pprint(JSlist)


if __name__ == "__main__":
    main()