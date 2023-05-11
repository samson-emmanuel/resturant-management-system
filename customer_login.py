import tkinter as tk
import customtkinter as ctk
import sqlite3
from tkinter import messagebox
from tkinter import ttk



ctk.set_default_color_theme('green')
ctk.set_appearance_mode('Dark')


def customers_frames():
    global frame1_s1, registration_screen, login_scren, login_button, register_button
    #lefhand frame
    frame1_s1 = ctk.CTkFrame(window, border_width=0)
    frame1_s1.grid(row=0, column=0, padx=50, pady=50)
    
    #righthand frame
    login_scren = ctk.CTkFrame(window, border_width=0)
    login_scren.grid(row=0, column=2, padx=50, pady=50)

    #frame holding all the labels and entry
    registration_screen = ctk.CTkFrame(window, border_width=0, corner_radius=10, height=100, width=100)
    registration_screen.grid(row=0, column=2, padx=50, pady=50)

    #Login button on the lefhand side
    login_button=ctk.CTkButton(frame1_s1, text='Login',command=login_recover)
    login_button.grid(row=0, column=0, padx=30, pady=15)
    
    #registration button on the right hand side
    register_button=ctk.CTkButton(frame1_s1, text='Register', command=register)
    register_button.grid(row=1, column=0, padx=30, pady=15)



    
#function to call back the login frame
def login_recover():
    registration_screen.grid_forget()
    login_scren.grid(row=0, column=2, padx=50, pady=50)





#function for the login section
def login():
    global label1, login_scren, login_entry1, password_entry1, running
    if  running ==True:
        login_scren.grid_forget()
        login_scren = ctk.CTkFrame(window, border_width=0, corner_radius=10)
        login_scren.grid(row=0, column=2, padx=50, pady=50)
        #login_scren.destroy()
        #instruction label
        label1= ctk.CTkLabel(login_scren, text='   Login into your account   ', bg_color='green')
        label1.grid(row=0, column=2, padx = 105, pady=30)
        
        #username and password label
        login_name_label=ctk.CTkLabel(login_scren, text='Enter your Email', )
        login_name_label.grid(row=1, column=2, pady=5)
        login_entry1=ctk.CTkEntry(login_scren, border_color='gray', placeholder_text='Email')
        login_entry1.grid(row=2, column=2, pady=10)
        
        login_password_label=ctk.CTkLabel(login_scren, text='Enter your password')
        login_password_label.grid(row=3, column=2, pady=5)
        password_entry1=ctk.CTkEntry(login_scren, border_color='gray', placeholder_text='Password', show='*')
        password_entry1.grid(row=4, column=2, pady=10)
        
        login_btn=ctk.CTkButton(login_scren, text='Login', width=100, hover_color='green', command=check_login)
        login_btn.grid(row=5, column=2, padx=30, pady=15)
        
        # forget_password=ctk.CTkLabel(login_scren, text='Forget Password')
        # forget_password.grid(row=5, column=3, padx=10)
        running = False
        registration_screen.grid_forget()
        



def check_login():
    email=login_entry1.get()
    password=password_entry1.get()
    con=sqlite3.connect('CustomerDatabase.db')
    cur=con.cursor()
    statement= f"SELECT email from CustomerTable WHERE Email='{email}' AND Password ='{password}';"
    cur.execute(statement)
    if not cur.fetchone():
        print('Login failed')
        messagebox.showerror('RMS', 'Incorrect details.\nPlease check information again')
        
    elif email=='':
        messagebox.showerror("RMS", "Email can't be empty")
    elif password=='':
        messagebox.showerror("RMS", "Password can't be empty")
    else:
        #print('Welcome')
        messagebox.showinfo('RMS', 'You have successfully Log in')
        frame1_s1.grid_forget()
        login_scren.grid_forget()
        registration_screen.grid_forget()
        login_button.grid_forget()
        register_button.grid_forget()


        frame_bottom=ctk.CTkFrame(window)

        frame_m_right=ctk.CTkFrame(window,)
        frame_m_left=ctk.CTkFrame(window)
        frame_m_left.grid(row=1,column=0,sticky='WENS')
        frame_m_right.grid(row=1,column=1,sticky='WENS')
        frame_bottom.grid(row=2,column=0,sticky='WENS',columnspan=2)
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
        main_body()
        

        frame_m_left.grid_forget()
        frame_m_right.grid_forget()
        frame_bottom.grid_forget()
        tree_view.grid_forget()
            



