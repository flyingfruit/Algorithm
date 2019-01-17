if __name__ == '__main__':
    queue = [[2, 1], [1, 3], [4, 0], [5, 0], [4, 1]]
    print("第一次排序")
    print(queue)
    for i in range(0, 5):
        for j in range(0, 4 - i):
            if queue[j][0] + queue[j][1] * 10 > queue[j + 1][0] + queue[j + 1][1] * 10:
                temp = queue[j]
                queue[j] = queue[j + 1]
                queue[j + 1] = temp
    print("第二次排序")
    print(queue)
    i=0
    flat=0
    while i<5:
        temp = 0
        for j in range(0,i):
            if queue[j][0]>queue[i][0]:
                temp+=1
        if temp ==queue[i][1]:
            i+=1
        elif temp<queue[i][1]:
            print("no feasible output")
            flat =-1
            break
        else:
            temp2 = queue[j]
            queue[j] = queue[j + 1]
            queue[j + 1] = temp2
            flat=flat+1
            print("第"+str(flat)+"交换顺序:")
            print(queue)
    if flat !=-1:
        print(queue)
