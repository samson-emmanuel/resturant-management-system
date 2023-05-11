import tkinter as tk
from tkinter import *
from tkinter import ttk
import customtkinter as ctk
from tkinter import messagebox
#from tkinter import BOTH, END, LEFT

menu={0:['Rice',700],
      1:['Beans',500],
      2:['Semo',300],
      3:['Amala',300],
      4:['Fufu',200],
      5:['Egusi',200],
      6:['Okro',40],
      7:['Afang',30],
      8:['Fish',500],
      9:['Beef',500],
      10:['Turkey',600],
      11:['Pork',700]}
sb=[]

ctk.set_appearance_mode('Dark')
ctk.set_default_color_theme('green')
menu_window = ctk.CTk()
menu_window.geometry("1000x800")

menu_window.columnconfigure(0,weight=8)
menu_window.columnconfigure(1,weight=2)
menu_window.rowconfigure(0, weight=1) 
menu_window.rowconfigure(1, weight=4) # change weight to 4
menu_window.rowconfigure(2, weight=1)

# frame_top=ctk.CTkFrame(menu_window)
#frame_bottom=ctk.CTkFrame(menu_window)

frame_m_right=ctk.CTkFrame(menu_window,)
frame_m_left=ctk.CTkFrame(menu_window)

#placing in grid
#frame_top.grid(row=0,column=0,sticky='WENS',columnspan=2)
frame_m_left.grid(row=1,column=0, sticky='WENS')
frame_m_right.grid(row=1,column=1, sticky='WENS', padx=20)
#frame_bottom.grid(row=2,column=0, columnspan=2)
tree_view = ttk.Treeview(frame_m_right, selectmode ='browse')
tree_view.grid(row=0,column=0,columnspan=2,padx=3,pady=2)

# column identifiers 
tree_view["columns"] = ("1", "2","3")
tree_view.column("#0", width = 80, anchor ='w')
tree_view.column("1", width = 60, anchor ='w')
tree_view.column("2", width =50 , anchor ='c')
tree_view.column("3", width = 50, anchor ='c')
  
# Headings  
# respective columns
tree_view.heading("#0", text ="Item",anchor='w')
tree_view.heading("1", text ="Price",anchor='w')
tree_view.heading("2", text ="qty",anchor='c')
tree_view.heading("3", text ="Total",anchor='c')
def my_reset():
    for item in tree_view.get_children():
        tree_view.delete(item)
    # for i in range(len(sb)):
    #    sb[i].config(textvariable=0)    # reset spinbox 
    l1=[]
    for i in range(12):
        l1.append(tk.IntVar(value=0))
    for i in range(len(sb)):
        print(sb[i].config(textvariable=l1[i]))

    for w in frame_m_right.grid_slaves(1):
        w.grid_remove()
    for w in frame_m_right.grid_slaves(2):
        w.grid_remove()    
    for w in frame_m_right.grid_slaves(3):
        w.grid_remove()
        table.grid_remove()
    
def my_bill():
    global table
    total=0
    for item in tree_view.get_children():
        tree_view.delete(item)
    for i in range(len(sb)):
        if(int(sb[i].get())>0):
            price=int(sb[i].get())*menu[i][1]
            total=total+price
            my_str1=(str(menu[i][1]), str(sb[i].get()), str(price))
            tree_view.insert("",'end',iid=i,text=menu[i][0],values=my_str1)
            
    lr1=tk.Label(frame_m_right,text='Total',font=font1)
    lr1.grid(row=1,column=0,sticky='nw')
    lr2=tk.Label(frame_m_right,text=str(total),font=font1)
    lr2.grid(row=1,column=1,sticky='nw')
    lr21=tk.Label(frame_m_right,text='Tax 7.5%',font=font1)
    lr21.grid(row=2,column=0,sticky='nw')
    tax=0.075*total
    lr22=tk.Label(frame_m_right,text=str(tax),font=font1)
    lr22.grid(row=2,column=1,sticky='nw')
    lr31=tk.Label(frame_m_right,text='Total',font=font2)
    lr31.grid(row=3,column=0,sticky='nw')
    final=total+tax
    lr32=tk.Label(frame_m_right,text=str(final),font=font2)
    lr32.grid(row=3,column=1,sticky='nw')
    
    table=ctk.CTkLabel(frame_m_right, text=f'Table Number: {number.get()}', font=('montserat', 14, 'bold'))
    table.grid(row=4, column=0)
    proceed_button=ctk.CTkButton(frame_m_right, text='Proceed', font=('montserat', 14, 'bold'), command=proceed)
    proceed_button.grid(row=5, column=1, pady=25)
    
    
    
