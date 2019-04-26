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
        data=data[0:(len(data)-1K)]
        data = [ line.split('\t') for line in data]
        data = [Container(l) for l in data]
        return data

    def rm(self):
        ret = subprocess.run(['docker','rm',self.id],stdout=subprocess.PIPE,check=True)
        logging.info(ret)
        data = ret.stdout.decode('utf-8')


l = Container.all()
for c in l:
    logging.info(c.status)
    c.rm()
