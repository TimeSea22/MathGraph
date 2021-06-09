import os
import ast
import argparse
'''import pdb

pdb.set_trace()'''
parser = argparse.ArgumentParser(description = 'MathGraph')
parser.add_argument('-r', '--read', dest = 'read', type = str, help = "read the Graph")
parser.add_argument('-s', '--save', dest = 'save', type = str, help = "save the Graph")
parser.add_argument('-n', '--new', dest = 'new', type = str, help = "create new Graph")
parser.add_argument('-ade', '--addedge', dest = 'addedge', type = str, help = 'add a new edge')
parser.add_argument('-adv', '--addvertex', dest = 'addvertex', type = str, help = 'add a new vertex')
parser.add_argument('-dle', '--deleteedge', dest = 'deleteedge', type = str, help = 'delete an edge')
parser.add_argument('-dlv', '--deletevertex', dest = 'deletevertex', type = str, help = 'delete a vertex')
parser.add_argument('-sv', '--searchvertex', dest = 'searchvertex', type = str, help = 'search all the vertex on the Graph')
parser.add_argument('-se', '--searchedge', dest = 'searchedge', type = str, help = 'search all the edges on the Graph')
parser.add_argument('-sl', '--searchlatter', dest = 'searchlatter', type = str, help = 'search all the vertex the point can go to')
parser.add_argument('-sbf', '--searchbefore', dest = 'searchbefore', type = str, help = 'search all the vertex that can go to the point')
parser.add_argument('-spth', '--searchpath',  dest = 'searchpath', type = str, help = 'search the path contains the point')
args = parser.parse_args()

class File:
    def __init__(self, name):
        self.name = name

    def create(self):
        if os.path.exists(self.name) == True:
            os.remove(self.name, dir_fd=None)
            f = open(self.name, 'w')
            f.close()
        else:
            f = open(self.name, 'w')
            f.close()

    def delete(self):
        if os.path.exists(self.name) == True:
            os.remove(self.name, dir_fd=None)
        

    def edit(self, text):
        f = open(self.name, 'w')
        f.write(text)
        f.close()
            

    def rename(self, newname):
        if os.path.exists(newname) == True:
            os.remove(newname, dir_fd=None)
            f = open(newname, 'w')
            self.name = newname
            f.close()
        if os.path.exists(self.name) == True:
            os.renames(self.name, newname)
            self.name = newname
        else:
            f = open(newname, 'w')
            f.close()

    def read(self):
        if os.path.exists(self.name) == True:
            f = open(self.name, 'r')
            text = f.readlines()
            f.close()
            return text
        else:
            raise Exception('文件不存在')

class MathGraph:
    def __init__(self):
        # self.dict1 = {0:'a', 1:'b'}
        # self.dict2 = {'a':0, 'b':1}
        # self.connection = [[1],[0]]
        # self.vertexNum = 2
        self.dict1 = {}
        self.dict2 = {}
        self.connection = []
        self.vertexNum = 0

    def addVertex(self, key):
        if key in self.dict2:
            print ('vertex存在，无法添加')
        else:
            self.dict1[self.vertexNum] = key
            self.dict2[key] = self.vertexNum
            self.connection.append([])
            self.vertexNum += 1


    def addEdge(self, f, g):
        if f not in self.dict2:
            self.addVertex(f)
        if g not in self.dict2:
            self.addVertex(g)
        if self.dict2[f] in self.exists_path_to(self.dict2[g]):
            print('存在循环，无法添加')
            return
        self.connection[self.dict2[f]].append(self.dict2[g])
        

    def neighbors(self, v):  
        return set(self.connection[v])

    def exists_path_to(self, v):
        vSet = {v}
        for n in self.neighbors(v):
            vSet.update(self.exists_path_to(n))
        return vSet

    def save(self, name):
        f = File(name)
        f.edit(f'{self.dict1}\n{self.dict2}\n{self.connection}')

    def read(self, name):
        f = File(name)
        t = f.read()
        if t == []:
            self.dict1 = {}
            self.dict2 = {}
            self.connection = []
            self.vertexNum = 0
        else:
            self.dict1 = ast.literal_eval(t[0])
            self.dict2 = ast.literal_eval(t[1])
            self.connection = list(eval(t[2]))
            self.vertexNum = len(self.dict1)


'''g = MathGraph()
g.addEdge('a', 'b')
g.addEdge('c', 'd')
g.save('b.txt')
g.read('b.txt')
print(g.dict1)
print(g.dict2)
print(g.connection)
print(g.vertexNum)
print(g.exists_path_to(0))


f = MathGraph()
f.read('a.txt')'''

while True:
    action = input('请输入您的操作：')
    if action == 'read':
        fileName = input('请输入您的文件名：')
        g = MathGraph()
        print (fileName)
        g.read(fileName)
        continue

    if action == 'save':
        fileName = input('请输入您的文件名：')
        g.save(fileName)
        break

    if action == 'new':
        fileName = input('请输入您的文件名：')
        file = File(fileName)
        file.create()
        continue

    if action == 'addedge':
        string = input('请输入您的边名或者节点名：')
        g.addEdge(string[0], string[1])
        continue

    if action == 'addvertex':
        string = input('请输入您的边名或者节点名：')
        g.addVertex(string)
        continue

    if action == 'deleteedge':
        string = input('请输入您的边名或者节点名：')
        if g.dict2[string[1]] in g.connection[g.dict2[string[0]]]:
            g.connection[g.dict2[string[0]]].remove(g.dict2[string[1]])
        else:
            print('edge不存在')
        continue

   if action == 'deletevertex':
        string = input('请输入您的边名或者节点名：')
        if string in g.dict2:
            del g.connection[g.dict2[string]]
            for m in range(len(g.connection)):
                for n in g.connection[m]:
                    if g.dict2[string] in g.connection[m]:
                        g.connection[m].remove(g.dict2[string])
            g.dict1.pop(g.dict2[string])
            print(g.dict1)
            l1 = g.dict1.values()
            print(l1)
            l2 = list(range(len(g.dict1)))
            print(l2)
            g.dict1 = dict(zip(l2,l1))
            print(g.dict1)
            g.dict2 = dict(zip(l1,l2))
            print(g.dict2)
        else:
            print('vertex不存在')
        continue

    if action == 'searchvertex':
        fileName = input('请输入您的文件名：')
        f = MathGraph()
        f.read(fileName)
        print (f.dict2.keys())
        continue

    if action == 'searchedge':
        fileName = input('请输入您的文件名：')
        f = MathGraph()
        f.read(fileName)
        l = []
        for m in range(len(f.connection)):
            for n in f.connection[m]:
                l.append(f.dict1[m] + f.dict1[n])
        print(l)
        continue


    if action == 'searchlatter':
        string = input('请输入您的边名或者节点名：')
        print (g.exists_path_to(g.dict2[string]))
        continue

    if action == 'searchbefore':
        string = input('请输入您的边名或者节点名：')
        v = []
        for n in g.dict1:
            if g.dict2[string] in g.exists_path_to(n):
                v.append(g.dict1[n])
        print (v)
        continue

    if action == 'searchpath':
        string = input('请输入您的边名或者节点名：')
        v = []
        for n in g.dict1:
            if g.dict2[string] in g.exists_path_to(n):
                v.append(g.dict1[n])
        print ('后置节点：' + str(g.exists_path_to(g.dict2[string])) + '\n前置节点:' + str(v))
        continue

    else:
        print ('您的操作不存在，请重新输入')
        continue
