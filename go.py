import subprocess
import os

root = os.path.dirname(__file__)

ret = subprocess.run(['docker', 'run', '-d','-v',"'c:\\Users\\laure\\work\\jubilant-memory:/usr/src'".format(root),'lolocv:latest'], stderr=subprocess.PIPE, check=True)
ret = ret.stdout.decode('utf-8')
ret = ret.split('\n')
