# Author = "Hao Li"
# Creation Time = "2023/09/24"

import tkinter as tk
from tkinter import filedialog

# 创建主窗口
root = tk.Tk()
root.title("My_Texteditor")

# 创建文本编辑区域
text = tk.Text(root, wrap=tk.WORD)
text.pack()

# 定义打开文件函数
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("文本文件", "*.txt"), ("以逗号分隔", "*.csv")])
    if file_path:
        with open(file_path, 'r') as file:
            text.delete('1.0', tk.END)
            text.insert(tk.END, file.read())

# 定义保存文件函数
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("文本文件", "*.txt"), ("以逗号分隔", "*.csv")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get('1.0', tk.END))

# 创建菜单栏
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="文件", menu=file_menu)
file_menu.add_command(label="打开", command=open_file)
file_menu.add_command(label="保存", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="退出", command=root.quit)

# 创建工具栏
toolbar = tk.Frame(root)
toolbar.pack(fill=tk.X)

open_button = tk.Button(toolbar, text="打开", command=open_file)
open_button.pack(side=tk.LEFT)
save_button = tk.Button(toolbar, text="保存", command=save_file)
save_button.pack(side=tk.LEFT)

# 运行主循环
root.mainloop()
