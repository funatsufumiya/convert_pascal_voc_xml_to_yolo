############    Please edit this section only. ###############################################################################################################################################################################################################################

#  The paths must end with '/'.      
absolutepath_of_directory_with_xmlfiles = './pascalvoc/Annotations/'  #　It is okay to have a mix of xml files and images in the same directory.
absolutepath_of_directory_with_imgfiles = './pascalvoc/JPEGImages/'
absolutepath_of_directory_with_yolofiles = './yolo_out/'  # Yolo files will be created under this directory.
absolutepath_of_directory_with_classes_txt = './yolo_classes/'  # You do not need to create classes.txt. classes.txt will be generated automatically.
absolutepath_of_directory_with_error_txt = './yolo_errors/'  # The names of files that do not have a paired xml or image file will be written to a text file under this directory.

train_valid_rate = 0.9  # The ratio of training data to validation data. 0.8 means 80% of the data will be used for training and 20% will be used for validation.

out_dir = "./yolov5_out/"
dataset_name = "custom_dataset"
data_dir_name = "data"
train_dir_name = "train"
valid_dir_name = "val"

##############################################################################################################################################################################################################################################################################

base_dir = f"{out_dir}{data_dir_name}/"
train_dir = f"{base_dir}{train_dir_name}/"
valid_dir = f"{base_dir}{valid_dir_name}/"
yaml_name = f"{dataset_name}.yaml"

import os
import random

labels = []
with open(f"{absolutepath_of_directory_with_classes_txt}classes.txt", "r") as f:
    labels = f.read().splitlines()

# labels to json array string
labels_str = "["
for label in labels:
    labels_str += f"'{label}',"
labels_str = labels_str[:-1] + "]"

# print(labels)

yaml_str = f'''names: {labels_str}
nc: {len(labels)}
train: {data_dir_name}/{train_dir_name}/images
val: {data_dir_name}/{valid_dir_name}/images'''

# print(yaml_str)

os.makedirs(base_dir, exist_ok=True)
os.makedirs(train_dir, exist_ok=True)
os.makedirs(f"{train_dir}images", exist_ok=True)
os.makedirs(f"{train_dir}labels", exist_ok=True)
os.makedirs(valid_dir, exist_ok=True)
os.makedirs(f"{valid_dir}images", exist_ok=True)
os.makedirs(f"{valid_dir}labels", exist_ok=True)

with open(f"{base_dir}../{yaml_name}", "w") as f:
    f.write(yaml_str)

list_txt_files = os.listdir(absolutepath_of_directory_with_yolofiles)
# randomize
random.shuffle(list_txt_files)

# print(list_txt_files)

# create txt file to image filename map from annotation xml
xml_files = os.listdir(absolutepath_of_directory_with_xmlfiles)
xml_file_to_img_file = {}
for xml_file in xml_files:
    with open(f"{absolutepath_of_directory_with_xmlfiles}{xml_file}", "r") as f:
        xml = f.read()
        img_file = xml.split("<filename>")[1].split("</filename>")[0]
        key = xml_file.split(".")[0]
        xml_file_to_img_file[key] = img_file

# print(xml_file_to_img_file)

# randam pickup train/valid from list_txt_files
train_files = []
valid_files = []
for i, txt_file in enumerate(list_txt_files):
    if i % (1 / train_valid_rate) == 0:
        valid_files.append(txt_file)
    else:
        train_files.append(txt_file)

# print(train_files)
# print(valid_files)

# copy train/valid files
for train_file in train_files:
    key = train_file.split(".")[0]
    img_file = xml_file_to_img_file[key]
    os.system(f"cp {absolutepath_of_directory_with_yolofiles}{train_file} {train_dir}labels")
    os.system(f"cp {absolutepath_of_directory_with_imgfiles}{img_file} {train_dir}images")

for valid_file in valid_files:
    key = valid_file.split(".")[0]
    img_file = xml_file_to_img_file[key]
    os.system(f"cp {absolutepath_of_directory_with_yolofiles}{valid_file} {valid_dir}labels")
    os.system(f"cp {absolutepath_of_directory_with_imgfiles}{img_file} {valid_dir}images")