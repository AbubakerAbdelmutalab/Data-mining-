import pprint
from Message import Message

def main():
    messages = Message.dataparser("data.csv")
    authentication_result = {}
    # print(len(messages))
    for message in messages:
        if message.nodeID in authentication_result:
            if message.messagetype in [1,2,3,4,5,8]:
                authentication_result[message.nodeID][1] += 1
            elif message.messagetype in [6,7,9]:
                authentication_result[message.nodeID][0] += 1
            else:
                print("Message type invalid")
        else:
            if message.messagetype in [1,2,3,4,5,8]:
                authentication_result[message.nodeID] = [0, 1]
            elif message.messagetype in [6,7,9]:
                authentication_result[message.nodeID] = [1, 0]
            else:
                print("Message type invalid")
    print(len(authentication_result))
    for item in authentication_result.items():
        if item[1][1] != 0:
            item[1].append(item[1][0]/item[1][1])
        else:
            item[1].append(0)
    sorted_d = sorted(authentication_result.items(), key=lambda x: x[1][2])
    pprint.pprint(sorted_d)

if __name__ == "__main__":
    main()