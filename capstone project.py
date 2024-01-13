import tkinter as tk
from tkinter import ttk, Text, messagebox
# for the themed widgets, text widget, displaying message boxes


class FeedBack:
    def __init__(self):
        self.main_window = tk.Tk()

        self.main_window.title('feedback')

        self.frame_header = ttk.Frame(self.main_window)
        self.frame_header.pack()

        self.header_label = ttk.Label(self.frame_header, text='L&D FEEDBACK SYSTEM', foreground='brown',
                                      font=('Arial', 24, 'bold'))
        self.header_label.grid(row=0, column=1, pady=10)
        # learned that grid is for grid-based layout while pack is for block-based layout
        self.message_label = ttk.Label(self.frame_header,
                                       text='PLEASE TELL US YOUR EXPERIENCE',
                                       foreground='green', font=('Arial', 10, 'bold'))
        self.message_label.grid(row=1, column=1)

        self.frame_content = ttk.Frame(self.main_window)
        self.frame_content.pack()

        self.name_label = ttk.Label(self.frame_content, text='name of student: ')
        self.name_label.grid(row=0, column=0, padx=10, pady=7, sticky='sw')
        self.entry_name = ttk.Entry(self.frame_content, width=18, font=('Arial', 14))
        self.entry_name.grid(row=1, column=0)

        self.email_label = ttk.Label(self.frame_content, text='email of student: ')
        self.email_label.grid(row=0, column=1, padx=10, pady=7, sticky='sw')
        self.entry_email = ttk.Entry(self.frame_content, width=18, font=('Arial', 14))
        self.entry_email.grid(row=1, column=1)

        self.comment_label = ttk.Label(self.frame_content, text='please include feedback for deodat', font=('Arial', 10))
        self.comment_label.grid(row=2, column=0, padx=7, pady=7, sticky='sw')
        self.text_comment = Text(self.frame_content, width=55, height=10)
        self.text_comment.grid(row=3, column=0, padx=10, columnspan=2)

        self.text_comment.config(wrap='word')

        def clear():
            messagebox.showinfo(title='clear', message='are you sure?')
            self.entry_name.delete(0, tk.END)
            self.entry_email.delete(0, tk.END)
            self.text_comment.delete(1.0, tk.END)

        def submit():
            messagebox.showinfo(title='submit', message='thank you for your feedback, your comments have been submitted')
            self.entry_name.delete(0, tk.END)
            self.entry_email.delete(0, tk.END)
            self.text_comment.delete(1.0, tk.END)

        submit_button = ttk.Button(self.frame_content, text='submit', command=submit)
        submit_button.grid(row=4, column=0, pady=10, sticky='e')
        clear_button = ttk.Button(self.frame_content, text='clear', command=clear)
        clear_button.grid(row=4, column=1, pady=10, sticky='w')


if __name__ == '__main__':
    feedback_app = FeedBack()
    feedback_app.main_window.mainloop()
