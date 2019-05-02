import argparse

from trainer import BaseTrainer
from trainer import FedTrainer
from option import Option
import pdb
import os
import utils 
import numpy as np
import pandas as pd
import sys
sys.path.append("../")

from datasets.vgg_face2 import VGG_Face2

import torch
import torch.nn as nn
import torch.optim
import torch.utils.data
import torchvision
import torchvision.transforms as transforms
import torchvision.datasets as datasets
import torchvision.models as models
import torch.backends.cudnn as cudnn
from torch.utils.data.sampler import SubsetRandomSampler

from models.lenet import LeNet
from fed_train import train

"""
Experiment to vary iid-ness of client and sybils using FG
Saves Val Accuracy, Val Poisoning Rate, Memory, and WVHistory
"""
def main():
    parser = argparse.ArgumentParser(description='Training')
    parser.add_argument('conf_path', type=str, metavar='conf_path')
    args = parser.parse_args()

    option = Option(args.conf_path)
    for client_iid in [.0, .25, .5, .75, 1.0]:
        for sybil_iid in [.0, .25, .5, .75, 1.0]:
            train(option, [client_iid, sybil_iid])

if __name__ == "__main__":
    main()