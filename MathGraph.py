import os
import unittest

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

class TestFile(unittest.TestCase):

    def test_create1(self):
        f = File('123.txt')
        f.create()
        self.assertTrue(os.path.exists('123.txt'))
     
    
    def test_create2(self):
        f = File('123.txt')
        f.create()
        f.create()
        self.assertTrue(os.path.exists('123.txt'))
        
    
    def test_delete1(self):
        f = File('123.txt')
        f.create()
        f.delete()
        self.assertFalse(os.path.exists('123.txt'))
        
    def test_delete2(self):
        f = File('123.txt')
        f.delete()
        self.assertFalse(os.path.exists('123.txt'))
        
    def test_edit1(self):
        f = File('123.txt')
        f.edit('123')
        r = f.read()
        self.assertEqual(['123'], r)
    
    def test_rename1(self):
        f = File('123.txt')
        f.create()
        f.rename('456.txt')
        self.assertTrue(os.path.exists('456.txt'))
      
    def test_rename2(self):
        f = File('abc.txt')
        f.create()
        f.rename('abc.txt')
        self.assertTrue(os.path.exists('abc.txt'))
      
    def test_rename3(self):
        f = File('789.txt')
        f.rename('789.txt')
        self.assertTrue(os.path.exists('789.txt'))
    
    def test_read1(self):
        f = File('789.txt')
        f.edit('qwerty\nuiopas\ndfggh\nzkdjfhgr')
        t = f.read()
        self.assertEqual(t,['qwerty\n','uiopas\n','dfggh\n','zkdjfhgr'])
        
    def test_read2(self):
        f = File('sdf.txt')
        self.assertRaisesRegex(Exception, '文件不存在', f.read)
      
if __name__ == '__main__':
    unittest.main()
