import re #regular eexpressions

from collections import defaultdict
url = 'logs/10krandauth_test.txt'
with open(url, 'r') as f:
    connections = [line for line in f if 'node4'  in line][1:] #why!!

connections_by_node_and_sshd = defaultdict(list)
pattern = '\s\d+\:\d+\:\d+\s(\w+).*sshd\[(\d+)'
for c in connections:
    matches = re.findall(pattern, c)#re!!
    if len(matches) > 0:
        match_key = '*'.join(matches[0])#
        connections_by_node_and_sshd[match_key] += [c]
with open("example8.txt", 'w') as f:
	f.write(''.join([''.join(c) for c in connections_by_node_and_sshd.values()]))


