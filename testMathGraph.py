from MathGraph import File
from MathGraph import MathGraph
import unittest
import os

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

class testMathGraph(unittest.TestCase):

    def test_addVertex(self):
        g = MathGraph()
        g.addVertex('a')
        self.assertEqual(g.dict1, {0: 'a'})
        self.assertEqual(g.dict2, {'a': 0})
        self.assertEqual(g.connection, [[]])
        self.assertEqual(g.vertexNum, 1)

    def test_addEdge1(self):
        h = MathGraph()
        h.addEdge('a', 'b')
        self.assertEqual(h.dict1, {0: 'a', 1: 'b'})
        self.assertEqual(h.dict2, {'a': 0, 'b':1})
        self.assertEqual(h.connection, [[1], []])
        self.assertEqual(h.vertexNum, 2)

    def test_addEdge2(self):
        s = MathGraph()
        s.addEdge('a', 'b')
        s.addEdge('b', 'a')
        self.assertEqual(s.dict1, {0: 'a', 1: 'b'})
        self.assertEqual(s.dict2, {'a': 0, 'b':1})
        self.assertEqual(s.connection, [[1], []])
        self.assertEqual(s.vertexNum, 2)

    def test_neighbors(self):
        h = MathGraph()
        h.addEdge('a', 'b')
        self.assertEqual(h.neighbors(0), {1})

    def test_exist_path_to(self):
        a = MathGraph()
        a.addEdge('a', 'b')
        a.addEdge('c', 'd')
        a.addEdge('d', 'b')
        a.addEdge('d', 'e')
        self.assertTrue(4 in a.exists_path_to(2))
        self.assertFalse(0 in a.exists_path_to(1))
      
if __name__ == '__main__':
    unittest.main()