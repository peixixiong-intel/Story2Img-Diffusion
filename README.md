# Story2Img-Diffusion

## Requirements
The required package are here.
>```bash install_req.sh```

## Saved Parameters
Due to the storage limiatation, I store the saved parameters and config files in [here](https://intel-my.sharepoint.com/:f:/p/peixi_xiong/EinjGCttSi9DjWlOpcIGp7oBedA99gOSSyR5OH0GlGPKpw?e=waNBrA). 

The file name is story2img_train. Please directly substitute the one in ```Story2Img-Diffusion/OUTPUT/story2img_train/```

## Inference Code
>```sbatch -p gpu --gres=gpu:1 --nodelist=csr-a100x6 --qos=high  -c 8 running_command/run_inference.sh```

The python file for inference is ```inference_Story2Img_Diffusion.py```
