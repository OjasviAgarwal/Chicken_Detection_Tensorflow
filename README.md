# Chicken_Detection_Tensorflow
This project starts with 4 Images having chickens in a farm, augments the dataset and trains it using the Tensorflow 2 Object Detection API (Faster RCNN ResNet 50 640x640) 

Prerequisites
1. Jupyter Notebook (Can be accessed via Spyder after installing anaconda or you can spin up a Notebook Instance from AWS SageMaker [Choose tensorflow kernel py36-tf2])
2. Ubuntu VM 18.04 (If local, GPU is a good to have else you can use the Deep Learning AMI from AWS [t2.2xLarge]) with Tensorflow 2 installed either CPU support ot GPU support > https://github.com/abdelrahman-gaber/tf2-object-detection-api-tutorial
3. Access to Ubuntu GUI (for AWS EC2 > https://ubuntu.com/tutorials/ubuntu-desktop-aws#1-overview)

Approach 
1. Take 4 Images and augment them to 100
2. Label the Images using the https://github.com/tzutalin/labelImg tool
3. Convert the xml files we get from prev tool to one csv file 
4. convert the csv file to a TFRecord file as that is compatible with the Tensorflow 2 Object Dectection API
5. Choose your training model --> I chose F RCNN ResNet 640 x 640
6. Train and evaluate the model 
7. Visualize using Tensorboard 

Info about AWS Desktop
1. Use instance Ip instead of DNS URL while connecting for the VNC session

Info about data_augmentation.py
1. You will save your images to specific folders in SageMaker Notebook
2. To download them , open terminal in jupyter to zip them and then download them 

Info about labelImg
1. During setup ignrore > sudo pip3 install -r requirements/requirements-linux-python3.txt and install pyQt5 and lxml seperately using pip install




