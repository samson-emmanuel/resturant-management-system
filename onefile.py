import tkinter as tk
from PIL import ImageTk, Image
import customtkinter as ctk
import subprocess

ctk.set_default_color_theme('green')
ctk.set_appearance_mode('Dark')

#first page section
def homepage_frame():
    global home_frame
    home_frame = ctk.CTkFrame(window, width=500, height=500)
    home_frame.grid(row=2, column=0, padx=250, pady=100)

def homepage_buttons():
    top_banner = ctk.CTkLabel(home_frame, text='Welcome', font=('montserat', 16, 'bold'), width=50)
    top_banner.grid(row=0, column=1, pady=20, padx=100)
    staff_button = ctk.CTkButton(home_frame, text='Staff', font=('montserat', 14, 'bold'), command=staff_third_page)
    staff_button.grid(row=1, column=1, pady=5)
    customer_button = ctk.CTkButton(home_frame, text='Customer', font=('montserat', 14, 'bold'), command=nextPage)
    customer_button.grid(row=2, column=1, pady=5)  
    our_tag=ctk.CTkLabel(home_frame, text='d')
    
#END OF FIRST SECTION
    
#second page staff button clicked    
# def staff_second_page():
#     global staff_home_frame
#     home_frame.grid_forget()
#     staff_home_frame = ctk.CTkFrame(window, width=500, height=500)
#     staff_home_frame.grid(row=2, column=1, padx=240, pady=150)
#     top_banner = ctk.CTkLabel(staff_home_frame, text='Staff Section', font=('montserat', 16, 'bold'), width=50)
#     top_banner.grid(row=0, column=1, pady=25)
#     # staff_button = ctk.CTkButton(staff_home_frame, text='Manager', font=('montserat', 14, 'bold'))
#     # staff_button.grid(row=1, column=1, pady=25, padx=100)
#     customer_button = ctk.CTkButton(staff_home_frame, text='Staff', font=('montserat', 14, 'bold'), command=staff_third_page)
#     customer_button.grid(row=2, column=1, padx= 50, pady=25)
#     back_button1=ctk.CTkButton(staff_home_frame, text='<<', font=('montserat', 16, 'bold'), width=20, command=clickable_button1)
#     back_button1.grid(row=0, column=0, padx=10)
    
# def clickable_button1():
#     home_frame.grid_forget()
#     home_frame.grid(row=2, column=0, padx=250, pady=150)

#END OF THE SECOND PAGE

#secton for the thirdpage which is the login page for the staff
def staff_third_page():
    global frame1_s1, frame1_s2
    home_frame.grid_forget()
    
    frame1_s1 = ctk.CTkFrame(window, border_width=0)
    frame1_s1.grid(row=0, column=0, padx=50, pady=50)
    
    #frame holding all the labels and entry
    frame1_s2 = ctk.CTkFrame(window, border_width=0, corner_radius=10, height=100, width=100)
    frame1_s2.grid(row=0, column=2, padx=50, pady=100)
    
  
    welcome=ctk.CTkLabel(frame1_s1, text='Welcome, please enter your \nstaff login details', font=('Motserat', 14, 'bold'))
    welcome.grid(row=1, column=0, padx=20, pady=15) 
    #instruction label
    label1= ctk.CTkLabel(frame1_s2, text='   Staff Login Account   ', bg_color='green')
    label1.grid(row=0, column=2, padx = 45, pady=30)
    
    #email and password label
    entry_label1=ctk.CTkLabel(frame1_s2, text='Enter your Email')
    entry_label1.grid(row=1, column=2)
    entry=ctk.CTkEntry(frame1_s2, border_color='gray')
    entry.grid(row=2, column=2, pady=10)
    
    entry_label1=ctk.CTkLabel(frame1_s2, text='Enter your password')
    entry_label1.grid(row=3, column=2)
    entry=ctk.CTkEntry(frame1_s2, border_color='gray', show='*')
    entry.grid(row=4, column=2, pady=10)
    
    staff_login_button=ctk.CTkButton(frame1_s2, text='Login')
    staff_login_button.grid(row=5, column=2, pady=15)
    
    back_button1=ctk.CTkButton(frame1_s1, text='<<', font=('montserat', 16, 'bold'), width=20, command=clickable_button2)
    back_button1.grid(row=0, column=0, padx=10)
    
def clickable_button2():
    frame1_s1.grid_forget()
    frame1_s2.grid_forget()
    home_frame.grid(row=2, column=0, padx=240, pady=150)
#END OF THE THIRD SECTION FOR THE STAFF

#The first page for customer
def nextPage():
    window.destroy()
    subprocess.call(['python', 'customer_login.py'])
    
    
    
if __name__ == "__main__":

    window = ctk.CTk()
    window.geometry('800x500')
    window.title('Resturant Management System')
    window.iconbitmap('logo.ico')

    

    
    homepage_frame()
    homepage_buttons()
    
    
    
    
    window.mainloop()