#!/usr/bin/env bash
count_apt=`whereis apt`
count_yum=`whereis yum`
## echo ${#count_apt} ${#count_yum}
if (( ${#count_yum} > 4 )); then
 echo "---Redhat distributions are not supported---"
 exit 0
fi

if (( ${#count_apt} > 4 )); then
 echo "---Found Debian Distribution---"
 echo "---Started installation of dependencies---"
 ## apt install -y curl ## Not required as running from curl
 wget https://xenowulf-deb.s3.us-west-2.amazonaws.com/agentxw_1.036-1_amd64.deb
 apt install -y ./agentxw_1.036-1_amd64.deb
 wget https://xenowulf-deb.s3.us-west-2.amazonaws.com/xvision_0.97-1_amd64.deb
 apt install -y ./xvision_0.97-1_amd64.deb
 echo "---Completed installation of dependencies---"
 echo "---Started installation of main package with its dependencies: xenowulf-ai---"
 wget https://github.com/uday1kiran/python_deb_create/raw/testdeb2/tmp/xenowulf-ai_1.0_all.deb
 apt install -y ./xenowulf-ai_1.0_all.deb
 echo "---Completed installation of main pacakge: xenowulf-ai---"
fi
