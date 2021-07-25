import pathlib
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText

class Notepad(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Notepad")
        self.menubar = tk.Menu(self, tearoff=False)
        self['menu'] = self.menubar
        self.menu_file = tk.Menu(self.menubar, tearoff=False)
        self.menu_tools = tk.Menu(self.menubar, tearoff=False)
        self.menu_help = tk.Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(menu=self.menu_file, label='File')
        self.menubar.add_cascade(menu=self.menu_tools, label='Tools')
        self.menubar.add_cascade(menu=self.menu_help, label='Help')
        self.menu_file.add_command(label='Novo', accelerator='Ctrl+N', command=self.new_file)
        self.menu_file.add_command(label='Abrir', accelerator='Ctrl+O', command=self.open_file)
        self.menu_file.add_command(label='Salvar', accelerator='Ctrl+S', command=self.save_file)
        self.menu_file.add_command(label='Salvar como', command=self.save_file_as)
        self.menu_file.add_separator()
        self.menu_file.add_command(label='Sair', command=self.destroy)
        self.menu_tools.add_command(label='Contar palavras', command=self.word_count)
        self.menu_help.add_command(label='Sobre', command=self.about_me)
        self.info_var = tk.StringVar()
        self.info_var.set('>  New File  <')
        self.info_bar = tk.Label(self, textvariable=self.info_var, bg='#333', fg='white')
        self.info_bar.configure(anchor=tk.W, font='-size -14 -weight bold', padx=5, pady=5)
        self.text = ScrolledText(self, font='-size -16')
        self.info_bar.pack(side=tk.TOP, fill=tk.X)
        self.text.pack(fill=tk.BOTH, expand=tk.YES)
        self.file = None

        self.bind("<Control-n>", self.new_file)
        self.bind("<Control-s>", self.save_file)
        self.bind("<Control-o>", self.open_file)

    def open_file(self, event=None):
        """Open file and update infobar"""
        file = filedialog.askopenfilename(title='Abrir', filetypes=(('Text', '*.txt'), ('All Files', '*.*')))
        if file:
            self.file = pathlib.Path(file)
            self.text.delete('1.0', tk.END)
            self.text.insert(tk.END, self.file.read_text())
            self.info_var.set(self.file.absolute())

    def new_file(self, event=None):
        """Reset body and clear variables"""
        self.file = None
        self.text.delete('1.0', tk.END)
        self.info_var.set('>  Novo arquivo  <')

    def save_file(self, event=None):
        """Save file instantly, otherwise use Save As method"""
        if self.file:
            text = self.text.get('1.0', tk.END)
            self.file.write_text(text)
        else:
            self.save_file_as()

    def save_file_as(self):
        """Save new file or existing file to new name or location"""
        file = filedialog.asksaveasfilename(title="Salvar", filetypes=(('Text', '*.txt'),('All Files', '*.*')))
        if file:
            self.file = pathlib.Path(file)
            text = self.text.get('1.0', tk.END)
            self.file.write_text(text)
            self.info_var.set(self.file.absolute())

    def word_count(self):
        """Display estimated word count"""
        words = list(self.text.get('1.0', tk.END).split(' '))
        word_count = len(words)
        messagebox.showinfo(title='Contar palavras', message=f'Contar palavras: {word_count:,d}')

    def about_me(self):
        """Short pithy quote"""
        text = '"All great things have small beginnings" - Peter Senge'
        messagebox.showinfo(title="Sobre", message=text)

if __name__ == '__main__':
    app = Notepad()
    app.mainloop()
