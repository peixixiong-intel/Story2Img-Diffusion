#!/bin/sh
#python -m torch.distributed.launch --nproc_per_node=2 --master_port 7787 train_ddp.py --name coco_train --config_file configs/coco.yaml --num_node 1
# --tensorboard --load_path OUTPUT/pretrained_model/CC_pretrained.pth
python running_command/run_train_coco.py