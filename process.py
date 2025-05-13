#This code is edited by Claude AI as it was asked for a modern UI and desgin changes.

import tkinter as tk
import os
import sys
from tkinter import font as tkfont
from utilities.function import on_click
from utilities.function import prompt
from utilities.function import randomize
from utilities.function import print_time
from PIL import Image, ImageTk, ImageSequence
from utilities.function import local_user

limit = 39
rand = randomize(17, 5)

if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(__file__)

gif_path = os.path.join(base_path, "static/animation.gif")


COLORS = {
    "primary": "#3498db",       # Blue
    "secondary": "#2ecc71",     # Green
    "accent": "#e74c3c",        # Red
    "background": "#ecf0f1",    # Light gray
    "text_dark": "#2c3e50",     # Dark blue/gray
    "text_light": "#ffffff",    # White
    "warning": "#f39c12"        # Orange
}


ui_root = tk.Tk()
ui_root.title("Don't Click It!!!")
ui_root.geometry("400x300")
ui_root.configure(bg=COLORS["background"])
ui_root.resizable(False, False)


title_font = tkfont.Font(family="Helvetica", size=14, weight="bold")
button_font = tkfont.Font(family="Helvetica", size=12, weight="bold")
text_font = tkfont.Font(family="Helvetica", size=12)
warning_font = tkfont.Font(family="Helvetica", size=36, weight="bold")


time_frame = tk.Frame(ui_root, bg=COLORS["primary"], height=30)
time_frame.pack(fill="x")

init_reference = tk.Label(time_frame, text=print_time())
init_reference.config(font=title_font, bg=COLORS["primary"], fg=COLORS["text_light"], pady=5)
init_reference.pack()


body = tk.Frame(ui_root, width=400, height=200, bg=COLORS["background"], 
               highlightbackground=COLORS["primary"], highlightthickness=2)
body.place(x=0, y=30)


footer = tk.Frame(ui_root, width=400, height=70, bg=COLORS["secondary"], 
                 highlightbackground=COLORS["text_dark"], highlightthickness=1)
footer.place(x=0, y=230)

def create_hover_effect(button):
    """Create hover effect for buttons"""
    orig_color = button["background"]
    orig_fg = button["foreground"]
    
    def on_enter(e):
        button['background'] = COLORS["accent"]
        button['foreground'] = COLORS["text_light"]
    
    def on_leave(e):
        button['background'] = orig_color
        button['foreground'] = orig_fg
        
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)
    return button

def small_boy():
    ui_root.geometry("300x200")
    ui_root.configure(bg=COLORS["accent"])
    
    body = tk.Frame(ui_root, width=300, height=200, bg=COLORS["accent"], 
                   highlightbackground=COLORS["text_dark"], highlightthickness=2)
    body.place(x=0, y=0)
    
    buttonVend = tk.Button(body, text="END", width=8, height=2, command=ui_root.quit,
                         font=button_font, bg=COLORS["text_dark"], fg=COLORS["text_light"],
                         relief="raised", borderwidth=3)
    buttonVend.place(relx=0.5, rely=0.5, anchor='center')
    create_hover_effect(buttonVend)

