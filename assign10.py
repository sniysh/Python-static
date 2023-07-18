import tkinter as tk
import webbrowser

def navigate_to_website():
    website = entry.get()
    command_prompt_text.set("Navigating to " + website + "...")
    webbrowser.open(website)

window = tk.Tk()
window.title("Navigator")

entry = tk.Entry(window, width=30)
entry.pack(pady=10)

button = tk.Button(window, text="Navigate", command=navigate_to_website)
button.pack()

command_prompt_text = tk.StringVar()
command_prompt_label = tk.Label(window, textvariable=command_prompt_text)
command_prompt_label.pack()

window.mainloop()
