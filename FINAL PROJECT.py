from tkinter import *
from tkinter import messagebox    #msg box will not work in absence of this command
import mysql.connector as sc
from tkinter import ttk
import matplotlib.pyplot as plt


sqlcon=sc.connect(host='localhost',user='root',passwd='3010',database='Year_2020',autocommit=True)
cursor=sqlcon.cursor()
def Exit(root):
    root.destroy()
    menu(3)
def menu(root):
    if root==3:
        pass
    else:
        root.destroy()
    root=Tk()
    root.geometry('1600x1000')
    root.title('Menu')

    #the instruction
    frame=LabelFrame(root,padx=10,pady=10)
    frame.grid(row=0,column=0,padx=250,pady=15,columnspan=3)
    instrc=Label(frame,text='Select the operation you want to execute and click ok',font=("Arial", 44))
    instrc.pack()

    #RadioButton
    operations=[
        ('Enter a new student','Enter a new student'),
        ('Enter Marks for a Student','Enter Marks for a Student'),
        ('Delete a student from databse','Delete a student from databse'),
        ('Modify Student Data','Modify Student Data'),
        ('Go to Graph Section','Go to Graph Section'),
        ('Display marks records','Display marks records')
        ,('Display report card','Display report card'),
        ("Exit the Program","Exit the Program")
        ]

    choice=StringVar()
    choice.set('Enter a new student')

    j=1
    for oprtn,mode in operations:
        Radiobutton(root,text=oprtn,variable=choice,value=mode,font=("Arial", 35)).grid(row=j,column=1,pady=8)
        j+=1
    ####
    def opt_info():
        
        root.destroy()
        if choice.get()=='Enter a new student':
            fnc_Enter_a_new_student()
        elif choice.get()=='Enter Marks for a Student':
            fnc_Enter_Marks()
        elif choice.get()=='Delete a student from databse':
            fnc_delete()
        elif choice.get()=='Modify Student Data':
            fnc_modify()
        elif choice.get()=='Go to Graph Section':
            fnc_graph()
        elif choice.get()=='Display marks records':
            disp()
        elif choice.get()=='Display report card':
            repcar()
        elif choice.get()=="Exit the Program":
            exit_prog(root)
        
            
    #Button
    ok=Button(root,text='OK',command=opt_info,padx=40,pady=10)
    ok.grid(row=j,column=1,pady=100)
        
    root.mainloop()
