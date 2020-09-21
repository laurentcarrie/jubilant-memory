import logging
import os

from prepare import prepare
from build_cv import clean,generate
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s -- %(process)d -- %(levelname)s -- %(message)s')

if __name__ == '__main__':
    texdir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'latex')
    logging.info("texdir : {0}".format(texdir))
    prepare(texdir)

    clean(".")
    dropboxdir='/home/laurent/Dropbox/cv'
    clean(dropboxdir)
    options = [ (langue,cvanon) for langue in ['english','francais'] for cvanon in [True,False]]
    for (l,cvanon) in options :
     generate(l,cvanon,texdir,dropboxdir)
