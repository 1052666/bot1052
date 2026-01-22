# 1052 独立配置模块
# 请在此处填写您的 API 配置

# DeepSeek / OpenAI API 配置
API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxx"  # 替换为您的 API Key
BASE_URL = "https://api.deepseek.com"    # 替换为您的 Base URL
MODEL_NAME = "deepseek-chat"             # 替换为您的模型名称

# 系统提示词 (System Prompt)
# 定义 AI 的人设和行为准则
SYSTEM_PROMPT = """
你是一个运行在微信上的智能助手。
请使用自然、亲切的语气与用户交流。
回答要简洁明了，避免长篇大论，除非用户要求详细解释。
不要使用 Markdown 格式（如 **粗体**），因为微信不支持。
"""

# 历史记录配置
MAX_HISTORY_LENGTH = 10  #保留最近的 N 条对话记录（问+答）
