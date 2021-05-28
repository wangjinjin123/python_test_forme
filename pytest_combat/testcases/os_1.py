import inspect
import os


def be_call_fun():
    # stack()返回的是调用栈列表。
    frame_stack = inspect.stack()
    # 0是标识当前函数的栈，1是标识上一层函数的栈，依此类推。
    # 也就是这个数值不一定是1，要看你要获取其文件路径的函数在第几层
    caller_frame = frame_stack[1]
    caller_file_path = caller_frame.filename
    # 由于当前调用函数和被调用函数放在同一个文件，所以文件名还是当前文件名
    # 可将调用函数和被调用函数放到不同文件进行观察
    print(f"caller_file_path: {caller_file_path}")

def caller_fun():
    be_call_fun()


print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
print(os.path.abspath(os.path.dirname(os.getcwd())))
print(os.path.abspath(os.path.join(os.getcwd(), "..")))
print(os.path.dirname(os.getcwd()))
if __name__ == "__main__":
    caller_fun()

