# breadth_first search 广度优先搜索
from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def person_is_seller(name):
    if name[-1] == 'm':
        return True
    else:
        return False


def search(name):
    search_queue = deque()  # 创建一个搜索队列
    search_queue += graph[name]  # 把我的邻居加入队列
    seearched = []  # 创建一个已搜索过的队列
    while search_queue:
        person = search_queue.popleft()  # 取出第一个人
        if person not in seearched:
            if person_is_seller(person):
                print(person+" is seller")
                break
            else:
                print(person+" is not seller")
                search_queue += graph[person]
                seearched.append(person)
    return False


search("you")
