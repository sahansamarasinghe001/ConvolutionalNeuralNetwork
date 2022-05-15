import cv2
import glob
import pandas as pd

path = '/Users/wsesr/Desktop/Lectures/COMP1804-AML/Project/vol/deform/dk15/attribute_db/emotionet_6/all/*'
count =0
items = glob.glob(path)
aaa = []
for each_image in items:

   image = cv2.imread(each_image)
   image = cv2.resize(image, (96,96))
   aaa.append(image)
   count = count+1
   print(count)


file1= pd.DataFrame()
file1["images"]= aaa
file1.to_csv(r'/Users/wsesr/Desktop/Lectures/img.csv', index=0)
print(file1)

#read_file = pd.read_csv ('/Users/wsesr/Desktop/Lectures/img.csv', index=0)
#read_file.columns = ['Images']
#read_file.to_csv (r'/Users/wsesr/Desktop/Lectures/conv.csv', index=None)
