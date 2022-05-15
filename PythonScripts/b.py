infile = "/Users/wsesr/Desktop/Lectures/COMP1804-AML/pythonProject1/image_names.txt"
outfile = "/Users/wsesr/Desktop/Lectures/COMP1804-AML/pythonProject1/Cleared.txt"

wordLne = "/Users/wsesr/Desktop/Lectures/COMP1804-AML/Project/vol/deform/dk15/attribute_db/emotionet_6/all\ "




delete_list = [wordLne.strip()]
with open(infile) as fin, open(outfile, "w+") as fout:
    for line in fin:
        for word in delete_list:
            line = line.replace(word, "")
        fout.write(line)