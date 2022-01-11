from radiomics import featureextractor, getTestCase
import SimpleITK as sitk
from skimage import io, color
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image, ImageOps
import os
import cv2
import six
import pandas as pd

if __name__ == '__main__':
    '''
    image_RGB = sitk.ReadImage(r'sample/TCGA_CS_4941_19960909_18.tif')
    print(image_RGB)
    image = sitk.GetArrayFromImage(image_RGB)
    print(image.shape)
    io.imshow(image)
    plt.show()
    pass
    sitk.Show(image_RGB)
    '''

    '''
    image = Image.open(r'sample/TCGA_CS_4941_19960909_18_mask.tif')
    print(image.mode)
    img = np.array(image)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i, j] == 255:
                img[i, j] = 1
    image = Image.fromarray(img)
    image.save(r'sample/TCGA_CS_4941_19960909_18_mask.tif')

    image = sitk.ReadImage(r'sample/TCGA_CS_4941_19960909_18_mask.tif')
    image = sitk.GetArrayFromImage(image)
    io.imshow(image)
    plt.show()
    '''

    '''
    im_gray = cv2.imread(r'sample/TCGA_CS_4941_19960909_18_mask.tif', cv2.IMREAD_GRAYSCALE)
    #cvcv(thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY)
    for i in range(im_gray.shape[0]):
        for j in range(im_gray.shape[1]):
            if im_gray[i, j] == 255:
                im_gray[i, j] = 1
    im_bw = np.float32(im_gray / 255)
    cv2.imwrite(r'sample/TCGA_CS_4941_19960909_18_mask.tif', im_bw)
    '''

    dataDir = r'sample'

    # imageName, maskName = getTestCase('brain1', dataDir)
    imageName = os.path.join(dataDir, 'TCGA_CS_4941_19960909_18.tif')
    maskName = os.path.join(dataDir, 'TCGA_CS_4941_19960909_18_mask.tif')

    print(imageName)
    print(maskName)

    #image = sitk.ReadImage(imageName)
    #mask = sitk.ReadImage(maskName)

    #sitk.Show(image)
    #sitk.Show(mask)


    params = os.path.join(dataDir, "Params.yaml")

    print(params)

    extractor = featureextractor.RadiomicsFeatureExtractor(params)

    result = extractor.execute(imageName, maskName)
    for key, val in result.items():
        if 'diagnostics' not in key:
            print("\t%s: %s" %(key, val))

    df = pd.DataFrame({})
    for key, val in result.items():
        if 'diagnostics' not in key:
            df[key.replace('original_', '')] = pd.Series(val)
    print(df)
    df.to_csv(r'sample/test.csv', index=False)

    '''
    PATH=$(echo "$PATH" | sed -e 's/:\/home\/pinkr1ver\/fiji-linux64\/Fiji.app$//')
    
    directory_to_remove=/home/pinkr1ver/fiji-linux64/Fiji.app
    PATH=:$PATH:
    PATH=${PATH//:$directory_to_remove:/:}
    PATH=${PATH#:}; PATH=${PATH%:}

    export PATH=$PATH:/home/pinkr1ver/Fiji.app/ImageJ-linux64

    export PATH="$PATH:/home/pinkr1ver/Fiji.app"
    export PATH="$PATH:/home/pinkr1ver/Fiji.app/ImageJ-linux64"
    '''