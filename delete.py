import tkinter as tk

root = tk.Tk()
root.geometry('500x600')
root.title('Dashboard')

def bird_page():
    hide_frames()
    bird_frame.pack(pady=20)

def eggs_page():
    hide_frames()
    eggs_frame.pack(pady=20)

def feed_page():
    hide_frames()
    feed_frame.pack(pady=20)

def hide_frames():
    for frame in [bird_frame, eggs_frame, feed_frame]:
        frame.pack_forget()

def indicate(lb, page):
    hide_indicators()
    lb.config(bg='#158aff')
    page()

def hide_indicators():
    bird_indicate.config(bg='#c3c3c3')
    eggs_indicate.config(bg='#c3c3c3')
    feed_indicate.config(bg='#c3c3c3')

options_frame = tk.Frame(root, bg='#c3c3c3')
bird_btn = tk.Button(options_frame, text='bird', font=('Bold', 16), fg='#158aff', bd=0, bg='#c3c3c3',
                     command=lambda: indicate(bird_indicate, bird_page))
bird_btn.place(x=10, y=50)
bird_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
bird_indicate.place(x=3, y=50, width=5, height=40)
bird_indicate.bind("<Button-1>", lambda event: indicate(bird_indicate, bird_page))

eggs_btn = tk.Button(options_frame, text='eggs', font=('Bold', 16), fg='#158aff', bd=0, bg='#c3c3c3',
                     command=lambda: indicate(eggs_indicate, eggs_page))
eggs_btn.place(x=10, y=100)
eggs_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
eggs_indicate.place(x=3, y=100, width=5, height=40)
eggs_indicate.bind("<Button-1>", lambda event: indicate(eggs_indicate, eggs_page))

feed_btn = tk.Button(options_frame, text='feed', font=('Bold', 16), fg='#158aff', bd=0, bg='#c3c3c3',
                      command=lambda: indicate(feed_indicate, feed_page))
feed_btn.place(x=10, y=150)
feed_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
feed_indicate.place(x=3, y=150, width=5, height=40)
feed_indicate.bind("<Button-1>", lambda event: indicate(feed_indicate, feed_page))

options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=100, height=400)

main_frame = tk.Frame(root)
bird_frame = tk.Frame(main_frame)
bird_label = tk.Label(bird_frame, text='bird Page\n\nPage:1', font=('Bold', 30))
bird_label.pack()
eggs_frame = tk.Frame(main_frame)
eggs_label = tk.Label(eggs_frame, text='eggs Page\n\nPage:2', font=('Bold', 30))
eggs_label.pack()
feed_frame = tk.Frame(main_frame)
feed_label = tk.Label(feed_frame, text='feed Page\n\nPage:3', font=('Bold', 30))
feed_label.pack()

main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=400, width=500)

root.mainloop()
