# NOTICE: THIS PROJECT IS MEANLESS, you can use pyradiomics to extract ROI features. THIS PROJECT WILL NEVER UPDATE

# Feature extraction

## According to the essasy:*A Review on Tissue Segmentation and Feature Extraction of MRI Brain images*, there is the classic feature which can be extracted from MRI image
![Feature types](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F0329981e-d358-4778-a8c2-a3272260699c%2FScreenshot_from_2021-11-30_14-13-59.png?table=block&id=570c4c2a-00ec-42c2-babc-86351a3291cd&spaceId=e0cb3551-7dbe-4f03-a44f-f7d9328ecd4f&width=1900&userId=80c81d2c-5396-4c72-be40-5220dd79ce33&cache=v2)
You can see, it is divided into three main types, including itensity based features, texture based features and shape based features. Actually, there are hundreds of features can be extracted and used in classical CV, but we just extract this featured at first.


## Considering the README using formula and github don't support katex here. You can download the README to read.
## Also, you can download the chrome extensions: https://chrome.google.com/webstore/detail/mathjax-plugin-for-github/ioemnmodlmafdkllaclgeombjnmnbima?hl=en, it can help you to show the math formula. But it seems LaTex, not Katex, so it may be some wrong preview here.

## Intensity features

$f(x,y)$ be a two dimensional function of an image

$h(i)$ be the intensity level of an image

$\text{N}_\text{g}$ be the total number of gray levels in the entire image

$\text{p}(i)$  be the probability density.

where:

$$
f(x,y)=
\begin{bmatrix}
    f(0,0) & f(0,1) & f(0,2) & \dots &  f(0, \text{N}_y-1) \\
    f(1,0) & f(1,1) & f(1,2) & \dots &  f(1, \text{N}_y-1) \\
    \vdots & \vdots & \vdots & \ddots & \vdots \\
    f(\text{N}_x-1,0) & f(\text{N}_x-1,1) & f(\text{N}_x-1,2) & \dots &  f(\text{N}_x-1, \text{N}_y-1)
\end{bmatrix}
$$

$$
h(i) = \sum_{x=0}^{\text{N}_\text{g}-1}\sum_{y=0}^{\text{N}_\text{g}-1}\delta(f(x,y),i), i=0,1,2,\dots, N-1
$$

$$\delta(i,j)=\begin{cases}
1, & i=j \\
0, & i \not = j
\end{cases}$$

$$p(i)=\frac{h(i)}{\text{N}_x\text{N}_y}, i=0,1,2,\dots,N-1$$

$p(i)$ is probability density of intensity, which can be obtained by using impluse function

1) Mean: defines the average level of intensity of the image or texture.

$$\text{Mean}, \mu = \sum_{i=0}^{\text{N}_\text{g}-1}i \cdot p(i)$$

2) Variance:

The variance defines the variation of intensity around the mean.

$$\text{Variance}, \sigma^2 = \sum_{i=0}^{\text{N}_\text{g}-1}(i-\mu)^2\cdot p(i)$$

3) Standard Deviation:(SD)

$$\text{SD} \ \text{or} \ \sigma = \sqrt{\sum_{i=0}^{\text{N}_\text{g}-1}(i-\mu)^2\cdot p(i)}$$

4) Skewness:

The Skewness defines the symmetry of an image.

$$\mu^3 = \sigma^{-3} \sum_{i=0}^{\text{N}_\text{g}-1}(i-\mu)^3\cdot p(i)$$

$$\text{Skewness} = \begin{cases}
\mu^3<0, & \text{Histogram below the mean} \\
\mu^3 = 0, & \text{Histogram is equal to the mean} \\
\mu^3 >0, & \text{Histogram above the mean}
\end{cases}$$

5) Kurtosis:

The Kurtosis defines the measure of the flatness of the histogram.

$$\text{Kurtosis}, \mu^4 = \sigma^{-4} \sum_{i=0}^{\text{N}_\text{g}-1}((i-\mu)^4 \cdot p(i))-3$$

6) Energy:

Energy defines the measure of the sum of squared elements.

$$\text{Energy}, \text{E} = \sum_{i=0}^{\text{N}_\text{g}-1}[p(i)]^2$$

7) Entropy:

Entropy is defined as a measure of uncertainty in a random variable

$$\text{Entropy}, \text{EN} = -\sum_{i=0}^{\text{N}_\text{g}-1}p(i)\cdot \log_2[p(i)]$$

## Texture Features

