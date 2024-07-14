import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
im = plt.imread("download.jpeg")
cv2.imshow('idk', im[:, :, 1])
