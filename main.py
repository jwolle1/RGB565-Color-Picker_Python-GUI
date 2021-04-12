from tkinter import *


def update_r(value):
    r_pct = "{:.1f}%".format(int(value) / 31 * 100)
    label_r_output.config(text=r_pct)
    update_final_output()


def update_g(value):
    g_pct = "{:.1f}%".format(int(value) / 63 * 100)
    label_g_output.config(text=g_pct)
    update_final_output()


def update_b(value):
    b_pct = "{:.1f}%".format(int(value) / 31 * 100)
    label_b_output.config(text=b_pct)
    update_final_output()


def update_final_output():
    label_color_output.config(bg=slider_to_888())
    label_rgb565_output.config(text=slider_to_565())
    label_rgb888_output.config(text=slider_to_888())


def slider_to_565():
    r = scale_r.get()
    g = scale_g.get()
    b = scale_b.get()
    return "#{:04X}".format(r << 11 | g << 5 | b)


def slider_to_888():
    r_hex = "{:02X}".format(round(scale_r.get() / 31 * 255))
    g_hex = "{:02X}".format(round(scale_g.get() / 63 * 255))
    b_hex = "{:02X}".format(round(scale_b.get() / 31 * 255))
    return f"#{r_hex}{g_hex}{b_hex}"


def copy_rgb565():
    txt = label_rgb565_output.cget("text")
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append(txt)


def copy_rgb888():
    txt = label_rgb888_output.cget("text")
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append(txt)


text_font = "Arial"
slider_length = 120

root = Tk()

root.title("RGB-565-888 Color Picker")

label_r = Label(root, text="Red", font=(text_font, 14, "bold"), fg="black")
label_r.grid(row=10, column=0, pady=(15, 0), padx=(20, 10))

label_g = Label(root, text="Green", font=(text_font, 14, "bold"), fg="black")
label_g.grid(row=10, column=1, pady=(15, 0), padx=(10, 10))

label_b = Label(root, text="Blue", font=(text_font, 14, "bold"), fg="black")
label_b.grid(row=10, column=2, pady=(15, 0), padx=(10, 20))

scale_r = Scale(root, from_=0, to=31, resolution=1, length=slider_length, orient=HORIZONTAL, font=(text_font, 12), command=update_r)
scale_r.set(21)
scale_r.grid(row=15, column=0, padx=(20, 10))

scale_g = Scale(root, from_=0, to=63, resolution=1, length=slider_length, orient=HORIZONTAL, font=(text_font, 12), command=update_g)
scale_g.set(14)
scale_g.grid(row=15, column=1, padx=(10, 10))

scale_b = Scale(root, from_=0, to=31, resolution=1, length=slider_length, orient=HORIZONTAL, font=(text_font, 12), command=update_b)
scale_b.set(18)
scale_b.grid(row=15, column=2, padx=(10, 20))

label_r_output = Label(root, text=None, font=(text_font, 12), fg="black", bg=None)
label_r_output.grid(row=20, column=0, pady=(10, 10), padx=(20, 10))

label_g_output = Label(root, text=None, font=(text_font, 12), fg="black", bg=None)
label_g_output.grid(row=20, column=1, pady=(10, 10), padx=(10, 10))

label_b_output = Label(root, text=None, font=(text_font, 12), fg="black", bg=None)
label_b_output.grid(row=20, column=2, pady=(10, 10), padx=(10, 20))

label_rgb565_output = Label(root, text=None, font=(text_font, 16, "bold"), fg="black")
label_rgb565_output.grid(row=25, column=0, pady=(20, 0), padx=(20, 10))

label_color_output = Label(root, text=None, fg="black", width=12, height=3)
label_color_output.grid(row=25, column=1, pady=(20, 0), padx=(5, 5))

label_rgb888_output = Label(root, text=None, font=(text_font, 16, "bold"), fg="black")
label_rgb888_output.grid(row=25, column=2, pady=(20, 0), padx=(10, 20))

button_copy565 = Button(root, text="Copy", font=(text_font, 10), width=5, height=1, bg="gray", command=copy_rgb565)
button_copy565.grid(row=30, column=0, padx=(20, 10), pady=(0, 15), sticky="n")

button_copy888 = Button(root, text="Copy", font=(text_font, 10), width=5, height=1, bg="gray", command=copy_rgb888)
button_copy888.grid(row=30, column=2, padx=(10, 20), pady=(0, 15), sticky="n")

root.mainloop()
