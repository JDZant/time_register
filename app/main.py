# main.py
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from app.view.main_view import MainWindow
import tkinter as tk

# Load environment variables
load_dotenv()


def main():
    root = tk.Tk()
    app = MainWindow(root)
    app.grid()
    root.mainloop()


if __name__ == "__main__":
    main()
