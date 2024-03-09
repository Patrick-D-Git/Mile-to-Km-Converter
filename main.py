import tkinter as tk


def convert(label):
    """function that converts miles to km and display it in a label"""
    number_of_miles = float(input_box.get())
    kilometers = round(number_of_miles * 1.60934)
    label.config(text=f"{kilometers}")


window = tk.Tk()  # Create a tkinter window
# center_window(window, window_width, window_height)  # Center the window on the screen
window.config()
window.title("Mile to Km Converter")
window.geometry("+100+100")
input_box = tk.Entry(window, width=5)

equal_to_label = tk.Label(window, text="is equal to")
miles_label = tk.Label(window, text="Miles")
km_label = tk.Label(window, text="Km")
result_label = tk.Label(window, text=f" ")

calculate_button = tk.Button(window, text="Convert", command=lambda: convert(result_label))

equal_to_label.grid(row=1, column=0, padx=10, pady=10)
input_box.grid(row=0, column=1, padx=10, pady=10)
miles_label.grid(row=0, column=2, padx=10, pady=10)
result_label.grid(row=1, column=1, padx=10, pady=10)
km_label.grid(row=1, column=2, padx=10, pady=10)
calculate_button.grid(row=2, column=1, pady=10)

window.mainloop()
