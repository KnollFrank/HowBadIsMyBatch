#!/bin/bash
sudo -i -u frankknoll bash << EOF
PATH=/home/frankknoll/Dokumente/Corona/phantomjs-2.1.1-linux-x86_64/bin:/home/frankknoll/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/snap/bin
cd /home/frankknoll/Dokumente/Corona/projects/HowBadIsMyBatch-pages/src/intensivstationen

jupyter nbconvert --to notebook --allow-errors --execute Intensivstationen.ipynb
jupyter nbconvert --to html Intensivstationen.nbconvert.ipynb
mailx -a 'Content-Type: text/html' -s "Intensivstationen" -r Knoll_Frank@web.de Knoll_Frank@web.de < Intensivstationen.nbconvert.html

cd /home/frankknoll/Dokumente/Corona/projects/HowBadIsMyBatch-pages/src
jupyter nbconvert --to notebook --allow-errors --execute HowBadIsMyBatch.ipynb
jupyter nbconvert --to html HowBadIsMyBatch.nbconvert.ipynb
mailx -a 'Content-Type: text/html' -s "How Bad is My Batch" -r Knoll_Frank@web.de Knoll_Frank@web.de < HowBadIsMyBatch.nbconvert.html
EOF
