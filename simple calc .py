from tkinter import Tk, Button, Entry, Label

class MyCalc:
    def __init__(self, window):
        self.window = window
        self.window.title("Simple Calculator")

        self.entry = Entry(window, width=14, font=('Calibri', 16), borderwidth=4, relief="solid")
        self.entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            Button(window, text=button, width=4, height=2, command=lambda b=button: self.on_button_click(b)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, button):
        current_text = self.entry.get()

        if button == '=':
            try:
                result = eval(current_text)
                self.entry.delete(0, 'end')
                self.entry.insert('end', str(result))
            except Exception as e:
                self.entry.delete(0, 'end')
                self.entry.insert('end', 'Error')
        else:
            self.entry.insert('end', button)


window = Tk()
calc = MyCalc(window)
window.mainloop()
