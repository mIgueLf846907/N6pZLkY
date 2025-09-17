# 代码生成时间: 2025-09-17 08:42:41
import os
import zipfile
import gzip
import tarfile
import shutil
from gradio import *

class DecompressionTool:
    """
    A tool for decompressing files using GRADIO interface.
    """

    def __init__(self):
        self.decompressed_directory = "decompressed_files"
        os.makedirs(self.decompressed_directory, exist_ok=True)

    def decompress_zip(self, file_path):
        """
        Decompress a zip file to the decompressed directory.
        """
        try:
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(self.decompressed_directory)
        except zipfile.BadZipFile:
            return "The file is not a valid zip file."
        except Exception as e:
            return f"An error occurred: {e}"

    def decompress_gz(self, file_path):
        """
        Decompress a gzip file to the decompressed directory.
        """
        try:
            with gzip.open(file_path, 'rb') as f_in:
                with open(os.path.join(self.decompressed_directory, os.path.basename(file_path)[:-3]), 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
        except gzip.BadGzipFile:
            return "The file is not a valid gzip file."
        except Exception as e:
            return f"An error occurred: {e}"

    def decompress_tar(self, file_path):
        """
        Decompress a tar file to the decompressed directory.
        """
        try:
            with tarfile.open(file_path) as tar_ref:
                tar_ref.extractall(self.decompressed_directory)
        except tarfile.TarError:
            return "The file is not a valid tar file."
        except Exception as e:
            return f"An error occurred: {e}"

    def decompress_file(self, file_path):
        """
        Decompress a file based on its extension.
        """
        if file_path.endswith(".zip"):
            return self.decompress_zip(file_path)
        elif file_path.endswith(".gz"):
            return self.decompress_gz(file_path)
        elif file_path.endswith(".tar") or file_path.endswith(".tar.gz"):
            return self.decompress_tar(file_path)
        else:
            return "Unsupported file format."

# Create an instance of the tool
decompression_tool = DecompressionTool()

# Define the GRADIO interface
iface = Interface(
    fn=decompression_tool.decompress_file,
    inputs=File(label="Select a file"),
    outputs="text",
    title="Decompression Tool",
    description="Upload a zip, gzip, or tar file to decompress it."
)

iface.launch(share=True)