#registration function with its frame    
def register():
    global label1, running, registration_screen, first_name_entry, last_name_entry, email_entry, phone_entry, password_entry, conirm_password_entry
    if running==False:
        login_scren.grid_forget()
        registration_screen = ctk.CTkFrame(window, border_width=0, corner_radius=10)
        registration_screen.grid(row=0, column=2, padx=50, pady=50)
        #Registration form for new customers
        label1= ctk.CTkLabel(registration_screen, text='   Register   ', bg_color='green')
        label1.grid(row=0, column=2, padx = 45, pady=20)
        
        #username and password label
        first_name_label=ctk.CTkLabel(registration_screen, text='First Name ', )
        first_name_label.grid(row=1, column=2, pady=5)
        first_name_entry=ctk.CTkEntry(registration_screen, border_color='gray', placeholder_text='First Name',  width=200, textvariable=firstnameVar)
        first_name_entry.grid(row=2, column=2, padx=45)
        
        last_name_label=ctk.CTkLabel(registration_screen, text='Last Name ', )
        last_name_label.grid(row=3, column=2, pady=5)
        last_name_entry=ctk.CTkEntry(registration_screen, border_color='gray', placeholder_text='Last Name',  width=200, textvariable=lastnameVar)
        last_name_entry.grid(row=4, column=2, padx=45)
        
        email_label=ctk.CTkLabel(registration_screen, text='Email Address', )
        email_label.grid(row=5, column=2, pady=5)
        email_entry=ctk.CTkEntry(registration_screen, border_color='gray', placeholder_text='example@gmail.com', width=250, textvariable=emailVar)
        email_entry.grid(row=6, column=2, padx=45)
        
        phone_label=ctk.CTkLabel(registration_screen, text='Phone Number', )
        phone_label.grid(row=7, column=2, pady=5)
        phone_entry=ctk.CTkEntry(registration_screen, border_color='gray', placeholder_text='+234 123456789',  width=200, textvariable=phoneVar)
        phone_entry.grid(row=8, column=2, padx=45)
        
        password_label=ctk.CTkLabel(registration_screen, text='Password', )
        password_label.grid(row=9, column=2, pady=5)
        password_entry=ctk.CTkEntry(registration_screen, border_color='gray', placeholder_text='Password',  width=200, show='*', textvariable=passwordVar)
        password_entry.grid(row=10, column=2, padx=45)
        
        confirm_password_label=ctk.CTkLabel(registration_screen, text='Confirm Password')
        confirm_password_label.grid(row=11, column=2, padx=35)
        conirm_password_entry=ctk.CTkEntry(registration_screen, border_color='gray', placeholder_text='Confirm Password', show='*', textvariable=password2Var )
        conirm_password_entry.grid(row=12, column=2, padx=45)
        
        register_now=ctk.CTkButton(registration_screen, text='Register', command=new_registration )
        register_now.grid(row=13, column=2, pady=25)




