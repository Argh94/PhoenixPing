import time
import threading
import subprocess
import platform
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import rcParams
import arabic_reshaper
from bidi.algorithm import get_display
import tkinter as tk
from tkinter import simpledialog, messagebox
import ipaddress
from collections import deque
import csv
import datetime
import sys

# تنظیم فونت برای پشتیبانی از فارسی
rcParams['font.family'] = 'Tahoma'
rcParams['font.size'] = 12

# متغیر جهانی برای کنترل توقف برنامه
running = True

# تابع اعتبارسنجی آدرس IP
def validate_ip(ip):
    try:
        ipaddress.ip_address(ip.strip())
        return True
    except ValueError:
        return False

# تابع دریافت IPها از کاربر
def get_ips():
    root = tk.Tk()
    root.withdraw()  # مخفی کردن پنجره اصلی
    ip_input = simpledialog.askstring("Input", "لطفاً IPهای معتبر را وارد کنید (با کاما جدا کنید):")
    if not ip_input:
        messagebox.showerror("خطا", "هیچ IP وارد نشد!")
        root.destroy()
        exit(1)
    ip_list = [ip.strip() for ip in ip_input.split(",") if validate_ip(ip.strip())]
    if not ip_list:
        messagebox.showerror("خطا", "هیچ IP معتبری وارد نشد!")
        root.destroy()
        exit(1)
    root.destroy()
    return ip_list

# دریافت IPها
ips = get_ips()

# تنظیمات قابل‌تغییر
config = {
    "ping_interval": 1,  # فاصله زمانی پینگ (ثانیه)
    "max_display_time": 100  # حداکثر نقاط زمانی در نمودار
}

# استفاده از deque برای بهینه‌سازی حافظه
ping_results = deque(maxlen=config["max_display_time"])

# تابع پینگ با پشتیبانی چندپلتفرمی
def ping_ips():
    ping_flag = "-n" if platform.system() == "Windows" else "-c"
    while running:
        responses = []
        for ip in ips:
            try:
                response = subprocess.run(
                    ["ping", ping_flag, "1", "-w", "500", ip],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    creationflags=(subprocess.CREATE_NO_WINDOW if platform.system() == "Windows" else 0)
                )
                responses.append(response.returncode == 0)
            except subprocess.SubprocessError as e:
                print(f"خطا در پینگ IP {ip}: {e}")
                responses.append(False)
        ping_results.append(responses)
        time.sleep(config["ping_interval"])

# تابع ذخیره لاگ‌ها در فایل CSV
def log_results():
    with open("ping_log.csv", "a", newline="") as f:
        writer = csv.writer(f)
        if f.tell() == 0:
            writer.writerow(["Timestamp"] + ips)
        while running:
            if ping_results:
                writer.writerow([datetime.datetime.now()] + list(ping_results)[-1])
            time.sleep(config["ping_interval"])

# تابع به‌روزرسانی نمودار
def update_graph(i):
    ax.clear()
    xlabel = arabic_reshaper.reshape("زمان (ثانیه)")
    ylabel = arabic_reshaper.reshape("وضعیت")
    xlabel = get_display(xlabel)
    ylabel = get_display(ylabel)
    
    ax.set_title("PHOENIX Monitoring", fontname='Tahoma', loc='right')
    ax.set_xlabel(xlabel, fontname='Tahoma', loc='right')
    ax.set_ylabel(ylabel, fontname='Tahoma', loc='top')

    times = list(range(len(ping_results)))
    colors = ['b', 'r', 'g', 'y', 'm']  # رنگ‌های مختلف برای هر IP
    for idx, ip in enumerate(ips):
        ax.plot(
            times,
            [result[idx] for result in ping_results],
            label=ip,
            color=colors[idx % len(colors)],
            marker='o',
            markersize=4
        )

    ax.set_xlim(left=max(0, len(ping_results) - config["max_display_time"]), right=len(ping_results))
    ax.set_ylim(-0.1, 1.1)
    ax.set_yticks([0, 1])
    ax.set_yticklabels([get_display(arabic_reshaper.reshape("آفلاین")), get_display(arabic_reshaper.reshape("آنلاین"))])

    labels = [get_display(arabic_reshaper.reshape(ip)) for ip in ips]
    ax.legend(labels=labels, prop={'family': 'Tahoma'}, loc='upper right')

# تابع مدیریت بستن برنامه
def on_closing():
    global running
    running = False
    plt.close()
    sys.exit(0)

# راه‌اندازی نخ‌ها
ping_thread = threading.Thread(target=ping_ips)
ping_thread.daemon = True
ping_thread.start()

log_thread = threading.Thread(target=log_results)
log_thread.daemon = True
log_thread.start()

# تنظیم نمودار
fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, update_graph, interval=500, save_count=100, cache_frame_data=False)

# مدیریت بستن پنجره
fig.canvas.mpl_connect('close_event', lambda event: on_closing())

# نمایش نمودار
plt.show()
