# 代码生成时间: 2025-10-07 02:05:22
import re
def check_compliance(text):
    """
    检查文本是否符合规定的合规性标准。
    
    参数:
    text (str): 需要检查的文本内容。
    
    返回：
    tuple: 包含检查结果和错误信息的元组。
    """
    # 定义合规性规则（例如，禁止包含特定关键词）
    banned_keywords = ["敏感词1", "敏感词2"]
    
    # 遍历所有禁止关键词
    for keyword in banned_keywords:
        # 如果文本包含禁止关键词，则返回错误信息
        if keyword in text:
            return False, f"文本包含禁止关键词：{keyword}"
    
    # 检查文本长度
    if len(text) < 10:  # 假设合规性要求文本长度至少为10个字符
        return False, "文本长度不足。"
    
    # 检查文本是否包含至少一个数字和一个大写字母
    if not re.search(r"[0-9]", text) or not re.search(r"[A-Z]", text):
        return False, "文本必须包含至少一个数字和一个大写字母。"
    
    # 如果所有检查通过，返回True
    return True, "文本符合合规性要求。"

# 使用Gradio框架创建用户界面
import gradio as gr

# 创建一个输入框，允许用户输入文本
text_input = gr.Textbox(label="请输入文本")

# 创建一个输出框，显示检查结果和错误信息
result_output = gr.Textbox(label="检查结果")

# 定义一个函数，用于更新输出框的内容
def update_output(text):
    result, message = check_compliance(text)
    return message

# 创建Gradio界面
iface = gr.Interface(
    fn=update_output,
    inputs=text_input,
    outputs=result_output,
    title="合规性检查工具",
    description="输入文本进行检查，确保符合合规性要求。"
)

# 启动Gradio界面
iface.launch()