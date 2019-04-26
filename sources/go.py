import subprocess
import logging
import os
import shutil

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s -- %(levelname)s -- %(message)s')

dropboxdir="c:\\Users\\laure\\Dropbox\\cv"
#dropboxdir="/Users/st5797/Dropbox/cv"


def is_git_committed() -> bool :
    ret = subprocess.run(['git','status','--porcelain'],stdout=subprocess.PIPE,check=True)
    ret = ret.stdout.decode('utf-8')
    ret = ret.split('\n')
    is_committed = (len(ret) == 1)
    logging.info("is committed : {0}, files : {1}".format(is_committed,ret))
    return is_committed

def git_version() -> str :
    ret = subprocess.run(['git', 'log', '--format=%H'], stdout=subprocess.PIPE, check=True)
    ret = ret.stdout.decode('utf-8')
    ret = ret.split('\n')[0]
    logging.info("version : '{0}'".format(ret))
    return ret

is_git_committed = is_git_committed()
git_version = git_version()

def clean(d):
    files = os.listdir(d)
    to_be_deleted = [ f for f in files if f.endswith(".pdf") or f.endswith(".aux")
                      or f.endswith(".out")]
    for f in to_be_deleted:
        fullpath = os.path.join(d,f)
        logging.info("remove {0}".format(fullpath))
        os.remove(fullpath)

def generate(langue,version) :
    if not is_git_committed:
        version = 'draft'

    cvname = 'cv-laurent-carrie-{0}-{1}.pdf'.format(langue, version)

    with open('gitlog.tex','w') as fout:
        fout.write(version)
        fout.write('\n')

    with open('watermark.tex', 'w') as fout:
        if not is_git_committed:
            fout.write('\\usepackage{draftwatermark}')
            fout.write('\\SetWatermarkText{draft}')
            fout.write('\\SetWatermarkScale{1}')

    shutil.copyfile('langue-{0}.tex'.format(langue),'langue.tex')

    ret = subprocess.run(['pdflatex', 'main.tex'], stderr=subprocess.PIPE, check=True)
    ret = subprocess.run(['pdflatex', 'main.tex'], stdout=subprocess.PIPE, check=True)
    ret = subprocess.run(['pdflatex', 'main.tex'], stdout=subprocess.PIPE, check=True)

    shutil.copyfile('main.pdf',cvname)
    logging.info('generated {0}'.format(cvname))
    if is_git_committed:
       shutil.copyfile('main.pdf',os.path.join(dropboxdir,cvname))



clean(".")
clean(dropboxdir)

generate('english',git_version)
generate('francais',git_version)


