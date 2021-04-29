import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

class Application(tk.Frame):
    def __init__(self, master=None, title="<application>", **kwargs):
        super().__init__(master, **kwargs)
        self.master.title(title)
        self.rowconfigure(0, minsize=640, weight=1)
        self.columnconfigure(1, minsize=800, weight=1)
        self.grid(sticky = "news")
        self.createWidgets()
    
    def createWidgets(self):
        self.txt_edit = tk.Text(self, undo=True, width=40, height=15, font='fixed', borderwidth=2, relief='groove')
        self.fr_buttons = tk.Frame(self)

        self.scale_option_list = ["25%", "50%", "75%", "100%", "125%"]

        self.scale_option = tk.StringVar(self)
        self.scale_option.set(self.scale_option_list[2])
        self.scale = tk.OptionMenu(self.fr_buttons, self.scale_option, *self.scale_option_list)
        self.scale.config(width=1)
        self.scale_option.trace("w", self.change_scale)

        self.btn_open = tk.Button(self.fr_buttons, text="Open", command=self.file_open)
        self.btn_save = tk.Button(self.fr_buttons, text="Save")
        self.btn_save_as = tk.Button(self.fr_buttons, text="Save As", command=self.save_as)
        self.close = tk.Button(self.fr_buttons, text="Close", command=self.file_close)

        self.btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        self.btn_save.grid(row=1, column=0, sticky="ew", padx=5)
        self.btn_save_as.grid(row=1, column=1, sticky="ew", padx=5)
        self.close.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
        self.scale.grid(row=2, column=1, sticky="ew", padx=5, pady=5)
        self.fr_buttons.grid(row=0, column=0, sticky="ns")
        self.txt_edit.grid(row=0, column=1, sticky="nsew")

    def change_scale(self, *args):
        if self.scale_option.get() == self.scale_option_list[0]:
            self.txt_edit.config(font=('Helvetica', 4))
        elif self.scale_option.get() == self.scale_option_list[1]:
            self.txt_edit.config(font=('Helvetica', 8))
        elif self.scale_option.get() == self.scale_option_list[2]:
            self.txt_edit.config(font=('Helvetica', 12))
        elif self.scale_option.get() == self.scale_option_list[3]:
            self.txt_edit.config(font=('Helvetica', 16))
        elif self.scale_option.get() == self.scale_option_list[4]:
            self.txt_edit.config(font=('Helvetica', 20))

        self.txt_edit.insert(tk.END, "")

    def save_as(self):
        """Saves the current file as new"""
        path_to_file = asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text files","*.txt"),("All files", "*.*")]
        )
        if not path_to_file:
            return
        with open(path_to_file, "w") as output_file:
            text = self.txt_edit.get("1.0", tk.END)
            output_file.write(text)
        self.master.title(f"Gavrix - {path_to_file}")

    def file_open(self):
        """Opens the file that user wants to edit"""
        path_to_file = askopenfilename(
                filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if not path_to_file:
            return
        self.txt_edit.delete("1.0", tk.END)
        with open(path_to_file, "r") as input_file:
            text = input_file.read()
            self.txt_edit.insert(tk.END, text)
        self.master.title(f"Gavrix - {path_to_file}")

    def file_close(self):
        self.txt_edit.delete("1.0", tk.END)
        self.master.title(f"Gavrix - NewFile.txt")

app = Application(title="Gavrix - NewFile.txt")
app.mainloop()
