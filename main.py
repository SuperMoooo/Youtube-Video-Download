from pytube import YouTube
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import customtkinter as ctk
import io
import requests

root = Tk()
root.title('Video Downloader')
root.geometry('800x400+500+200')
root.resizable(0, 0)
root.iconbitmap('logo.ico')

BG = '#383838'
FG = 'white'
vid_name = StringVar()
vid_views = StringVar()

main_frame = Frame(root, width=800, height=400, bg=BG)
main_frame.pack(expand=True, fill='both')

title = Label(main_frame, text='Youtube Video Downloader', font='Consolas 18', bg=BG, fg=FG)
title.pack(pady=10)

link_frame = Frame(main_frame, bg=BG)
link_frame.pack(pady=10)

LINK = Entry(link_frame, width=51, bg=BG, fg=FG, font='Consolas 14')
LINK.pack(side='left', padx=10, pady=10, anchor='center')

def find_video():
    link = LINK.get()
    yt = YouTube(link)
    title = yt.title
    views = yt.views
    img = yt.thumbnail_url
    vid_name.set(f'Name: {title}')
    vid_views.set(f'Views: {views}')

    # Retrieve the thumbnail image data
    response = requests.get(img)
    image_data = response.content

    # Open the image using PIL from the retrieved data
    image = Image.open(io.BytesIO(image_data))
    image = image.resize((300, 200))  # Resize the image if necessary
    photo = ImageTk.PhotoImage(image)

    # Update the thumbnail image
    thumbnail_label.configure(image=photo)
    thumbnail_label.image = photo


def download_video():
    link = LINK.get()
    yt = YouTube(link)
    yd = yt.streams.get_highest_resolution()
    filepath = filedialog.askdirectory(title='Save in')
    yd.download(filepath)

find_button = ctk.CTkButton(link_frame, text='Find Video', command=find_video)
find_button.pack(side='left', padx=10, pady=10, anchor='center')

vid_frame = Frame(main_frame, bg=BG)
vid_frame.pack()

thumbnail_label = Label(vid_frame, bg=BG, fg=FG)
thumbnail_label.pack(side='left', pady=10)

info_frame = Frame(vid_frame, bg=BG)
info_frame.pack(side='left', padx=10)

name_label = Label(info_frame, textvariable=vid_name, bg=BG, fg=FG, font='Consolas 8')
name_label.pack(anchor='w', pady=(0, 5))

views_label = Label(info_frame, textvariable=vid_views, bg=BG, fg=FG, font='Consolas 8')
views_label.pack(anchor='w')

download_button = ctk.CTkButton(main_frame, text='Download', command=download_video)
download_button.pack()

root.mainloop()
