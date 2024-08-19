#######~~~~~Student_change_password~~~~~~############
 
from tkinter import *
from customtkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
 
 
# Initialize the main window:
root = CTk()
root.geometry('1920x1080+0+0')
root.title('Student Management System')
# root.iconbitmap("logo.ico")
root._set_appearance_mode("light")
 
#adding mainframe:
std_chng_pw_fr = CTkFrame(root,fg_color="#0D336B")
std_chng_pw_fr.place(relwidth = 1, relheight = 1,relx=0,rely=0)
 
 
def current_pass():
     if scp_crnt_pw_btn.cget("show") == "*":
        scp_crnt_pw_btn.configure(show = '')
     else:
        scp_crnt_pw_btn.configure(show = '*')
   
     pass
 
def new_pass():
     if scp_new_pw_btn.cget("show") == "*":
        scp_new_pw_btn.configure(show = '')
     else:
        scp_new_pw_btn.configure(show = '*')
   
   
     pass
 
def confirm_pass():
     if scp_Cnew_btn.cget("show") == "*":
        scp_Cnew_btn.configure(show = '')
     else:
        scp_Cnew_btn.configure(show = '*')
   
     pass
 
 
 
 
 
 
#Left Top Frame:
std_chng_pw_fr1 = CTkFrame(root,fg_color="#2C87CF",bg_color="#0D336B",width=530, height=100,corner_radius=10)
std_chng_pw_fr1.place(x=20,y=25)
 
#Heading label:
scp_st_dsh_lbl = CTkLabel(std_chng_pw_fr1,text="STUDENT DASHBOARD",text_color="#FFFFFF",fg_color="#2C87CF",font=("Times New Roman",35,"bold"))  #Label of title in top frame
scp_st_dsh_lbl.place(x=60,y=25)
 
 
#Left Bottom Frame:
std_chng_pw_fr2 = CTkFrame(root,fg_color="#2C87CF",bg_color="#0D336B",width=530, height=525,corner_radius=10)
std_chng_pw_fr2.place(x=20,y=145)
 
 
#Button:
 
scp_std_rd_btn = CTkButton(std_chng_pw_fr2,hover_color="#0D336B",fg_color="#0D3380",text=" My Profile ",font=("Times New Roman", 20, "bold"),bg_color="#2C87CF",width=400,height=50,corner_radius=10) #Student records button
scp_std_rd_btn.place(x=60,y=35)
 
scp_my_crs_btn = CTkButton(std_chng_pw_fr2,hover_color="#0D336B",fg_color="#0D3380",text=" My Courses ",font=("Times New Roman", 20, "bold"),bg_color="#2C87CF",width=400,height=50,corner_radius=10) #Student records button
scp_my_crs_btn.place(x=60,y=120)
 
scp_ntc_brd_btn = CTkButton(std_chng_pw_fr2,hover_color="#0D336B",fg_color="#0D3380",text=" View Notice ",font=("Times New Roman", 20, "bold"),bg_color="#2C87CF",width=400,height=50,corner_radius=10) #Student records button
scp_ntc_brd_btn.place(x=60,y=210)
 
scp_cng_pw_btn = CTkButton(std_chng_pw_fr2,hover_color="#0D336B",fg_color="#0D3380",text=" Change Password ",font=("Times New Roman", 20, "bold"),bg_color="#2C87CF",width=400,height=50,corner_radius=10) #Student records button
scp_cng_pw_btn.place(x=60,y=300)
 
 
#logOutButton:
scp_log_out_btn = CTkButton(std_chng_pw_fr2, text='LogOut',font=("Times New Roman",19,"bold") ,text_color='#000000',fg_color="#F1BC60", bg_color='#2C87CF',width=130,height=45,hover_color="#E49C1F", corner_radius=10) #LogOut button
scp_log_out_btn.place(x=195, y=420)
 
 
 
 
 