"=========================================================================================================="
def fnc_Enter_a_new_student():
    root=Tk()
    root.geometry('1400x1000')
    root.title('Enter A New Student')
     
    #the instruction
    frame=LabelFrame(root,padx=10,pady=10)
    frame.grid(row=0,column=0,padx=170,pady=15,columnspan=2)
    instrc=Label(frame,text='Enter details as required and click ok',font=("Arial", 44))
    instrc.pack()
    #the labels
    label_id=Label(root,text='Student ID:',pady=7,font=("Arial", 35))
    label_id.grid(row=1,column=0)
    label_id=Label(root,text='Student ID:',pady=7,font=("Arial", 35))
    label_id.grid(row=1,column=0)
    
    label_name=Label(root,text='Name:',pady=7,font=("Arial", 35))
    label_name.grid(row=2,column=0)
    
    label_sex=Label(root,text='Sex:',pady=7,font=("Arial", 35))
    label_sex.grid(row=3,column=0)
    
    label_class=Label(root,text='Class:',pady=7,font=("Arial", 35))
    label_class.grid(row=5,column=0)
    
    label_sec=Label(root,text='Section:',pady=7,font=("Arial", 35))
    label_sec.grid(row=6,column=0)

    label_stream=Label(root,text='Stream:',pady=7,font=("Arial", 35))
    label_stream.grid(row=7,column=0)
    
    label_No=Label(root,text='Phone Number:',pady=7,font=("Arial", 35))
    label_No.grid(row=8,column=0)
    
    label_mail=Label(root,text='E-mail Id:',pady=7,font=("Arial", 35))
    label_mail.grid(row=9,column=0)

    #the entries
    entry_id=Entry(root,width=20,font=("Arial", 35))
    entry_id.grid(row=1,column=1)
    
    entry_name=Entry(root,width=20,font=("Arial", 35))
    entry_name.grid(row=2,column=1)

    val_sex=StringVar()
    Radiobutton(root,text='Male',variable=val_sex,value='M',font=("Arial", 35)).grid(row=3,column=1,pady=0)
    Radiobutton(root,text='Female',variable=val_sex,value='F',font=("Arial", 35)).grid(row=4,column=1,pady=0)
    
    val_class=StringVar()
    val_class.set('XI')
    drop_class=OptionMenu(root,val_class,'XI','XII')
    drop_class.grid(row=5,column=1)
    
    val_sec=StringVar()
    val_sec.set('A')
    drop_sec=OptionMenu(root,val_sec,'A','B')
    drop_sec.grid(row=6,column=1)

    val_strm=StringVar()
    val_strm.set('Science')
    drop_strm=OptionMenu(root,val_strm,'Science','Commerce')
    drop_strm.grid(row=7,column=1)
    
    entry_No=Entry(root,width=20,font=("Arial", 35))
    entry_No.grid(row=8,column=1)
    
    entry_mail=Entry(root,width=20,font=("Arial", 35))
    entry_mail.grid(row=9,column=1)

    #fnc for ok
    def ok_fnc(a):
        
        if entry_id.get() or entry_name.get() or entry_No.get() or entry_mail.get() == '':
            messagebox.showerror('Reminder', 'Please fill in all the records')
            
        def done():
            #inserting values into database
            code=''
            if val_strm.get()=='Science':
                code+='S'
                code+=(val_me.get())[:1]
                code+=(val_bcp.get())[:1]
            else:
                if val_strm.get()=='Commerce':
                    code+='C'
                    code+=(val_mcp.get())[:1]
            try:        
                query="insert into std_details values('{}','{}','{}','{}','{}','{}',{},'{}','{}')".format(entry_id.get(),entry_name.get(),val_sex.get(),val_class.get(),val_sec.get(),val_strm.get(),int(entry_No.get()),entry_mail.get(),code)
                cursor.execute(query)
                sqlcon.commit()
                query="insert into marks_details (id) values('{}')".format(entry_id.get())
                sqlcon.commit()
                messagebox.showinfo('Data was successfully added',entry_name.get()+' has been added as a new student')
                top.destroy()
                root.destroy()
                menu(3)
            except sc.errors.IntegrityError:
                messagebox.showinfo('Please choose another ID', 'This ID already exists in data base')
            
            

        
        reply=messagebox.askquestion('Please ensure you have filled all the fields','Are you sure you want to Enter these details into database')
        if reply=='yes':
            # the choice of subjects
            
            top=Toplevel()
            top.title("Enter their choosen subject")
            if val_strm.get()=='Science':
                #Math/Eco
                label_me=Label(top,text='Math/Eco:',pady=7,font=("Arial", 35))
                label_me.grid(row=0,column=0)
               
                val_me=StringVar()
                val_me.set('Mathematics')
                drop_me=OptionMenu(top,val_me,'Mathematics','Economics')
                drop_me.grid(row=0,column=1)
                #Bio/Comp/Psy
                label_bcp=Label(top,text='Bio/Comp/Psy:',pady=7,font=("Arial", 35))
                label_bcp.grid(row=1,column=0)

                val_bcp=StringVar()
                val_bcp.set('Biology')
                drop_bcp=OptionMenu(top,val_bcp,'Biology','Computer Science','Psychology')
                drop_bcp.grid(row=1,column=1)

                #done-button
                done_button=Button(top,text='Done',command=done,padx=30)
                done_button.grid(row=4,column=1,pady=10)
                
            elif val_strm.get()=='Commerce':
                #Math/Comp/Psy
                label_mcp=Label(top,text='Math/Comp/Psy:',pady=7,font=("Arial", 35))
                label_mcp.grid(row=0,column=0)

                val_mcp=StringVar()
                val_mcp.set('Mathematics')
                drop_mcp=OptionMenu(top,val_mcp,'Mathematics','Computer Science','Psychology')
                drop_mcp.grid(row=0,column=1)

                #done-button
                done_button=Button(top,text='Done',command=done,padx=30)
                done_button.grid(row=1,column=1,pady=10)
                
                bk2M=Button(root,text='Back to Menu',command=lambda:Exit(root)).grid(row=2,column=0,sticky=W+S)


    #ok button
    ok_button=Button(root,text='OK',command=lambda:ok_fnc(1),padx=30)
    ok_button.grid(row=10,column=1,pady=10)

    bk2M=Button(root,text='Back to Menu',command=lambda:Exit(root)).grid(row=11,column=0,sticky=W+S,pady=250,padx=10)
    root.mainloop()
