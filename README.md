# HDR2Cubemap
## A Blender CLI script to render cubemap faces from HDR map

### 1. Usage 
Install [Blender 3.6 LTS](https://www.blender.org/download/lts/3-6/) or newer. (Blender 4.0 is not tested)

Run from the CLI:
```
blender -b -P hdr_render.py -- [PATH_TO_HDR_FILE] [OUTPUT_PATH] [OUTPUT_RESOLUTION] [Z_SHIFT] [X_SHIFT] [Y_SHIFT]
```
Example usage:
```
blender -b -P hdr_render.py -- /Downloads/old_hall_8k.hdr . 1024 0 15
```
#### Optional parameters:
* OUTPUT_RESOLUTION: default 1024
* Z_SHIFT: camera z rotation shift, in degrees, default 0
* X_SHIFT: camera x rotation shift, in degrees, default 0
* Y_SHIFT: camera y rotation shift, in degrees, default 0

### 2. Result
Input HDR image from: https://polyhaven.com/a/old_hall

#### Output images:
Tonemapped using [Luminance HDR](https://github.com/LuminanceHDR/LuminanceHDR)

![oldhall_5_reinhard05](https://github.com/akifuslu/HDR2Cubemap/assets/40760783/3a7c9a8d-f4a2-41b3-8d53-294d042954ce)
![oldhall_4_reinhard05](https://github.com/akifuslu/HDR2Cubemap/assets/40760783/f5eb4338-30fe-4125-888f-f918fceb0cee)
![oldhall_3_reinhard05](https://github.com/akifuslu/HDR2Cubemap/assets/40760783/be19c6ba-9b41-480c-a552-923d1bc0e4a9)
![oldhall_2_reinhard05](https://github.com/akifuslu/HDR2Cubemap/assets/40760783/93af3180-142f-48cc-bacb-7dc1c873cc3c)
![oldhall_1_reinhard05](https://github.com/akifuslu/HDR2Cubemap/assets/40760783/b9652fcf-302a-4028-b552-48a4e5adba52)
![oldhall_0_reinhard05](https://github.com/akifuslu/HDR2Cubemap/assets/40760783/fabb3ab6-8b43-4c58-ac47-8c58df8bb52e)

