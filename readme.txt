https://www.youtube.com/playlist?list=PLke5uKXgh5l5ibYZk_lLDPbrivLz0uBZt

python3 macc.py -i eth0 -m 00:55:22:44:55:66

choosealicense.com
https://choosealicense.com/licenses/mit/

sudo apt-get install python3-stdeb
## pip install stdeb
sudo apt install dh-python

## to fix error
sudo apt install python-all

from root folder,package:
python3 setup.py --comamnd-packages=stdeb.command bdist_deb
## deb_dist folder contains deb file

to test install:
sudo dpkg -i python3-macc_1.0.0-1_all.deb
macc -h

links:
- https://python-packaging.readthedocs.io/en/latest/dependencies.html
