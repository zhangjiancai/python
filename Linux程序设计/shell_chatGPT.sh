#!/bin/bash

# 获取当前用户、主机和日期信息
USER=$(whoami)
THIS_HOST=$(hostname)
MYDATE=$(date +"%Y-%m-%d")

# 显示菜单选项
while true; do
    echo "---------------------------------------------------------------------"
    echo "User:$USER		Host:$THIS_HOST			Date:$MYDATE"
    echo "---------------------------------------------------------------------"
    echo "		1 : List subdirectory in current directory "
    echo "		2 : List files in current directory which can run"
    echo "		3 : See who is on the system"
    echo "		H : Help screen"
    echo "		Q : Exit Menu"
    echo "---------------------------------------------------------------------"
    # 读取用户输入
    read -p "Enter your choice: " choice

    # 根据用户选择执行不同的操作
    case $choice in
        1)
            # 列出当前目录下的所有子目录
            echo "Subdirectories in current directory:"
            ls -l | awk '/^d/ { print $NF }'
            ;;
        2)
            # 列出当前目录下的所有可执行文件
            echo "Executable files in current directory:"
            find . -maxdepth 1 -type f -executable -printf "%f\n"
            ;;
        3)
            # 显示当前在线的用户
            echo "Users currently on the system:"
            who
            ;;
        h|H)
            # 显示帮助信息
            echo "This script provides a simple menu to perform various tasks."
            echo "Choose an option by entering the corresponding number or letter."
            ;;
        q|Q)
            # 退出菜单
            echo "Goodbye!"
            exit 0
            ;;
        *)
            # 无效的选项
            echo "Invalid choice. Please try again."
            ;;
    esac

    echo
done

