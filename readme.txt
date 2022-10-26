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


fpm part:
-------
fpm -d nano -d vim -s gem -t deb bundler




git','tmux','screen','vim','emacs','htop','valgrind','build-essential','net-tools'



install_requires=['TensorFlow', 'Keras', 'PyTorch', 'Caffe', 'Caffe 2']




sudo apt install nvidia-cuda-toolkit
sudo apt install caffe-cpu



pytorch giving error:
   Running setup.py install for PyTorch ... error
    ERROR: Command errored out with exit status 1:
     command: /usr/bin/python3 -u -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/tmp/pip-install-9_t8c95i/PyTorch/setup.py'"'"'; __file__='"'"'/tmp/pip-install-9_t8c95i/PyTorch/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' install --record /tmp/pip-record-qn618bdn/install-record.txt --single-version-externally-managed --user --prefix= --compile --install-headers /home/azureuser/.local/include/python3.8/PyTorch
         cwd: /tmp/pip-install-9_t8c95i/PyTorch/
    Complete output (5 lines):
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
      File "/tmp/pip-install-9_t8c95i/PyTorch/setup.py", line 11, in <module>
        raise Exception(message)
    Exception: You tried to install "pytorch". The package named for PyTorch is "torch"


pip3 install TensorFlow Keras torch

 pip3 install conda


fpm -d nano -d vim -d tmux -d screen -d emacs -d htop -d valgrind -d build-essential -d git -d nvidia-cuda-toolkit -d caffe-cpu -s deb -t deb ./deb_dist/python3-macc_1.0.0-1_all.deb

fpm -s dir -t deb -n test -d python3 -d python3-pip -d vim -d tmux -d screen -d emacs -d htop -d valgrind -d build-essential -d git -d nvidia-cuda-toolkit -d caffe-cpu --after-install ./tmp/post-install.sh -C /home/osboxes/Desktop/python_deb_create tmp
Created package {:path=>"test_1.0_amd64.deb"}

https://linuxconfig.org/how-to-install-cuda-on-ubuntu-20-04-focal-fossa-linux



https://caffe2.ai/docs/getting-started.html?platform=ubuntu&configuration=prebuilt
https://caffe.berkeleyvision.org/install_apt.html
https://github.com/astraw/stdeb/issues/153

fpm:
https://www.digitalocean.com/community/tutorials/how-to-use-fpm-to-easily-create-packages-in-multiple-formats
https://fpm.readthedocs.io/en/v1.14.0/cli-reference.html
https://stackoverflow.com/questions/30802265/deb-package-creation-using-fpm-with-build-dependencies
