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
    # If -b argument : Use the reduced files
    if args.balanced:
        if not os.path.exists("files/"+class_name+"_balanced.txt"):
            print("\nFile \"files/"+class_name+"_balanced.txt\" missing.")
            exit()
    # Else use the completed files
    else:
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
    if args.balanced:
        file = open("files/"+class_name + "_balanced.txt","r")
    else:
        file = open("files/"+class_name + ".txt","r")
    
    # Read the content
    lines = file.readlines()
   
    # Loop that copy the files
    for index,line in enumerate(lines):
        s = "\r{:.4}% Complete   Class: {}       ".format((index)*100/len(lines),class_name)
        sys.stdout.write(s)
        arr = line.split("/")
        
        # If the folder doesnt exist, its created
        if not os.path.exists(os.path.join(dest_path, arr[0])):
            os.mkdir(os.path.join(dest_path, arr[0]))
        
        # Copy the file
        shutil.copy(os.path.join(args.mega,line[:-1] ), os.path.join(dest_path,line[:-1]))
        
    print()

    # Close the class file and continue the loop    
    file.close()
    
        
