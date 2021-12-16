Brain = imread('sample/Ivy.jpeg');
whos Brain
%image(Brain)
Brain = rgb2gray(Brain);
whos Brain
figure
imshow(Brain)
mean2(Brain)
std2(Brain)
skewness(double(Brain), 1, 'all')
kurtosis(double(Brain), 1, 'all')

[glcms,SI] = graycomatrix(Brain, 'offset', [0 1], 'NumLevels', 8);

stats = graycoprops(glcms)

figure
imshow(rescale(SI))
