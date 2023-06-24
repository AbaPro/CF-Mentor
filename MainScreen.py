import requests
import datetime
import tkinter as tk
from tkinter import ttk
from Hyperlink import Hyperlink

def on_select(event):
    # Get the selected row
    selected_item = treeview.focus()
    values = treeview.item(selected_item, 'values')
    # Set the label to the value of the selected row
    try:
        labelgg.config(text=values[1])
        Hyperlink.change_url(ContestLink,f"https://codeforces.com/contest/{values[0]}")
    except:
        print("error")


if __name__ == '__main__':
    root = tk.Tk()
    root.title("CF Mentor")
    root.option_add("*tearOff", False) # This is always a good idea


    # Make the app responsive
    root.columnconfigure(index=0, weight=1)
    root.columnconfigure(index=1, weight=1)
    root.columnconfigure(index=2, weight=1)
    root.rowconfigure(index=0, weight=1)
    root.rowconfigure(index=1, weight=1)
    root.rowconfigure(index=2, weight=1)

    # Create a style
    style = ttk.Style(root)
    # Import the tcl file
    root.tk.call("source", "forest-light.tcl")
    # Set the theme with the theme_use method
    style.theme_use("forest-light")

    placeholder="N/A"

    user_res=requests.get("https://codeforces.com/api/user.info?handles=abanobRaffet")
    user_res_data=user_res.json()
    user_result=user_res_data['result']
    user_rank=user_result[0]['rank']
    user_handle=user_result[0]['handle']
    user_rating=user_result[0]['rating']

    # Create a Frame for the User Info
    user_frame = ttk.LabelFrame(root, text="Welcome", padding=(20, 10))
    user_frame.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")
    rank_label=ttk.Label(user_frame,text=f"Rank: {user_rank}")
    rank_label.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")
    handle_label=ttk.Label(user_frame,text=f"Handle: {user_handle}")
    handle_label.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")
    rating_label=ttk.Label(user_frame,text=f"Rating: {user_rating}")
    rating_label.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")
    profile_link=Hyperlink(user_frame,url=f'https://codeforces.com/profile/{user_handle}',text='Codeforces Profile')
    profile_link.grid(row=3, column=0, padx=5, pady=10, sticky="nsew")

    separator = ttk.Separator(root)
    separator.grid(row=1, column=0, padx=(20, 10), pady=10, sticky="ew")

    # Create a Frame for the Buttons
    buttons_frame = ttk.LabelFrame(root, text="Solve", padding=(20, 10))
    buttons_frame.grid(row=2, column=0, padx=(20, 10), pady=10, sticky="nsew")
    button1 = ttk.Button(buttons_frame, text="Let's Solve", style="Accent.TButton")
    button1.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")
    button2 = ttk.Button(buttons_frame, text="Rescources")
    button2.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")
    # Panedwindow
    paned = ttk.PanedWindow(root)
    paned.grid(row=0, column=2, pady=(25, 5), sticky="nsew", rowspan=3)



    pane_1 = ttk.Frame(paned)
    paned.add(pane_1, weight=1)


    # Create a Frame for the Treeview
    treeFrame = ttk.Frame(pane_1)
    treeFrame.pack(expand=True, fill="both", padx=5, pady=5)
    # Scrollbar
    treeScroll = ttk.Scrollbar(treeFrame)
    treeScroll.pack(side="right", fill="y")

    # Treeview
    treeview = ttk.Treeview(treeFrame, selectmode="extended", yscrollcommand=treeScroll.set, columns=(1,2,3,4), height=12)
    treeview.bind('<<TreeviewSelect>>', on_select)
    treeview.pack(expand=True, fill="both")
    treeScroll.config(command=treeview.yview)
    # Treeview columns
    treeview.column("#0", width=10)
    treeview.column(1, anchor="w", width=40)
    treeview.column(2, anchor="w", width=315)
    treeview.column(3, anchor="w", width=70)
    treeview.column(4, anchor="w", width=120)
    # Treeview headings
    treeview.heading("#0", text="#", anchor="w")
    treeview.heading(1, text="ID", anchor="w")
    treeview.heading(2, text="Name", anchor="w")
    treeview.heading(3, text="Phase", anchor="w")
    treeview.heading(4, text="Date", anchor="w")


    # Get data from API call
    response = requests.get('https://codeforces.com/api/contest.list?gym=false')
    response_json=response.json()
    i=0
    for row in response_json['result']:
        unix_timestamp = row['startTimeSeconds']
        date_obj = datetime.datetime.fromtimestamp(unix_timestamp)
        # Convert datetime object to desired string format
        date_string = date_obj.strftime('%H:%M:%S  %d-%m-%Y')
        treeview.insert(parent="", index='end', iid=i, text="", values=(row['id'],row['name'],row['phase'],date_string))
        i=i+1
        if (i==50):
            break


    # Pane #2
    pane_2 = ttk.Frame(paned)
    paned.add(pane_2, weight=3)

    # Notebook
    notebook = ttk.Notebook(pane_2)

    # Tab #1
    tab_1 = ttk.Frame(notebook)
    tab_1.columnconfigure(index=0, weight=1)
    tab_1.columnconfigure(index=1, weight=1)
    tab_1.rowconfigure(index=0, weight=1)
    tab_1.rowconfigure(index=1, weight=1)
    notebook.add(tab_1, text="Contest")

    # Problems Labels
    labelgg = ttk.Label(tab_1, text="Abanob Raffet S. Makar")
    labelgg.grid(row=0, column=0,columnspan=2)
    ContestLink = Hyperlink(tab_1,text="Contest Link",url="https://codeforces.com/")
    ContestLink.grid(row=1,column=0,columnspan=2)

    # paned.grid_remove()
    # buttons_frame.grid_remove()
    # separator.grid_remove()
    # user_frame.grid_remove()

    notebook.pack(expand=True, fill="both", padx=5, pady=5)

    # Sizegrip
    sizegrip = ttk.Sizegrip(root)
    sizegrip.grid(row=100, column=100, padx=(0, 5), pady=(0, 5))

    # Center the window, and set minsize
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cordinate = int((root.winfo_screenwidth()/2) - (root.winfo_width()/2))
    y_cordinate = int((root.winfo_screenheight()/2) - (root.winfo_height()/2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate))
    # Start the main loop
    root.mainloop()


