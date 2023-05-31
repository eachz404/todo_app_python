import datetime
import hashlib
import json
import os
import pickle
import tkinter as tk
import tkinter.messagebox

import task

# ASSET_BASE_PATH = "D:\\Code\\To-Do App\\assets\\"
ASSET_BASE_PATH = os.path.dirname(os.path.abspath(__file__)) + "\\assets\\"

global current_user_id

class WelcomeScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do App")
        # 设置窗口大小不可调整
        self.root.resizable(False, False)
        self.create_widgets()
        self.create_interactive_controls()

    def create_widgets(self):
        # 设置窗口大小和背景色
        self.root.geometry("430x932+0+0")
        self.root.configure(bg="#FFFFFF")

        # 创建Canvas控件
        self.canvas = tk.Canvas(
            self.root,
            bg="#FFFFFF",
            height=932,
            width=430,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        global image_image_1
        # 加载图片并创建Image控件
        image_image_1 = tk.PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(215.0, 466.0, image=image_image_1)

    def create_interactive_controls(self):
        global button_image_1, button_image_2
        button_image_1 = tk.PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = tk.Button(
            self.root,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.goto_register_screen,
            relief="flat"
        )
        self.button_1.place(x=237.0, y=827.0, width=150.0, height=60.0)

        button_image_2 = tk.PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_2 = tk.Button(
            self.root,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.goto_login_screen,
            relief="flat"
        )
        self.button_2.place(x=43.0, y=827.0, width=152.0, height=60.0)

    def goto_login_screen(self):
        # 销毁欢迎界面，显示登陆界面
        self.root.destroy()
        root = tk.Tk()
        app = LoginScreen(root)
        root.mainloop()

    def goto_register_screen(self):
        self.root.destroy()
        root = tk.Tk()
        app = RegisterScreen(root)
        root.mainloop()

    @staticmethod
    def relative_to_assets(path: str):
        assets_dir = ASSET_BASE_PATH + "frame0\\"
        full_path = os.path.join(assets_dir, path)
        return full_path


class LoginScreen:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do App")
        self.master.geometry("430x932+0+0")
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
        global image_image_1, entry_image_1
        image_image_1 = tk.PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(215.0, 466.0, image=image_image_1)

    def create_interactive_controls(self):
        global entry_image_2, button_image_1, button_image_2

        self.entry_1_text = tk.StringVar()
        entry_image_1 = tk.PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(265.5, 199.0, image=entry_image_1)
        self.entry_1 = tk.Entry(bd=0,
                                bg="#FFFFFF",
                                fg="#000716",
                                highlightthickness=0,
                                textvariable=self.entry_1_text)
        self.entry_1.place(x=110.0, y=185.0, width=311.0, height=26.0)

        self.entry_2_text = tk.StringVar()
        entry_image_2 = tk.PhotoImage(file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(265.5, 241.0, image=entry_image_2)
        self.entry_2 = tk.Entry(bd=0,
                                bg="#FFFFFF",
                                fg="#000716",
                                highlightthickness=0,
                                show="*",
                                textvariable=self.entry_2_text)
        self.entry_2.place(x=110.0, y=227.0, width=311.0, height=26.0)
        self.entry_2.bind("<Return>", self.call_login)

        button_image_1 = tk.PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = tk.Button(image=button_image_1,
                                  borderwidth=0,
                                  highlightthickness=0,
                                  command=self.goto_main_screen,
                                  relief="flat")
        self.button_1.place(x=371.0, y=59.0, width=47.0, height=20.0)

        button_image_2 = tk.PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_2 = tk.Button(image=button_image_2,
                                  borderwidth=0,
                                  highlightthickness=0,
                                  command=self.goto_welcome_screen,
                                  relief="flat")
        self.button_2.place(x=13.120635986328125, y=59.0, width=82.87936401367188, height=20.0)

    def call_login(self, arg):
        # print(arg)
        self.goto_main_screen()

    def login(self):  # TODO: 增加密码强度验证功能
        account = self.entry_1.get().rstrip()
        password = self.entry_2.get()
        with open("user_info.json", "r") as f:
            user_info = json.load(f)
        if account in user_info:
            if user_info[account] == get_md5(password):
                global current_user_id
                current_user_id = account
                return True
            else:
                tk.messagebox.showwarning(title='警告', message='密码错误')
                self.entry_1_text.set("")
                self.entry_2_text.set("")
                return False
        else:
            tk.messagebox.showwarning(title='警告', message='账号不存在')
            self.entry_1_text.set("")
            self.entry_2_text.set("")
            return False

    def goto_welcome_screen(self):
        # 销毁登陆界面，显示欢迎界面
        self.master.destroy()
        # 创建主窗口并运行程序
        master = tk.Tk()
        app = WelcomeScreen(master)
        master.mainloop()

    def goto_main_screen(self):
        if self.login():
            # 销毁登陆界面，显示主界面
            self.master.destroy()
            # 创建主窗口并运行程序
            master = tk.Tk()
            app = MainScreen(master)
            master.mainloop()

    @staticmethod
    def relative_to_assets(path: str):
        assets_dir = ASSET_BASE_PATH + "frame1\\"
        full_path = os.path.join(assets_dir, path)
        return full_path


class RegisterScreen:
    def __init__(self, master):
        self.master = master
        self.master.geometry("430x932+0+0")
        self.master.configure(bg="#FFFFFF")
        self.master.title("To-Do App")
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
        self.image_1 = self.canvas.create_image(215.0, 466.0, image=image_image_1)

    def create_interactive_controls(self):
        global entry_image_1, entry_image_2, button_image_1, button_image_2

        self.entry_text_1 = tk.StringVar()
        entry_image_1 = tk.PhotoImage(file=self.relative_to_assets("entry_1.png"))
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
        self.entry_2.bind("<Return>", self.call_register)

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

    def call_register(self, arg):
        self.goto_main_screen()

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
            global current_user_id
            current_user_id = account
            if os.getcwd().split('\\')[-1] != "tasks":
                base_dir = os.getcwd()
                os.chdir(os.getcwd() + "\\tasks\\")
                os.makedirs(account)
                os.chdir(base_dir)
                print(base_dir)
            else:
                base_dir = os.path.abspath(os.path.dirname(os.getcwd()))
            with open("user_info.json", "w") as f:
                json.dump(user_info, f)
            return True

    def goto_welcome_screen(self):
        # 销毁注册界面，显示欢迎界面
        self.master.destroy()
        # 创建主窗口并运行程序
        master = tk.Tk()
        app = WelcomeScreen(master)
        master.mainloop()

    def goto_main_screen(self):
        if self.register():
            # 销毁登陆界面，显示主界面
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


class MainScreen:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do App")
        self.master.geometry("430x932+0+0")
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

    def create_interactive_controls(self):  # TODO: 增加“我的”界面
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

    def goto_today_page(self):
        # 销毁登陆界面，显示主界面
        self.master.destroy()
        # 创建主窗口并运行程序
        master = tk.Tk()
        app = TodayPage(master)
        master.mainloop()

    def goto_important_page(self):
        self.master.destroy()
        master = tk.Tk()
        app = ImportantPage(master)
        master.mainloop()

    def goto_search_page(self):
        self.master.destroy()
        master = tk.Tk()
        app = SearchPage(master)
        master.mainloop()

    def goto_trash_bin(self):
        self.master.destroy()
        master = tk.Tk()
        app = TrashBin(master)
        master.mainloop()

    @staticmethod
    def relative_to_assets(path: str):
        assets_dir = ASSET_BASE_PATH + "frame3\\"
        full_path = os.path.join(assets_dir, path)
        return full_path


class TodayPage:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do App")
        self.master.geometry("430x932+0+0")
        self.master.configure(bg="#FFFFFF")
        self.master.resizable(False, False)
        self.create_widgets()
        self.create_interactive_controls()
        self.init_listbox()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.master,
                                bg="#FFFFFF",
                                height=932,
                                width=430,
                                bd=0,
                                highlightthickness=0,
                                relief="ridge")
        self.canvas.place(x=0, y=0)

        self.image_image_1 = tk.PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(215.0, 466.0, image=self.image_image_1)

    def create_interactive_controls(self):
        global button_image_1, button_image_2, button_image_3, button_image_4, button_image_5

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
                                  command=self.delete_item,
                                  relief="flat")
        self.button_4.place(x=69.0,
                            y=864.0,
                            width=48.0,
                            height=48.0)

        button_image_5 = tk.PhotoImage(file=self.relative_to_assets("button_5.png"))
        self.button_5 = tk.Button(image=button_image_5,
                                  borderwidth=0,
                                  highlightthickness=0,
                                  command=self.mark_done,
                                  relief="flat")
        self.button_5.place(x=197.0,
                            y=864.0,
                            width=48.0,
                            height=48.0)

        self.listbox = tk.Listbox(self.canvas,
                                  border=0,
                                  selectbackground="#b0b7c1",
                                  font=("Microsoft YaHei UI", 24),
                                  bg="#f5f5f5")
        self.listbox.place(x=0, y=143, width=430, height=720)

    def init_listbox(self):
        result = []
        if os.getcwd().split('\\')[-1] != "tasks":
            base_dir = os.getcwd()
            os.chdir(os.getcwd() + "\\tasks\\" + current_user_id + "\\")
        else:
            base_dir = os.path.abspath(os.path.dirname(os.getcwd()))
        all_tasks = []

        for data in os.listdir(os.getcwd()):
            with open(data, "rb") as f:
                obj = pickle.load(f)
                print(f"loading {obj.get_info()}")
                all_tasks.append(obj)
        os.chdir(base_dir)
        for task in all_tasks:
            info = task.get_info()
            if info["label"] == "today" and info["status"] != "done":
                result.append(task)
        for i in result:
            # print(i.get_info())
            self.listbox.insert('end', i.content)

    def delete_item(self):
        curselection = self.listbox.curselection()
        if curselection:
            index = curselection[0]
            content = self.listbox.get(index)
            if os.getcwd().split('\\')[-1] != "tasks":
                base_dir = os.getcwd()
                os.chdir(os.getcwd() + "\\tasks\\" + current_user_id + "\\")
            else:
                base_dir = os.path.abspath(os.path.dirname(os.getcwd()))
            for data in os.listdir(os.getcwd()):
                with open(data, "rb") as f:
                    obj = pickle.load(f)
                    if obj.content == content:
                        data_path = data
                        selection = obj
            if selection.get_label() == "today":
                selection.set_label("today_deleted")
            if selection.get_label() == "important":
                selection.set_label("important_deleted")
            # print(data_path)
            # os.remove(data_path)
            with open(data_path, "wb") as f:
                pickle.dump(selection, f)
            os.chdir(base_dir)
            self.listbox.delete(index)

    def mark_done(self):
        curselection = self.listbox.curselection()
        if curselection:
            index = curselection[0]
            content = self.listbox.get(index)
            if os.getcwd().split('\\')[-1] != "tasks":
                base_dir = os.getcwd()
                os.chdir(os.getcwd() + "\\tasks\\" + current_user_id + "\\")
            else:
                base_dir = os.path.abspath(os.path.dirname(os.getcwd()))
            for data in os.listdir(os.getcwd()):
                with open(data, "rb") as f:
                    obj = pickle.load(f)
                    if obj.content == content:
                        data_path = data
                        selection = obj
            selection.set_status("done")
            # print(data_path)
            # os.remove(data_path)
            with open(data_path, "wb") as f:
                pickle.dump(selection, f)
            os.chdir(base_dir)
            self.listbox.delete(index)

    def edit(self):
        curselection = self.listbox.curselection()
        if curselection:
            index = curselection[0]
            content = self.listbox.get(index)
            # print(content)
            if os.getcwd().split('\\')[-1] != "tasks":
                base_dir = os.getcwd()
                os.chdir(os.getcwd() + "\\tasks\\" + current_user_id + "\\")
            else:
                base_dir = os.path.abspath(os.path.dirname(os.getcwd()))
            for data in os.listdir(os.getcwd()):
                with open(data, "rb") as f:
                    obj = pickle.load(f)
                    # print(f"obj.content : {obj.content}")
                    if obj.content == content:
                        info = obj.get_info()
                        file_name = data
                        break
            self.master.destroy()
            # 创建主窗口并运行程序
            master = tk.Tk()
            app = TodayEdit(master, base_dir, file_name, info)
            master.mainloop()

    def goto_main_screen(self):
        # 销毁登陆界面，显示主界面
        self.master.destroy()
        # 创建主窗口并运行程序
        master = tk.Tk()
        app = MainScreen(master)
        master.mainloop()

    def goto_today_add(self):
        # 销毁登陆界面，显示主界面
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