def new_registration():
    #global email, password
    first_name=first_name_entry.get()
    last_name=last_name_entry.get()
    email=email_entry.get()
    phone=phone_entry.get()
    password=password_entry.get()
    password2=conirm_password_entry.get()
    
    #checking if there is empty entry in the form
    if first_name=='':
        messagebox.showwarning('RMS', 'Kindly type your First Name in the form') 
    elif last_name=='':
        messagebox.showwarning('RMS', 'Kindly type your Last Name in the form') 
    elif email=='':
        messagebox.showwarning('RMS', 'Kindly type your Email Address in the form') 
    elif phone=='':
        messagebox.showwarning('RMS', 'Kindly type your Phone Number in the form') 
    elif password=='':
        messagebox.showwarning('RMS', 'Kindly fill out the empty spaces in the form') 
    elif password2=='':
        messagebox.showwarning('RMS', 'Kindly fill out the empty spaces in the form') 
    elif password == password2:
        # print(first_name,last_name,email,phone,password ) 
        conn=sqlite3.connect('CustomerDatabase.db')        
        c =conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS CustomerTable(First_Name TEXT,Last_Name TEXT,Email TEXT,Phone INTEGER,Password TEXT)')
        c.execute('INSERT INTO CustomerTable(First_Name,Last_Name,Email,Phone,Password) VALUES(?,?,?,?,?)',(first_name,last_name,email,phone,password))
        conn.commit() 
        messagebox.showinfo('RMS', 'Registration successful\nClick on Login to proceed')    
    else:
        messagebox.showinfo('RMS', 'Wrong Password. Please enter the correct passwor and process')
        
        



#SECTION FOR THE CUSTOMERS VIEW
window = ctk.CTk()
window.geometry("1000x800")
window.iconbitmap('logo.ico')
window.columnconfigure(0,weight=8)
window.columnconfigure(1,weight=2)
window.rowconfigure(0, weight=1) 
window.rowconfigure(1, weight=4)
window.rowconfigure(2, weight=1)
def menu_things():
    global menu
    menu={0:['Rice',700],
        1:['Beans',500],
        2:['Semo',300],
        3:['Amala',300],
        4:['Fufu',200],
        5:['Egusi',200],
        6:['Okro',300],
        7:['Afang',300],
        8:['Fish',500],
        9:['Beef',500],
        10:['Turkey',600],
        11:['Pork',700]}
sb=[]

# ctk.set_appearance_mode('Dark')
# ctk.set_default_color_theme('green')




# frame_top=ctk.CTkFrame(menu_window)
def frames():
    global frame_bottom, frame_m_left, frame_m_right, tree_view
    frame_bottom=ctk.CTkFrame(window)

    frame_m_right=ctk.CTkFrame(window,)
    frame_m_left=ctk.CTkFrame(window)

    #placing in grid
    #frame_top.grid(row=0,column=0,sticky='WENS',columnspan=2)
    frame_m_left.grid(row=1,column=0,sticky='WENS')
    frame_m_right.grid(row=1,column=1,sticky='WENS')
    #frame_bottom.grid(row=2,column=0,sticky='WENS',columnspan=2)
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
        proceed_button.grid_remove()
        
        
        
    
def my_bill():
    global table, proceed_button, lr1, lr2, lr21, lr22, lr31, lr32
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
    
    table=ctk.CTkLabel(frame_m_right, text=f'Table Number: {number_for_table.get()}', font=('montserat', 14, 'bold'))
    table.grid(row=4, column=0)
    proceed_button=ctk.CTkButton(frame_m_right, text='Proceed', font=('montserat', 14, 'bold'), command=proceed)
    proceed_button.grid(row=5, column=0, pady=25)   
    


def proceed():
    messagebox.showinfo('RMS', 'Thank you.\nYour order has been recieved.')




