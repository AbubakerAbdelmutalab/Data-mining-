import pprint
from Message import Message
import matplotlib.pyplot as plt

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


def IPaddress_target(messages):
    message_type_list = {}
    for message in messages:
        if message.IPAddress in message_type_list:
            message_type_list[message.IPAddress].append(message.messagetype)
        else:
            message_type_list[message.IPAddress] = [message.messagetype]
    # pprint.pprint(message_type_list)
    return k_grams(message_type_list, 2)


def username_target(messages):
    message_type_list = {}
    for message in messages:
        if message.username in message_type_list:
            message_type_list[message.username].append(message.messagetype)
        else:
            message_type_list[message.username] = [message.messagetype]
    # pprint.pprint(message_type_list)
    return k_grams(message_type_list, 2)


def calculate_js(set1, set2):
    if len(set1.union(set2)) == 0:
        return 0
    return float(len(set1.intersection(set2))) / float(len(set1.union(set2)))


def main():
    messages = Message.dataparser("data.csv")
    # k_message_type_grams_list = node_target(messages)
    # k_message_type_grams_list = IPaddress_target(messages)
    k_message_type_grams_list = username_target(messages)
    print(len(k_message_type_grams_list))
    # JSlist = []
    # for i in range(len(k_message_type_grams_list)-1):
    #     for j in range(i+1, len(k_message_type_grams_list)):
    #         JSlist.append(calculate_js(k_message_type_grams_list[i], k_message_type_grams_list[j]))
    # print(len(JSlist))
    # pprint.pprint(JSlist)

    # x=[]
    # for i in range(1,len(JSlist)+1):
    #     x.append(float(i)/len(JSlist))
    # # print(x)

    # JSlist.sort()
    # # 207046
    # plt.xlabel("Jaccard Similarity")
    # plt.ylabel("Fraction of pairs of nodes")
    # plt.plot(JSlist, x)
    # plt.show()


if __name__ == "__main__":
    main()