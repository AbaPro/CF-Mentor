import tkinter as tk
from tkinter import ttk
from quotes import get_quote

def startMain():
    handle=inputF.get()
    if(handle!=''):
        W_notebook.pack_forget()
        print(handle)



if __name__ == '__main__':
    root = tk.Tk()
    root.title("CF Mentor")
    root.option_add("*tearOff", False)

    # Create a style
    style = ttk.Style(root)
    # Import the tcl file
    root.tk.call("source", "forest-light.tcl")
    # Set the theme with the theme_use method
    style.theme_use("forest-light")

    handle=""
    quote,author=get_quote()
    W_notebook = ttk.Notebook(root)
    W_tab_1 = ttk.Frame(W_notebook)
    W_tab_1.columnconfigure(index=0, weight=1)
    W_tab_1.columnconfigure(index=1, weight=1)
    W_tab_1.rowconfigure(index=0, weight=1)
    W_tab_1.rowconfigure(index=1, weight=1)
    W_notebook.add(W_tab_1, text=f"Welcome {handle}!")
    label = tk.Label(W_tab_1, text=" Are You Ready to Practice?",justify='center')
    label.grid(row=0, column=0, padx=(10, 10), pady=(20, 45), sticky="ew")
    inputF = tk.Entry(W_tab_1)
    if handle == "":
        nameLabel = tk.Label(W_tab_1,text='enter your cf handle first')
        nameLabel.grid(row=1, column=0, padx=(50, 50), sticky="nsew")
        inputF.grid(row=2, column=0, padx=(10, 10), pady=(0, 20), sticky="s",columnspan=2)
    W_accentbutton = ttk.Button(W_tab_1, text="Yes!", style="Accent.TButton",command=startMain)
    W_accentbutton.grid(row=3, column=0, padx=5, pady=15, sticky="s")
    quotesLabel = tk.Label(W_tab_1,text=quote)
    quotesLabel.grid(row=4, column=0, padx=20, sticky="nsew")
    authorLabel = tk.Label(W_tab_1,text=author)
    authorLabel.grid(row=5, column=0, padx=15,  sticky="nsew")
    W_notebook.pack(expand=True, fill="both", padx=25, pady=15)

    # Center the window, and set minsize
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cordinate = int((root.winfo_screenwidth()/2) - (root.winfo_width()/2))
    y_cordinate = int((root.winfo_screenheight()/2) - (root.winfo_height()/2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate))
    # Start the main loop
    root.mainloop()