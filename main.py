import os
import shutil 

src ="C:\\Users\\ACER-PC\\Downloads\\"
destination ={'png':"C:\\Users\\ACER-PC\\Desktop\\images",
'JPG':"C:\\Users\\ACER-PC\\Desktop\\images",
"mp3":"C:\\Users\\ACER-PC\\Desktop\\audio",
"mp4":"C:\\Users\\ACER-PC\\Desktop\\videos",
"pdf":"C:\\Users\\ACER-PC\\Desktop\\pdf's",
"docx":"C:\\Users\\ACER-PC\\Desktop\\documents",
"xlsx":"C:\\Users\\ACER-PC\\Desktop\\excel",
"pptx":"C:\\Users\\ACER-PC\\Desktop\\power poiny",
"XLSX":"C:\\Users\\ACER-PC\\Desktop\\excel",
"doc":"C:\\Users\\ACER-PC\\Desktop\\documents",
"xls":"C:\\Users\\ACER-PC\\Desktop\\excel",
"rtf":"C:\\Users\\ACER-PC\\Desktop\\documents",
'zip':"C:\\Users\\ACER-PC\\Desktop\\downloded zips",
}
os.chdir(src)
files = os.listdir()

for file in files:
   if '.' in file:
    ext = file.split('.')[-1].strip()
    if ext in destination:
        shutil.move(file,destination[ext])
