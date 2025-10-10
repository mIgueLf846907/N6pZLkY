# 代码生成时间: 2025-10-10 16:30:47
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import gradio as gr
def on_file_change(event):
    # 事件处理函数，当文件发生变化时被调用
    if not event.is_directory:
        # 仅处理文件变化
        print(f"File {event.src_path} changed")
        info.value = f"File {event.src_path} changed"

class ChangeHandler(FileSystemEventHandler):
    """自定义文件系统事件处理器"""
    def on_modified(self, event):
        on_file_change(event)

# 设置监控目录和回调函数
def setup_monitor(folder_path):
    event_handler = ChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, folder_path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

if __name__ == "__main__":
    # GRADIO界面设置
    folder_path = "/path/to/monitor"  # 需要监控的文件夹路径
    info = gr.Textbox()
    monitor_button = gr.Button("Start Monitoring")
    monitor_button.click(fn=setup_monitor, inputs=[folder_path], outputs=info)
    gr.Interface(
        fn=lambda: "Monitoring started",  # 初始界面信息
        inputs=[folder_path],
        outputs=info,
        live=True,
    ).launch()