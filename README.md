# evolv-fit-cricket
My Solution to the Evolv Machine Learning Challenge.

Initial Model:
![image](https://user-images.githubusercontent.com/13780335/118634027-b95eda00-b7ef-11eb-9ce1-e677bb4fb371.png)

- Low Validation Accuracy: ~40%
- 576 Images, 15 Classes used with composition:
  - Training: 371 Images
  - Validation: 84 Images
  - Testing: 121 Images
- Model: 
<pre>
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d (Conv2D)              (None, 148, 148, 64)      1792      
_________________________________________________________________
max_pooling2d (MaxPooling2D) (None, 74, 74, 64)        0         
_________________________________________________________________
conv2d_1 (Conv2D)            (None, 72, 72, 64)        36928     
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 36, 36, 64)        0         
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 34, 34, 128)       73856     
_________________________________________________________________
max_pooling2d_2 (MaxPooling2 (None, 17, 17, 128)       0         
_________________________________________________________________
conv2d_3 (Conv2D)            (None, 15, 15, 128)       147584    
_________________________________________________________________
max_pooling2d_3 (MaxPooling2 (None, 7, 7, 128)         0         
_________________________________________________________________
flatten (Flatten)            (None, 6272)              0         
_________________________________________________________________
dropout (Dropout)            (None, 6272)              0         
_________________________________________________________________
dense (Dense)                (None, 512)               3211776   
_________________________________________________________________
dense_1 (Dense)              (None, 15)                7695      
=================================================================
Total params: 3,479,631
Trainable params: 3,479,631
Non-trainable params: 0
</pre>
- Images reduced to 150 x 150 px
- Dataset not cleaned
