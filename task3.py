#!/usr/bin/python3

import os


def get_system_info():
    print(os.uname())
    current_dir = os.getcwd()
    print(current_dir)
    content = os.listdir(current_dir)
    print(content)
    test_dir = "test_dir"
    os.mkdir(test_dir)
    
    cnt = 2
    for i in range(cnt):
        dir_name = f"dir_{i}"
        dir_path = os.path.join(test_dir, dir_name)
        os.mkdir(dir_path)
        print(os.listdir(test_dir))
    cmd = f"rm -rf {test_dir}"
    os.system(cmd)

if __name__ == "__main__":
    get_system_info()