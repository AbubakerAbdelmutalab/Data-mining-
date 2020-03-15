class Message:
    def __init__(self, message_id, time_stamp, nid, message_type, ip, user_name):
        self.messageid = message_id
        self.timestamp = time_stamp
        self.nodeID = nid
        self.messagetype = message_type
        self.IPAddress = ip
        self.username = user_name

    def __str__(self):
        return f'messageID: {self.messageid}, timestamp: {self.timestamp}, nodeID: {self.nodeID}, messagetype: {self.messagetype}, IPAddress: {self.IPAddress}, username: {self.username}'


    def dataparser(input_file):
        input_file = open(input_file, 'r')
        lines = input_file.readlines()
        messages = []
        for line in lines[1:]:
            line = line.split(",")
            messages.append(Message(int(line[0]), line[1], line[2], int(line[3]), line[4], line[5]))
        # for message in messages:
        #     print(message)
        return messages