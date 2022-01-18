try:
    from hashlib import md5
    from tkinter import messagebox, simpledialog
    from win32ui import CreateFileDialog
    from win32con import OFN_OVERWRITEPROMPT, OFN_FILEMUSTEXIST
    file_open_type = 'All File(*.*)|*.*|'\
        '|'
    d = CreateFileDialog(1, None, None,
                         OFN_OVERWRITEPROMPT | OFN_FILEMUSTEXIST,
                         file_open_type)
    d.DoModal()
    with open(d.GetPathName(), "rb") as file_object:
        MD5 = md5(file_object.read()).hexdigest()
        messagebox.showinfo(message=f"此文件的md5值为：{MD5}", title="此文件的md5值")
        a = simpledialog.askstring(prompt="输入下载时提供的md5：", title="输入下载时提供的md5")
        if a == MD5:
            messagebox.showinfo(message="文件未被篡改！", title="文件未被篡改！")
        else:
            messagebox.showinfo(message="文件可能已经被篡改！！！", title="文件可能已经被篡改！！！")
except Exception as e:
    print(e)