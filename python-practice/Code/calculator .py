import tkinter as tk

class SimpleCalculator:
    def __init__(self, window):
        # Set up the main window
        self.main_window = window
        self.main_window.title("My Awesome Calculator")

        # Input display
        self.result_display = tk.Entry(self.main_window, width=25, font=('Helvetica', 14))
        self.result_display.grid(row=0, column=0, columnspan=4, padx=8, pady=8)

        # Define button labels
        button_digits = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '0']
        button_operators = ['/', '*', '-', '+', '=', 'Clear']

        # Create and place digit buttons
        row_num = 1
        col_num = 0
        for digit in button_digits:
            digit_button = tk.Button(
                self.main_window,
                text=digit,
                width=5,
                height=2,
                command=lambda d=digit: self.update_display(d)
            )
            digit_button.grid(row=row_num, column=col_num, padx=5, pady=5)
            col_num += 1
            if col_num > 2:
                col_num = 0
                row_num += 1

        # Create and place operator buttons
        for operator in button_operators:
            operator_button = tk.Button(
                self.main_window,
                text=operator,
                width=5,
                height=2,
                command=lambda op=operator: self.process_operation(op)
            )
            operator_button.grid(row=row_num, column=col_num, padx=5, pady=5)
            col_num += 1
            if col_num > 3:
                col_num = 0
                row_num += 1

    def update_display(self, value):
        # Add the clicked digit to the display
        self.result_display.insert(tk.END, value)

    def process_operation(self, operation):
        if operation == 'Clear':
            # Clear the display
            self.result_display.delete(0, tk.END)
        elif operation == '=':
            # Evaluate the expression
            try:
                expression = self.result_display.get()
                calculation_result = eval(expression)
                self.result_display.delete(0, tk.END)
                self.result_display.insert(tk.END, calculation_result)
            except Exception:
                self.result_display.delete(0, tk.END)
                self.result_display.insert(tk.END, "Error!")
        else:
            # Append the operator to the display
            self.result_display.insert(tk.END, operation)

# Create the main Tkinter window
root_window = tk.Tk()
calculator_app = SimpleCalculator(root_window)

# Start the Tkinter event loop
root_window.mainloop()