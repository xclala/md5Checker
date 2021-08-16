try:
    from hashlib import sha256
    from win32ui import CreateFileDialog
    from win32con import OFN_OVERWRITEPROMPT, OFN_FILEMUSTEXIST
    file_open_type = 'All File(*.*)|*.*|'\
        '|'
    d = CreateFileDialog(1, None, None, OFN_OVERWRITEPROMPT | OFN_FILEMUSTEXIST, file_open_type)
    d.DoModal()
    with open(d.GetPathName(), encoding='utf-8') as file_object:
        file = file_object.read()
        SHA256 = sha256(file.encode(encoding='utf-8')).hexdigest()
        print("此文件的SHA256值为："+SHA256)

except Exception as e:
    print(e)
