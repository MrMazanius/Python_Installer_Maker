import os
import urllib.request
import tkinter as tk
from tkinter import ttk
import time

print("Installer by MrMazanius#0001")

class InstallerGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Installer")
        self.window.geometry("300x100")
        self.window.iconbitmap("misc\Media\icon.ico")
        
        self.progress_bar = ttk.Progressbar(self.window, orient="horizontal", length=250, mode="determinate")
        self.progress_bar.grid(row=0, column=0, padx=20, pady=10)
        
        self.label = tk.Label(self.window, text="Downloading...")
        self.label.grid(row=1, column=0, padx=20)
        
    def set_progress(self, progress):
        self.progress_bar["value"] = progress
        self.window.update_idletasks()
        
    def set_label_text(self, text):
        self.label["text"] = text
        self.window.update_idletasks()
        
    def close(self):
        self.window.destroy()
        
def download_file(url, file_name):
    with urllib.request.urlopen(url) as response, open(file_name, "wb") as out_file:
        content_length = response.info().get("Content-Length")
        total_size = int(content_length.strip()) if content_length else None
        downloaded_size = 0
        
        gui = InstallerGUI()
        
        while True:
            data = response.read(8192)
            if not data:
                break
            out_file.write(data)
            downloaded_size += len(data)
            if total_size:
                progress = int(downloaded_size / total_size * 100)
            else:
                progress = 0
            gui.set_progress(progress)
            gui.set_label_text(f"Downloading {file_name}... {progress}%")
        
        gui.close()

download_file("<ZIP_LINK_HERE>", "ZIP_FILE.zip")