from tkinter import * 

def normal_mod_hover(parent):
    hover=Message(parent," In this mode you have to solve one calculation at a time with no time limit. \
                        If you make a mistake the game will be over")
    hover.pack(side="bottom")
    return


if __name__ == "__main__":
    print("Esti in gui")
    root= Tk()
    root.title("Math calculus game")
    root.geometry('500x300')
    frame=Frame(root)
    frame.pack()
    choose_style_label=Label(frame,text="Choose the game style:")
    choose_style_label.pack()               
    button_normal_mod=Button(frame,text="Normal")
    button_normal_mod.bind('<Enter>',normal_mod_hover(button_normal_mod))
    button_snow_ball_mod=Button(frame,text="Snow-ball")
    button_normal_mod.pack(side='left')
    button_snow_ball_mod.pack()
    root.mainloop()  