#food menu
def food_menu():
    food_banner=ctk.CTkLabel(frame_m_left, text='Select food per plate', font=('montserat', 16, 'bold'))
    food_banner.grid(row=0, column=0,padx=15, pady=20, columnspan=4)
    menu1=ctk.CTkButton(frame_m_left,text=menu[0], font=font1)
    menu1.grid(row=1,column=0,sticky='nw',padx=pdx,pady=pdy)    
    menu2=ctk.CTkButton(frame_m_left,text=menu[1], font=font1)
    menu2.grid(row=1,column=1,sticky='nw',padx=pdx,pady=pdy)
    menu3=ctk.CTkButton(frame_m_left,text=menu[2], font=font1)
    menu3.grid(row=1,column=2,sticky='nw',padx=pdx,pady=pdy)
    menu4=ctk.CTkButton(frame_m_left,text=menu[3], font=font1)
    menu4.grid(row=1,column=3,sticky='nw',padx=pdx,pady=0)
    sv1=tk.IntVar()
    sb1 = tk.Spinbox(frame_m_left,from_=0,to_=100,font=font3,width=4, textvariable=sv1)
    sb1.grid(row=2,column=0,sticky='nw',padx=45,pady=5)
    sb.append(sb1)    
    sv2=tk.IntVar()
    sb2 = tk.Spinbox(frame_m_left,from_=0,to_=100,font=font3,width=4,textvariable=sv2)
    sb2.grid(row=2,column=1,sticky='nw',padx=45,pady=5)
    sb.append(sb2)    
    sv3=tk.IntVar()
    sb3 = tk.Spinbox(frame_m_left,from_=0,to_=100,font=font3,width=4,textvariable=sv3)
    sb3.grid(row=2,column=2,sticky='nw',padx=45,pady=5)
    sb.append(sb3)    
    sv4=tk.IntVar()
    sb4 = tk.Spinbox(frame_m_left,from_=0,to_=100,font=font3,width=4,textvariable=sv4)
    sb4.grid(row=2,column=3,sticky='nw',padx=45,pady=5)
    sb.append(sb4)




#Section for soup
def soup_menu():
    soup_banner=ctk.CTkLabel(frame_m_left, text='Select your soup', font=('montserat', 16, 'bold'))  
    soup_banner.grid(row=3, column=0, pady=20, columnspan=4)
    menu5=ctk.CTkButton(frame_m_left,text=menu[4], font=font1)
    menu5.grid(row=4,column=0,sticky='nw',padx=pdx,pady=pdy)
    menu6=ctk.CTkButton(frame_m_left,text=menu[5], font=font1)
    menu6.grid(row=4,column=1,sticky='nw',padx=pdx,pady=pdy)
    menu7=ctk.CTkButton(frame_m_left,text=menu[6], font=font1)
    menu7.grid(row=4,column=2,sticky='nw',padx=pdx,pady=pdy)
    menu8=ctk.CTkButton(frame_m_left,text=menu[7], font=font1)
    menu8.grid(row=4,column=3,sticky='nw',padx=pdx,pady=pdy)
    sv5=tk.IntVar()
    sb5 = tk.Spinbox(frame_m_left,from_=0,to_=100,font=font3,width=1,textvariable=sv5)
    sb5.grid(row=5,column=0,sticky='nw',padx=45,pady=pdy)
    sb.append(sb5)
    sv6=tk.IntVar()
    sb6 = tk.Spinbox(frame_m_left,from_=0,to_=100,font=font3,width=4,textvariable=sv6)
    sb6.grid(row=5,column=1,sticky='nw',padx=45,pady=pdy)
    sb.append(sb6)
    sv7=tk.IntVar()
    sb7 = tk.Spinbox(frame_m_left,from_=0,to_=100,font=font3,width=4,textvariable=sv7)
    sb7.grid(row=5,column=2,sticky='nw',padx=45,pady=pdy)
    sb.append(sb7)
    sv8=tk.IntVar()
    sb8 = tk.Spinbox(frame_m_left,from_=0,to_=100,font=font3,width=4,textvariable=sv8)
    sb8.grid(row=5,column=3,sticky='nw',padx=45,pady=pdy)
    sb.append(sb8)




