import os
import shutil


'''自动化实现：创建文件夹，复制指定文件到指定目录'''


abspath = os.path.abspath('.')

def mkdir(new_dir):
    '''自动创建目录，如果目录存在则pass，传入参数：new_dir ——相对py文件的绝对路径的相对路径字符串'''
    for i in os.listdir():#遍历当前目录中所有子目录
        try:
            if 'checkio' in i:#目录名中包含'checkio'则开始进入该目录并创建目标目录
                new_path = os.path.join(abspath, i + new_dir)
                os.makedirs(new_path)
                print(new_path + " created!")
        except FileExistsError:#如果文件夹存在则不作处理
            pass

def cpfile():
    '''自动复制文件到指定目录的方法'''
    for i in os.listdir():#遍历当前目录中所有子目录
        try:
            new_file = os.path.join(abspath, i + '/translations/zh-cn/info/task_description.html')
            old_file = os.path.join(abspath, i + '/info/task_description.html')
            if 'checkio' in i and os.path.exists(new_file) == 0:#判断文件是否已经存在，如果不存在，则从指定目录下copy文件到目标目录
                shutil.copyfile(old_file, new_file)
        except:
            pass

def main():    
    new_dir = '/translations/zh-cn/info'
    mkdir(new_dir)
    cpfile()

if __name__ == "__main__":
    main()
    