def master():
    global limit
    if limit == -2:
        ui_root.geometry("640x492")
        
        body2 = tk.Frame(ui_root, width=640, height=492, bg=COLORS["accent"], 
                        highlightbackground="black", highlightthickness=0)
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
        # Matrix-inspired terminal look
        ui_root.configure(bg="black")
        body2 = tk.Frame(ui_root, width=500, height=325, bg="black", 
                        highlightbackground=COLORS["secondary"], highlightthickness=3)
        body2.place(x=0, y=30) 
        p2_out = tk.Label(body2, text=text_print, font=("Courier", 24, "bold"), 
                         bg="black", fg=COLORS["secondary"], wraplength=300)
        p2_out.place(relx=0.5, rely=0.5, anchor='center') 

    elif limit == 0:
        text_print = "Hi!" + "\nUsername: " + local_user.name + "\nUser Id: " + str(local_user.id) + "\nHome Dir: " + local_user.home_dir + "\nIP Addr: " + local_user.ip_address
        # Terminal-style display with better formatting
        ui_root.configure(bg="black")
        body2 = tk.Frame(ui_root, width=500, height=325, bg="black", 
                        highlightbackground=COLORS["secondary"], highlightthickness=3)
        body2.place(x=0, y=30) 
        
        header_label = tk.Label(body2, text="SYSTEM INFO", font=("Courier", 16, "bold"), 
                              bg="black", fg=COLORS["secondary"])
        header_label.place(relx=0.5, rely=0.2, anchor='center')
        
        p2_out = tk.Label(body2, text=text_print, font=("Courier", 14), 
                         bg="black", fg=COLORS["secondary"], wraplength=400, justify="left")
        p2_out.place(relx=0.5, rely=0.5, anchor='center')

    else:
        if limit <= 1:
            footer2 = tk.Frame(ui_root, width=500, height=75, bg=COLORS["warning"], 
                             highlightbackground=COLORS["text_dark"], highlightthickness=1)
            footer2.place(x=0, y=345)  
            
            buttonV2 = tk.Button(footer2, text="Exit Now!!", width=15, command=master,
                               font=button_font, bg=COLORS["text_dark"], fg=COLORS["text_light"])
            buttonV2.place(relx=0.5, rely=0.5, anchor='center')
            create_hover_effect(buttonV2)
            
        text_print = prompt(limit)
        body2 = tk.Frame(ui_root, width=500, height=325, bg=COLORS["background"], 
                        highlightbackground=COLORS["primary"], highlightthickness=2)
        body2.place(x=0, y=30) 
        
        p2_out = tk.Label(body2, text=text_print, font=text_font, bg=COLORS["background"], 
                         fg=COLORS["text_dark"], wraplength=450)
        p2_out.place(relx=0.5, rely=0.5, anchor='center') 

    limit = limit - 1

def on_click_action():
    output_text = on_click()
    
    ui_root.geometry("500x420")
    body2 = tk.Frame(ui_root, width=500, height=345, bg=COLORS["background"], 
                    highlightbackground=COLORS["primary"], highlightthickness=2)
    body2.place(x=0, y=30)
    
    footer2 = tk.Frame(ui_root, width=500, height=75, bg=COLORS["secondary"], 
                      highlightbackground=COLORS["text_dark"], highlightthickness=1)
    footer2.place(x=0, y=345)  
    
    p_out = tk.Label(body2, text=output_text, font=text_font, bg=COLORS["background"], 
                    fg=COLORS["text_dark"], wraplength=450)
    p_out.place(relx=0.5, rely=0.5, anchor='center') 
    
    buttonV2 = tk.Button(footer2, text="Don't click me!!", width=15, height=1, command=master,
                        font=button_font, bg=COLORS["warning"], fg=COLORS["text_dark"],
                        relief="raised", borderwidth=2)
    buttonV2.place(relx=0.5, rely=0.5, anchor='center')
    create_hover_effect(buttonV2)
    
    button.destroy()
    footer.destroy()

# Warning symbol with animated effect
warning_frame = tk.Frame(body, bg=COLORS["background"], width=300, height=150)
warning_frame.place(relx=0.5, rely=0.5, anchor='center')

p_in = tk.Label(warning_frame, text="⚠️ Don't Click ⚠️", font=warning_font, 
              bg=COLORS["background"], fg=COLORS["accent"], wraplength=350)
p_in.pack()

subtitle = tk.Label(warning_frame, text="Serious warning: clicking is not advised", 
                  font=text_font, bg=COLORS["background"], fg=COLORS["text_dark"])
subtitle.pack(pady=10)


button = tk.Button(footer, text="Don't click me!!", width=20, height=1, command=on_click_action,
                 font=button_font, bg=COLORS["warning"], fg=COLORS["text_dark"],
                 relief="raised", borderwidth=3)
button.place(relx=0.5, rely=0.5, anchor='center')
create_hover_effect(button)

# Add a subtle blinking effect to make the warning more noticeable
def blink_warning():
    current_color = p_in.cget("foreground")
    next_color = COLORS["text_dark"] if current_color == COLORS["accent"] else COLORS["accent"]
    p_in.config(foreground=next_color)
    ui_root.after(800, blink_warning)

blink_warning()  # Start the blinking of the warning text

ui_root.mainloop()