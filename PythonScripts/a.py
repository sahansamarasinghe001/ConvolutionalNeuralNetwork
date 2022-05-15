## put here the full path of the generated file of the annotation tool, e.g.: /Users/jim/Desktop/AU_video.txt


file_name = '/Users/wsesr/Desktop/Lectures/COMP1804-AML/pythonProject1/AU_video.txt'
with open(file_name) as fil:
    content = fil.readlines()

f = open("demofile.txt", "a")
outputs = []

for elem in content:
    if 'N/A' in elem:
        continue
    else:
        line = elem.split(',')
        outputs.append([int(line[1]), int(line[3]), int(line[5]), int(line[7]), int(line[9]), int(line[11])])
        f.write(line[1]+","+line[3]+","+line[5]+","+line[7]+","+line[9]+","+line[11]+"\n")

print(outputs)
f.close()

# always the outputs correspond to (in that order): wrinkles, freakles, glasses, hair color, hair top, no face shown or not human
## put here the full path of the generated file of the annotation tool, e.g.: /Users/jim/Desktop/AU_video.txt
# import pandas as pd
#
# #file_name = '/Users/wsesr/Desktop/Lectures/COMP1804-AML/pythonProject1/demofile2.txt'
# read_file = pd.read_csv (r'/Users/wsesr/Desktop/Lectures/COMP1804-AML/pythonProject1/demofile2.txt')
# read_file.columns = ['wrinkles','freakles','glasses','hair color','hair top','not human']
# read_file.to_csv (r'/Users/wsesr/Desktop/Lectures/COMP1804-AML/pythonProject1/conv.csv', index=None)

# always the outputs correspond to (in that order): wrinkles, freakles, glasses, hair color, hair top, no face shown or not human
# read_file1 = pd.read_csv (r'/Users/wsesr/Desktop/Lectures/COMP1804-AML/pythonProject1/final/Cleared.txt')
# read_file2 = pd.read_csv (r'/Users/wsesr/Desktop/Lectures/COMP1804-AML/pythonProject1/final/demofile.txt')
# read_file1.columns = ['Images']
# read_file2.columns = ['wrinkles','freakles','glasses','hair color','hair top','not human']
# # read_file1['wrinkles'] = read_file2['wrinkles']
# read_file1['freakles'] = read_file2['freakles']
# read_file1['glasses'] = read_file2['glasses']
# read_file1['hair color'] = read_file2['hair color']
# read_file1['hair top'] = read_file2['hair top']
# read_file1['not human'] = read_file2['not human']
