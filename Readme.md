# Readme

## 项目简介

本项目是用Python语言编写的一个待办事项应用程序，GUI界面使用tkinter 库实现。目前版本已经实现了大部分预想的功能。

代码仅在Windows系统下测试通过，Linux和MacOS用户请自行修改路径相关变量。

## 使用手册

### 项目结构

![img](https://github.com/eachz404/todo_app_python/blob/main/imgs/File_structure.png?raw=true)

### 欢迎界面

![img](https://github.com/eachz404/todo_app_python/blob/main/imgs/Welcome_screen.png?raw=true)

- 点击`Login`按钮可以跳转到`登陆界面`
- 点击`Register`按钮可以跳转到`注册界面`

### 登录、注册界面

![img](https://github.com/eachz404/todo_app_python/blob/main/imgs/Login_screen.png?raw=true)

![img](https://github.com/eachz404/todo_app_python/blob/main/imgs/Register_screen.png?raw=true)

输入完信息以后点击登录/注册按钮就可以跳转到主界面。


同时，你也可以在键入账号与密码信息后按下键盘上的`Enter`按键进行登录/注册。

### 主界面

![img](https://github.com/eachz404/todo_app_python/blob/main/imgs/Main_screen.png?raw=true)

主页面上有四个按钮，分别指向四个功能模块。

### Today / Important 界面

![img](https://github.com/eachz404/todo_app_python/blob/main/imgs/Today_screen.png?raw=true)

### 任务添加/任务编辑界面

![img](https://github.com/eachz404/todo_app_python/blob/main/imgs/Add_and_edit_screen.png?raw=true)

### 搜索界面

![img](https://github.com/eachz404/todo_app_python/blob/main/imgs/Search_screen.png?raw=true)

在键入关键词以后，你可以按下键盘上的`Enter`按键进行搜索。

### 回收站界面

![img](https://github.com/eachz404/todo_app_python/blob/main/imgs/Trash_bin_screen.png?raw=true)

## 功能的代码实现

### 路径检测

涉及文件：`Todo.py`

```Python
import os

from UI import *  # 导入UI模块

# 设定基准路径
ASSET_BASE_PATH = os.path.dirname(os.path.abspath(__file__)) + "\\assets\\"
TASKS_PATH = os.path.dirname(os.path.abspath(__file__)) + "\\tasks\\"

# 设定开发人员标签
dev_flag = False


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
        if dev_flag:  # 如果 dev_flag 为真就跳过登录界面 直接进入主界面
            print("Dev Mode:Enabled")
            app = MainScreen(root)
        else:
            app = WelcomeScreen(root)
        root.mainloop()        
```

### 登陆注册模块

以注册界面为例。

涉及文件:`UI.py`

```Python
class RegisterScreen:
    def __init__(self, master):
        self.master = master
        master.geometry("430x932")
        master.configure(bg="#FFFFFF")
        master.title("To-Do App")

        self.canvas = tk.Canvas(
            self.master,
            bg="#FFFFFF",
            height=932,
            width=430,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        global image_image_1, entry_image_1, entry_image_2, button_image_1, button_image_2
        image_image_1 = tk.PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(215.0, 466.0, image=image_image_1)

        entry_image_1 = tk.PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.entry_text_1 = tk.StringVar()
        self.entry_bg_1 = self.canvas.create_image(265.5, 199.0, image=entry_image_1)
        self.entry_1 = tk.Entry(
            self.canvas,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            textvariable=self.entry_text_1
        )
        self.entry_1.place(x=110.0, y=185.0, width=311.0, height=26.0)

        self.entry_text_2 = tk.StringVar()
        entry_image_2 = tk.PhotoImage(file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(265.5, 241.0, image=entry_image_2)
        self.entry_2 = tk.Entry(
            self.canvas,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            textvariable=self.entry_text_2
        )
        self.entry_2.place(x=110.0, y=227.0, width=311.0, height=26.0)

        button_image_1 = tk.PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = tk.Button(
            self.canvas,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.goto_main_screen,
            relief="flat"
        )
        self.button_1.place(x=355.0, y=59.0, width=63.0, height=20.0)

        button_image_2 = tk.PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_2 = tk.Button(
            self.canvas,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.goto_welcome_screen,
            relief="flat"
        )
        self.button_2.place(x=13.12060546875, y=59.0, width=82.87939453125, height=20.0)

        self.master.resizable(False, False)

    def goto_welcome_screen(self):
        # 销毁注册界面，显示欢迎界面
        self.master.destroy()
        # 创建主窗口并运行程序
        master = tk.Tk()
        app = WelcomeScreen(master)
        master.mainloop()

    def register(self):
        if "user_info.json" not in os.listdir():
            with open("user_info.json", "w"):
                user_info = {}
        else:
            with open("user_info.json", "r") as f:
                user_info = json.load(f)

        account = self.entry_1.get().rstrip()
        password = self.entry_2.get()
        if account == "" or password == "":
            tk.messagebox.showwarning(title='警告', message='账号或密码不能为空')
            return False
        if account in user_info:
            tk.messagebox.showwarning(title='警告', message='账号已存在')
            self.entry_text_1.set("")
            self.entry_text_2.set("")
            return False
        else:
            user_info[account] = get_md5(password)
            with open("user_info.json", "w") as f:
                json.dump(user_info, f)
            return True

    def goto_main_screen(self):
        if self.register():
            # 销毁注册界面，显示主界面
            self.master.destroy()
            # 创建主窗口并运行程序
            master = tk.Tk()
            app = MainScreen(master)
            master.mainloop()

    @staticmethod
    def relative_to_assets(path: str):
        assets_dir = ASSET_BASE_PATH + "frame2\\"
        full_path = os.path.join(assets_dir, path)
        return full_path
```

### 主页面

#### 主页面

主页面的设计实际上为各个功能的入口，在代码中实现了跳转到各个页面的功能。

```Python
class MainScreen:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do App")
        self.master.geometry("430x932")
        self.master.configure(bg="#FFFFFF")
        self.master.resizable(False, False)
        self.create_widgets()
        self.create_interactive_controls()

    def create_widgets(self):
        self.canvas = tk.Canvas(
            self.master,
            bg="#FFFFFF",
            height=932,
            width=430,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        global image_image_1
        image_image_1 = tk.PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(217.0, 466.0, image=image_image_1)

    def create_interactive_controls(self):
        global button_image_1, button_image_2, button_image_3, button_image_4

        button_image_1 = tk.PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = tk.Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.goto_today_page,
            relief="flat"
        )
        self.button_1.place(x=0.0, y=143.0, width=430.0, height=60.0)

        button_image_2 = tk.PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_2 = tk.Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.goto_important_page,
            relief="flat"
        )
        self.button_2.place(x=0.0, y=203.0, width=430.0, height=60.0)

        button_image_3 = tk.PhotoImage(file=self.relative_to_assets("button_3.png"))
        self.button_3 = tk.Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.goto_search_page,
            relief="flat"
        )
        self.button_3.place(x=0.0, y=263.0, width=430.0, height=60.0)

        button_image_4 = tk.PhotoImage(
            file=self.relative_to_assets("button_4.png"))
        self.button_4 = tk.Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.goto_trash_bin,
            relief="flat"
        )
        self.button_4.place(
            x=0.0,
            y=323.0,
            width=430.0,
            height=60.0
        )

    def goto_today_page(self):  # 跳转到Today界面 
        self.master.destroy()
        master = tk.Tk()
        app = TodayPage(master)
        master.mainloop()

    def goto_important_page(self):  # 跳转到Important界面
        self.master.destroy()
        master = tk.Tk()
        app = ImportantPage(master)
        master.mainloop()

    def goto_search_page(self):  # 跳转到Search界面
        self.master.destroy()
        master = tk.Tk()
        app = SearchPage(master)
        master.mainloop()

    def goto_trash_bin(self):  # 跳转到TrashBin界面
        self.master.destroy()
        master = tk.Tk()
        app = TrashBin(master)
        master.mainloop()

    @staticmethod
    def relative_to_assets(path: str):
        assets_dir = ASSET_BASE_PATH + "frame3\\"
        full_path = os.path.join(assets_dir, path)
        return full_path
```

#### Today页面和Important页面

实际上这两个页面只存在细微的差别，所以只拿其中的一个页面讲解。

```Python
class TodayPage:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do App")
        self.master.geometry("430x932")
        self.master.configure(bg="#FFFFFF")
        self.master.resizable(False, False)
        self.create_widgets()
        self.create_interactive_controls()
        self.init_listbox()
```

上面的代码是初始化页面的代码，调用了三个方法分别初始化了画布，可交互控件以及列表。三个方法是`create_widgets()`、`create_interactive_controls()`和`init_listbox()`。

```Python
    def create_widgets(self):
        # 创建画布
        self.canvas = tk.Canvas(self.master,
                                bg="#FFFFFF",
                                height=932,
                                width=430,
                                bd=0,
                                highlightthickness=0,
                                relief="ridge")
        self.canvas.place(x=0, y=0)
        # 添加背景
        self.image_image_1 = tk.PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(215.0, 466.0, image=self.image_image_1)

    def create_interactive_controls(self):
        global button_image_1, button_image_2, button_image_3, button_image_4, button_image_5
        # 创建按钮
        button_image_1 = tk.PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = tk.Button(image=button_image_1,
                                  borderwidth=0,
                                  highlightthickness=0,
                                  command=self.goto_main_screen,
                                  relief="flat")
        self.button_1.place(x=13.12060546875,
                            y=59.0,
                            width=57.87939453125,
                            height=20.0)

        button_image_2 = tk.PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_2 = tk.Button(image=button_image_2,
                                  borderwidth=0,
                                  highlightthickness=0,
                                  command=self.goto_today_add,
                                  relief="flat")
        self.button_2.place(x=378.0,
                            y=47.0,
                            width=44.0,
                            height=44.0)

        button_image_3 = tk.PhotoImage(file=self.relative_to_assets("button_3.png"))
        self.button_3 = tk.Button(image=button_image_3,
                                  borderwidth=0,
                                  highlightthickness=0,
                                  command=self.edit,
                                  relief="flat")
        self.button_3.place(x=325.0,
                            y=864.0,
                            width=48.0,
                            height=48.0)

        button_image_4 = tk.PhotoImage(file=self.relative_to_assets("button_4.png"))
        self.button_4 = tk.Button(image=button_image_4,
                                  borderwidth=0,
                                  highlightthickness=0,
                                  command=self.mark_done,
                                  relief="flat")
        self.button_4.place(x=69.0,
                            y=864.0,
                            width=48.0,
                            height=48.0)

        button_image_5 = tk.PhotoImage(file=self.relative_to_assets("button_5.png"))
        self.button_5 = tk.Button(image=button_image_5,
                                  borderwidth=0,
                                  highlightthickness=0,
                                  command=self.delete_item,
                                  relief="flat")
        self.button_5.place(x=197.0,
                            y=864.0,
                            width=48.0,
                            height=48.0)
        # 创建列表控件
        self.listbox = tk.Listbox(self.canvas,
                                  border=0,
                                  selectbackground="#b0b7c1",
                                  font=("Microsoft YaHei UI", 24),
                                  bg="#f5f5f5")
        self.listbox.place(x=0, y=143, width=430, height=720)
    # 初始化列表控件
    def init_listbox(self):
        result = []
        # 识别路径
        if os.getcwd().split('\\')[-1] != "tasks":
            base_dir = os.getcwd()
            os.chdir(os.getcwd() + "\\tasks\\")
        else:
            base_dir = os.path.abspath(os.path.dirname(os.getcwd()))
        all_tasks = []
        # 读取所有任务 -> Task()的实例
        for data in os.listdir(os.getcwd()):
            with open(data, "rb") as f:
                obj = pickle.load(f)
                # print(f"loading {obj.get_info()}")
                all_tasks.append(obj)
        os.chdir(base_dir)
        for task in all_tasks:
            info = task.get_info()
            # 检测实例的task属性
            if info["label"] == "today":
                result.append(task)
        for i in result:
            # print(i.get_info())
            # 插入到列表
            self.listbox.insert('end', i.content)
```

上述的代码是页面初始化的具体实现。

接下来的代码会介绍对列表项的各项操作，包含以下几点：

- 删除任务
- 标记任务为完成
- 编辑任务

```Python
    def delete_item(self):
        curselection = self.listbox.curselection()
        # 获取当前选中选项
        if curselection:
            index = curselection[0]  # 获取选中项索引
            content = self.listbox.get(index)  # 获取选中项内容
            if os.getcwd().split('\\')[-1] != "tasks":
                base_dir = os.getcwd()
                os.chdir(os.getcwd() + "\\tasks\\")
            else:
                base_dir = os.path.abspath(os.path.dirname(os.getcwd()))
            for data in os.listdir(os.getcwd()):
                with open(data, "rb") as f:
                    obj = pickle.load(f)
                    if obj.content == content:
                        data_path = data
                        selection = obj
            if selection.get_label() == "today":  # 修改标签
                selection.set_label("today_deleted")
            if selection.get_label() == "important":
                selection.set_label("important_deleted")
            # print(data_path)
            # os.remove(data_path)
            # 存储修改完的对象
            with open(data_path, "wb") as f:
                pickle.dump(selection, f)
            os.chdir(base_dir)
            self.listbox.delete(index)
            
    def mark_done(self):
    curselection = self.listbox.curselection()
    # 获取当前选中选项
    if curselection:
        index = curselection[0]  # 获取选中项索引
        content = self.listbox.get(index) # 获取选中项内容
        if os.getcwd().split('\\')[-1] != "tasks":
            base_dir = os.getcwd()
            os.chdir(os.getcwd() + "\\tasks\\")
        else:
            base_dir = os.path.abspath(os.path.dirname(os.getcwd()))
        for data in os.listdir(os.getcwd()):
            with open(data, "rb") as f:
                obj = pickle.load(f)
                if obj.content == content:
                    data_path = data
                    selection = obj
        # 修改标签
        selection.set_status("done")
        # print(data_path)
        # os.remove(data_path)
        # 存储修改完的对象
        with open(data_path, "wb") as f:
            pickle.dump(selection, f)
        os.chdir(base_dir)
        

    def edit(self):
        curselection = self.listbox.curselection() # 获取当前选中选项
        if curselection:
            index = curselection[0]   # 获取选中项索引
            content = self.listbox.get(index)  # 获取选中项内容
            # print(content)
            if os.getcwd().split('\\')[-1] != "tasks":
                base_dir = os.getcwd()
                os.chdir(os.getcwd() + "\\tasks\\")
            else:
                base_dir = os.path.abspath(os.path.dirname(os.getcwd()))
            for data in os.listdir(os.getcwd()):
                with open(data, "rb") as f:
                    obj = pickle.load(f)
                    # print(f"obj.content : {obj.content}")
                    if obj.content == content:
                        info = obj.get_info()  # 获取对象数据
                        file_name = data
                        break
            self.master.destroy()
            # 创建主窗口并运行程序
            master = tk.Tk()
            app = TodayEdit(master, base_dir, file_name, info)  # 将对象数据传入编辑页面 
            master.mainloop()

    def goto_main_screen(self):
        # 销毁界面，显示主界面
        self.master.destroy()
        # 创建主窗口并运行程序
        master = tk.Tk()
        app = MainScreen(master)
        master.mainloop()

    def goto_today_add(self):
        # 销毁界面，显示今天界面
        self.master.destroy()
        # 创建主窗口并运行程序
        master = tk.Tk()
        app = TodayAdd(master)
        master.mainloop()

    @staticmethod
    def relative_to_assets(path: str):
        assets_dir = ASSET_BASE_PATH + "frame4\\"
        full_path = os.path.join(assets_dir, path)
        return full_path
```

### 任务处理模块（Add, Edit)

#### Add模块

```Python
class TodayAdd:
    def __init__(self, master, info=None):
        self.task = task.Task()
        self.info = info
        self.master = master
        self.master.title("To-Do App")
        self.master.geometry("430x932")
        self.master.configure(bg="#FFFFFF")
        self.master.resizable(False, False)
        self.create_widgets()
        self.create_interactive_controls()
    # 创建组件
    def create_widgets(self):
        self.canvas = tk.Canvas(
            self.master,
            bg="#FFFFFF",
            height=932,
            width=430,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        global image_image_1
        image_image_1 = tk.PhotoImage(file=self.relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(215.0, 466.0, image=image_image_1)
    # 创建交互式组件
    def create_interactive_controls(self):
        global button_image_1, button_image_2, button_image_3, button_image_4, \
            button_image_5, button_image_6, button_image_7, button_image_8, \
            button_image_3_selected, button_image_4_selected, \
            button_image_5_selected, button_image_6_selected, \
            button_image_7_selected, button_image_8_selected, \
            entry_image_1, entry_image_2, entry_image_3

        button_image_1 = tk.PhotoImage(file=self.relative_to_assets("button_1.png"))
        button_1 = tk.Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.goto_today_page,
            relief="flat"
        )

        button_1.place(
            x=8.368408203125,
            y=57.5,
            width=64.631591796875,
            height=20.844512939453125
        )

        button_image_2 = tk.PhotoImage(file=self.relative_to_assets("button_2.png"))
        button_2 = tk.Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.add_task,
            relief="flat"
        )

        button_2.place(
            x=370.0,
            y=59.0,
            width=50.0,
            height=20.0
        )

        button_image_3 = tk.PhotoImage(file=self.relative_to_assets("button_3.png"))
        self.button_3 = tk.Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.set_priority("unimportant"),
            relief="flat"
        )

        self.button_3.place(
            x=336.218017578125,
            y=210.0,
            width=82.807373046875,
            height=28.0
        )

        button_image_4 = tk.PhotoImage(file=self.relative_to_assets("button_4_selected.png"))
        self.button_4 = tk.Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.set_priority("normal"),
            relief="flat"
        )

        self.button_4.place(
            x=222.19189453125,
            y=210.0,
            width=100.349609375,
            height=28.0
        )

        button_image_5 = tk.PhotoImage(file=self.relative_to_assets("button_5.png"))
        self.button_5 = tk.Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.set_priority("urgent"),
            relief="flat"
        )
        self.button_5.place(
            x=124.7099609375,
            y=210.0,
            width=85.800537109375,
            height=28.0
        )

        button_image_6 = tk.PhotoImage(file=self.relative_to_assets("button_6.png"))
        self.button_6 = tk.Button(
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.set_status("done"),
            relief="flat"
        )

        self.button_6.place(
            x=336.0,
            y=254.0,
            width=82.807373046875,
            height=28.0
        )

        button_image_7 = tk.PhotoImage(file=self.relative_to_assets("button_7.png"))
        self.button_7 = tk.Button(
            image=button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.set_status("processing"),
            relief="flat"
        )

        self.button_7.place(
            x=231.0,
            y=254.0,
            width=82.807373046875,
            height=28.0
        )

        button_image_8 = tk.PhotoImage(file=self.relative_to_assets("button_8_selected.png"))
        self.button_8 = tk.Button(
            image=button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.set_status("has not started"),
            relief="flat"
        )

        self.button_8.place(
            x=128.0,
            y=254.0,
            width=82.807373046875,
            height=28.0
        )

        self.entry_1_text = tk.StringVar()
        self.entry_2_text = tk.StringVar()
        self.entry_3_text = tk.StringVar()

        entry_image_1 = tk.PhotoImage(file=self.relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(272.0, 311.0, image=entry_image_1)
        self.entry_1 = tk.Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            textvariable=self.entry_1_text
        )

        self.entry_1.place(x=117.0, y=296.0, width=310.0, height=28.0)

        entry_image_2 = tk.PhotoImage(file=self.relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(272.0, 179.0, image=entry_image_2)
        self.entry_2 = tk.Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            textvariable=self.entry_2_text
        )

        self.entry_2.place(x=117.0, y=164.0, width=310.0, height=28.0)

        entry_image_3 = tk.PhotoImage(file=self.relative_to_assets("entry_3.png"))
        entry_bg_3 = self.canvas.create_image(272.0, 135.0, image=entry_image_3)
        self.entry_3 = tk.Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            textvariable=self.entry_3_text
        )

        self.entry_3.place(x=117.0, y=120.0, width=310.0, height=28.0)
        # 对传入的info信息进行应用
        if self.info is not None:
            self.entry_1_text.set(self.info['deadline'])
            self.entry_2_text.set(self.info['description'])
            self.entry_3_text.set(self.info['content'])
            self.set_priority(self.info["priority"])
            self.set_status(self.info["status"])
    # 优先级按钮集的实现
    def set_priority(self, priority):
        global button_5_image, button_4_image, button_3_image
        self.task.set_priority(priority)
        if priority == "urgent":
            button_5_image = tk.PhotoImage(file=self.relative_to_assets("button_5_selected.png"))
            button_4_image = tk.PhotoImage(file=self.relative_to_assets("button_4.png"))
            button_3_image = tk.PhotoImage(file=self.relative_to_assets("button_3.png"))
        elif priority == "normal":
            button_5_image = tk.PhotoImage(file=self.relative_to_assets("button_5.png"))
            button_4_image = tk.PhotoImage(file=self.relative_to_assets("button_4_selected.png"))
            button_3_image = tk.PhotoImage(file=self.relative_to_assets("button_3.png"))
        elif priority == "unimportant":
            button_5_image = tk.PhotoImage(file=self.relative_to_assets("button_5.png"))
            button_4_image = tk.PhotoImage(file=self.relative_to_assets("button_4.png"))
            button_3_image = tk.PhotoImage(file=self.relative_to_assets("button_3_selected.png"))
        self.button_3.configure(image=button_3_image)
        self.button_4.configure(image=button_4_image)
        self.button_5.configure(image=button_5_image)
    # 状态按钮集的实现
    def set_status(self, status):
        global button_6_image, button_7_image, button_8_image
        self.task.set_status(status)
        if status == "done":
            button_6_image = tk.PhotoImage(file=self.relative_to_assets("button_6_selected.png"))
            button_7_image = tk.PhotoImage(file=self.relative_to_assets("button_7.png"))
            button_8_image = tk.PhotoImage(file=self.relative_to_assets("button_8.png"))
        elif status == "processing":
            button_6_image = tk.PhotoImage(file=self.relative_to_assets("button_6.png"))
            button_7_image = tk.PhotoImage(file=self.relative_to_assets("button_7_selected.png"))
            button_8_image = tk.PhotoImage(file=self.relative_to_assets("button_8.png"))
        elif status == "has not started":
            button_6_image = tk.PhotoImage(file=self.relative_to_assets("button_6.png"))
            button_7_image = tk.PhotoImage(file=self.relative_to_assets("button_7.png"))
            button_8_image = tk.PhotoImage(file=self.relative_to_assets("button_8_selected.png"))
        self.button_6.configure(image=button_6_image)
        self.button_7.configure(image=button_7_image)
        self.button_8.configure(image=button_8_image)
    # 创建task对象的代码
    def add_task(self):
        # 获取输入框内容，然后传入到对象中
        # print("deadline:", self.entry_1.get(), "description：", self.entry_2.get(), "content:", self.entry_3.get())
        self.task.set_deadline(self.entry_1.get())
        self.task.set_description(self.entry_2.get())
        self.task.set_content(self.entry_3.get())
        self.task.set_label("today")
        # 获取当前路径
        base_dir = os.getcwd()
        # 判断并跳转到tasks目录，存储对象
        if "tasks" not in os.listdir(os.getcwd()):
            os.makedirs("tasks")
        os.chdir(os.getcwd() + "\\tasks\\")
        now = datetime.datetime.now() # 获取时间
        formatted_time = now.strftime("%Y-%m-%d_%H-%M-%S")
        # 以创建时间命名数据文件
        with open(f"task_{formatted_time}.dat", "wb") as f:
            # print(f"saving {self.task.get_info()}")
            pickle.dump(self.task, f)
        os.chdir(base_dir)
        # 跳转回today页面
        self.goto_today_page()

    def goto_today_page(self):
        # 销毁当前界面，显示Today界面
        self.master.destroy()
        # 创建主窗口并运行程序
        master = tk.Tk()
        app = TodayPage(master)
        master.mainloop()

    @staticmethod
    def relative_to_assets(path: str):
        assets_dir = ASSET_BASE_PATH + "frame5\\"
        full_path = os.path.join(assets_dir, path)
        return full_path
```

#### Edit模块

Edit模块实际上是在Add模块上加以修改而成的。只要在进入Edit模块的时候传入任务对象的各个参数，字典传入到Edit以后把属性赋值给一个新的空对象，从而实现编辑任务的功能。不同之处在于定义了一个新的`edit_task()`方法实现任务的编辑。具体代码如下：

```Python
def edit_task(self):
    # print("deadline:",self.entry_1.get(), "description：",self.entry_2.get(),"content:",self.entry_3.get())
    self.task.set_deadline(self.entry_1.get())
    self.task.set_description(self.entry_2.get())
    self.task.set_content(self.entry_3.get())
    self.task.set_label("today")
    # print(self.task.get_info())
    os.remove(self.filename)
    now = datetime.datetime.now()
    formatted_time = now.strftime("%Y-%m-%d_%H-%M-%S")
    with open(self.filename, "wb") as f:
        # print(f"saving {self.task.get_info()}")
        pickle.dump(self.task, f)
    os.chdir(self.base_dir)
    self.goto_today_page()
```

### 搜索模块

搜索模块实现了对所有任务的内容和描述的关键词搜索。通过以下的`search()`函数实现。以下是`search()`函数的具体实现。

```python
    def search(self):
        # 清空搜索框
        self.listbox.delete(0, tk.END)
        kw = self.entry_1.get()  # 获取搜索关键词
        result = []
        if os.getcwd().split('\\')[-1] != "tasks":
            base_dir = os.getcwd()
            os.chdir(os.getcwd() + "\\tasks\\")
        else:
            base_dir = os.path.abspath(os.path.dirname(os.getcwd()))
        all_tasks = []  # 定义列表用于存储对象
        # 遍历数据文件
        for data in os.listdir(os.getcwd()):
            with open(data, "rb") as f:
                obj = pickle.load(f)
                all_tasks.append(obj)
       	# 遍历所有对象实现搜索
        for task in all_tasks:
            info = task.get_data()
            for information in info:
                if information.find(kw) != -1:
                    result.append(task)
                    break
        print(f"result:{result}")
        # 将结果写入到listbox中
        for item in result:
            self.listbox.insert('end', item.content + " " + item.description)
        os.chdir(base_dir)  # 切换工作目录
```

### 回收站模块

有的时候会出现误删的情况，所以我们设计了回收站的模块。在删除任务的时候实际上数据文件并没有被删除，而是打上了已删除的标签。而当我们打开回收站的时候，这些标记已删除的任务就会显示出来。对于这些任务我们提供了两个选项，分别为彻底删除以及还原，在代码中使用的是`remove()`和`restore()`这两个函数实现。以下是这两个函数的实现代码。

```python
    def restore(self):
        # 获取选中项
        curselection = self.listbox.curselection()
        if curselection:
            index = curselection[0]
            content = self.listbox.get(index)
            if os.getcwd().split('\\')[-1] != "tasks":
                base_dir = os.getcwd()
                os.chdir(os.getcwd() + "\\tasks\\")
            else:
                base_dir = os.path.abspath(os.path.dirname(os.getcwd()))
            # 读取数据
            for data in os.listdir(os.getcwd()):
                with open(data, "rb") as f:
                    obj = pickle.load(f)
                    if obj.content == content:
                        data_path = data
                        selection = obj
            # 更改标签，实现数据恢复
            if selection.get_label() == "today_deleted":
                selection.set_label("today")
            if selection.get_label() == "important_deleted":
                selection.set_label("important")
            # print(data_path)
            # os.remove(data_path)
            # 将新的数据存入文件中
            with open(data_path, "wb") as f:
                pickle.dump(selection, f)
            os.chdir(base_dir)
            # 在列表中删除这一项
            self.listbox.delete(index)

    def remove(self):
        # 获取选中项
        curselection = self.listbox.curselection()
        if curselection:
            index = curselection[0]  # 获取索引
            content = self.listbox.get(index)
            if os.getcwd().split('\\')[-1] != "tasks":
                base_dir = os.getcwd()
                os.chdir(os.getcwd() + "\\tasks\\")
            else:
                base_dir = os.path.abspath(os.path.dirname(os.getcwd()))
            # 匹配对象
            for data in os.listdir(os.getcwd()):
                with open(data, "rb") as f:
                    obj = pickle.load(f)
                    if obj.content == content:
                        data_path = data
                        selection = obj
            # 删除数据文件            
            os.remove(data_path)
            os.chdir(base_dir)
            # 在列表中删除这一项
            self.listbox.delete(index)
```

