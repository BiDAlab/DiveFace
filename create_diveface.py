# -*- coding: utf-8 -*-
"""
@author: BiDALab
"""
import shutil
import os
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--mega","-m", help="MegaFace folder")
parser.add_argument("--dive","-d", help="DiveFace folder")
parser.add_argument("--balanced","-b",action='store_true', help="DiveFace folder")
args = parser.parse_args()

# Check if is only one argument
if len(sys.argv) == 1:
    print("\nNo arguments. Try\n python {} --mega <MegaFaceFolder> --dive <DiveFaceFolder> [-b]".format(sys.argv[0]))
    exit()

# Check if folders exist
if not os.path.exists(args.mega) or os.path.exists(args.dive):
    print ( "\nError. MegaFace folder doesnt exist or DiveFace folder already exists.")
    exit()
    
# Classes definition    
db_classes = ("Group1_Male","Group2_Male","Group3_Male","Group1_Female","Group2_Female","Group3_Female") 

# For each class, check if the photos file exists
for class_name in db_classes:
    if not os.path.exists("files/"+class_name+".txt"):
        print("\nFile \"files/"+class_name+".txt\" missing.")
        exit()
        
# If DiveFace folder doesnt exist, its created        
if not os.path.exists(args.dive):
    os.mkdir(args.dive)
    
# For each class
for class_name in db_classes:
    dest_path = os.path.join(args.dive, class_name)
    # Create the folder
    if not os.path.exists(dest_path):
        os.mkdir(dest_path)
        
    # Choose the file
    file = open("files/"+class_name + ".txt","r")
    
    # Read the content
    lines = file.readlines()
     # Close the class file and continue the loop    
    file.close()
    
    # User Dictionary
    dict_users = {}

    for line in lines:
        # Split to get the user and the image
        splited = line.split("/")
        
        # If the value is empty, create a new list
        if dict_users.get(splited[0]) == None:
            tmp = []
            tmp.append(splited[1])
            dict_users[splited[0]]=tmp
        else:
            tmp = dict_users[splited[0]] 
            # Else if not balanced, add all
            if not args.balanced:
                tmp.append(splited[1])
                dict_users[splited[0]]=tmp
            elif len(tmp) != 3:
                # Else if has less than 3, add until it has 3
                tmp.append(splited[1])
                dict_users[splited[0]]=tmp
   
    # Loop that copy the files
    for index, user in enumerate(dict_users):
        if args.balanced:
            s = "\r{:.4}% Complete   Class: {}       ".format((index)*100*3/len(dict_users),class_name)
        else:
            s = "\r{:.4}% Complete   Class: {}       ".format((index)*100/len(dict_users),class_name)
        sys.stdout.write(s)
        
        # If the folder doesnt exist, its created
        if not os.path.exists(os.path.join(dest_path, user)):
            os.mkdir(os.path.join(dest_path, user))
        
        for img in dict_users.get(user):
            if img[-1] == "\n":
                img = img[:-1]
            # Copy the file
            shutil.copy(os.path.join(args.mega,user,img ), os.path.join(dest_path,user,img))
        
    print()

   
    
        
