import logging
import os

from py.prepare import prepare
from py.build_cv import clean,generate
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s -- %(process)d -- %(levelname)s -- %(message)s')

if __name__ == '__main__':
    texdir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'latex')
    logging.info("texdir : {0}".format(texdir))
    prepare(texdir)

    clean(".")
    dropboxdir='/Dropbox/cv'
    clean(dropboxdir)
    generate('english',texdir,dropboxdir)
    generate('francais',texdir,dropboxdir)