def proceed():
    messagebox.showinfo('Ultimate Coders', 'Thank you.\nYour order has been recieved.')
    
        
# Layout is over , sart placing buttons 
#path_image="G:\\My Drive\\testing\\plus2_restaurant_v1\\images\\"
font1=('montserat',14,'normal')
font2=('Times',32,'bold')
pdx,pdy=20,5
#img_top = tk.PhotoImage(file = path_image+"restaurant-3.png")
#bg=tk.PhotoImage(file=path_image+'bg.png')

#c1 = tk.Canvas(frame_m_left,width=1000,height=500)
#c1.grid(row=0,column=0,columnspan=4,rowspan=4,sticky='nw',padx=0)
#c1.create_image(0,0,image=bg,anchor='nw')

#img_l1 = tk.Label(frame_top,  image=img_top)
#img_l1.grid(row=0,column=0,sticky='nw',pady=1)

#img_menu1=tk.PhotoImage(file=path_image+"food-item-1.png")
#img_menu2=tk.PhotoImage(file=path_image+"food-item-2.png")
#img_menu3=tk.PhotoImage(file=path_image+"food-item-3.png")
#img_menu4=tk.PhotoImage(file=path_image+"food-item-4.png")
#img_menu5=tk.PhotoImage(file=path_image+"food-item-5.png")
#img_menu6=tk.PhotoImage(file=path_image+"food-item-6.png")
#img_menu7=tk.PhotoImage(file=path_image+"food-item-7.png")
#img_menu8=tk.PhotoImage(file=path_image+"food-item-8.png")

#food menu
food_banner=ctk.CTkLabel(frame_m_left, text='Select food per plate', font=('montserat', 16, 'bold'))
food_banner.grid(row=0, column=0,padx=15, pady=20, columnspan=4)
menu1=ctk.CTkButton(frame_m_left,text=menu[0], font=('montserat', 12))
menu1.grid(row=1,column=0,sticky='nw',padx=pdx,pady=pdy)    
menu2=ctk.CTkButton(frame_m_left,text=menu[1], font=('montserat', 12))
menu2.grid(row=1,column=1,sticky='nw',padx=pdx,pady=pdy)
menu3=ctk.CTkButton(frame_m_left,text=menu[2], font=('montserat', 12))
menu3.grid(row=1,column=2,sticky='nw',padx=pdx,pady=pdy)
menu4=ctk.CTkButton(frame_m_left,text=menu[3], font=('montserat', 12))
menu4.grid(row=1,column=3,sticky='nw',padx=pdx,pady=0)
sv1=tk.IntVar()
sb1 = tk.Spinbox(frame_m_left,from_=0,to_=5,font=font1,width=1,textvariable=sv1)
sb1.grid(row=2,column=0,sticky='nw',padx=pdx,pady=5)
sb.append(sb1)    
sv2=tk.IntVar()
sb2 = tk.Spinbox(frame_m_left,from_=0,to_=5,font=font1,width=1,textvariable=sv2)
sb2.grid(row=2,column=1,sticky='nw',padx=pdx,pady=5)
sb.append(sb2)    
sv3=tk.IntVar()
sb3 = tk.Spinbox(frame_m_left,from_=0,to_=5,font=font1,width=1,textvariable=sv3)
sb3.grid(row=2,column=2,sticky='nw',padx=pdx,pady=5)
sb.append(sb3)    
sv4=tk.IntVar()
sb4 = tk.Spinbox(frame_m_left,from_=0,to_=5,font=font1,width=1,textvariable=sv4)
sb4.grid(row=2,column=3,sticky='nw',padx=pdx,pady=5)
sb.append(sb4)