class TodayAdd:
    def __init__(self, master, info=None):
        self.task = task.Task()
        self.info = info
        self.master = master
        self.master.title("To-Do App")
        self.master.geometry("430x932+0+0")
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
        image_1 = self.canvas.create_image(215.0, 466.0, image=image_image_1)

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

        if self.info is not None:
            self.entry_1_text.set(self.info['deadline'])
            self.entry_2_text.set(self.info['description'])
            self.entry_3_text.set(self.info['content'])
            self.set_priority(self.info["priority"])
            self.set_status(self.info["status"])

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

    def add_task(self):
        # print("deadline:", self.entry_1.get(), "description：", self.entry_2.get(), "content:", self.entry_3.get())
        self.task.set_deadline(self.entry_1.get())
        self.task.set_description(self.entry_2.get())
        self.task.set_content(self.entry_3.get())
        self.task.set_label("today")
        base_dir = os.getcwd()

        if "tasks" not in os.listdir(os.getcwd()):
            os.makedirs("tasks")
        os.chdir(os.getcwd() + "\\tasks\\" + current_user_id + "\\")
        now = datetime.datetime.now()
        formatted_time = now.strftime("%Y-%m-%d_%H-%M-%S")
        with open(f"task_{formatted_time}.dat", "wb") as f:
            # print(f"saving {self.task.get_info()}")
            pickle.dump(self.task, f)
        os.chdir(base_dir)
        self.goto_today_page()

    def goto_today_page(self):
        # 销毁登陆界面，显示主界面
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


