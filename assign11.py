import tkinter as tk
import webbrowser

def navigate_faq():
    name = name_entry.get()
    email = email_entry.get()
    selection = option_var.get()
    
    if selection == "Instagram Ads":
        faq_url = "https://www.example.com/faq/instagram"
    elif selection == "YouTube Ads":
        faq_url = "https://www.example.com/faq/youtube"
    else:
        faq_url = "https://www.example.com/faq"
    
    command_prompt_text.set("Navigating to FAQ page...")
    webbrowser.open(faq_url)

    # Save user information to a text file
    with open("user_info.txt", "w") as file:
        file.write(f"Name: {name}\n")
        file.write(f"Email: {email}\n")
        file.write(f"Source: {selection}\n")

window = tk.Tk()
window.title("Course Enquiry Form")

name_label = tk.Label(window, text="Name:")
name_label.pack()

name_entry = tk.Entry(window, width=30)
name_entry.pack()

email_label = tk.Label(window, text="Email:")
email_label.pack()

email_entry = tk.Entry(window, width=30)
email_entry.pack()

source_label = tk.Label(window, text="Where did you hear about us?")
source_label.pack()

option_var = tk.StringVar()
option_var.set("Options")

option_menu = tk.OptionMenu(window, option_var, "Instagram Ads", "YouTube Ads", "Other")
option_menu.pack()

submit_button = tk.Button(window, text="Submit", command=navigate_faq)
submit_button.pack(pady=10)

command_prompt_text = tk.StringVar()
command_prompt_label = tk.Label(window, textvariable=command_prompt_text)
command_prompt_label.pack()

window.mainloop()
