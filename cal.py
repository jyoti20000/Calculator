import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        
        # Entry widget to display the result
        self.result_var = tk.StringVar()
        entry = tk.Entry(root, textvariable=self.result_var, font=('Arial', 18), bd=10, insertwidth=4, width=14, justify='right')
        entry.grid(row=0, column=0, columnspan=4)
        
        # Buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('AC', 4, 2), ('+', 4, 3),
            ('+/-', 5, 0), ('.', 5, 1), ('=', 5, 2)
        ]
        
        for (text, row, column) in buttons:
            btn = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14), command=lambda t=text: self.button_click(t))
            btn.grid(row=row, column=column)

        # Internal variables
        self.current_number = ''
        self.result = 0
        self.last_operation = ''
        self.display_error = False

    def button_click(self, button_text):
        if button_text.isdigit() or button_text == '.':
            self.handle_number(button_text)
        elif button_text in {'+', '-', '*', '/'}:
            self.handle_operation(button_text)
        elif button_text == '=':
            self.calculate_result()
        elif button_text == 'C':
            self.clear_last()
        elif button_text == 'AC':
            self.clear_all()
        elif button_text == '+/-':
            self.change_sign()

    def handle_number(self, button_text):
        if len(self.current_number) < 8:
            if button_text == '.' and '.' in self.current_number:
                return
            self.current_number += button_text
            self.display_error = False
            self.update_display()

    def handle_operation(self, operation):
        if self.current_number:
            self.calculate_result()
            self.last_operation = operation
            self.current_number = ''
        elif self.last_operation:
            self.last_operation = operation
            self.update_display()

    def calculate_result(self):
        try:
            if self.last_operation == '+':
                self.result += float(self.current_number)
            elif self.last_operation == '-':
                self.result -= float(self.current_number)
            elif self.last_operation == '*':
                self.result *= float(self.current_number)
            elif self.last_operation == '/':
                if float(self.current_number) == 0:  # Check for division by zero
                    raise ZeroDivisionError
                self.result /= float(self.current_number)
            else:
                self.result = float(self.current_number)
        except ZeroDivisionError:
            self.display_error = True
            self.result_var.set('ERR')
            self.result = 0  # Reset the result to avoid incorrect calculations after an error
            self.current_number = ''
            self.last_operation = ''
            return
        self.current_number = ''
        self.last_operation = ''
        self.update_display()

    def clear_last(self):
        if self.current_number:
            self.current_number = ''
        elif self.last_operation:
            self.last_operation = ''
        elif self.result != 0:
            self.result = 0
        self.update_display()

    def clear_all(self):
        self.current_number = ''
        self.result = 0
        self.last_operation = ''
        self.display_error = False
        self.update_display()

    def change_sign(self):
        if self.current_number:
            if self.current_number[0] == '-':
                self.current_number = self.current_number[1:]
            else:
                self.current_number = '-' + self.current_number
            self.update_display()

    def update_display(self):
        if self.display_error:
            self.result_var.set('ERR')
        elif self.current_number:
            self.result_var.set(self.current_number)
        else:
            self.result_var.set(str(self.result))

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