"============================================================================================================="
def fnc_Enter_Marks():
    root=Tk()
    root.geometry('600x500')
    root.title('Enter the student id')
     #id 
    id_label=Label(root,text='ID:',padx=50,pady=50,font=("Arial", 35))
    id_label.grid(row =0,column=0)

    entry_id=Entry(root,width=20,font=("Arial", 35))
    entry_id.grid(row=0,column=1)
     
    def fnc_data_enter(Class,Stream,Code,ID):
        cursor.execute("select id from marks_details")
        L=cursor.fetchall()
        if (ID,) in L:
            messagebox.showerror("Student's marks has already been entered","Try to enter different id or modify the marks of the student")
            menu(3)
        if Stream == 'Science':
            _1='English'
            _2='Physics'
            _3='Chemistry'
            if Code[1]=='M':
                _4="Maths"
            else:_4='Economics'
            if Code[2]=='B':
                _5="Biology"
            elif Code[2]=='C': _5="Psychology"
            else:_5='Computer Science'
        elif Stream == 'Commerce':
            _1='English'
            _2='Accounts'
            _3='Business Studies'
            _4="Economics"
            if Code[1]=='M':
                _5="Maths"
            elif Code[1]=='P': _5="Psychology"
            else:_5='Computer Science'
        
        root=Tk()
        root.geometry()
        root.title('Enter Marks')

        #the instruction
        frame=LabelFrame(root,padx=10,pady=10)
        frame.grid(row=0,column=0,padx=170,pady=15,columnspan=2)
        instrc=Label(frame,text='Enter Marks and click ok',font=("Arial", 35))
        instrc.pack()
        #the labels
        label_1=Label(root,text=_1,pady=7,font=("Arial", 35))
        label_1.grid(row=1,column=0)
        
        label_2=Label(root,text=_2,pady=7,font=("Arial", 35))
        label_2.grid(row=2,column=0)
        
        label_3=Label(root,text=_3,pady=7,font=("Arial", 35))
        label_3.grid(row=3,column=0)
        
        label_4=Label(root,text=_4,pady=7,font=("Arial", 35))
        label_4.grid(row=4,column=0)

        label_5=Label(root,text=_5,pady=7,font=("Arial", 35))
        label_5.grid(row=5,column=0)

        entry_1=Entry(root,width=20,font=("Arial", 35))
        entry_1.grid(row=1,column=1)

        entry_2=Entry(root,width=20,font=("Arial", 35))
        entry_2.grid(row=2,column=1)
        
        entry_3=Entry(root,width=20,font=("Arial", 35))
        entry_3.grid(row=3,column=1)
       
        entry_4=Entry(root,width=20,font=("Arial", 35))
        entry_4.grid(row=4,column=1)
        
        entry_5=Entry(root,width=20,font=("Arial", 35))
        entry_5.grid(row=5,column=1)

        
        #fnc for ok
        def fnc_EnterM():
            try:
                total=float(entry_1.get()) + float(entry_2.get()) + float(entry_3.get()) + float(entry_4.get()) + float(entry_5.get()) 
                percent=(total/500)*100
                query="insert into marks_details values('{}',{},{},{},{},{},{},{})".format(ID,float(entry_1.get()),float(entry_2.get()),float(entry_3.get()),float(entry_4.get()),float(entry_5.get()),total,percent)
                reply=messagebox.askquestion('Please ensure you have filled all the fields','Are you sure you want to Enter these details into database')
                if reply=='yes':
                    cursor.execute(query)
                    sqlcon.commit()
                    messagebox.showinfo(' ','Data was successfully added')
                    root.destroy()
                    menu(3)
            except:
                messagebox.showerror('Error','Please ensure you have filled all the records correctly')
        #ok button
        ok_button=Button(root,text='OK',command=fnc_EnterM,padx=30)
        ok_button.grid(row=6,column=1,pady=10)
        bk2M=Button(root,text='Back to Menu',command=lambda:Exit(root)).grid(row=7,column=0,sticky=W+S)
        root.mainloop()


    def fnc_ok():
        try:
            #code to which table to go to in database
            ID=entry_id.get()
            query="select Class,Stream,Code from std_details where id='{}'".format(ID)
            cursor.execute(query)
            L=cursor.fetchall()
            Class=L[0][0]
            Stream=L[0][1]
            Code=L[0][2]
            root.destroy()
            fnc_data_enter(Class,Stream,Code,ID)
        except:
             messagebox.showerror('Error', 'Please fill in valid id')
             root.destroy()
             fnc_Enter_Marks()
             
         
             
    ok_bttn=Button(root,text='OK',command=fnc_ok,padx=30)
    ok_bttn.grid(row=1,column=1,pady=7)
    bk2M=Button(root,text='Back to Menu',command=lambda:Exit(root)).grid(row=2,column=0,sticky=W+S,pady=70,padx=15)
"=========================================================================================================="
def fnc_delete():
    root=Tk()
    root.geometry('600x500')
    root.title('Enter the student id')
     #id 
    id_label=Label(root,text='ID:',padx=50,pady=150,font=("Arial", 35))
    id_label.grid(row =0,column=0)

    entry_id=Entry(root,width=20,font=("Arial", 35))
    entry_id.grid(row=0,column=1)
    def fnc_ok():
        try:
             #code to which table to go to in database
             ID=entry_id.get()
             query="select Class,Stream,Code from std_details where id='{}'".format(ID)
             cursor.execute(query)
             L=cursor.fetchall()
             j=L[0][0]
             
             
             query="delete from std_details where id='{}'".format(ID)
             cursor.execute(query)
             Q="delete from marks_details where id='{}'".format(ID)
             cursor.execute(Q)
             sqlcon.commit()
             messagebox.showinfo('Successful','Student has been removed from the database')
             root.destroy()
             menu(3)
        except :
             messagebox.showerror('Error', 'Please fill in valid id')
             
    ok_bttn=Button(root,text='OK',command=fnc_ok,padx=30)
    ok_bttn.grid(row=1,column=1,pady=7)
    bk2M=Button(root,text='Back to Menu',command=lambda:Exit(root)).grid(row=2,column=0,sticky=W+S,pady=70,padx=15)
"=============================================================================================================="
def fnc_modify():
    root=Tk()
    root.geometry('600x500')
    root.title('Menu')

    #the instruction
    frame=LabelFrame(root,padx=8,pady=10)
    frame.grid(row=0,column=0,padx=100,pady=15,columnspan=3)
    instrc=Label(frame,text='Select option and click ok',font=("Arial", 35))
    instrc.pack()

    #RadioButton
    operations=[
        ('Modify Student Details','Modify Student Details'),
        ('Modify Student marks','Modify Student marks'),
        ]

    choice=StringVar()
    choice.set('Enter a new student')

    j=1
    for oprtn,mode in operations:
        Radiobutton(root,text=oprtn,variable=choice,value=mode,font=("Arial", 35)).grid(row=j,column=1,pady=8)
        j+=1
    ####
    def opt_info():
        reply=messagebox.askquestion('Are you sure you want to',choice.get())
        if reply=='yes':
            root.destroy()
            if choice.get()=='Modify Student Details':
                fnc_Modify_student()
            elif choice.get()=='Modify Student marks':
                fnc_Modify_Marks()
        elif reply=='no':
            root.destroy()
            menu(3)

    #Button
    ok=Button(root,text='OK',command=opt_info,padx=30)
    ok.grid(row=j,column=1,pady=8)
    bk2M=Button(root,text='Back to Menu',command=lambda:Exit(root)).grid(row=j+1,column=0,sticky=W+S,pady=150,padx=20)
    root.mainloop()

