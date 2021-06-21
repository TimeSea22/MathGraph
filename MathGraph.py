from File import File
import ast
from graphviz import Digraph

dot = Digraph(comment = 'MathGraph')
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
            dot.node(key[0], key)
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
        dot.edges([f + g])
        

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
        g = MathGraph()
        g.turn(name)
        dot.render(r'C:\Users\86139\PycharmProjects\MathGraph\src\图\ ' + name + '.gv', view = True)

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

    def turn(self,name):
        f = MathGraph()
        t = f.read(name)
        for n in self.dict2:
            dot.node(n[0], n)
        for m in range(len(self.connection)):
            for n in self.connection[m]:
                dot.edges([self.dict1[m][0] + self.dict1[n][0]])
        dot.render(r'C:\Users\86139\PycharmProjects\MathGraph\src\图\ ' + name + '.gv', view = True)