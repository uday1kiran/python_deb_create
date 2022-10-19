from setuptools import setup

with open("README.md","r",encoding="utf-8") as readme_file:
  long_description=readme_file.read()

setup(
  name="macc",
  version="1.0.0",
  description="Change MAC addresss, DEB package",
  long_description=long_description,
  long_description_content_type="text/markdown",
  author="Uday",
  author_email="uday@kiran.com",
  license="MIT",
  packages=['macc'],
  package_dir={'macc':'macc/'},
  install_requires=['git','tmux','screen','vim','emacs','htop','valgrind','build-essential','network-tools'],
  classifiers=[
     "Pragramming language :: Python :: 3",
     "License :: OSI Approved :: MIT License",
     "Environment :: Console",
     "Operating System :: POSIX :: Linux"
   ],
  entry_points={
     'console_scripts':['macc=macc.macc:main']
   },
  data_files=[
   ('share/applications/',['macc.desktop'])
  ],
  keywords="mac address changer",
  python_requires=">=3.6"
)