def fnc_Modify_student():
    root=Tk()
    root.geometry('600x500')
    root.title('Enter the student id')
     #id 
    id_label=Label(root,text='ID:',padx=50,pady=7,font=("Arial", 35))
    id_label.grid(row =0,column=0)

    entry_id=Entry(root,width=20,font=("Arial", 35))
    entry_id.grid(row=0,column=1)

    def fnc_ok(root):
        #code to which table to go to in database
        
        ID=entry_id.get()
        root.destroy()
        try:
            query="select * from std_details where id='{}'".format(ID)
            cursor.execute(query)
            L=cursor.fetchall()
            code=L[0][-1]
            fnc_Modify_studentdetails(L,ID)
        except:
            messagebox.showerror('Error', 'Please fill in valid id')
        

    ok_bttn=Button(root,text='OK',command=lambda:fnc_ok(root),padx=30)
    ok_bttn.grid(row=1,column=1,pady=7)
    bk2M=Button(root,text='Back to Menu',command=lambda:Exit(root)).grid(row=2,column=0,sticky=W+S,pady=150,padx=15)
    

def fnc_Modify_studentdetails(L,ID):
    root=Tk()
    root.geometry('1100x1000')
    root.title('With reference to the previous student data printed, you may modify the data')
     
    #the instruction
    frame=LabelFrame(root,padx=10,pady=10)
    frame.grid(row=0,column=0,padx=170,pady=15,columnspan=2)
    instrc=Label(frame,text='Enter details as required and click ok',font=("Arial", 35))
    instrc.pack()
    #the labels
    label_id=Label(root,text='Student ID:',pady=7,font=("Arial", 35))
    label_id.grid(row=1,column=0)
    label_id=Label(root,text='Student ID:',pady=7,font=("Arial", 35))
    label_id.grid(row=1,column=0)
    
    label_name=Label(root,text='Name:',pady=7,font=("Arial", 35))
    label_name.grid(row=2,column=0)
    
    label_sex=Label(root,text='Sex:',pady=7,font=("Arial", 35))
    label_sex.grid(row=3,column=0)
    
    label_class=Label(root,text='Class:',pady=7,font=("Arial", 35))
    label_class.grid(row=5,column=0)
    
    label_sec=Label(root,text='Section:',pady=7,font=("Arial", 35))
    label_sec.grid(row=6,column=0)

    label_stream=Label(root,text='Stream:',pady=7,font=("Arial", 35))
    label_stream.grid(row=7,column=0)
    
    label_No=Label(root,text='Phone Number:',pady=7,font=("Arial", 35))
    label_No.grid(row=8,column=0)
    
    label_mail=Label(root,text='E-mail Id:',pady=7,font=("Arial", 35))
    label_mail.grid(row=9,column=0)

    #the entries
    entry_id=Entry(root,width=20,font=("Arial", 35))
    entry_id.grid(row=1,column=1)
    entry_id.insert(0,L[0][0])
    
    entry_name=Entry(root,width=20,font=("Arial", 35))
    entry_name.grid(row=2,column=1)
    entry_name.insert(0,L[0][1])
    
    val_sex=StringVar()
    val_sex.set('M')
    Radiobutton(root,text='Male',variable=val_sex,value='M',font=("Arial", 35)).grid(row=3,column=1,pady=0)
    Radiobutton(root,text='Female',variable=val_sex,value='F',font=("Arial", 35)).grid(row=4,column=1,pady=0)
    val_sex.set('M')
    
    val_class=StringVar()
    val_class.set('XI')
    drop_class=OptionMenu(root,val_class,'XI','XII')
    drop_class.grid(row=5,column=1)
    
    val_sec=StringVar()
    val_sec.set('A')
    drop_sec=OptionMenu(root,val_sec,'A','B')
    drop_sec.grid(row=6,column=1)

    val_strm=StringVar()
    val_strm.set('Science')
    drop_strm=OptionMenu(root,val_strm,'Science','Commerce')
    drop_strm.grid(row=7,column=1)
    
    entry_No=Entry(root,width=20,font=("Arial", 35))
    entry_No.grid(row=8,column=1)
    entry_No.insert(0,L[0][-3])
    
    entry_mail=Entry(root,width=20,font=("Arial", 35))
    entry_mail.grid(row=9,column=1)
    entry_mail.insert(0,L[0][-2])
    #fnc for ok
    def ok_fnc(L,ID):
        L[0]=list(L[0])
        L[0][0]=entry_id.get()
        L[0][1]=entry_name.get()
        L[0][-3]=entry_No.get()
        L[0][-2]=entry_mail.get()
        
        if len(L[0][0])== 0 or len(L[0][1])== 0 or len(L[0][-3])== 0 or len(L[0][-2]) == 0:
            messagebox.showerror('Retry','Ensure you fill all the fields')
            L[0]=list(L[0])
            L[0][0]=entry_id.get()
            L[0][1]=entry_name.get()
            L[0][-3]=entry_No.get()
            L[0][-2]=entry_mail.get()
            root.destroy()
            fnc_Modify_studentdetails(L)
        def done():
            #inserting values into database
            
            code=''
            if val_strm.get()=='Science':
                code+='S'
                code+=(val_me.get())[:1]
                code+=(val_bcp.get())[:1]
            else:
                if val_strm.get()=='Commerce':
                    code+='C'
                    code+=(val_mcp.get())[:1]
            Q="delete from std_details where id='{}'".format(ID)
            cursor.execute(Q)
            query="insert into std_details values('{}','{}','{}','{}','{}','{}',{},'{}','{}')".format(entry_id.get(),entry_name.get(),val_sex.get(),val_class.get(),val_sec.get(),val_strm.get(),int(entry_No.get()),entry_mail.get(),code)
            cursor.execute(query)
            sqlcon.commit()
            messagebox.showinfo('Data was successfully updated',entry_name.get()+' record has been chnaged')
            top.destroy()
            root.destroy()
            menu(3)
            

        
        reply=messagebox.askquestion('Are you sure you want to','Enter these details into database')
        if reply=='yes':
            # the choice of subjects
            
            top=Toplevel()
            top.title("Enter their choosen subject")
            if val_strm.get()=='Science':
                #Math/Eco
                label_me=Label(top,text='Math/Eco:',pady=7)
                label_me.grid(row=0,column=0)

                val_me=StringVar()
                val_me.set('Mathematics')
                drop_me=OptionMenu(top,val_me,'Mathematics','Economics')
                drop_me.grid(row=0,column=1)
                #Bio/Comp/Psy
                label_bcp=Label(top,text='Bio/Comp/Psy:',font=("Arial", 35),pady=7)
                label_bcp.grid(row=1,column=0)

                val_bcp=StringVar()
                val_bcp.set('Biology')
                drop_bcp=OptionMenu(top,val_bcp,'Biology','Computer Science','Psychology')
                drop_bcp.grid(row=1,column=1)

                #done-button
                done_button=Button(top,text='Done',command=done,padx=30)
                done_button.grid(row=4,column=1,pady=10)
                
            elif val_strm.get()=='Commerce':
                #Math/Comp/Psy
                label_mcp=Label(top,text='Math/Comp/Psy:',pady=7,font=("Arial", 35))
                label_mcp.grid(row=0,column=0)

                val_mcp=StringVar()
                val_mcp.set('Mathematics')
                drop_mcp=OptionMenu(top,val_mcp,'Mathematics','Computer Science','Psychology')
                drop_mcp.grid(row=0,column=1)

                #done-button
                done_button=Button(top,text='Done',command=lambda:done,padx=30)
                done_button.grid(row=1,column=1,pady=10)

    #ok button
    ok_button=Button(root,text='OK',command=lambda:ok_fnc(L,ID),padx=30)
    ok_button.grid(row=10,column=1,pady=10)
    bk2M=Button(root,text='Back to Menu',command=lambda:Exit(root)).grid(row=11,column=0,sticky=W+S,pady=70,padx=20)
    root.mainloop()

