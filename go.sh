#!/bin/sh

set -e
#set -x


dropboxdir=c:/users/laurent/dropbox/cv

#set PATH=F:\\miktex\\texmfs\\install\\miktex\\bin:$PATH

#set count=`git log --format="%H"`
count=`git status --porcelain | wc --lines | tr --delete '\r' | tr --delete '\n' | tr --delete ' '` 

case $count in
0)
version=`git log --format="%H" -n 1 | tr --delete '\r' | tr --delete '\n' | tr --delete ' '` 
git log --format="%H" -n 1 > gitlog.tex
cvname=cv-laurent-carrie-$version.pdf

rm -rf *.pdf
pdflatex main.tex
pdflatex main.tex
pdflatex main.tex
cp main.pdf $cvname
rm -f $dropboxdir/cv*.pdf
cp $cvname $dropboxdir/$cvname
;;
*)
echo $count files not checked in
git status --porcelain 
exit 1
;;
esac


