# 代码生成时间: 2025-09-20 10:04:29
import gradio as gr

# 定义数学计算功能

def add(x, y):
    """Add two numbers.
    
    Args:
    x (float): The first number.
    y (float): The second number.
    
    Returns:
    float: The sum of x and y.
    """
    return x + y

def subtract(x, y):
    """Subtract two numbers.
    
    Args:
    x (float): The first number.
    y (float): The second number.
    
    Returns:
    float: The difference between x and y.
    """
    return x - y

def multiply(x, y):
    """Multiply two numbers.
    
    Args:
    x (float): The first number.
    y (float): The second number.
    
    Returns:
    float: The product of x and y.
    """
    return x * y

def divide(x, y):
    """Divide two numbers with error handling.
    
    Args:
    x (float): The first number (numerator).
    y (float): The second number (denominator).
    
    Returns:
    float: The quotient of x divided by y.
    Raises:
    ValueError: If y is zero.
    """
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

# 创建Gradio界面
def main():
    # 定义输入和输出组件
    add_interface = gr.Interface(
        fn=add, inputs=[gr.Textbox(label="Number 1"), gr.Textbox(label="Number 2")],
        outputs=gr.Textbox(label="Result"), title="Addition")
    subtract_interface = gr.Interface(
        fn=subtract, inputs=[gr.Textbox(label="Number 1"), gr.Textbox(label="Number 2")],
        outputs=gr.Textbox(label="Result"), title="Subtraction")
    multiply_interface = gr.Interface(
        fn=multiply, inputs=[gr.Textbox(label="Number 1"), gr.Textbox(label="Number 2")],
        outputs=gr.Textbox(label="Result"), title="Multiplication")
    divide_interface = gr.Interface(
        fn=divide, inputs=[gr.Textbox(label="Number 1"), gr.Textbox(label="Number 2")],
        outputs=gr.Textbox(label="Result"), title="Division")
    
    # 启动Gradio应用
    gr.Blocks(
        layout="horizontal",
        block=gr.TabbedInterface(
            tab1=add_interface,
            tab2=subtract_interface,
            tab3=multiply_interface,
            tab4=divide_interface
        )
    ).launch()

# 运行主函数
if __name__ == "__main__":
    main()