def fnc_Modify_Marks():
    root=Tk()
    root.geometry('600x500')
    root.title('Enter the student id')
     #id 
    id_label=Label(root,text='ID:',padx=50,pady=7,font=("Arial", 35))
    id_label.grid(row =0,column=0)

    entry_id=Entry(root,width=20,font=("Arial", 35))
    entry_id.grid(row=0,column=1)

    def fnc_ok1(root):
       
        ID=entry_id.get()
        try:
            #code to which table to go to in database
            query="select * from marks_details where id='{}'".format(ID)
            cursor.execute(query)
            L=cursor.fetchall()
            query1="select * from std_details where id='{}'".format(ID)
            cursor.execute(query1)
            L1=cursor.fetchall()
            code=L1[0][-1]
            #fnc_Modify_marksdetails()
            query1="select * from std_details where id='{}'".format(ID)
            cursor.execute(query1)
            L1=cursor.fetchall()
            
            if L1[0][5]=='Science':
                _1,_2,_3="English","Physics","Chemistry"
                if code[1]=='M':
                    _4="Mathematics"
                else: _4="Economics"
                if code[2]=="B":
                    _5="Biology"
                elif code[2]=="P":
                    _5="Psycology"
                else: _5="Computer"
            else:
                _1,_2,_3,_4="English","Accounts","Bussiness_Std","Economics"
                if code[-1]=="M":
                    _5="Mathematics"
                elif code[-1]=="P":
                    _5="Psycology"
                else: _5="Computer"
            root.destroy()
            root=Tk()
            root.geometry('1300x500')
            root.title('Enter Marks')

            #the instruction
            frame=LabelFrame(root,padx=10,pady=10)
            frame.grid(row=0,column=0,padx=170,pady=15,columnspan=2)
            instrc=Label(frame,text='With reference to the previous data printed, you may modify the data',font=("Arial", 35))
            instrc.pack()
            #the labels
            label_1=Label(root,text=_1,pady=7,font=("Arial", 35))
            label_1.grid(row=1,column=0)
            
            label_2=Label(root,text=_2,pady=7,font=("Arial", 35))
            label_2.grid(row=2,column=0)
            
            label_3=Label(root,text=_3,pady=7,font=("Arial", 35))
            label_3.grid(row=3,column=0)
            
            label_4=Label(root,text=_4,pady=7,font=("Arial", 35))
            label_4.grid(row=4,column=0)

            label_5=Label(root,text=_5,pady=7,font=("Arial", 35))
            label_5.grid(row=5,column=0)

            entry_1=Entry(root,width=20,font=("Arial", 35))
            entry_1.grid(row=1,column=1)
            entry_1.insert(0,str(L[0][1]))

            entry_2=Entry(root,width=20,font=("Arial", 35))
            entry_2.grid(row=2,column=1)
            entry_2.insert(0,str(L[0][2]))
            
            entry_3=Entry(root,width=20,font=("Arial", 35))
            entry_3.grid(row=3,column=1)
            entry_3.insert(0,str(L[0][3]))
            
            entry_4=Entry(root,width=20,font=("Arial", 35))
            entry_4.grid(row=4,column=1)
            entry_4.insert(0,str(L[0][4]))
            
            entry_5=Entry(root,width=20,font=("Arial", 35))
            entry_5.grid(row=5,column=1)
            entry_5.insert(0,str(L[0][5]))

            
            #fnc for ok
            def fnc_EnterM():
                ############################################################
                M=[ID,int(float(entry_1.get())),int(float(entry_2.get())),int(float(entry_3.get())),int(float(entry_4.get())),int(float(entry_5.get()))]
                if '' in M or 0 in M:
                    messagebox.showerror('Pls enter valid records')
                else:
                    total=int(float(entry_1.get())) + int(float(entry_2.get())) + int(float(entry_3.get())) + int(float(entry_4.get())) + int(float(entry_5.get())) 
                    percent=(total/500)*100
                    Q="delete from marks_details where id='{}'".format(ID)
                    cursor.execute(Q)
                    query="insert into marks_details values('{}',{},{},{},{},{},{},{})".format(ID,int(float(entry_1.get())),int(float(entry_2.get())),int(float(entry_3.get())),int(float(entry_4.get())),int(float(entry_5.get())),total,percent)
                    
                    cursor.execute(query)
                    sqlcon.commit()
                    messagebox.showinfo(' ','Data was successfully added')
                    root.destroy()
                    menu(3)
                
            #ok button
            ok_button=Button(root,text='OK',command=fnc_EnterM,padx=30)
            ok_button.grid(row=6,column=1,pady=10)
            bk2M=Button(root,text='Back to Menu',command=lambda:Exit(root)).grid(row=7,column=0,sticky=W+S)

            
            root.mainloop()
        except:
            messagebox.showerror('Retry','Please enter student\'s marks first')
            root.destroy()
            fnc_Modify_Marks()
            
            
        
        

    ok_bttn=Button(root,text='OK',command=lambda:fnc_ok1(root),padx=30)
    ok_bttn.grid(row=1,column=1,pady=7)
    bk2M=Button(root,text='Back to Menu',command=lambda:Exit(root)).grid(row=2,column=0,sticky=W+S)

   
  
