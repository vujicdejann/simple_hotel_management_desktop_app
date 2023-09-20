from tkinter import *
import check_in_ui
import check_out
import get_info
import customer_info
import os


class Hotel:
    def __init__(self, root):
        self.root = root
        pad = 3
        self.root.title("Hotelski sistem za rezevacije")
        self.root.geometry(
            "{0}x{1}+0+0".format(self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad))

        # Glavni okvir za obaveštenja i informacije
        top = Frame(self.root)
        top.pack(side="top")

        # Okvir za dugme
        bottom = Frame(self.root)
        bottom.pack(side="top")

        # Prikaz informacija
        self.label = Label(top, font=('arial', 50, 'bold'), text="Hotelski sistem rezvacija", fg="#CE0404", anchor="center")
        self.label.grid(row=0, column=3)

        # Check-in dugme
        self.check_in_button = Button(bottom, text="Check-in", font=('', 20), bg="#CE0404", relief=RIDGE, height=2,
                                      width=50,
                                      fg="white", anchor="center",
                                      command=check_in_ui.check_in_ui_fun)  # call check_in_ui_fun from check_in_ui.py file
        self.check_in_button.grid(row=0, column=2, padx=10, pady=10)

        # Check-out dugme
        self.check_out_button = Button(bottom, text="Check-out", font=('', 20), bg="#CE0404", relief=RIDGE, height=2,
                                       width=50, fg="white", anchor="center",
                                       command=check_out.check_out_ui)  # call check_out_ui function from check_out.py file
        self.check_out_button.grid(row=1, column=2, padx=10, pady=10)

        # Informacije o sobama dugme
        self.room_info_button = Button(bottom, text="Informacije o sobama", font=('', 20), bg="#CE0404", relief=RIDGE,
                                       height=2,
                                       width=50, fg="white", anchor="center",
                                       command=get_info.get_info_ui)  # call get_info_ui function from get_info.py file
        self.room_info_button.grid(row=2, column=2, padx=10, pady=10)

        # Informacije o gostima dugme
        self.get_info_button = Button(bottom, text="Informacije o gostima", font=('', 20), bg="#CE0404",
                                      relief=RIDGE,
                                      height=2, width=50, fg="white", anchor="center",
                                      command=customer_info.customer_info_ui)
        # Poziv funkcije
        self.get_info_button.grid(row=3, column=2, padx=10, pady=10)

        # Break - kraj programa
        self.exit_button = Button(bottom, text="Izlaz", font=('', 20), bg="#CE0404", relief=RIDGE, height=2, width=50,
                                  fg="white",
                                  anchor="center", command=quit)
        self.exit_button.grid(row=4, column=2, padx=10, pady=10)


def home_ui():
    root = Tk()
    application = Hotel(root)
    root.mainloop()


if __name__ == '__main__':
    home_ui()
