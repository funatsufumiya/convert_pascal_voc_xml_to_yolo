# Convert Pascal VOC XML Annotation files to YOLO format text files
This script converts a Pascal voc file to a text file in YOLO format.
For Japanese → https://qiita.com/Rihib/items/e163d90c009f4fe12782

### Instructions
1. Rewrite the following part at the top of the main.py file according to the instructions written in the comment out. You don't need to worry about the location of each directory at all. It's okay to mix xml files and image files in the same directory. Of course, you can also put them in separate directories.
2. Run the script.

If it doesn't work, check the contents of your xml files against the GetDataFromXMLfile class in main.py to make sure that your xml files are being parsed properly.
