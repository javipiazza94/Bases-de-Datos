import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import warnings
warnings.filterwarnings('ignore')

from pathlib import Path
import urllib.request
from PIL import Image

data_path = Path('C:/Users/javier.puente.ext/Documents/PYTHON/Visualizacion_datos/Datos')

# Abrir la URL y leer la imagen con Pillow
url = 'https://raw.githubusercontent.com/tphinkle/tphinkle.github.io/master/images/2017-8-15/mnist_0.png'
with urllib.request.urlopen(url) as url:
    with Image.open(url) as img:
        image = np.array(img)

print(image)
imgplot = plt.imshow(image)
lum_img = image[:, :, 1]
imgplot2 = plt.imshow(lum_img)
plt.colorbar()
imgplot2.set_cmap('nipy_spectral')
print(plt.show())