def fnc_graph():
    
    root=Tk()
    root.geometry('600x500')
    label=Label(root,text='Choose class:',font=("Arial", 35)).grid(row=0,column=0,padx=24,pady=20)

    val_class=StringVar()
    val_class.set('XI_SCI')
    drop_class=OptionMenu(root,val_class,'XI_SCI','XI_COM','XII_SCI','XII_COM').grid(row=0,column=1)

    def opt_info(root):
        x=val_class.get()
        root.destroy()
        
        root=Tk()
        root.geometry('600x500')
        label=Label(root,text='Do you want graph:',font=("Arial", 35)).grid(row=0,column=0,padx=24,pady=20)
        

        val_opt=StringVar()
        val_opt.set('All subject-wise')
        drop_opt=OptionMenu(root,val_opt,'All subject-wise','One subject-wise').grid(row=0,column=1)

        
        def graph(x,root):
            
            if val_opt.get()== 'All subject-wise':
                info=x.split('_')
                if info[1]=='SCI':
                    info[1]='Science'
                else: info[1]='Commerce'
                Class,Strm=info
                Q="select Percentage from marks_details M ,std_details S where class='{}' and stream='{}' and M.Id=S.Id".format(Class,Strm)
                cursor.execute(Q)
                L=cursor.fetchall()
            
                D={'0-10':0,'10-20':0,'20-30':0,'30-40':0,'40-50':0,'50-60':0,'60-70':0,'70-80':0,'80-90':0,'90-100':0}
                for i in L:
                    if i[0]==None:
                        continue
                    x=int(i[0]//10)
                    if x==10:
                        x=9
                    D[str(x)+'0-'+str(x+1)+'0']=D[str(x)+'0-'+str(x+1)+'0']+1
               
                plt.plot(list(D.keys()),list(D.values()))
                plt.ylabel('number of students')
                plt.xlabel('range of percentage')
                plt.show()

            else:
                L=[['English','Physics','Chemistry','Mathematics','Economics','CompurterScience','Biology','Psycology'],['English','Accounts','BusinessStds','Economics','Mathematics','CompurterScience','Psycology','']]
                info=x.split('_')
                if info[1]=='SCI':
                    info[1]='Science'
                    L=L[0]
                else:
                    info[1]='Commerce'
                    L=L[1]
                root.destroy()

                root=Tk()
                root.geometry('600x250')
                label=Label(root,text='Choose subject:',font=("Arial", 35)).grid(row=0,column=0,padx=24,pady=20)
                
                val_sub=StringVar()
                val_sub.set('English')
                drop_sub=OptionMenu(root,val_sub,L[0],L[1],L[2],L[3],L[4],L[5],L[6],L[7]).grid(row=0,column=1)                    

                def graph_sub(info,root):
                    if info[1]=='Science':
                        D={'English':1,'Physics':2,'Chemistry':3,'Mathematics':4,'Economics':4,'CompurterScience':5,'Biology':5,'Psycology':5}
                    else:
                        D={'English':1,'Accounts':2,'BusinessStds':3,'Economics':4,'Mathematics':5,'CompurterScience':5,'Psycology':5}
                    column='Subject'+str(D[val_sub.get()])
                    Q="select {} from marks_details M ,std_details S where class='{}' and stream='{}' and M.Id=S.Id".format(column,info[0],info[1])
                    cursor.execute(Q)
                    L=cursor.fetchall()
          
                    D={'0-10':0,'10-20':0,'20-30':0,'30-40':0,'40-50':0,'50-60':0,'60-70':0,'70-80':0,'80-90':0,'90-100':0}
                    for i in L:
                        if i[0]==None:
                            continue
                        x=int(i[0]//10)
                        if x==10:
                            x=9
                        D[str(x)+'0-'+str(x+1)+'0']=D[str(x)+'0-'+str(x+1)+'0']+1
                    plt.plot(list(D.keys()),list(D.values()))
                    plt.ylabel('number of students')
                    plt.xlabel('range of scores')
                    plt.show()
                        
                
                ok=Button(root,text='OK',command=lambda:graph_sub(info,root),padx=30)
                ok.grid(row=1,column=1,pady=8)
                bk2M=Button(root,text='Back to Menu',command=lambda:Exit(root)).grid(row=1,column=0)
                
        ok=Button(root,text='OK',command=lambda:graph(x,root),padx=30)
        ok.grid(row=1,column=1,pady=8)
        bk2M=Button(root,text='Back to Menu',command=lambda:Exit(root)).grid(row=2,column=0,sticky=W+S)    
        root.mainloop()
    #Button
    ok=Button(root,text='OK',command=lambda:opt_info(root),padx=30)
    ok.grid(row=1,column=1,pady=8)
    bk2M=Button(root,text='Back to Menu',command=lambda:Exit(root)).grid(row=2,column=0,sticky=W+S)

    root.mainloop()

def disp():
    cursor.execute("select id from marks_details")
    listid=cursor.fetchall()
    cursor.execute("select id from std_details")
    listidmrks=cursor.fetchall()
    list2del=[]
    for i in listid:
        if i not in listidmrks:
            list2del.append(i[0])
    
    if len(list2del)==1:
        cursor.execute(f"delete from marks_details where id in ({list2del[0]})")
    elif list2del !=[]:
        cursor.execute(f"delete from marks_details where id in {tuple(list2del)}")
    root=Tk()
    root.geometry("400x150")

    Choose=Label(root,text="Choose Class:",font=("Arial", 35))
    Choose.grid(row=0,column=0,padx=10,pady=10)

    cls=StringVar()
    cls.set("XI A")

    drop=OptionMenu(root,cls,"XI A","XI B","XII A","XII B")
    drop.grid(row=0,column=1)
    def fnc(CLASS,root):
        clas=CLASS.split()[0]
        sec=CLASS.split()[1]

        Q="select*from std_details where Class='{}' and Section='{}'".format(clas,sec)
        cursor.execute(Q)
        L1=cursor.fetchall()
        for a in range(len(L1)):
            L1[a]=list(L1[a])
        
        list_id_std=[]
        for i in L1:
            list_id_std.append(i[0])
        
        cursor.execute("select M.Id,Name,Subject1,Subject2,Subject3,Subject4,Subject5,Total,Percentage from marks_details M,std_details S where M.Id=S.id and Class='{}' and Section='{}'".format(clas,sec))

        L1=cursor.fetchall()
        
        list_id_mrk=[]
        for i in L1:
            list_id_mrk.append(i[0])

        '''list_names=[]
    
        for i in list_id_std:
            if i not in list_id_mrk:'''
                
        cursor.execute("select id, name from std_details where Class='{}' and Section='{}'".format(clas,sec))
        L2=cursor.fetchall()
        
        for i in list_id_std:
            if i in list_id_mrk:
                pass
            else:
                name=0
                for rec in L2:
                    if i in rec:
                        name=rec[1]
                        break
                L1.append([i,name,"NULL","NULL","NULL","NULL","NULL","NULL"])
                
          
        for a in range(len(L1)):
            L1[a]=list(L1[a])
        
        for i in L1:
            for j in range(len(i)):
                if i[j]== None:
                    i[j]='NULL'
        
        root.destroy()
        root=Tk()
        root.geometry('1600x500')

        main_frame=Frame(root)
        main_frame.pack(fill=BOTH,expand=1)

        my_canvas=Canvas(main_frame)
        my_canvas.pack(side=LEFT,fill=BOTH,expand=1)

        my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT,fill=Y)

        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>',lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

        second_frame=Frame(my_canvas)
        my_canvas.create_window((0,0),window=second_frame,anchor='nw')
        
        Label(second_frame,text='Student Details').grid(row=0,column=0,columnspan=9)
        if sec=="A":
            L1.insert(0,['Id','Name','English',"Physics","Chemistry","Math/Eco",'Comp/Bio/Psy','Total','Percentage'])
        else:
            L1.insert(0,['Id','Name','English',"Accounts","Bussiness_Stds","Economics",'Comp/Math/Psy','Total','Percentage'])
            
        for row in range(len(L1)):
            for col in range(8):
                l=Entry(second_frame,width=20)
                l.insert(0,L1[row][col])
                l.grid(row=row+1,column=col)
        bk2M=Button(second_frame,text='Back to Menu',command=lambda:Exit(root)).grid(row=row+2,column=0)
    
    Bttn2=Button(root,text="OK",command=lambda:fnc(cls.get(),root))
    Bttn2.grid(row=1,column=1,padx=5,pady=5)
    bk2M=Button(root,text='Back to Menu',command=lambda:Exit(root))
    bk2M.grid(row=1,column=0)
    root.mainloop()

    

def repcar(k=3):
    root=Tk()
    root.geometry('600x500')
    root.title('Enter the student id')
     #id 
    id_label=Label(root,text='ID:',padx=50,pady=7,font=("Arial", 35))
    id_label.grid(row =0,column=0)

    entry_id=Entry(root,width=20,font=("Arial", 35))
    entry_id.grid(row=0,column=1)
    def fnc_ok(root):
         #code to which table to go to in database
         ID=entry_id.get()
         
         cursor.execute("select id from marks_details")
         list_of_id=cursor.fetchall()
         if (ID,) in list_of_id:
              query="select Class,Stream,Code,Name from std_details where id='{}'".format(ID)
              cursor.execute(query)
              L=cursor.fetchall()
              code=L[0][2]
              L1=['English']
              if code[0]=='S':
                  L1.append('Physics')
                  L1.append('Chemistry')
              else:
                  L1.append('Accounts')
                  L1.append('Business Studies')
                  L1.append('Economics')
                      
              for i in range(1,len(code)):
                 if code[i]=='M':
                      L1.append('Mathematics')
                 if code[i]=='E':
                      L1.append('Economics')
                 if code[i]=='C':
                      L1.append('Computer Science')
                 if code[i]=='B':
                      L1.append('Biology')
                 if code[i]=='P':
                      L1.append('Psychology')
              L1.append('Total Marks')
              L1.append('Percentage')
              Q="select * from marks_details where id='{}'".format(ID)
              cursor.execute(Q)
              L2=cursor.fetchall()
              s=''
              if L2[0][-1]<35:
                 s='Fail'
              else:
                 s='Pass'
              root.destroy()
              root=Tk()
              root.geometry('700x900')
              root.title('REPORT CARD')
              
              entry1=Entry(root,width=15,font=("Arial", 35))
              entry1.grid(row=1,column=0,padx=10)
              entry1.insert(1,"Student Name:")
              
              entry2=Entry(root,width=15,font=("Arial", 35))
              entry2.grid(row=1,column=1)
              entry2.insert(1,L[0][3])

              entry3=Entry(root,width=15,font=("Arial", 35))
              entry3.grid(row=2,column=0)
              entry3.insert(1,'Class')
              
              entry4=Entry(root,width=15,font=("Arial", 35))
              entry4.grid(row=2,column=1)
              entry4.insert(1,L[0][0])

              entry5=Entry(root,width=15,font=("Arial", 35))
              entry5.grid(row=3,column=0)
              entry5.insert(1,'Stream:')
              
              entry6=Entry(root,width=15,font=("Arial", 35))
              entry6.grid(row=3,column=1)
              entry6.insert(1,L[0][1])

              
              entry7=Entry(root,width=15,font=("Arial", 35))
              entry7.grid(row=4,column=0)
              entry7.insert(1,'==========')
              
              entry8=Entry(root,width=15,font=("Arial", 35))
              entry8.grid(row=4,column=1)
              entry8.insert(1,'=========')

              entry9=Entry(root,width=15,font=("Arial", 35))
              entry9.grid(row=5,column=0)
              entry9.insert(1,'Subject')
              
              entry10=Entry(root,width=15,font=("Arial", 35))
              entry10.grid(row=5,column=1)
              entry10.insert(1,'Marks')

              entry11=Entry(root,width=15,font=("Arial", 35))
              entry11.grid(row=6,column=0)
              entry11.insert(1,'==========')
              
              entry12=Entry(root,width=15,font=("Arial", 35))
              entry12.grid(row=6,column=1)
              entry12.insert(1,'========')

              for i in range(len(L1)):

                  entry11=Entry(root,width=15,font=("Arial", 35))
                  entry11.grid(row=7+i,column=0)
                  entry11.insert(1,L1[i])
                  
                  entry12=Entry(root,width=15,font=("Arial", 35))
                  entry12.grid(row=7+i,column=1)
                  entry12.insert(1,L2[0][i+1])


              entry13=Entry(root,width=15,font=("Arial", 35))
              entry13.grid(row=7+len(L1),column=0)
              entry13.insert(1,'==========')
              
              entry14=Entry(root,width=15,font=("Arial", 35))
              entry14.grid(row=7+len(L1),column=1)
              entry14.insert(1,'==========')

              entry15=Entry(root,width=15,font=("Arial", 35))
              entry15.grid(row=8+len(L1),column=0)
              entry15.insert(1,'Result: ')
              
              entry16=Entry(root,width=15,font=("Arial", 35))
              entry16.grid(row=8+len(L1),column=1)
              entry16.insert(1,s)
              
              ok_bttn=Button(root,text='OK',command=lambda:Exit(root),padx=30)
              ok_bttn.grid(row=9+len(L1),column=1,pady=7)
            
         else:
              messagebox.showerror("Invalid ID","Please enter marks of the student first")
              
                  
                  

    ok_bttn=Button(root,text='OK',command=lambda:fnc_ok(root),padx=30)
    ok_bttn.grid(row=1,column=1,pady=7)

    bk2M=Button(root,text='Back to Menu',command=lambda:Exit(root)).grid(row=2,column=0)
    
def startscreen():    
    root=Tk()
    root.geometry("1000x600")
    root.title('Computer project-Grade 12')

    student=Label(root,text="STUDENT \nREPORT CARD",font=("Menlo",35,"bold"))
    student.grid(row=0,column=0,padx=50,pady=50)

    proj=Label(root,text="COMPUTER SCIENCE PROJECT",font=("Menlo", 35))
    proj.grid(row=1,column=0,padx=50)

    Label(root,text='').grid(row=2,column=0)

    Done=Label(root,text=' '*30+'DONE BY:',font=("Menlo", 25))
    Done.grid(row=3,column=0)

    Arnav=Label(root,text='ARNAV SRINIVAS ATREY',font=("Menlo", 25))
    Arnav.grid(row=4,column=1)

    Ritvik=Label(root,text='RITVIK RAJESH RAO',font=('Menlo',25))
    Ritvik.grid(row=5,column=1)

    Label(root,text='').grid(row=6,column=1)

    Grade=Label(root,text='Grade 12',font=('Menlo',30))
    Grade.grid(row=7,column=1)

    B=Button(root,text="START",padx=100,pady=20,command=lambda:menu(root))
    B.grid(row=8,column=0)

    root.mainloop()
def exit_prog(root):
    pass #exits prog
    
startscreen()
