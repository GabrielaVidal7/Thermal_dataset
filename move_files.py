import os
import shutil

txt_test = [f for f in os.listdir("Dataset/test/") if '.txt' in f.lower()]
images_test = [f for f in os.listdir("Dataset/test/") if '.jpg' in f.lower()]

txt_valid = [f for f in os.listdir("Dataset/validation/") if '.txt' in f.lower()]
images_valid = [f for f in os.listdir("Dataset/validation/") if '.jpg' in f.lower()]

txt_train = [f for f in os.listdir("Dataset/train/") if '.txt' in f.lower()]
images_train = [f for f in os.listdir("Dataset/train/") if '.jpg' in f.lower()]

os.mkdir('Dataset/test/labels')
for text in txt_test:
    new_path = 'Dataset/test/labels/' + text
    shutil.move('Dataset/test/'+text, new_path)

os.mkdir('Dataset/test/images')
for image in images_test:
    new_path = 'Dataset/test/images/' + image
    shutil.move('Dataset/test/'+image, new_path)

os.mkdir('Dataset/validation/labels')
for text in txt_valid:
    new_path = 'Dataset/validation/labels/' + text
    shutil.move('Dataset/validation/'+text, new_path)

os.mkdir('Dataset/validation/images')
for image in images_valid:
    new_path = 'Dataset/validation/images/' + image
    shutil.move('Dataset/validation/'+image, new_path)

os.mkdir('Dataset/train/labels')
for text in txt_train:
    new_path = 'Dataset/train/labels/' + text
    shutil.move('Dataset/train/'+text, new_path)

os.mkdir('Dataset/train/images')
for image in images_train:
    new_path = 'Dataset/train/images/' + image
    shutil.move('Dataset/train/'+image, new_path)