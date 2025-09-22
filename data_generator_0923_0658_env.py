# 代码生成时间: 2025-09-23 06:58:08
import gr
import random
import string
from typing import List

"""
Data Generator application using Gradio framework.
This application generates random test data.
"""

class TestDataGenerator:
    def __init__(self):
        # Initialize the test data generator
        pass

    def generate_random_number(self, min_value: int, max_value: int) -> int:
        """
        Generate a random number between min_value and max_value.
        Args:
        min_value (int): The minimum value.
        max_value (int): The maximum value.
        Returns:
        int: A random number within the specified range.
        """
        return random.randint(min_value, max_value)

    def generate_random_string(self, length: int) -> str:
        """
        Generate a random string of the specified length.
        Args:
        length (int): The length of the string to be generated.
        Returns:
        str: A random string.
        """
        return ''.join(random.choice(string.ascii_letters) for _ in range(length))

    def generate_random_list(self, length: int) -> List[int]:
        """
        Generate a random list of integers of the specified length.
        Args:
        length (int): The length of the list to be generated.
        Returns:
        List[int]: A random list of integers.
        """
        return [random.randint(0, 100) for _ in range(length)]

# Create an instance of the TestDataGenerator class
generator = TestDataGenerator()

# Define the Gradio interface
iface = gr.Interface(
    fn=lambda min_val, max_val, str_len, list_len: (
        generator.generate_random_number(min_val, max_val),
        generator.generate_random_string(str_len),
        generator.generate_random_list(list_len)
    ),
    inputs=[
        gr.Slider(minimum=1, maximum=100, step=1, label='Min Value'),
        gr.Slider(minimum=101, maximum=200, step=1, label='Max Value'),
        gr.Slider(minimum=1, maximum=20, step=1, label='String Length'),
        gr.Slider(minimum=1, maximum=20, step=1, label='List Length')
    ],
    outputs=[
        gr.Textbox(label='Random Number'),
        gr.Textbox(label='Random String'),
        gr.Dataframe(label='Random List', headers=['Value'])
    ]
)

# Launch the Gradio interface
iface.launch()