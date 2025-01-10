import yaml
import argparse
import numpy as np
import torch
import torch.nn as nn
import random
from PIL import Image
import cv2
import matplotlib.pyplot as plt
from glob import glob
from tqdm import tqdm
from glob import glob

data = {
    'name': 'Kaikai',
    'age': 27,
    'work': 'water coke',
    'hobby': ['Basketball', 'Black Myth Wukong', 'KPL']
}

with open('example.yml', 'w+') as fin:
    yaml.dump(data, fin)

