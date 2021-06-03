"""
文件的读取
读写文件的操作步骤：
1、打开文件，获取文件描述符
2、操作文件描述符（读 |写）
3、关闭文件

使用方法：
open(file,mode='r',buffering=-1.encoding=None,errors=None,newline=None,closefd=True,opener=None)
参数说明：
name：文件名称
mode：只读r、写入w、追加a，默认文件访问模式为r;x创建一个文件并编写它  +：磁盘更新（读+写）
buffering：寄存区缓存
   0-不寄存
   1-访问文件时会寄存行
   >1-寄存区的缓冲大小
   负值-寄存区的缓冲大小则为系统默认
注意：文件读写操作完成后，应该及时关闭文件
"""


f = open("data.txt")
print(f.readable())
#读取全部行
#print(f.readlines())
#读取一行
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())

f.close()

#with语句块可以将文件打开后操作完毕后自动关闭这个文件
#图片读取需要使用rb，读取二进制的格式
#正常的文本，可以使用rt，也就是默认格式即可
with open("data.txt") as f:
    while True:
        line = f.readline()
        if line:
            print(line)
        else:
            break
    #print(f.readlines())