#Extra
#Section for extra
def extra_menu():
    global number_for_table
    soup_banner=ctk.CTkLabel(frame_m_left, text='Choose extra for your meal', font=('montserat', 16, 'bold'))  
    soup_banner.grid(row=6, column=0, pady=20, columnspan=4)
    menu9=ctk.CTkButton(frame_m_left,text=menu[8], font=font1)
    menu9.grid(row=7,column=0,sticky='nw',padx=pdx,pady=pdy)
    menu10=ctk.CTkButton(frame_m_left,text=menu[9], font=font1)
    menu10.grid(row=7,column=1,sticky='nw',padx=pdx,pady=pdy)
    menu11=ctk.CTkButton(frame_m_left,text=menu[10], font=font1)
    menu11.grid(row=7,column=2,sticky='nw',padx=pdx,pady=pdy)
    menu12=ctk.CTkButton(frame_m_left,text=menu[11], font=font1)
    menu12.grid(row=7,column=3,sticky='nw',padx=pdx,pady=pdy)
    sv9=tk.IntVar()
    sb9 = tk.Spinbox(frame_m_left,from_=0,to_=100,font=font3,width=4,textvariable=sv9)
    sb9.grid(row=8,column=0,sticky='nw',padx=45,pady=pdy)
    sb.append(sb9)
    sv10=tk.IntVar()
    sb10= tk.Spinbox(frame_m_left,from_=0,to_=100,font=font3,width=4,textvariable=sv10)
    sb10.grid(row=8,column=1,sticky='nw',padx=45,pady=pdy)
    sb.append(sb10)
    sv11=tk.IntVar()
    sb11 = tk.Spinbox(frame_m_left,from_=0,to_=100,font=font3,width=4,textvariable=sv11)
    sb11.grid(row=8,column=2,sticky='nw',padx=45,pady=pdy)
    sb.append(sb11)
    sv12=tk.IntVar()
    sb12 = tk.Spinbox(frame_m_left,from_=0,to_=100,font=font3,width=4,textvariable=sv12)
    sb12.grid(row=8,column=3,sticky='nw',padx=45,pady=pdy)
    sb.append(sb12)

    #billings
    table_number=ctk.CTkLabel(frame_m_left, text='Enter your table number below', font=('montserat', 14, 'bold'))
    table_number.grid(row=9, column=0, padx=(25,0))
    
    number_for_table=ctk.CTkEntry(frame_m_left, width=40)
    number_for_table.grid(row=9, column=1, padx=(0,25))
    
    b1=ctk.CTkButton(frame_m_left,text='Get Bill',command=my_bill)
    b1.grid(row=9,column=2, pady=60)
    b2=ctk.CTkButton(frame_m_left,text='Confirm ( Reset)',command=my_reset)
    b2.grid(row=9,column=3, pady=60)
    
    b3= ctk.CTkButton(frame_m_left, text='Log Out', command=logout)
    b3.grid(row=10, column=3)






#function for login out   
def logout():
    frame_m_left.grid_forget()
    frame_m_right.grid_forget()
    frame_bottom.grid_forget()
    tree_view.grid_forget()

    
    frame1_s1.grid(row=0, column=0, padx=50, pady=50)
    login_scren.grid(row=0, column=2, padx=50, pady=50)
    registration_screen.grid(row=0, column=2, padx=50, pady=50)
    login_button.grid(row=0, column=0, padx=30, pady=15)
    register_button.grid(row=1, column=0, padx=30, pady=15)
    

def main_body():
    frames()
    menu_things()
    food_menu()
    soup_menu()
    extra_menu()


#END OF THE SECTION FOR CUSTOMERS VIEW
        
        
    

if __name__ == "__main__":

    window = ctk.CTk()
    window.geometry('1100x700')
    window.title('Resturant Management System')
    window.iconbitmap('logo.ico')
    
    
    running = True

    

    firstnameVar=str()
    lastnameVar=str()
    emailVar=str()
    phoneVar=str()
    passwordVar=str()
    password2Var=str()
    
    
    customers_frames()
    login()
    
    font1=('montserat',14,'normal')
    font2=('Times',32,'bold')
    font3=('montserat', 20 ,'normal')
    pdx,pdy=20,5
    

    

    

    
    
    
    window.mainloop()