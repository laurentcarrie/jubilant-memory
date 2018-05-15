#!/bin/sh

set -e
set -x

git log --format="%H" -n 1 > gitlog.tex

#set PATH=F:\\miktex\\texmfs\\install\\miktex\\bin:$PATH


pdflatex main.tex
pdflatex main.tex
pdflatex main.tex

