from UI import *  # 导入UI模块

# 设定基准路径
ASSET_BASE_PATH = os.path.dirname(os.path.abspath(__file__)) + "\\assets\\"
TASKS_PATH = os.path.dirname(os.path.abspath(__file__)) + "\\tasks\\"


# 路径检测函数
def check_path():
    if os.path.isdir(ASSET_BASE_PATH):  # 检测assets目录是否存在
        print("Assets Detected.")
        asset_flag = True
    else:
        raise FileNotFoundError
    if os.path.isdir(TASKS_PATH):  # 检测tasks目录是否存在
        print("Tasks Detected.")
        tasks_flag = True
    else:
        raise FileNotFoundError
    if "user_info.json" in os.listdir("."):  # 检测user_info文件是否存在
        print("User Info Detected.")
        user_flag = True
    else:
        raise FileNotFoundError
    if asset_flag and tasks_flag and user_flag:  # 如果检测正常返回True
        return True


if __name__ == "__main__":
    if check_path():
        # 创建主窗口并运行程序
        root = tk.Tk()
        app = WelcomeScreen(root)
        root.mainloop()
