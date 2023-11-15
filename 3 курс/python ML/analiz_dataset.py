from glob import glob
import os
import time

# test = sorted(glob("test\*"))
# images = sorted(glob("nigger_white_man\*"))
# labels = sorted(glob("niggers_neyron\obj_train_data\*"))
images = sorted(glob("train\images\*"))
labels = sorted(glob("train\labels\*"))
images_labels = dict(zip(images, labels))
print(len(images), len(labels))
for i, l in images_labels.items():
    i = os.path.splitext(os.path.basename(i))[0]
    f = open(l)
    l = os.path.splitext(os.path.basename(l))[0] 
    print(i, l, f.read())
    time.sleep(1)