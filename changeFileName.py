import os

path='./somefiles'; #要管理的文件夹名字
count=0;
filelist=os.listdir(path)#该文件夹下所有的文件（包括文件夹）
def rename():
    global count
    for files in filelist:#遍历所有文件
        Olddir=os.path.join(path,files);#原来的文件路径
        filename=os.path.splitext(files)[0];#文件名
        filetype=os.path.splitext(files)[1];#文件扩展名
        Newdir=os.path.join(path,str(count)+filetype);#新的文件路径，这一行可以根据需要进行修改
        os.rename(Olddir,Newdir);#重命名
        count+=1;
rename();
