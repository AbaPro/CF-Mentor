import tkinter as tk
import requests
from tkinter import ttk
from Hyperlink import Hyperlink

def on_select(event):
    # Get the selected row
    selected_item = treeview.focus()
    values = treeview.item(selected_item, 'values')
    # Set the label to the value of the selected row
    try:
        labelgg.config(text=values[2])
        Hyperlink.change_url(ContestLink,f"https://codeforces.com/problemset/problem/{values[0]}/{values[1]}")
    except:
        print("error")

def getnewProblems():
    response = requests.get(' https://codeforces.com/api/problemset.problems')
    res=response.json()
    problemset=res['result']['problems']
    userRating=1000
    c=0
    probs=[]
    for i in problemset:
        if i.get('rating'):
            if i not in solvedProblems and i.get('rating')>userRating-150 and i.get('rating')<userRating+150:
                if i==4:
                    break
                probs.append(i)
    Problem1Name.config(text=probs[0]['name'])
    rate='not found'
    if probs[0].get('rating'):
        rate=probs[0]['rating']
    Problem1Rate.config(text=rate) 
    
    Problem2Name.config(text=probs[1]['name'])
    rate='not found'
    if probs[1].get('rating'):
        rate=probs[1]['rating']
    Problem2Rate.config(text=rate)
    
    Problem3Name.config(text=probs[2]['name'])
    rate='not found'
    if probs[2].get('rating'):
        rate=probs[2]['rating']
    Problem3Rate.config(text=rate)


    # Hyperlink.change_url(ContestLink,f"https://codeforces.com/contest/{values[0]}")



def isDup(name,list):
    for problem in list:
        if problem['name']==name:
            return True
    return False

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

    response = requests.get('https://codeforces.com/api/user.status?handle=abanobRaffet')
    d=response.json()
    solvedProblems=[]
    for i in d['result']:
        problem=i['problem']
        if i['verdict']=='OK' and not isDup(problem['name'],solvedProblems):
            solvedProblems.append(problem)

    # Create a Frame for the User Info
    user_frame = ttk.LabelFrame(root, text="Suggested Problems", padding=(20, 10))
    user_frame.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")

    label = tk.Label(user_frame, text=" Problem Name",justify='center')
    label.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="ew")
    label2 = tk.Label(user_frame, text=" Problem Rate",justify='center')
    label2.grid(row=0, column=1, padx=(10, 10), pady=(10, 10), sticky="ew")
    label3 = tk.Label(user_frame, text=" Problem Link",justify='center')
    label3.grid(row=0, column=2, padx=(10, 10), pady=(10, 10), sticky="ew")

    separator = ttk.Separator(user_frame)
    separator.grid(row=1, column=1, padx=(20, 10), pady=2, sticky="ew")
    separator2 = ttk.Separator(user_frame)
    separator2.grid(row=1, column=0, padx=(20, 10), pady=2, sticky="ew")
    separator3 = ttk.Separator(user_frame)
    separator3.grid(row=1, column=2, padx=(20, 10), pady=2, sticky="ew")


    Problem1Name=tk.Label(user_frame, text="Click Shuffle",justify='center')
    Problem1Name.grid(row=2, column=0, padx=(10, 10), sticky="ew")
    Problem1Rate=tk.Label(user_frame,text="Problem Rating",justify='center')
    Problem1Rate.grid(row=2,column=1,padx=(10,10),sticky='ew')
    Problem1Link=Hyperlink(user_frame,url="--",text="Codeforces Link")
    Problem1Link.grid(row=2,column=2,padx=(10,10),sticky='ew')

    Problem2Name=tk.Label(user_frame, text="Click Shuffle",justify='center')
    Problem2Name.grid(row=3, column=0, padx=(10, 10), sticky="ew")
    Problem2Rate=tk.Label(user_frame,text="Problem Rating",justify='center')
    Problem2Rate.grid(row=3,column=1,padx=(10,10),sticky='ew')
    Problem2Link=Hyperlink(user_frame,url="--",text="Codeforces Link")
    Problem2Link.grid(row=3,column=2,padx=(10,10),sticky='ew')

    Problem3Name=tk.Label(user_frame, text="Click Shuffle",justify='center')
    Problem3Name.grid(row=4, column=0, padx=(10, 10), sticky="ew")
    Problem3Rate=tk.Label(user_frame,text="Problem Rating",justify='center')
    Problem3Rate.grid(row=4,column=1,padx=(10,10),sticky='ew')
    Problem3Link=Hyperlink(user_frame,url="--",text="Codeforces Link")
    Problem3Link.grid(row=4,column=2,padx=(10,10),sticky='ew')


    # Create a Frame for the Buttons
    buttons_frame = ttk.Frame(root, padding=(20, 10))
    buttons_frame.grid(row=2, column=0, padx=(20, 10), pady=10)
    button1 = ttk.Button(buttons_frame, text="Shuffle", style="Accent.TButton",command=getnewProblems)
    button1.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")

    # Panedwindow
    paned = ttk.PanedWindow(root)
    paned.grid(row=0, column=2, pady=(25, 5), sticky="nsew", rowspan=3)

    pane_1 = ttk.Frame(paned)
    paned.add(pane_1, weight=1)


    # Create a Frame for the Treeview
    treeFrame = ttk.LabelFrame(pane_1,text="Last Solved Problems")
    treeFrame.pack(expand=True, fill="both", padx=5, pady=5)
    # Scrollbar
    treeScroll = ttk.Scrollbar(treeFrame)
    treeScroll.pack(side="right", fill="y")

    # Treeview
    treeview = ttk.Treeview(treeFrame, selectmode="extended", yscrollcommand=treeScroll.set, columns=(1,2,3,4), height=12)
    treeview.bind('<<TreeviewSelect>>',on_select)
    treeview.pack(expand=True, fill="both")
    treeScroll.config(command=treeview.yview)
    # Treeview columns
    treeview.column("#0", width=10)
    treeview.column(1, anchor="w", width=180)
    treeview.column(2, anchor="w", width=70)
    treeview.column(3, anchor="w", width=300)
    treeview.column(4, anchor="w", width=120)
    # Treeview headings
    treeview.heading("#0", text="#", anchor="w")
    treeview.heading(1, text="ContestID", anchor="w")
    treeview.heading(2, text="Index", anchor="w")
    treeview.heading(3, text="Name", anchor="w")
    treeview.heading(4, text="Rate", anchor="w")

    c=0
    for row in solvedProblems:
        treeview.insert(parent="", index='end', iid=c, text="", values=(row['contestId'],row['index'],row['name'],row['rating']))
        c=c+1
        if (c==50):
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
    notebook.add(tab_1, text="Problem")

    # Problems Labels
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    labelgg = ttk.Label(tab_1, text="Abanob Raffet S. Makar")
    labelgg.grid(row=0, column=0,columnspan=2)
    ContestLink = Hyperlink(tab_1,text="Problem Link",url="https://codeforces.com/")
    ContestLink.grid(row=1,column=0,columnspan=2)
    notebook.pack(expand=True, fill="both", padx=5, pady=5)
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # paned.grid_remove()
    # buttons_frame.grid_remove()
    # separator.grid_remove()
    # user_frame.grid_remove()

    # Center the window, and set minsize
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cordinate = int((root.winfo_screenwidth()/2) - (root.winfo_width()/2))
    y_cordinate = int((root.winfo_screenheight()/2) - (root.winfo_height()/2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate))
    # Start the main loop
    root.mainloop()