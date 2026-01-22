# 1052微信聊天机器人 
这是一个智能微信聊天机器人
本程序现已支持微信4.1.6.46

## 快速开始 (推荐)

直接运行 `run.py` 即可。该脚本会自动检测并安装依赖，然后启动机器人。

```bash
python run.py
```

或者直接双击 `run.py` (如果您的系统关联了 Python)。

## 手动安装依赖

如果您喜欢手动管理，可以使用以下命令安装依赖：

```bash
pip install -r requirements.txt
```

**注意**: `wxautox4_wechatbot` 是一个特殊库。如果上述命令无法安装它，请查看当前目录下的 `libs` 文件夹，选择对应您 Python 版本的 `.whl` 文件进行安装。例如：

```bash
pip install ./libs/wxautox4_wechatbot-40.1.10-cp310-cp310-win_amd64.whl
```

## 目录结构

- **run.py**: **一键启动脚本**。自动检查依赖并运行主程序。
- **requirements.txt**: 依赖列表文件。
- **libs/**: 存放 `wxautox4_wechatbot` 等本地依赖包。
- **main.py**: 程序入口。
- **config.py**: 配置文件 (API Key)。
- **ai_manager.py**: AI 服务层。
- **wechat_manager.py**: 微信传输层。
- **processor.py**: 业务逻辑层。

## 配置

请记得在 `config.py` 中填入您的 API Key。