#Section for soup
soup_banner=ctk.CTkLabel(frame_m_left, text='Select your soup', font=('montserat', 16, 'bold'))  
soup_banner.grid(row=3, column=0, pady=20, columnspan=4)
menu5=ctk.CTkButton(frame_m_left,text=menu[4], font=('montserat', 12))
menu5.grid(row=4,column=0,sticky='nw',padx=pdx,pady=pdy)
menu6=ctk.CTkButton(frame_m_left,text=menu[5], font=('montserat', 12))
menu6.grid(row=4,column=1,sticky='nw',padx=pdx,pady=pdy)
menu7=ctk.CTkButton(frame_m_left,text=menu[6], font=('montserat', 12))
menu7.grid(row=4,column=2,sticky='nw',padx=pdx,pady=pdy)
menu8=ctk.CTkButton(frame_m_left,text=menu[7], font=('montserat', 12))
menu8.grid(row=4,column=3,sticky='nw',padx=pdx,pady=pdy)
sv5=tk.IntVar()
sb5 = tk.Spinbox(frame_m_left,from_=0,to_=5,font=font1,width=1,textvariable=sv5)
sb5.grid(row=5,column=0,sticky='nw',padx=pdx,pady=pdy)
sb.append(sb5)
sv6=tk.IntVar()
sb6 = tk.Spinbox(frame_m_left,from_=0,to_=5,font=font1,width=1,textvariable=sv6)
sb6.grid(row=5,column=1,sticky='nw',padx=pdx,pady=pdy)
sb.append(sb6)
sv7=tk.IntVar()
sb7 = tk.Spinbox(frame_m_left,from_=0,to_=5,font=font1,width=1,textvariable=sv7)
sb7.grid(row=5,column=2,sticky='nw',padx=pdx,pady=pdy)
sb.append(sb7)
sv8=tk.IntVar()
sb8 = tk.Spinbox(frame_m_left,from_=0,to_=5,font=font1,width=1,textvariable=sv8)
sb8.grid(row=5,column=3,sticky='nw',padx=pdx,pady=pdy)
sb.append(sb8)


#Extra
#Section for extra
soup_banner=ctk.CTkLabel(frame_m_left, text='Choose extra for your meal', font=('montserat', 16, 'bold'))  
soup_banner.grid(row=6, column=0, pady=20, columnspan=4)
menu9=ctk.CTkButton(frame_m_left,text=menu[8], font=('montserat', 12))
menu9.grid(row=7,column=0,sticky='nw',padx=pdx,pady=pdy)
menu10=ctk.CTkButton(frame_m_left,text=menu[9], font=('montserat', 12))
menu10.grid(row=7,column=1,sticky='nw',padx=pdx,pady=pdy)
menu11=ctk.CTkButton(frame_m_left,text=menu[10], font=('montserat', 12))
menu11.grid(row=7,column=2,sticky='nw',padx=pdx,pady=pdy)
menu12=ctk.CTkButton(frame_m_left,text=menu[11], font=('montserat', 12))
menu12.grid(row=7,column=3,sticky='nw',padx=pdx,pady=pdy)
sv9=tk.IntVar()
sb9 = tk.Spinbox(frame_m_left,from_=0,to_=5,font=font1,width=1,textvariable=sv9)
sb9.grid(row=8,column=0,sticky='nw',padx=pdx,pady=pdy)
sb.append(sb9)
sv10=tk.IntVar()
sb10= tk.Spinbox(frame_m_left,from_=0,to_=5,font=font1,width=1,textvariable=sv10)
sb10.grid(row=8,column=1,sticky='nw',padx=pdx,pady=pdy)
sb.append(sb10)
sv11=tk.IntVar()
sb11 = tk.Spinbox(frame_m_left,from_=0,to_=5,font=font1,width=1,textvariable=sv11)
sb11.grid(row=8,column=2,sticky='nw',padx=pdx,pady=pdy)
sb.append(sb11)
sv12=tk.IntVar()
sb12 = tk.Spinbox(frame_m_left,from_=0,to_=5,font=font1,width=1,textvariable=sv12)
sb12.grid(row=8,column=3,sticky='nw',padx=pdx,pady=pdy)
sb.append(sb12)

#billings
table_number=ctk.CTkLabel(frame_m_left, text='Enter your table number below', font=('montserat', 14, 'bold'))
table_number.grid(row=9, column=0, padx=(25,0))
number=ctk.CTkEntry(frame_m_left, width=40)
number.grid(row=9, column=1, padx=(0,25))
b1=ctk.CTkButton(frame_m_left,text='Get Bill',command=my_bill)
b1.grid(row=9,column=2, padx=30, pady=60)
b2=ctk.CTkButton(frame_m_left,text='Confirm ( Reset)',command=my_reset)
b2.grid(row=9,column=3, pady=60)

#function for login out   
def logout():
    frame_m_left.grid_forget()
    frame_m_right.grid_forget()
    tree_view.grid_forget()


b3= ctk.CTkButton(frame_m_left, text='Log Out', command=logout)
b3.grid(row=10, column=3)
menu_window.mainloop()