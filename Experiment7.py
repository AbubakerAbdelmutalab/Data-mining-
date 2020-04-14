import pprint
import matplotlib.pyplot as plt
import numpy as np
import copy
from Message import Message
import csv
import matplotlib.patches as mpatches

# Counts number of accesses to a node from each IPAddress accessing that node
def count_usage(messages):
    node_access_set = {}
    for message in messages:
        if message.nodeID in node_access_set:
            if message.IPAddress in node_access_set[message.nodeID]:
                node_access_set[message.nodeID][message.IPAddress] += 1
            else:
                node_access_set[message.nodeID][message.IPAddress] = 1
        else:
            node_access_set[message.nodeID] = {}
            node_access_set[message.nodeID][message.IPAddress] = 1
    return node_access_set

def LloydCluster(vertices,target_cluster_num,initial_centers):
    centers = copy.deepcopy(initial_centers)
    center2vertex_idx = {i:[] for i in range(target_cluster_num)}
    while True:
        last_centers = copy.deepcopy(centers)
        center2vertex_idx = {i:[] for i in range(target_cluster_num)}
        for i in range(np.shape(vertices)[0]):
            shortest_distance_idx = minDistanceToCenters(vertices[i],centers)['idx']
            center2vertex_idx[shortest_distance_idx].append(i)
        for i in range(target_cluster_num):
            centers[i] = np.mean(vertices[center2vertex_idx[i],:],axis=0)
        if matrixesEqual(centers,last_centers):
            break
    return centers

def matrixesEqual(matrix1,matrix2):
    if np.shape(matrix1) != np.shape(matrix2):
        return False
    for r in range(np.shape(matrix1)[0]):
        if not np.array_equal(matrix1[r], matrix2[r]):
            return False
    return True

def minDistanceToCenters(vertex,centers):
    vertex = np.reshape(vertex,(1,-1))
    distances = np.linalg.norm(centers - np.tile(vertex,(np.shape(centers)[0],1)),ord=2,axis=1)
    shortest_distance_idx = None
    for i in range(np.shape(distances)[0]):
        if (shortest_distance_idx == None or distances[i] < distances[shortest_distance_idx]):
            shortest_distance_idx = i
    return {'center':centers[shortest_distance_idx],'distance':distances[shortest_distance_idx],'idx':shortest_distance_idx}


def verticesCluster(vertices,centers):
    vertex2center = {}
    for i in range(np.shape(vertices)[0]):
        vertex2center[i] = minDistanceToCenters(vertices[i],centers)['center']
    return vertex2center


def GonzalezCluster(vertices,target_cluster_num,center1):
    centers = np.reshape(center1,(1,-1))
    for i in range(1,target_cluster_num):
        furthest = {'vertex':None,'distance':None}
        for vertex in vertices:
            cloest = minDistanceToCenters(vertex,centers)
            if(furthest['distance'] ==None or cloest['distance'] > furthest['distance'] ):
                furthest = {'vertex':vertex,'distance':cloest['distance']}
        centers = np.concatenate((centers,np.reshape(furthest['vertex'],(1,-1))),axis=0)
    return centers


def main():
    # Load the data from CSV file
    messages = Message.dataparser("data.csv")

    # Count number of accesses to a node from each IPAddress accessing that node
    node_access_set = count_usage(messages)
    # pprint.pprint(node_access_set)

    # print(len(node_access_set))
    # for nodeid in node_access_set.keys():
    #     print(nodeid + "   " + str(len(node_access_set[nodeid])))

    # Calculate the x and y co-ordinates for clustering.
    x = []
    y = []
    counter = 1
    plot_list = []
    for nodeid in node_access_set.keys():
        sum = 0
        for IPAddress in node_access_set[nodeid].keys():
            sum += node_access_set[nodeid][IPAddress]
        plot_list.append([nodeid, len(node_access_set[nodeid]), sum])
        x.append(counter)
        # x.append(len(node_access_set[nodeid]))
        y.append(sum)
        counter += 1
        if sum > 40000:
            print(nodeid + "\t" + str(sum))

    # for nodeid in node_access_set.keys():
    #     print(nodeid + "   " + str(len(node_access_set[nodeid])))
    # print(plot_list)
    # print(len(plot_list))
    # plt.scatter(x, y, s=2)
    # plt.show()


    # vertices_list = []
    # for m, n in zip(x, y):
    #     vertices_list.append([float(m), float(n)])
    # vertices = np.array(vertices_list)
    # print(vertices.shape)
    # centers = np.array([[0,0],[1000,0],[0,1000]])
    # centers_gonzalez = LloydCluster(vertices, 3, centers)
    # # centers_gonzalez = GonzalezCluster(vertices, 3, vertices[0])
    # vertex2center = verticesCluster(vertices, centers_gonzalez)
    # with open('gonzalez.csv', 'w') as f:
    #     for i in range(np.shape(vertices)[0]):
    #         f.write(','.join([str(elem) for elem in np.ndarray.tolist(vertices[i])]) + ',' +
    #                 str(vertex2center[i]) + '\n')

    file = "gonzalez.csv"
    x = []
    y = []
    z = []
    color = set()
    colours = ["red", "green", "blue", "black"]
    with open(file, "r") as csvfile:
        reader = csv.reader(csvfile)
        # print(reader)
        for row in reader:
            x.append(float(row[0]))
            y.append(float(row[1]))
            z.append(int(row[2]))
    for num in z:
        color.add(num)
    color = list(color)
    coldict = dict()
    for col,num in zip(colours,color):
        coldict[num] = col
    # print(coldict)

    # print(x)
    # print(y)
    # print(z)
    # z = map(lambda x: coldict[x], z)
    # print(list(z))
    plt.scatter(x, y, c=z, cmap="Accent", s=6)
    grey_patch = mpatches.Patch(color='grey', label='High risk nodes')
    green_patch = mpatches.Patch(color='green', label='Moderate risk nodes')
    black_patch = mpatches.Patch(color='black', label='Low risk nodes')
    plt.legend(handles=[grey_patch, green_patch, black_patch])
    plt.xlabel('#IPaddress')
    plt.ylabel('#Access')
    plt.title('Plot of #accesses vs #IPaddresses')
    # m = ['ms1102', 'hp005', 'hp054', 'hp053', 'hp017']
    # j = 0
    # for i in range(len(y)):
    #     if y[i] > 40000:
    #         plt.annotate(m[j], (x[i], y[i]))
    #         j += 1
    #     if j > 4:
    #         break
    plt.show()

    # centers = LloydCluster(vertices, 3, centers_gonzalez)

# ms1102	62117
# hp017	71710
# hp005	64268
# hp053	68192
# hp054	71677

if __name__ == "__main__":
    main()
