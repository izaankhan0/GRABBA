# save as downloader.py
# convert to exe later with:
# pyinstaller --onefile downloader.py

import tkinter as tk
from tkinter import ttk
import time
import threading

root = tk.Tk()
root.title("Downloader")
root.geometry("700x220")
root.configure(bg="#111111")
root.resizable(False, False)

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "dark.Horizontal.TProgressbar",
    troughcolor="#222222",
    background="#00ff99",
    bordercolor="#222222",
    lightcolor="#00ff99",
    darkcolor="#00cc77",
)

title = tk.Label(
    root,
    text="Downloading...",
    font=("Segoe UI", 22, "bold"),
    fg="white",
    bg="#111111"
)
title.pack(pady=30)

progress = ttk.Progressbar(
    root,
    style="dark.Horizontal.TProgressbar",
    orient="horizontal",
    length=500,
    mode="determinate",
    maximum=100
)
progress.pack(pady=20)

percent_label = tk.Label(
    root,
    text="0%",
    font=("Segoe UI", 14),
    fg="#00ff99",
    bg="#111111"
)
percent_label.pack()

# custom timing:
# 0 -> 10 in 1 sec
# 10 -> 20 in 10 sec
# 20 -> 30 in 100 sec
# then reverse speeds pattern repeatedly

stages = [
    (0, 10, 1),
    (10, 20, 10),
    (20, 30, 100),
    (30, 40, 10),
    (40, 50, 1),
    (50, 60, 10),
    (60, 70, 100),
    (70, 80, 10),
    (80, 90, 1),
    (90, 100, 10),
]

def animate():
    for start, end, duration in stages:
        steps = end - start
        delay = duration / steps

        for value in range(start, end + 1):
            progress["value"] = value
            percent_label.config(text=f"{value}%")
            root.update_idletasks()
            time.sleep(delay)

    title.config(text="Download Complete!")

threading.Thread(target=animate, daemon=True).start()

root.mainloop()