#Right Frame:
std_chng_pw_fr3 =CTkFrame(std_chng_pw_fr,fg_color="#2C87CF",bg_color="#0D336B",width=690,height=645,corner_radius=10)
std_chng_pw_fr3 .place(x=570,y=25)
 
#Inner Right Frame:
std_chng_pw_fr4 = CTkFrame(std_chng_pw_fr3,fg_color="#0F56A2",bg_color="#2C87CF",width=400, height=500,corner_radius=2)
std_chng_pw_fr4.place(x=160, y=80)
 
#Contains in inner right frame:
 
#adding label:
scp_cng_pw_lbl = CTkLabel(std_chng_pw_fr4,text="Change Password",text_color="white",font=("Times New Roman",25,"bold") ,fg_color="#0F56A2")
scp_cng_pw_lbl.place(x=100,y=25)
 
scp_cpw_lbl = CTkLabel(std_chng_pw_fr4,text="Enter Your Current Password",text_color="white",font=("Times New Roman",16) ,fg_color="#0F56A2")
scp_cpw_lbl.place(x=45,y=110)
 
scp_npw_lbl = CTkLabel(std_chng_pw_fr4,text="Enter Your New Password",text_color="white",font=("Times New Roman",16) ,fg_color="#0F56A2")
scp_npw_lbl.place(x=45,y=200)
 
scp_cn_pw_lbl = CTkLabel(std_chng_pw_fr4,text="Confirm Your New Password",text_color="white",font=("Times New Roman",16) ,fg_color="#0F56A2")
scp_cn_pw_lbl.place(x=45,y=290)
 
 
#adding entry:
scp_cpw_etr = CTkEntry(std_chng_pw_fr4,corner_radius=12,height=38,width=240,border_width=0,fg_color="white",text_color="black",placeholder_text="Current Password",placeholder_text_color="grey",show="*")  
scp_cpw_etr.place(x=45,y=150)
 
scp_npw_etr = CTkEntry(std_chng_pw_fr4,corner_radius=12,height=38,width=240,border_width=0,fg_color="white",text_color="black",placeholder_text="New Password",placeholder_text_color="grey", show='*')  
scp_npw_etr.place(x=45,y=240)
 
scp_cn_pw_etr = CTkEntry(std_chng_pw_fr4,corner_radius=12,height=38,width=240,border_width=0,fg_color="white",text_color="black",placeholder_text="Type Your New Password",placeholder_text_color="grey", show='*')
scp_cn_pw_etr.place(x=45,y=330)
 
#Button:
scp_submit_btn = CTkButton(std_chng_pw_fr4,hover_color="#0D336B",fg_color="#1792F3",text=" Submit ",font=("Times New Roman", 19, "bold"),bg_color="#0F56A2",width=100,height=40,corner_radius=9) #Submit button
scp_submit_btn.place(x=140,y=420)
 
#CheckButtons:
var = IntVar()
scp_crnt_pw_btn = Checkbutton(std_chng_pw_fr4, text = 'Show',font=("Times New Roman",18,"bold"),activebackground="#0F56A2",variable = var,bg="#0F56A2",  command = current_pass)  #for current password
scp_crnt_pw_btn.place(x=450,y=235)
 
varr = IntVar()
scp_new_pw_btn = Checkbutton(std_chng_pw_fr4, text = 'Show',font=("Times New Roman",18,"bold"),activebackground="#0F56A2",variable = varr,bg="#0F56A2",  command = new_pass)  #for new password
scp_new_pw_btn.place(x=450,y=370)
 
varrr = IntVar()
scp_Cnew_btn = Checkbutton(std_chng_pw_fr4, text = 'Show',font=("Times New Roman",18,"bold"),activebackground="#0F56A2",variable = varrr,bg="#0F56A2",  command = confirm_pass) #to confirm new password
scp_Cnew_btn.place(x=450,y=500)
 
 
 
root.mainloop()