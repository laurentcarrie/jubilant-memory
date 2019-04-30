import subprocess
import logging
import os

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s -- %(process)d -- %(levelname)s -- %(filename)s:%(lineno)d => %(message)s')

dockerfile_path = os.path.abspath(__file__)
dockerfile_path = os.path.dirname(os.path.dirname(dockerfile_path))
logging.info("dockerfile_path : '{0}'".format(dockerfile_path))

def is_git_committed() -> bool:
    ret = subprocess.run(['git', 'status', '--porcelain'], stdout=subprocess.PIPE, check=True)
    ret = ret.stdout.decode('utf-8')
    ret = ret.split('\n')
    is_committed = (len(ret) == 1)
    logging.info("is committed : {0}, files : {1}".format(is_committed, ret))
    return is_committed


def git_version() -> str:
    ret = subprocess.run(['git', 'log', '--format=%H'], stdout=subprocess.PIPE, check=True)
    ret = ret.stdout.decode('utf-8')
    ret = ret.split('\n')[0]
    logging.info("version : '{0}'".format(ret))
    return ret


def clean(d):
    files = os.listdir(d)
    to_be_deleted = [f for f in files if f.endswith(".pdf") or f.endswith(".aux")
                     or f.endswith(".out")]
    for f in to_be_deleted:
        fullpath = os.path.join(d, f)
        logging.info("remove {0}".format(fullpath))
        os.remove(fullpath)


def prepare(texdir):
    logging.info("prepare")
    version = git_version()
    if not is_git_committed():
        logging.info("is not committed")
        version = 'draft'
    filename = os.path.join(texdir,'gitlog.tex')
    with open(filename, 'w') as fout:
        logging.info("write {0}".format(filename))
        fout.write(version)
        fout.write('\n')


def run_docker():
    logging.info("build docker image")
    ret = subprocess.run(['docker', 'build',
                          '-t', 'lolocv', dockerfile_path],
                         stderr=subprocess.PIPE,
                         #                     stdout=subprocess.PIPE,
                         check=True)

    ret = ret.stderr.decode('utf-8')
    ret = ret.split('\n')
    logging.info("run container done")
    print(ret)

    ret = subprocess.run(['docker', 'run',
                          '-v', 'c:\\Users\\laure\\work\\jubilant-memory:/usr/src/work',
                          '-v', 'c:\\Users\\laure\\Dropbox:/Dropbox',
                          'lolocv:latest'],
                         stderr=subprocess.PIPE,
                         #                     stdout=subprocess.PIPE,
                         check=True)

    ret = ret.stderr.decode('utf-8')
    ret = ret.split('\n')
    logging.info("run container done")
    print(ret)


if __name__ == "__main__":
    texdir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'latex')
    prepare(texdir)


