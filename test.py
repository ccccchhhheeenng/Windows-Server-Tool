import tkinter as tk

win = tk.Tk()
win.geometry("700x350")  # Set the size of the Tkinter window

# Add a frame to set the size of the window
my_frame = tk.Frame(win, relief="sunken")
my_frame.grid(sticky="s")  # Make the frame sticky for both west and east

# Create and add your widget (e.g., a button) to my_frame
my_button = tk.Button(my_frame, text="Click Me")
my_button.grid()  # By default, it will be centered within the frame

win.mainloop()
