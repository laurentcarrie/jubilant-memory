import subprocess
import logging
import os
import shutil

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s')

dropboxdir="/cygdrive/c/users/laurent/dropbox/cv"
dropboxdir="/Users/st5797/Dropbox/cv"


def is_git_modified() -> bool :
    ret = subprocess.run(['git','status','--porcelain'],stdout=subprocess.PIPE,check=True)
    ret = ret.stdout.decode('utf-8')
    ret = ret.split('\n')
    logging.info(ret)
    return len(ret) != 0

def git_version() -> str :
    ret = subprocess.run(['git', 'log', '--format=%H'], stdout=subprocess.PIPE, check=True)
    ret = ret.stdout.decode('utf-8')
    ret = ret.split('\n')[0]
    logging.info("version : '{0}'".format(ret))
    return ret

is_git_modified = is_git_modified()
git_version = git_version()

def clean(d):
    files = os.listdir(d)
    pdfs = [ f for f in files if f.endswith(".pdf")]
    for f in pdfs:
        fullpath = os.path.join(d,f)
        logging.info("remove {0}".format(fullpath))
        os.remove(fullpath)

def generate(langue,version) :
    if is_git_modified:
        version = 'draft'

    cvname = 'cv-laurent-carrie-{0}-{1}.pdf'.format(langue, version)

    with open('gitlog.tex','w') as fout:
        fout.write(version)
        fout.write('\n')

    with open('watermark.tex','w') as fout:
        fout.write('\\usepackage{draftwatermark}')
        fout.write('\\SetWatermarkText{draft}')
        fout.write('\\SetWatermarkScale{1}')

    shutil.copyfile('langue-{0}.tex'.format(langue),'langue.tex')

    ret = subprocess.run(['pdflatex', 'main.tex'], stdout=subprocess.PIPE, check=True)
    ret = subprocess.run(['pdflatex', 'main.tex'], stdout=subprocess.PIPE, check=True)
    ret = subprocess.run(['pdflatex', 'main.tex'], stdout=subprocess.PIPE, check=True)

    shutil.copyfile('main.pdf',cvname)
    logging.info('generated {0}'.format(cvname))
    shutil.copyfile('main.pdf',os.path.join(dropboxdir,cvname))



clean(".")
clean(dropboxdir)

generate('english',git_version)
generate('francais',git_version)


