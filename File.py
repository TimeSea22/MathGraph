import os

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