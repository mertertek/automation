import re
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox, filedialog

card = "automation.html"

def get_valid_name(name_surname):
    if not name_surname.strip():
        raise ValueError("Name and surname cannot be empty.")

    if len(name_surname) > 25:
        raise ValueError("Name and surname cannot be more than 25 characters.")

    if not re.fullmatch(r"[A-Za-z\sçöğüşıÇÖĞÜŞİ]+", name_surname):
        raise ValueError("Name and surname should only contain letters and spaces.")

    return name_surname



def get_valid_url(url):
    if not url.strip():
        raise ValueError("URL cannot be empty.")
    return url

def update_html(name_surname, url, save_path):
    with open(card, 'r', encoding='utf-8') as html_file:
        content = html_file.read()

    soup = BeautifulSoup(content, 'html.parser')
    tags = soup.find("img")

    tags['alt'] = name_surname
    tags['src'] = url
    print("Updated <img> tag:", tags)

    updated_content = soup.prettify()

    with open(save_path, 'w', encoding='utf-8') as html_file:
        html_file.write(updated_content)

    print("Updated HTML:", updated_content)


def submit():
    try:
        name_surname = get_valid_name(entry_name.get())
        url = get_valid_url(entry_url.get())
        save_path = filedialog.asksaveasfilename(defaultextension=".html", filetypes=[("HTML files", "*.html")])
        if not save_path:
            return
        update_html(name_surname, url, save_path)
        messagebox.showinfo("Success", "HTML file updated and saved successfully.")
    except Exception as e:
        messagebox.showerror("Error", str(e))



root = tk.Tk()
root.title("HTML Updater")

tk.Label(root, text="Enter your name and surname:").grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(root, width=40)
entry_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Enter the new URL for the image:").grid(row=1, column=0, padx=10, pady=5)
entry_url = tk.Entry(root, width=40)
entry_url.grid(row=1, column=1, padx=10, pady=5)

submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
