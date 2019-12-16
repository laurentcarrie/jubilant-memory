import subprocess
import logging
import os
import shutil

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s -- %(levelname)s -- %(filename)s:%(lineno)d  -- %(message)s')



class Container:
    def __init__(self,data):
        assert(type(data) is list)
        assert(len(data) == 4)
        logging.info(data)
        self.id = data[0]
        self.name = data[1]
        self.image = data[2]
        self.status = data[3]

    @staticmethod
    def all()  :
        ret = subprocess.run(['docker','ps','-a','--format',""'{{.ID}}\t{{.Names}}\t{{.Image}}\t{{.Status}}'""],stdout=subprocess.PIPE,check=True)
        data = ret.stdout.decode('utf-8')
        data = data.split('\n')
        data=data[0:(len(data)-1)]
        data = [ line.split('\t') for line in data]
        data = [Container(l) for l in data]
        return data

    def rm(self):
        ret = subprocess.run(['docker','rm',self.id],stdout=subprocess.PIPE,check=True)
        logging.info(ret)
        data = ret.stdout.decode('utf-8')

class Image:
    def __init__(self,data):
        assert(type(data) is list)
        assert(len(data) == 3)
        logging.info(data)
        self.id = data[0]
        self.repository = data[1]
        self.tag = data[2]

    @staticmethod
    def all()  :
        ret = subprocess.run(['docker','images','-a','--format',""'{{.ID}}\t{{.Repository}}\t{{.Tag}}'""],stdout=subprocess.PIPE,check=True)
        data = ret.stdout.decode('utf-8')
        data = data.split('\n')
        data=data[0:(len(data)-1)]
        data = [ line.split('\t') for line in data]
        logging.info(data)
        data = [Image(l) for l in data]
        return data

    def rm(self):
        ret = subprocess.run(['docker','image','rm','-f',self.id],stdout=subprocess.PIPE,check=True)
        logging.info(ret)
        data = ret.stdout.decode('utf-8')

def rm_all():
    l = Container.all()
    for i in l :
        i.rm()

    l = Image.all()
    for i in l:
        i.rm()

rm_all()