#######~~~~~STUDENT_MY_Profile~~~~~~############
 
from tkinter import *
from customtkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
 
 
# Initialize the main window:
root = CTk()
root.geometry('1920x1080+0+0')
root.title('Student Management System')
root.iconbitmap("logo.ico")
root._set_appearance_mode("light")
 
#adding mainframe:
std_view_notice_fr = CTkFrame(root,fg_color="#0D336B")
std_view_notice_fr.place(relwidth = 1, relheight = 1,relx=0,rely=0)
 
 
#Left Top Frame:
std_view_notice_fr1 = CTkFrame(root,fg_color="#2C87CF",bg_color="#0D336B",width=530, height=100,corner_radius=10)
std_view_notice_fr1.place(x=20,y=25)
 
#Left Bottom Frame:
std_view_notice_fr2 = CTkFrame(root,fg_color="#2C87CF",bg_color="#0D336B",width=530, height=525,corner_radius=10)
std_view_notice_fr2.place(x=20,y=145)
 
#Right Frame:
std_view_notice_fr3 =CTkFrame(root,fg_color="#2C87CF",bg_color="#0D336B",width=690,height=645,corner_radius=10)
std_view_notice_fr3 .place(x=570,y=25)
 
#Label in left top frame:
std_dash_lbl = CTkLabel(std_view_notice_fr1,text="STUDENT DASHBOARD",text_color="#FFFFFF",fg_color="#2C87CF",font=("Times New Roman",35,"bold"))  #Label of title in top frame
std_dash_lbl.place(x=60,y=25)
 
 
#Button in left buttom frame:
 
mc_std_rd_btn = CTkButton(std_view_notice_fr2,hover_color="#0D336B",fg_color="#0D3380",text="My Profile",font=("Times New Roman", 20, "bold"),bg_color="#2C87CF",width=400,height=50,corner_radius=10) #Student records button
mc_std_rd_btn.place(x=60,y=35)
 
mc_my_crs_btn = CTkButton(std_view_notice_fr2,hover_color="#0D336B",fg_color="#0D3380",text=" My Courses ",font=("Times New Roman", 20, "bold"),bg_color="#2C87CF",width=400,height=50,corner_radius=10) #Student records button
mc_my_crs_btn.place(x=60,y=120)
 
mc_view_ntc_btn = CTkButton(std_view_notice_fr2,hover_color="#0D336B",fg_color="#0D3380",text="View Notice ",font=("Times New Roman", 20, "bold"),bg_color="#2C87CF",width=400,height=50,corner_radius=10) #Student records button
mc_view_ntc_btn.place(x=60,y=210)
 
mc_cng_pw_btn = CTkButton(std_view_notice_fr2,hover_color="#0D336B",fg_color="#0D3380",text=" Change Password ",font=("Times New Roman", 20, "bold"),bg_color="#2C87CF",width=400,height=50,corner_radius=10) #Student records button
mc_cng_pw_btn.place(x=60,y=300)

#logOutButton:
vn_log_out_btn = CTkButton(std_view_notice_fr2, text='LogOut',font=("Times New Roman",19,"bold") ,text_color='#000000',fg_color="#F1BC60", bg_color='#2C87CF',width=130,height=45,hover_color="#E49C1F", corner_radius=10) #LogOut button
vn_log_out_btn.place(x=195, y=420)
 
#keep the window open
root.mainloop()