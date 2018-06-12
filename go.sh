#!/bin/sh

set -e
#set -x


#dropboxdir=c:/users/laurent/dropbox/cv
dropboxdir=/cygdrive/c/users/laurent/dropbox/cv

#set PATH=F:\\miktex\\texmfs\\install\\miktex\\bin:$PATH

#set count=`git log --format="%H"`
count=`git status --porcelain | wc --lines | tr --delete '\r' | tr --delete '\n' | tr --delete ' '`

function generate {
    langue=$1
    version=$2
    cvname=cv-laurent-carrie-$langue-$version.pdf
    pdflatex main.tex
    pdflatex main.tex
    pdflatex main.tex
    cp main.pdf $cvname
    cp $cvname $dropboxdir/$cvname
    }

case $count in
*)
version=`git log --format="%H" -n 1 | tr --delete '\r' | tr --delete '\n' | tr --delete ' '` 
git log --format="%H" -n 1 > gitlog.tex
rm -rf *.pdf
rm -f $dropboxdir/cv*.pdf
cp langue-english.tex langue.tex
generate english $version
cp langue-francais.tex langue.tex
generate francais $version
;;
*)
echo $count files not checked in
git status --porcelain 
exit 1
;;
esac


