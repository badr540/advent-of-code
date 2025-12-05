import os
import time
from PIL import Image
import numpy as np

def find_networks(connections):
    networks = {}
    for con in connections:
        computers = con.split('-')
        if computers[0] not in networks.keys():
            networks[computers[0]] = [computers[1]]
        else:
            networks[computers[0]].append(computers[1])
        
        if computers[1] not in networks.keys():
            networks[computers[1]] = [computers[0]]
        else:
            networks[computers[1]].append(computers[0])
    

    networks_of_3 = []
    computers_scores = {}
    
    for con1 in networks.keys():
        for con2 in networks[con1]:
            for con3 in networks[con2]:
                if con1 in networks[con3]:
                    l = [con1,con2,con3]
                    l.sort()
                    if l not in networks_of_3:
                        networks_of_3.append(l)
                        for c in l:
                            if c not in computers_scores.keys():
                                computers_scores[c] = 1
                            else:
                                computers_scores[c] += 1

    return networks_of_3

def find_biggest_network(connections):
    cons_dict = {}
    networks = []
    for con in connections:
        computers = con.split('-')
        networks.append(computers)
        
        if computers[0] not in cons_dict.keys():
            cons_dict[computers[0]] = [computers[1]]
        else:
            cons_dict[computers[0]].append(computers[1])
        
        if computers[1] not in cons_dict.keys():
            cons_dict[computers[1]] = [computers[0]]
        else:
            cons_dict[computers[1]].append(computers[0])

    for con in cons_dict.keys():
        for net in networks:
            is_part_of_network = True
            for c in net:
                if c not in cons_dict[con]:
                    is_part_of_network = False
                    break
            
            if is_part_of_network:
                net.append(con)
    
    biggest_network = max(networks, key=len)
    return biggest_network
        

connections = []
filename = "{}/input.txt".format(os.path.abspath(__file__)[0:-8])
with open(filename, 'r') as file:
    for line in file:
        connections.append(line.strip('\n'))
        

total = 0
start = time.time()
networks = find_biggest_network(connections)
networks.sort()
#networks = list(filter(lambda x: any('t' in y[0] for y in x), networks))
print(",".join(networks))
#print(len(networks))

end = time.time()
