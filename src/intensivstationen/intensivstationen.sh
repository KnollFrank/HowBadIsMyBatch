#!/bin/bash
cd /home/frankknoll/Dokumente/Corona/projects/HowBadIsMyBatch-pages/src/intensivstationen
jupyter nbconvert --to notebook --allow-errors --execute Intensivstationen.ipynb
jupyter nbconvert --to html Intensivstationen.nbconvert.ipynb
mailx -a 'Content-Type: text/html' -s "Intensivstationen" -r Knoll_Frank@web.de Knoll_Frank@web.de < Intensivstationen.nbconvert.html

