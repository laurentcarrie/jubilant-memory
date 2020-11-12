import subprocess
import logging
import os
import shutil

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s -- %(process)d -- %(levelname)s -- %(message)s')


# dropboxdir="c:\\Users\\laure\\Dropbox\\cv"
# dropboxdir="/Users/st5797/Dropbox/cv"
# dropboxdir="/Dropbox/cv"


def clean(d):
    files = os.listdir(d)
    to_be_deleted = [f for f in files if f.endswith(".pdf") or f.endswith(".aux")
                     or f.endswith(".out")]
    for f in to_be_deleted:
        fullpath = os.path.join(d, f)
        logging.info("remove {0}".format(fullpath))
        os.remove(fullpath)


def generate(langue,cvanon ,texdir, dropboxdir):
    version = 'xxxx'
    with open(os.path.join(texdir, 'gitlog.tex'), 'r') as fin:
        version = fin.readline().strip('\n')

    cvname = 'cv-laurent-carrie-{0}-{1}.pdf'.format(langue, version)
    if cvanon:
        cvname = 'cv-{0}-{1}.pdf'.format(langue, version)

    with open(os.path.join(texdir, 'watermark.tex'), 'w') as fout:
        if version == 'draft':
            fout.write('\\usepackage{draftwatermark}')
            fout.write('\\SetWatermarkText{draft}')
            fout.write('\\SetWatermarkScale{1}')

    shutil.copyfile(os.path.join(texdir, 'langue-{0}.tex'.format(langue)),
                    os.path.join(texdir, 'vardata.tex'))

    with open(os.path.join(texdir, 'vardata.tex'),'a') as fout :
        if cvanon:
           fout.write("\\toggletrue{cvanon}")
        else:
            fout.write("\\togglefalse{cvanon}")

    ret = subprocess.run(['pdflatex', 'main.tex'], cwd=texdir, stdout=subprocess.PIPE, check=True)
    ret = subprocess.run(['pdflatex', 'main.tex'], cwd=texdir, stdout=subprocess.PIPE, check=True)
    ret = subprocess.run(['pdflatex', 'main.tex'], cwd=texdir, stdout=subprocess.PIPE, check=True)

    shutil.copyfile(os.path.join(texdir, 'main.pdf'), cvname)
    logging.info('generated {0}'.format(cvname))

    sourcename = os.path.join(texdir, 'main.pdf')
    targetname = os.path.join(dropboxdir, cvname)
    targetname2 = os.path.join(dropboxdir,f"cv-laurent.carrie-{langue}-{version}.pdf")
    logging.info("copy {0} to dropbox : {1}".format(sourcename,targetname))
    shutil.copyfile(sourcename,targetname)
    shutil.copyfile(sourcename,targetname2)
