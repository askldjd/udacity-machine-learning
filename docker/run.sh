#!/bin/sh
#sh stop.sh
sudo docker run \
    --rm \
    -it \
    -v ~/work/personal/machine-learning:/work/personal/machine-learning \
    --name udacity-ml \
    udacity-ml-img

