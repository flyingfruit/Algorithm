import math

if __name__ == '__main__':
    network = [[0, 0.741, 0.995], [0.741, 0, 1.366], [0.995, 1.366, 0]]
    for i in range(0,3):
        for j in range(0,3):
            item = network[i][j]
            if item == 0:
                item = 10000
            else:
                item = math.log(1/item, math.e)
            network[i][j] = item
    for k in range(0,3):
        for i in range(0,3):
            for j in range(0,3):
                if i==j:
                    continue
                if network[i][j]>network[i][k]+network[k][j]:
                    network[i][j]=network[i][k]+network[k][j]
    flag=0
    for row in network:
        for item in row:
            if item<0:
                print("exist")
                flag=1
                break
        if flag == 1:
            break
    if flag == 0:
        print("not exist")
