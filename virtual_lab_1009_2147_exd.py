# 代码生成时间: 2025-10-09 21:47:40
import gradio as gr
# 添加错误处理
def run_experiment(input_data):
    # 模拟实验过程
    # 此处应添加实际的实验代码
    # 为了演示，我们简单地返回输入数据的两倍
    return input_data * 2

# 定义Gradio界面
def main():
    demo = gr.Interface(
        fn=run_experiment, # 函数
        inputs=gr.Textbox(label="输入数据"), # 输入框
        outputs="text" # 输出格式
    )
    demo.launch()

if __name__ == "__main__":
    main()
