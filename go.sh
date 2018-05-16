#!/bin/sh

#set -e
#set -x



#set PATH=F:\\miktex\\texmfs\\install\\miktex\\bin:$PATH

#set count=`git log --format="%H"`
count=`git status --porcelain | wc --lines | tr --delete '\r' | tr --delete '\n' | tr --delete ' '` 

case $count in
1)
version=`git log --format="%H" -n 1 | tr --delete '\r' | tr --delete '\n' | tr --delete ' '` 
git log --format="%H" -n 1 > gitlog.tex

pdflatex main.tex
pdflatex main.tex
pdflatex main.tex
rm -rf *.pdf
cp main.pdf cv-laurent-carrie-$version.pdf
;;
*)
echo $count files not checked in
git status --porcelain 
exit 1
;;
esac


