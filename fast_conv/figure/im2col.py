import numpy as np
from numpy.lib.stride_tricks import as_strided

# Generate an image
H = 4
W = 5
x = np.arange(1, H*W+1).reshape(H,W)
print x
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]
#  [11 12 13 14 15]
#  [16 17 18 19 20]]

# Generate a filter
stride = 1
HH = 3
WW = 3

# Perform an im2col operation on x
OH = (H - HH) / stride + 1  # output height
OW = (W - WW) / stride + 1  # output width
shape = (OH, OW, HH, WW)  # define the shape of output matrix
strides = (stride*W, stride, 1*W, 1)  # define the strides(offset) according to shape
strides = x.itemsize * np.array(strides)  # turn unit of the strides into byte
x_stride = as_strided(x, shape=shape, strides=strides)
x_cols = np.ascontiguousarray(x_stride)  # put our convenience matrix together im memory
print x_cols[0, 0]
# [[ 1  2  3]
#  [ 6  7  8]
#  [11 12 13]]
print x_cols[1, 0]
# [[ 6  7  8]
#  [11 12 13]
#  [16 17 18]]
print x_cols[1, 2]
# [[ 8  9 10]
#  [13 14 15]
#  [18 19 20]]

