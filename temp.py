import pprint
from Message import Message

def main():
    messages = Message.dataparser("data.csv")
    msg_type_counts = [0,0,0,0,0,0,0,0,0]
    for message in messages:
        msg_type_counts[message.messagetype - 1] += 1
    print(msg_type_counts)

if __name__ == "__main__":
    main()