import re

class Message:
    def __init__(self, message_id, time_stamp, nid, message_type, ip, user_name):
        self.messageid = message_id
        self.timestamp = time_stamp
        self.nodeID = nid
        self.messagetype = message_type
        self.IPAddress = ip
        self.username = user_name

Messages = []
count = 0
input_file = open('TheText.txt', 'r') 
output_file = open("data.csv", 'w')
output_file.write("Messageid,Timestamp,NodeID,MessageType,IPaddress,Username\n")
lines = input_file.readlines()
for line in lines[1:]:
    newMessage = Message
    count = count + 1
    line = line.split("\t")
    line = line[1]
    timestamp = re.findall(r"\d{2}:\d{2}:\d{2}",line)[0]
    length = len(timestamp) + 1 + line.find(timestamp)
    # print(line.find(timestamp))
    nodeid = line[length:]
    nodeid = nodeid.split(" ")[0]
    ipadd = "NULL"
    username = "NULL"
    line = line.replace(timestamp,'')
    line = line[line.find(":")+2:]
    # print(line)
    if len(re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)) != 0:
        ipadd = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)[0]
    # print(ipadd)
    if(re.match(r"Disconnected from \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} port \d{3,} \[preauth\]",line)):
        message_type = 1
    elif(re.match(r"Disconnected from authenticating user [^\s]+ \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} port \d{3,} \[preauth\]",line)):
        u = line.split(" ")
        username = u[u.index("user")+1]
        message_type = 2
    elif(re.match(r"Received disconnect from \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} port \d{3,}:\d{1,}: Bye Bye \[preauth\]",line)):
        message_type = 3
    elif(re.match(r"Received disconnect from \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} port \d{3,}:\d{1,}: Normal Shutdown, Thank you for playing \[preauth\]",line)):
        message_type = 4
    elif(re.match(r"Received disconnect from \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} port \d{3,}:\d{1,}: disconnected by user",line)):
        message_type = 5
    elif(re.match(r"Invalid user [^\s]+ from \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}( port \d{3,})?",line)):
        u = line.split(" ")
        username = u[u.index("user")+1]
        message_type = 6
    elif(re.match(r"input_userauth_request: invalid user [^\s]+ \[preauth\]",line)):
        u = line.split(" ")
        username = u[u.index("user")+1]
        message_type = 7
    elif(re.match(r"Accepted publickey for root from \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",line)):
        message_type = 8
    elif(re.match(r"Disconnecting: Too many authentication failures \[preauth\]",line)):
        message_type = 9
    # print("messageid: ", count, "timestamp: ", timestamp, "NodeId: ", nodeid, "message_type: ", message_type, "IPaddresss: ", ipadd, "Username: ", username)
    output_file.write(str(count) + ',' + timestamp + ',' + nodeid + ',' + str(message_type) + ',' + ipadd + ',' + username + '\n')
    newMessage = Message(count, timestamp, nodeid, message_type, ipadd, username)
    Messages.append(newMessage)
input_file.close()
output_file.close()










#datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')