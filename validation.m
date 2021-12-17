Brain = imread('sample/Ivy.jpeg');
whos Brain
%image(Brain)
Brain = rgb2gray(Brain);
whos Brain
%figure
%imshow(Brain)
mean2(Brain)
std2(Brain)
skewness(double(Brain), 1, 'all')
kurtosis(double(Brain), 1, 'all')

test = [0,0,1,1;0,0,1,1;0,2,2,2;2,2,3,3;]
glcm = graycomatrix(test, 'Numlevels', 4, 'Graylimits', [0,4])

glcms = graycomatrix(Brain, 'Numlevels', 256)

glcmss = graycomatrix(Brain, 'GrayLimits', [0, 8]) 