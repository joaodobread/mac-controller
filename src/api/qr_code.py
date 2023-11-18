import tkinter as tk
import socket
import pyqrcode


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = str(s.getsockname()[0])
    s.close()
    return f"http://{ip}:5888"


def generate_qr_code(content: str):
    return pyqrcode.create(content)


def open_qr_code(content: str = get_ip()):
    qr = generate_qr_code(content)
    qr.show()
