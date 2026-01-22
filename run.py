import os
import sys
import subprocess
import time
import glob

def install_package(package_name):
    """尝试安装指定的包"""
    print(f"正在安装 {package_name}...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        print(f"{package_name} 安装成功。")
    except subprocess.CalledProcessError:
        print(f"{package_name} 安装失败。请尝试手动安装。")

def check_and_install_dependencies():
    """检查并安装依赖"""
    print("正在检查环境依赖...")
    
    # 1. 检查 OpenAI
    try:
        import openai
        print("OpenAI 库已安装。")
    except ImportError:
        print("未检测到 OpenAI 库，准备安装...")
        install_package("openai")

    # 2. 检查 wxautox4_wechatbot
    try:
        from wxautox4_wechatbot import WeChat
        print("wxautox4_wechatbot 库已安装。")
    except ImportError:
        print("未检测到 wxautox4_wechatbot 库。")
        
        # 获取当前脚本所在目录 (1052)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # 指向 1052/libs 目录
        libs_dir = os.path.join(current_dir, "libs")
        
        # 获取当前 python 版本
        py_ver = f"cp{sys.version_info.major}{sys.version_info.minor}"
        
        print(f"正在本地 libs 目录 ({libs_dir}) 中查找适配 {py_ver} 的 whl 包...")
        
        if os.path.exists(libs_dir):
            whl_files = glob.glob(os.path.join(libs_dir, f"wxautox4_wechatbot-*{py_ver}*.whl"))
            if whl_files:
                target_whl = whl_files[0]
                print(f"找到本地安装包: {target_whl}")
                install_package(target_whl)
            else:
                print(f"警告: 未在 libs 目录找到适配当前 Python 版本 ({py_ver}) 的 wxautox4_wechatbot 安装包。")
                print(f"请检查 {libs_dir} 目录下是否有对应的 .whl 文件。")
        else:
             print(f"警告: 无法找到 libs 目录: {libs_dir}")

def start_bot():
    """启动主程序"""
    main_script = os.path.join(os.path.dirname(os.path.abspath(__file__)), "main.py")
    if not os.path.exists(main_script):
        print(f"错误: 找不到 {main_script}")
        input("按回车键退出...")
        return

    print("\n" + "="*30)
    print("   微信 AI 助手 (1052版) 正在启动")
    print("="*30 + "\n")
    
    try:
        # 使用当前解释器运行 main.py
        subprocess.call([sys.executable, main_script])
    except KeyboardInterrupt:
        print("\n程序已停止。")
    except Exception as e:
        print(f"\n发生错误: {e}")
        input("按回车键退出...")

if __name__ == "__main__":
    check_and_install_dependencies()
    time.sleep(1)
    start_bot()
