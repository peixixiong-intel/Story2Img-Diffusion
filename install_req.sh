#!/bin/bash
pip3 install torch==1.9.0 torchvision --no-cache-dir -U | cat
pip3 install omegaconf pytorch-lightning --no-cache-dir -U | cat
pip3 install timm==0.3.4 --no-cache-dir -U | cat
pip3 install tensorboard==1.15.0 --no-cache-dir -U | cat
pip3 install lmdb tqdm --no-cache-dir -U | cat
pip3 install einops ftfy --no-cache-dir -U | cat