class TodayEdit:
    def __init__(self, master, base_dir, filename, info=None):
        self.base_dir = base_dir
        self.filename = filename
        self.info = info
        self.task = task.Task()
        self.master = master
        self.master.title("To-Do App")
        self.master.geometry("430x932+0+0")
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
        image_1 = self.canvas.create_image(215.0, 466.0, image=image_image_1)

    def create_interactive_controls(self):
        global button_image_1, button_image_2, button_image_3, button_image_4, \
            button_image_5, button_image_6, button_image_7, button_image_8, \
            button_image_3_selected, button_image_4_selected, \
            button_image_5_selected, button_image_6_selected, \
            button_image_7_selected, button_image_8_selected, \
            entry_image_1, entry_image_2, entry_image_3

        button_image_1 = tk.PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = tk.Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.goto_today_page,
            relief="flat"
        )

        self.button_1.place(
            x=8.368408203125,
            y=57.5,
            width=64.631591796875,
            height=20.844512939453125
        )

        button_image_2 = tk.PhotoImage(file=self.relative_to_assets("EditButton.png"))
        self.button_2 = tk.Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.edit_task,
            relief="flat"
        )

        self.button_2.place(
            x=370.0,
            y=59.0,
            width=50.0,
            height=20.0
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

        if self.info is not None:
            # print(f"editing {info}")
            self.entry_1_text.set(self.info['deadline'])
            self.entry_2_text.set(self.info['description'])
            self.entry_3_text.set(self.info['content'])
            self.set_priority(self.info["priority"])
            self.set_status(self.info["status"])

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

    def goto_today_page(self):
        # 销毁登陆界面，显示主界面
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


class ImportantPage:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do App")
        self.master.geometry("430x932+0+0")
        self.master.configure(bg="#FFFFFF")
        self.create_widgets()
        self.create_interactive_controls()
        self.init_listbox()

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

        image_image_1 = tk.PhotoImage(
            file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            215.0,
            466.0,
            image=image_image_1
        )

    def create_interactive_controls(self):
        global button_image_1, button_image_2, button_image_3, button_image_4, button_image_5

        button_image_1 = tk.PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        self.button_1 = tk.Button(
            self.master,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.goto_main_screen,
            relief="flat"
        )
        self.button_1.place(
            x=13.12060546875,
            y=59.0,
            width=57.87939453125,
            height=20.0
        )

        button_image_2 = tk.PhotoImage(
            file=self.relative_to_assets("button_2.png"))
        self.button_2 = tk.Button(
            self.master,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.goto_important_add,
            relief="flat"
        )
        self.button_2.place(
            x=378.0,
            y=47.0,
            width=44.0,
            height=44.0
        )
        button_image_3 = tk.PhotoImage(file=self.relative_to_assets("button_3.png"))
        self.button_3 = tk.Button(image=button_image_3, borderwidth=0, highlightthickness=0,
                                  command=self.edit, relief="flat")
        self.button_3.place(x=325.0, y=864.0, width=48.0, height=48.0)

        button_image_4 = tk.PhotoImage(file=self.relative_to_assets("button_4.png"))
        self.button_4 = tk.Button(image=button_image_4, borderwidth=0, highlightthickness=0,
                                  command=self.delete_item, relief="flat")
        self.button_4.place(x=69.0, y=864.0, width=48.0, height=48.0)

        self.button_image_5 = tk.PhotoImage(file=self.relative_to_assets("button_5.png"))
        self.button_5 = tk.Button(image=self.button_image_5, borderwidth=0, highlightthickness=0,
                                  command=self.mark_done, relief="flat")
        self.button_5.place(x=197.0, y=864.0, width=48.0, height=48.0)

        self.master.resizable(False, False)

        self.listbox = tk.Listbox(self.canvas,
                                  border=0,
                                  selectbackground="#b0b7c1",
                                  font=("Microsoft YaHei UI", 24),
                                  bg="#f5f5f5")
        self.listbox.place(x=0, y=143, width=430, height=720)

    def init_listbox(self):
        result = []
        if os.getcwd().split('\\')[-1] != "tasks":
            base_dir = os.getcwd()
            os.chdir(os.getcwd() + "\\tasks\\" + current_user_id + "\\")
        else:
            base_dir = os.path.abspath(os.path.dirname(os.getcwd()))
        all_tasks = []
        for data in os.listdir(os.getcwd()):
            with open(data, "rb") as f:
                obj = pickle.load(f)
                # print(f"loading {obj.get_info()}")
                all_tasks.append(obj)
        os.chdir(base_dir)
        for task in all_tasks:
            info = task.get_info()
            if info["label"] == "important" and info["status"] != "done":
                result.append(task)
        for i in result:
            self.listbox.insert('end', i.content)

    def delete_item(self):
        curselection = self.listbox.curselection()
        if curselection:
            index = curselection[0]
            content = self.listbox.get(index)
            if os.getcwd().split('\\')[-1] != "tasks":
                base_dir = os.getcwd()
                os.chdir(os.getcwd() + "\\tasks\\" + current_user_id + "\\")
            else:
                base_dir = os.path.abspath(os.path.dirname(os.getcwd()))
            for data in os.listdir(os.getcwd()):
                with open(data, "rb") as f:
                    obj = pickle.load(f)
                    if obj.content == content:
                        data_path = data
                        selection = obj
            if selection.get_label() == "today":
                selection.set_label("today_deleted")
            if selection.get_label() == "important":
                selection.set_label("important_deleted")
            # print(data_path)
            # os.remove(data_path)
            with open(data_path, "wb") as f:
                pickle.dump(selection, f)
            os.chdir(base_dir)
            self.listbox.delete(index)

    def mark_done(self):
        curselection = self.listbox.curselection()
        if curselection:
            index = curselection[0]
            content = self.listbox.get(index)
            if os.getcwd().split('\\')[-1] != "tasks":
                base_dir = os.getcwd()
                os.chdir(os.getcwd() + "\\tasks\\" + current_user_id + "\\")
            else:
                base_dir = os.path.abspath(os.path.dirname(os.getcwd()))
            for data in os.listdir(os.getcwd()):
                with open(data, "rb") as f:
                    obj = pickle.load(f)
                    if obj.content == content:
                        data_path = data
                        selection = obj
            selection.set_status("done")
            # print(data_path)
            # os.remove(data_path)
            with open(data_path, "wb") as f:
                pickle.dump(selection, f)
            os.chdir(base_dir)
            self.listbox.delete(index)

    def edit(self):
        curselection = self.listbox.curselection()
        if curselection:
            index = curselection[0]
            content = self.listbox.get(index)
            # print(content)
            if os.getcwd().split('\\')[-1] != "tasks":
                base_dir = os.getcwd()
                os.chdir(os.getcwd() + "\\tasks\\" + current_user_id + "\\")
            else:
                base_dir = os.path.abspath(os.path.dirname(os.getcwd()))
            for data in os.listdir(os.getcwd()):
                with open(data, "rb") as f:
                    obj = pickle.load(f)
                    # print(f"obj.content : {obj.content}")
                    if obj.content == content:
                        info = obj.get_info()
                        file_name = data
                        break
            # 销毁登陆界面，显示主界面
            self.master.destroy()
            # 创建主窗口并运行程序
            master = tk.Tk()
            app = ImportantEdit(master, base_dir, file_name, info)
            master.mainloop()

    def goto_main_screen(self):
        # 销毁登陆界面，显示主界面
        self.master.destroy()
        # 创建主窗口并运行程序
        master = tk.Tk()
        app = MainScreen(master)
        master.mainloop()

    def goto_important_add(self):
        # 销毁登陆界面，显示主界面
        self.master.destroy()
        # 创建主窗口并运行程序
        master = tk.Tk()
        app = ImportantAdd(master)
        master.mainloop()

    @staticmethod
    def relative_to_assets(path: str):
        assets_dir = ASSET_BASE_PATH + "frame6\\"
        full_path = os.path.join(assets_dir, path)
        return full_path


class ImportantAdd:
    def __init__(self, master):
        self.task = task.Task()
        self.master = master
        self.master.title("To-Do App")
        self.master.geometry("430x932+0+0")
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
        self.image_1 = self.canvas.create_image(
            215.0,
            466.0,
            image=image_image_1
        )

    def create_interactive_controls(self):
        global button_image_1, button_image_2, button_image_3, button_image_4, \
            button_image_5, button_image_6, button_image_7, button_image_8, \
            button_image_3_selected, button_image_4_selected, \
            button_image_5_selected, button_image_6_selected, \
            button_image_7_selected, button_image_8_selected, \
            entry_image_1, entry_image_2, entry_image_3

        button_image_1 = tk.PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = tk.Button(
            self.canvas,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.goto_important_page,
            relief="flat"
        )
        self.button_1.place(
            x=8.0,
            y=58.0,
            width=93.0,
            height=20.0
        )

        button_image_2 = tk.PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_2 = tk.Button(
            self.canvas,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.add_task,
            relief="flat"
        )
        self.button_2.place(
            x=370.0,
            y=59.0,
            width=50.0,
            height=20.0
        )

        entry_image_1 = tk.PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            272.0,
            311.0,
            image=entry_image_1
        )
        self.entry_1 = tk.Entry(
            self.canvas,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=117.0,
            y=296.0,
            width=310.0,
            height=28.0
        )

        entry_image_2 = tk.PhotoImage(file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            272.0,
            179.0,
            image=entry_image_2
        )
        self.entry_2 = tk.Entry(
            self.canvas,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2.place(
            x=117.0,
            y=164.0,
            width=310.0,
            height=28.0
        )

        entry_image_3 = tk.PhotoImage(file=self.relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            272.0,
            135.0,
            image=entry_image_3
        )
        self.entry_3 = tk.Entry(
            self.canvas,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_3.place(
            x=117.0,
            y=120.0,
            width=310.0,
            height=28.0
        )

        button_image_3 = tk.PhotoImage(file=self.relative_to_assets("button_3.png"))
        self.button_3 = tk.Button(
            self.canvas,
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
            self.canvas,
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
            self.canvas,
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
            self.canvas,
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
            self.canvas,
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
            self.canvas,
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
        elif status == "not_started":
            button_6_image = tk.PhotoImage(file=self.relative_to_assets("button_6.png"))
            button_7_image = tk.PhotoImage(file=self.relative_to_assets("button_7.png"))
            button_8_image = tk.PhotoImage(file=self.relative_to_assets("button_8_selected.png"))
        self.button_6.configure(image=button_6_image)
        self.button_7.configure(image=button_7_image)
        self.button_8.configure(image=button_8_image)

    def add_task(self):
        self.task.set_deadline(self.entry_1.get())
        self.task.set_description(self.entry_2.get())
        self.task.set_content(self.entry_3.get())
        self.task.set_label("important")
        base_dir = os.getcwd()
        if "tasks" not in os.listdir(os.getcwd()):
            os.makedirs("tasks")
        os.chdir(os.getcwd() + "\\tasks\\" + current_user_id + "\\")
        now = datetime.datetime.now()
        formatted_time = now.strftime("%Y-%m-%d_%H-%M-%S")
        with open(f"task_{formatted_time}.dat", "wb") as f:
            pickle.dump(self.task, f)
        os.chdir(base_dir)
        self.goto_important_page()

    def goto_important_page(self):
        # 销毁登陆界面，显示主界面
        self.master.destroy()
        # 创建主窗口并运行程序
        master = tk.Tk()
        app = ImportantPage(master)
        master.mainloop()

    @staticmethod
    def relative_to_assets(path: str):
        assets_dir = ASSET_BASE_PATH + "frame7\\"
        full_path = os.path.join(assets_dir, path)
        return full_path


class ImportantEdit:
    def __init__(self, master, base_dir, filename, info=None):
        self.base_dir = base_dir
        self.filename = filename
        self.task = task.Task()
        self.info = info
        self.master = master
        self.master.title("To-Do App")
        self.master.geometry("430x932+0+0")
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
        image_1 = self.canvas.create_image(215.0, 466.0, image=image_image_1)

    def create_interactive_controls(self):
        global button_image_1, button_image_2, button_image_3, button_image_4, \
            button_image_5, button_image_6, button_image_7, button_image_8, \
            button_image_3_selected, button_image_4_selected, \
            button_image_5_selected, button_image_6_selected, \
            button_image_7_selected, button_image_8_selected, \
            entry_image_1, entry_image_2, entry_image_3

        button_image_1 = tk.PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = tk.Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.goto_important_page,
            relief="flat"
        )

        self.button_1.place(
            x=8.0,
            y=58.0,
            width=93.0,
            height=20.0
        )

        button_image_2 = tk.PhotoImage(file=self.relative_to_assets("EditButton.png"))
        self.button_2 = tk.Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.edit_task,
            relief="flat"
        )

        self.button_2.place(
            x=370.0,
            y=59.0,
            width=50.0,
            height=20.0
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

        if self.info is not None:
            # print(f"editing {info}")
            self.entry_1_text.set(self.info['deadline'])
            self.entry_2_text.set(self.info['description'])
            self.entry_3_text.set(self.info['content'])
            self.set_priority(self.info["priority"])
            self.set_status(self.info["status"])

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

    def edit_task(self):
        # print("deadline:", self.entry_1.get(), "description：", self.entry_2.get(), "content:", self.entry_3.get())
        self.task.set_deadline(self.entry_1.get())
        self.task.set_description(self.entry_2.get())
        self.task.set_content(self.entry_3.get())
        self.task.set_label("important")
        # print(self.task.get_info())
        os.remove(self.filename)
        now = datetime.datetime.now()
        formatted_time = now.strftime("%Y-%m-%d_%H-%M-%S")
        with open(self.filename, "wb") as f:
            # print(f"saving {self.task.get_info()}")
            pickle.dump(self.task, f)
        os.chdir(self.base_dir)
        self.goto_important_page()

    def goto_important_page(self):
        # 销毁登陆界面，显示主界面
        self.master.destroy()
        # 创建主窗口并运行程序
        master = tk.Tk()
        app = ImportantPage(master)
        master.mainloop()

    @staticmethod
    def relative_to_assets(path: str):
        assets_dir = ASSET_BASE_PATH + "frame7\\"
        full_path = os.path.join(assets_dir, path)
        return full_path


class SearchPage:
    def __init__(self, master):
        self.master = master
        self.master.geometry("430x932+0+0")
        self.master.configure(bg="#FFFFFF")
        self.master.title("To-Do App")
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
        self.image_1 = self.canvas.create_image(215.0, 466.0, image=image_image_1)

    def create_interactive_controls(self):
        global button_image_1, entry_image_1, button_image_2
        button_image_1 = tk.PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = tk.Button(
            self.canvas,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.goto_main_screen,
            relief="flat"
        )
        self.button_1.place(x=8.083984375, y=59.0, width=62.916015625, height=20.0)
        button_image_2 = tk.PhotoImage(
            file=self.relative_to_assets("button_2.png"))
        self.button_2 = tk.Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.search,
            relief="flat"
        )
        self.button_2.place(
            x=355.0,
            y=59.0,
            width=53.0,
            height=20.0
        )
        entry_image_1 = tk.PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(224.0, 110.0, image=entry_image_1)
        self.entry_1 = tk.Entry(
            self.canvas,
            bd=0,
            bg="#E5E5E5",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(x=46.0, y=95.0, width=356.0, height=28.0)
        self.entry_1.bind("<Return>", self.call_search)

        self.listbox = tk.Listbox(self.canvas,
                                  border=0,
                                  selectbackground="#b0b7c1",
                                  font=("Microsoft YaHei UI", 24),
                                  bg="#f5f5f5")
        self.listbox.place(x=0.0, y=130, width=430, height=780)

        self.master.resizable(False, False)

    def call_search(self, arg):
        self.search()

    def search(self):  # TODO: 优化查找算法
        self.listbox.delete(0, tk.END)
        kw = self.entry_1.get()
        result = []
        if os.getcwd().split('\\')[-1] != "tasks":
            base_dir = os.getcwd()
            os.chdir(os.getcwd() + "\\tasks\\" + current_user_id + "\\")
        else:
            base_dir = os.path.abspath(os.path.dirname(os.getcwd()))
        all_tasks = []
        for data in os.listdir(os.getcwd()):
            with open(data, "rb") as f:
                obj = pickle.load(f)
                all_tasks.append(obj)
        for task in all_tasks:
            info = task.get_data()
            for information in info:
                if information.find(kw) != -1:
                    result.append(task)
                    break
        # print(f"result:{result}")
        if len(result) == 0:
            print("No matched result.")
        for item in result:
            self.listbox.insert('end', item.content + " " + item.description)
        os.chdir(base_dir)

    def goto_main_screen(self):
        # 销毁登陆界面，显示主界面
        self.master.destroy()
        # 创建主窗口并运行程序
        master = tk.Tk()
        app = MainScreen(master)
        master.mainloop()

    @staticmethod
    def relative_to_assets(path: str):
        assets_dir = ASSET_BASE_PATH + "frame8\\"
        full_path = os.path.join(assets_dir, path)
        return full_path


class TrashBin:
    def __init__(self, master):
        self.master = master
        self.master.geometry("430x932+0+0")
        self.master.configure(bg="#FFFFFF")
        self.master.title("To-Do App")
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

        image_image_1 = tk.PhotoImage(
            file=self.relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(
            215.0,
            466.0,
            image=image_image_1
        )

    def create_interactive_controls(self):
        global button_image_1, button_image_2, button_image_3

        button_image_1 = tk.PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        self.button_1 = tk.Button(
            self.canvas,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.goto_main_screen,
            relief="flat"
        )
        self.button_1.place(
            x=13.12060546875,
            y=59.0,
            width=57.87939453125,
            height=20.0
        )

        button_image_2 = tk.PhotoImage(
            file=self.relative_to_assets("button_2.png"))
        self.button_2 = tk.Button(
            self.canvas,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.restore,
            relief="flat"
        )
        self.button_2.place(
            x=288.0,
            y=864.0,
            width=48.0,
            height=48.0
        )

        button_image_3 = tk.PhotoImage(
            file=self.relative_to_assets("button_3.png"))
        self.button_3 = tk.Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.remove,
            relief="flat"
        )
        self.button_3.place(
            x=106.0,
            y=864.0,
            width=48.0,
            height=48.0
        )

        self.listbox = tk.Listbox(self.canvas,
                                  border=0,
                                  selectbackground="#b0b7c1",
                                  font=("Microsoft YaHei UI", 24),
                                  bg="#f5f5f5")
        self.listbox.place(x=0.0, y=130, width=430, height=730)

        result = []
        if os.getcwd().split('\\')[-1] != "tasks":
            base_dir = os.getcwd()
            os.chdir(os.getcwd() + "\\tasks\\" + current_user_id + "\\")
        else:
            base_dir = os.path.abspath(os.path.dirname(os.getcwd()))
        all_tasks = []
        for data in os.listdir(os.getcwd()):
            with open(data, "rb") as f:
                obj = pickle.load(f)
                # print(f"loading {obj.get_info()}")
                all_tasks.append(obj)
        os.chdir(base_dir)
        for task in all_tasks:
            info = task.get_info()
            if info["label"] == "today_deleted" or info["label"] == "important_deleted":
                result.append(task)
        for i in result:
            # print(i.get_info())
            self.listbox.insert('end', i.content)

        self.master.resizable(False, False)

    def restore(self):
        curselection = self.listbox.curselection()
        if curselection:
            index = curselection[0]
            content = self.listbox.get(index)
            if os.getcwd().split('\\')[-1] != "tasks":
                base_dir = os.getcwd()
                os.chdir(os.getcwd() + "\\tasks\\" + current_user_id + "\\")
            else:
                base_dir = os.path.abspath(os.path.dirname(os.getcwd()))
            for data in os.listdir(os.getcwd()):
                with open(data, "rb") as f:
                    obj = pickle.load(f)
                    if obj.content == content:
                        data_path = data
                        selection = obj
            if selection.get_label() == "today_deleted":
                selection.set_label("today")
            if selection.get_label() == "important_deleted":
                selection.set_label("important")
            # print(data_path)
            # os.remove(data_path)
            with open(data_path, "wb") as f:
                pickle.dump(selection, f)
            os.chdir(base_dir)
            self.listbox.delete(index)

    def remove(self):
        curselection = self.listbox.curselection()
        if curselection:
            index = curselection[0]
            content = self.listbox.get(index)
            if os.getcwd().split('\\')[-1] != "tasks":
                base_dir = os.getcwd()
                os.chdir(os.getcwd() + "\\tasks\\" + current_user_id + "\\")
            else:
                base_dir = os.path.abspath(os.path.dirname(os.getcwd()))
            for data in os.listdir(os.getcwd()):
                with open(data, "rb") as f:
                    obj = pickle.load(f)
                    if obj.content == content:
                        data_path = data
                        selection = obj
            os.remove(data_path)
            os.chdir(base_dir)
            self.listbox.delete(index)

    def goto_main_screen(self):
        # 销毁登陆界面，显示主界面
        self.master.destroy()
        # 创建主窗口并运行程序
        master = tk.Tk()
        app = MainScreen(master)
        master.mainloop()

    @staticmethod
    def relative_to_assets(path: str):
        assets_dir = ASSET_BASE_PATH + "frame9\\"
        full_path = os.path.join(assets_dir, path)
        return full_path


def get_md5(string):
    m2 = hashlib.md5()
    m2.update(string.encode())
    return m2.hexdigest()


if __name__ == "__main__":
    # 创建主窗口并运行程序
    root = tk.Tk()
    app = WelcomeScreen(root)
    # app = MainScreen(root)
    root.mainloop()
