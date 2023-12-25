#不一定最短
maze = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
[1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
[1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
[1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
[1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
[1, 0, 1, 1, 1, 0, 1, 1, 0, 1], 
[1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

dirs = [
    lambda x,y: (x+1,y),
    lambda x,y: (x-1,y),
    lambda x,y: (x,y-1),
    lambda x,y: (x,y+1)
]

def maze_path(x1,y1,x2,y2):
    stack = []
    stack.append((x1, y1))
    while (len(stack) > 0):
        curNode = stack[-1]#当前位置
        if curNode[0] == x2 and curNode[1] == y2:#已经到终点
            for p in stack:
                print(p)
            return True
            
        # x,y 四个方向
        for di in dirs:
            nextNode = di(curNode[0], curNode[1])
            #如果能走
            if maze[nextNode[0]][nextNode[1]] == 0:
                stack.append(nextNode)
                maze[nextNode[0]][nextNode[1]] = 2#表示已走过
                break
        else:
            maze[nextNode[0]][nextNode[1]] == 2#此时该位置已走过
            stack.pop()
    else:
        print("你已无路可走了")
        return False

maze_path(1,1,8,8)   