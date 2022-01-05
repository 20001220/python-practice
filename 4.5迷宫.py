'''
4.5迷宫
'''
class Node(object):  # 节点类
    def __init__(self, x, y, w):  # 添加类变量
        self.x = x
        self.y = y
        self.w = w

    def __str__(self):  # 类方法，调用此方法时返回w的内容
        return self.w


def up(node):
    return Node(node.x - 1, node.y, node.w+"U")  # 向上的情况


def down(node):
    return Node(node.x + 1, node.y, node.w+"D") # 向下的情况


def left(node):
    return Node(node.x, node.y - 1, node.w+"L")  # 向左的情况


def right(node):
    return Node(node.x, node.y + 1, node.w+"R")  # 向右的情况


if __name__ == '__main__':
    m, n = map(int, input().split())
    visited = set()  # 存储访问过的节点
    queue = []  # 首先建一个空队列用来存储访问的节点
    map_int = [[0] * (n + 1)]  # 第一行全置0
    for i in range(1, m+1):
        map_int.append([0]*(n+1))
        nums = input()  # 输入数据
        nums = "0" + nums  # 第一列全置0
        for j in range(0, n+1):
            map_int[i][j] = ord(nums[j]) - 48  # 把字符‘1’、‘0’转为数字
    # print(map_int)
    # exit()
    node = Node(1, 1, "")  # 开始位置节点
    queue.append(node)  # 放入队列
    while len(queue) != 0:  # 队不空时循环
        moveNode = queue[0]  # 移动节点
        queue.pop(0)  # 移动节点出队列
        moveStr = str(moveNode.x) + " "+ str(moveNode.y)  # 移动节点位置
        if moveStr not in visited:  # 移动节点若未访问
            visited.add(moveStr)  # 放入已访问节点列表
            if moveNode.x == m and moveNode.y == n:  # 到达最后位置时停止循环
                print(len(moveNode.__str__()))  # 输出步数，即长度
                print(moveNode)  # 输出路径
                break
            if moveNode.x < m:
                if map_int[moveNode.x + 1][moveNode.y] == 0:  # 向下的情况
                    queue.append(down(moveNode))
            if moveNode.y > 1:
                if map_int[moveNode.x][moveNode.y - 1] == 0:  # 向左的情况
                    queue.append(left(moveNode))
            if moveNode.y < n:
                if map_int[moveNode.x][moveNode.y + 1] == 0:  # 向右的情况
                    queue.append(right(moveNode))
            if moveNode.x > 1:
                if map_int[moveNode.x - 1][moveNode.y] == 0:  # 向上的情况
                    queue.append(up(moveNode))

