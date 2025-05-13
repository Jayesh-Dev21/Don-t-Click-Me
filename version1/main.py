import tkinter as tk
import os
import sys
from function import on_click
from function import prompt
from function import randomize
from function import print_time
from PIL import Image, ImageTk, ImageSequence
from function import local_user
from function import send_data

limit = 39

ui_root = tk.Tk()
ui_root.title("Don't Click It!!!")
ui_root.geometry("350x250")
ui_root.configure(bg="green")
ui_root.resizable(False, False)

init_reference = tk.Label(text=print_time())
init_reference.config(font=("Arial", 10, "bold"), bg="green", fg="black")
init_reference.pack()

footer = tk.Frame(ui_root, width=350, height=75, bg="lightgray", highlightbackground="black", highlightthickness=1)
footer.place(x=0, y=195)  

body = tk.Frame(ui_root, width=350, height=175, bg="white", highlightbackground="black", highlightthickness=1)
body.place(x=0, y=25)


def small_boy():
    ui_root.geometry("250x150")
    body = tk.Frame(ui_root, width=250, height=175, bg="white", highlightbackground="black", highlightthickness=1)
    body.place(x=0, y=25)
    buttonVend = tk.Button(body, text="END", width=5, height=1, command=ui_root.quit)
    buttonVend.config(font=("Arial", 14), bg="pink", fg="black")
    buttonVend.pack()


if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(__file__)

gif_path = os.path.join(base_path, "animation.gif")



def master():
    global limit
    if limit == -2:
        ui_root.geometry("640x492")
        body2 = tk.Frame(ui_root, width=640, height=492, bg="red", highlightbackground="black", highlightthickness=1)
        body2.place(x=0, y=0) 
        init_reference.destroy()

        def update(ind):
                frame = frames[ind]
                ind += 1
                if ind == frame_count:
                    ind = 0
                label.configure(image=frame)
                body2.after(delay, update, ind)
            
        try:
            img = Image.open(gif_path)
        except FileNotFoundError:
            print("Error: GIF file not found.")
            exit()
            
        frames = []
        try:
            while True:
                frame = ImageTk.PhotoImage(img.copy())
                frames.append(frame)
                img.seek(img.tell() + 1)
        except EOFError:
            pass
        
        frame_count = len(frames)
        
        label = tk.Label(body2)
        label.pack()
        
        try:
            delay = img.info['duration']
        except KeyError:
            delay = 100
        
        update(0)
        ui_root.after(5000, ui_root.destroy)


    elif limit == -1:
        text_print = "By 0x3xpl0it"
        body2 = tk.Frame(ui_root, width=500, height=325, bg="black", highlightbackground="black", highlightthickness=1)
        body2.place(x=0, y=25) 
        p2_out = tk.Label(body2, text=text_print, font=("Arial", 24, "bold"), bg="black", fg="darkgreen", wraplength=300)
        p2_out.place(relx=0.5, rely=0.5, anchor='center') 


    elif limit == 0:
        text_print = "Hi!" + "\nUsername: " + local_user.name + "\nUser Id: " + str(local_user.id) + "\nHome Dir: " + local_user.home_dir + "\nIP Addr: " + local_user.ip_address
        body2 = tk.Frame(ui_root, width=500, height=325, bg="black", highlightbackground="black", highlightthickness=1)
        body2.place(x=0, y=25) 
        p2_out = tk.Label(body2, text=text_print, font=("Arial", 18, "bold"), bg="black", fg="darkgreen", wraplength=300)
        p2_out.place(relx=0.5, rely=0.5, anchor='center') 

    else:
        if limit <= 1:
            footer2 = tk.Frame(ui_root, width=500, height=75, bg="lightgray", highlightbackground="black", highlightthickness=1)
            footer2.place(x=0, y=345)  
            buttonV2 = tk.Button(footer2, text="Exit Now!!", width=25, command=master)
            buttonV2.place(x=110, y=8)
        text_print = prompt(limit)
        body2 = tk.Frame(ui_root, width=500, height=325, bg="white", highlightbackground="black", highlightthickness=1)
        body2.place(x=0, y=25) 
        p2_out = tk.Label(body2, text=text_print, font=("Arial", 14), bg="white", fg="black", wraplength=300)
        p2_out.place(relx=0.5, rely=0.5, anchor='center') 
        

    limit = limit - 1

def on_click_action():
    output_text = on_click()
    
    
    ui_root.geometry("500x400")
    body2 = tk.Frame(ui_root, width=500, height=325, bg="white", highlightbackground="black", highlightthickness=1)
    body2.place(x=0, y=25)
    footer2 = tk.Frame(ui_root, width=500, height=75, bg="lightgray", highlightbackground="black", highlightthickness=1)
    footer2.place(x=0, y=345)  
    p_out = tk.Label(body2, text=output_text, font=("Arial", 14), bg="white", fg="black", wraplength=300)
    p_out.place(relx=0.5, rely=0.5, anchor='center') 
    buttonV2 = tk.Button(footer2, text="Don't click me!!", width=25, command=master)
    buttonV2.place(x=110, y=8)
    button.destroy()
    footer.destroy()


#❌
p_in = tk.Label(body, text="❌ Don't ❌ Click", font=("Arial", 34), bg="white", fg="black", wraplength=300)
p_in.place(relx=0.5, rely=0.5, anchor='center') 
button = tk.Button(footer, text="Don't click me!!", width=25, command=on_click_action)
button.place(x=35, y=10)
ui_root.mainloop()


