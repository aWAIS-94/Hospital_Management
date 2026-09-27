from tkinter import *
from tkinter import ttk
import customtkinter as ctk
import random
import time
import datetime
from tkinter import messagebox
from database import connect_db

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1530x850+0+0")
        self.root.minsize(1200,700)

        self.PatientId=StringVar()
        self.Nameoftablets=StringVar()
        self.Reference=StringVar()
        self.Dose=StringVar()
        self.NoOfTablets=StringVar()
        self.Lot=StringVar()
        self.IssueDate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.StorageAdvice=StringVar()
        self.NhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DateOfBirth=StringVar()
        self.Address=StringVar()
        self.PossibleSideEffects=StringVar()
        self.FurtherInformation=StringVar()
        self.BloodPressure=StringVar()
        self.Medication=StringVar()


        lbltitle=ctk.CTkLabel(self.root,text="Hospital Management System",font=("times new roman",50,"bold"),text_color="#0B7A3B")
        lbltitle.pack(fill=X,pady=(10,5))

        subtitle=ctk.CTkLabel(self.root,text="Patient & Prescription Management System",font=("times new roman",14),text_color="#666666")
        subtitle.pack(fill=X,pady=(0,10))

        # *************************DATA_FRAME*******************************

        DataFrame=ctk.CTkFrame(self.root,width=1500,height=390,corner_radius=15,fg_color="#F5F7FA")
        DataFrame.place(x=15,y=120)

        DataFrameLeft=ctk.CTkFrame(DataFrame,width=850,height=370,corner_radius=12,fg_color="white")
        DataFrameLeft.place(x=10,y=10)
        patient_title=ctk.CTkLabel(DataFrameLeft,text="Patient Information",font=("times new roman",20,"bold"),text_color="#1F2937")
        patient_title.place(x=20,y=10)


        DataFrameRight=ctk.CTkFrame(DataFrame,width=620,height=370,corner_radius=12,fg_color="white")
        DataFrameRight.place(x=870,y=10)
        prescription_title=ctk.CTkLabel(DataFrameRight,text="Prescription",font=("Arial",18,"bold"),text_color="#1F2937")
        prescription_title.place(x=20, y=10)

        # *************************BUTTON_FRAME*******************************

        ButtonFrame=ctk.CTkFrame(self.root,width=1500,height=65,corner_radius=10,fg_color="#F5F7FA")
        ButtonFrame.place(x=15,y=525)


        # *************************Details_FRAME*******************************
        
        DetailsFrame=ctk.CTkFrame(self.root,width=1500,height=270,corner_radius=12,fg_color="white")
        DetailsFrame.place(x=15,y=600)

        # *************************Data_Frame_Left******************************

        lblName = ctk.CTkLabel(DataFrameLeft,text="Names of Tablets",font=("Arial", 13, "bold"),text_color="#374151")
        lblName.grid(row=0, column=0, padx=(15, 8), pady=(50, 5), sticky="e") 
        comNametablet = ctk.CTkComboBox(DataFrameLeft,variable=self.Nameoftablets,values=["","Paracetamol","Ibuprofen", "Amoxicillin","Metformin","Omeprazole"],width=230,height=32,corner_radius=7)
        comNametablet.grid(row=0, column=1, padx=8, pady=(50, 5), sticky="w")


        lblReference = ctk.CTkLabel(DataFrameLeft,text="Reference No.",font=("Arial", 13, "bold"),text_color="#374151")
        lblReference.grid(row=1, column=0, padx=(15, 8), pady=3, sticky="e")
        txtReference = ctk.CTkEntry(DataFrameLeft,textvariable=self.Reference,width=230,height=32,corner_radius=7,placeholder_text="Reference number")
        txtReference.grid(row=1, column=1, padx=8, pady=3, sticky="w")
        
        
        lblDose = ctk.CTkLabel(DataFrameLeft,text="Dose",font=("Arial", 13, "bold"),text_color="#374151")
        lblDose.grid(row=2, column=0, padx=(15, 8), pady=3, sticky="e")
        txtDose = ctk.CTkEntry(DataFrameLeft,textvariable=self.Dose,width=230,height=32,corner_radius=7,placeholder_text="Enter dose")
        txtDose.grid(row=2, column=1, padx=8, pady=3, sticky="w")
        
        
        lblNoOfTablets = ctk.CTkLabel(DataFrameLeft,text="No. of Tablets",font=("Arial", 13, "bold"),text_color="#374151")
        lblNoOfTablets.grid(row=3, column=0, padx=(15, 8), pady=3, sticky="e")
        txtNoOfTablets = ctk.CTkEntry(DataFrameLeft,textvariable=self.NoOfTablets,width=230,height=32,corner_radius=7,placeholder_text="Number of tablets")
        txtNoOfTablets.grid(row=3, column=1, padx=8, pady=3, sticky="w")
        
        lblLot = ctk.CTkLabel(DataFrameLeft,text="Lot",font=("Arial", 13, "bold"),text_color="#374151")
        lblLot.grid(row=4, column=0, padx=(15, 8), pady=3, sticky="e")
        txtLot = ctk.CTkEntry(DataFrameLeft,textvariable=self.Lot,width=230,height=32,corner_radius=7,placeholder_text="Lot number")
        txtLot.grid(row=4, column=1, padx=8, pady=3, sticky="w")
        
        
        lblIssueDate = ctk.CTkLabel(DataFrameLeft,text="Issue Date",font=("Arial", 13, "bold"),text_color="#374151")
        lblIssueDate.grid(row=5, column=0, padx=(15, 8), pady=3, sticky="e")
        txtIssueDate = ctk.CTkEntry(DataFrameLeft,textvariable=self.IssueDate,width=230,height=32,corner_radius=7,placeholder_text="YYYY-MM-DD")
        txtIssueDate.grid(row=5, column=1, padx=8, pady=3, sticky="w")
        
        
        lblExpDate = ctk.CTkLabel(DataFrameLeft,text="Exp Date",font=("Arial", 13, "bold"),text_color="#374151")
        lblExpDate.grid(row=6, column=0, padx=(15, 8), pady=3, sticky="e")
        txtExpDate = ctk.CTkEntry(DataFrameLeft,textvariable=self.ExpDate,width=230,height=32,corner_radius=7,placeholder_text="YYYY-MM-DD")
        txtExpDate.grid(row=6, column=1, padx=8, pady=3, sticky="w")
        
        
        lblDailyDose = ctk.CTkLabel(DataFrameLeft,text="Daily Dose",font=("Arial", 13, "bold"),text_color="#374151")
        lblDailyDose.grid(row=7, column=0, padx=(15, 8), pady=3, sticky="e")
        txtDailyDose = ctk.CTkEntry(DataFrameLeft,textvariable=self.DailyDose,width=230,height=32,corner_radius=7,placeholder_text="Daily dose")
        txtDailyDose.grid(row=7, column=1, padx=8, pady=3, sticky="w")
        
        
        lblDateOfBirth = ctk.CTkLabel(DataFrameLeft,text="Date of Birth",font=("Arial", 13, "bold"),text_color="#374151")
        lblDateOfBirth.grid(row=8, column=0, padx=(15, 8), pady=3, sticky="e")
        txtDateOfBirth = ctk.CTkEntry(DataFrameLeft,textvariable=self.DateOfBirth,width=230,height=32,corner_radius=7,placeholder_text="YYYY-MM-DD")
        txtDateOfBirth.grid(row=8, column=1, padx=8, pady=3, sticky="w")



        # ---------- Second Column ----------
        # 
        lblPossibleSideEffects = ctk.CTkLabel(DataFrameLeft,text="Possible Side Effects",font=("Arial", 13, "bold"),text_color="#374151")
        lblPossibleSideEffects.grid(row=0,column=2,padx=(25, 8),pady=(50, 5),sticky="e")
        txtPossibleSideEffects = ctk.CTkEntry(DataFrameLeft,textvariable=self.PossibleSideEffects,width=230,height=32,corner_radius=7,placeholder_text="Possible side effects")
        txtPossibleSideEffects.grid(row=0,column=3,padx=8,pady=(50, 5),sticky="w")
        
        
        lblFurtherInformation = ctk.CTkLabel(DataFrameLeft,text="Further Information",font=("Arial", 13, "bold"),text_color="#374151")
        lblFurtherInformation.grid(row=1,column=2,padx=(25, 8),pady=3,sticky="e")
        txtFurtherInformation = ctk.CTkEntry(DataFrameLeft,textvariable=self.FurtherInformation,width=230,height=32,corner_radius=7,placeholder_text="Additional information")
        txtFurtherInformation.grid(row=1,column=3,padx=8,pady=3,sticky="w")


        lblStorageAdvice = ctk.CTkLabel(DataFrameLeft,text="Storage Advice",font=("Arial", 13, "bold"),text_color="#374151")
        lblStorageAdvice.grid(row=2,column=2,padx=(25, 8),pady=3,sticky="e")
        txtStorageAdvice = ctk.CTkEntry(DataFrameLeft,textvariable=self.StorageAdvice,width=230,height=32,corner_radius=7,placeholder_text="Storage advice")
        txtStorageAdvice.grid(row=2,column=3,padx=8,pady=3,sticky="w")


        lblBloodPressure = ctk.CTkLabel(DataFrameLeft,text="Blood Pressure",font=("Arial", 13, "bold"),text_color="#374151")
        lblBloodPressure.grid(row=3,column=2,padx=(25, 8),pady=3,sticky="e")
        txtBloodPressure = ctk.CTkEntry(DataFrameLeft,textvariable=self.BloodPressure,width=230,height=32,corner_radius=7,placeholder_text="Blood pressure")
        txtBloodPressure.grid(row=3,column=3,padx=8,pady=3,sticky="w")


        lblMedication = ctk.CTkLabel(DataFrameLeft,text="Medication",font=("Arial", 13, "bold"),text_color="#374151")
        lblMedication.grid(row=4,column=2,padx=(25, 8),pady=3,sticky="e")
        txtMedication = ctk.CTkEntry(DataFrameLeft,textvariable=self.Medication,width=230,height=32,corner_radius=7,placeholder_text="Medication")
        txtMedication.grid(row=4,column=3,padx=8,pady=3,sticky="w")
        
        
        lblPatientId = ctk.CTkLabel(DataFrameLeft,text="Patient ID",font=("Arial", 13, "bold"),text_color="#374151")
        lblPatientId.grid(row=5,column=2,padx=(25, 8),pady=3,sticky="e")
        txtPatientId = ctk.CTkEntry(DataFrameLeft,textvariable=self.PatientId,width=230,height=32,corner_radius=7,placeholder_text="Patient ID")
        txtPatientId.grid(row=5,column=3,padx=8,pady=3,sticky="w")


        lblNhsNumber = ctk.CTkLabel(DataFrameLeft,text="NHS Number",font=("Arial", 13, "bold"),text_color="#374151")
        lblNhsNumber.grid(row=6,column=2,padx=(25, 8),pady=3,sticky="e")
        txtNhsNumber = ctk.CTkEntry(DataFrameLeft,textvariable=self.NhsNumber,width=230,height=32,corner_radius=7,placeholder_text="NHS number")
        txtNhsNumber.grid(row=6,column=3,padx=8,pady=3,sticky="w")


        lblPatientName = ctk.CTkLabel(DataFrameLeft,text="Patient Name",font=("Arial", 13, "bold"),text_color="#374151")
        lblPatientName.grid(row=7,column=2,padx=(25, 8),pady=3,sticky="e")
        txtPatientName = ctk.CTkEntry(DataFrameLeft,textvariable=self.PatientName,width=230,height=32,corner_radius=7,placeholder_text="Patient name")
        txtPatientName.grid(row=7,column=3,padx=8,pady=3,sticky="w")


        lblAddress = ctk.CTkLabel(DataFrameLeft,text="Address",font=("Arial", 13, "bold"),text_color="#374151")
        lblAddress.grid(row=8,column=2,padx=(25, 8),pady=3,sticky="e")
        txtAddress = ctk.CTkEntry(DataFrameLeft,textvariable=self.Address,width=230,height=32,corner_radius=7,placeholder_text="Patient address")
        txtAddress.grid(row=8,column=3,padx=8,pady=3,sticky="w")
        
        # *************************Data_Frame_Right******************************

        self.textPresciption=ctk.CTkTextbox(DataFrameRight,width=570,height=260,corner_radius=10,font=("Arial",13))
        self.textPresciption.place(x=25,y=50)

        #************************Button_Frame*******************************

        # ************************* BUTTONS *******************************

        btnPrescription = ctk.CTkButton(ButtonFrame,text="💊  Prescription",width=220,height=45,corner_radius=8,font=("Arial", 13, "bold"),command=self.iprescription)
        btnPrescription.grid(row=0,column=0,padx=5,pady=10)


        btnPrescriptionData = ctk.CTkButton(ButtonFrame,text="💾  Save",width=220,height=45,corner_radius=8,font=("Arial", 13, "bold"),command=self.iPrescriptionData)
        btnPrescriptionData.grid(row=0,column=1,padx=5,pady=10)


        btnUpdate = ctk.CTkButton(ButtonFrame,text="✏  Update",width=220,height=45,corner_radius=8,font=("Arial", 13, "bold"),command=self.update_data)
        btnUpdate.grid(row=0,column=2,padx=5,pady=10)


        btnDelete = ctk.CTkButton(ButtonFrame,text="🗑  Delete",width=220,height=45,corner_radius=8,font=("Arial", 13, "bold"),command=self.idelete)
        btnDelete.grid(row=0,column=3,padx=5,pady=10)


        btnClear = ctk.CTkButton(ButtonFrame,text="🧹  Clear",width=220,height=45,corner_radius=8,font=("Arial", 13, "bold"),command=self.clear_data)
        btnClear.grid(row=0,column=4,padx=5,pady=10)


        btnExit = ctk.CTkButton(ButtonFrame,text="🚪  Exit",width=220,height=45,corner_radius=8,font=("Arial", 13, "bold"),command=self.exit_app)
        btnExit.grid(row=0,column=5,padx=5,pady=10)

        #*************************Details_Frame*******************************
        #************************Scrollbar*******************************

        scroll_x=ttk.Scrollbar(DetailsFrame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(DetailsFrame,orient=VERTICAL)

        style = ttk.Style()

        style.theme_use("clam")

        style.configure("Treeview",background="white",foreground="#1F2937",rowheight=32,font=("Arial", 10),fieldbackground="white")

        style.configure("Treeview.Heading",background="#0B7A3B",foreground="white",font=("Arial", 10, "bold"),padding=8)

        style.map("Treeview",background=[("selected", "#3B82F6")],foreground=[("selected", "white")])

        self.hospital_table=ttk.Treeview(DetailsFrame,column=("patientID","name of tablets","reference no.","dose","no of tablets","lot","issue date","exp date","daily dose","storage advice","nhs number","patient name","date of birth","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.config(command=self.hospital_table.xview)
        scroll_y.config(command=self.hospital_table.yview)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)


        self.hospital_table.heading("patientID",text="Patient ID")
        self.hospital_table.heading("name of tablets",text="Name of Tablets")
        self.hospital_table.heading("reference no.",text="Reference No.")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("no of tablets",text="No of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issue date",text="Issue Date")
        self.hospital_table.heading("exp date",text="Exp Date")
        self.hospital_table.heading("daily dose",text="Daily Dose")
        self.hospital_table.heading("storage advice",text="Storage Advice")
        self.hospital_table.heading("nhs number",text="NHS Number")
        self.hospital_table.heading("patient name",text="Patient Name")
        self.hospital_table.heading("date of birth",text="Date of Birth")
        self.hospital_table.heading("address",text="Address")

        self.hospital_table["show"]="headings"

        
        self.hospital_table.column("patientID", width=110, anchor="center")
        self.hospital_table.column("name of tablets", width=140, anchor="center")
        self.hospital_table.column("reference no.", width=120, anchor="center")
        self.hospital_table.column("dose", width=80, anchor="center")
        self.hospital_table.column("no of tablets", width=110, anchor="center")
        self.hospital_table.column("lot", width=80, anchor="center")
        self.hospital_table.column("issue date", width=110, anchor="center")
        self.hospital_table.column("exp date", width=110, anchor="center")
        self.hospital_table.column("daily dose", width=100, anchor="center")
        self.hospital_table.column("storage advice", width=150, anchor="center")
        self.hospital_table.column("nhs number", width=120, anchor="center")
        self.hospital_table.column("patient name", width=130, anchor="center")
        self.hospital_table.column("date of birth", width=110, anchor="center")
        self.hospital_table.column("address", width=180, anchor="center")
        
        self.hospital_table.pack(fill=BOTH,expand=1)
        self.fetch_data()      #fetch data from database and show in table
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)  #bind the function to the table





        #*************************Functionality Declaration*******************************
    def iPrescriptionData(self):
        if self.Nameoftablets.get()=="" or self.Reference.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            conn = connect_db()
            if conn:
                try:
                    cursor = conn.cursor()
                    cursor.execute("INSERT INTO prescriptions VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                            self.PatientId.get(),
                            self.Nameoftablets.get(),
                            self.Reference.get(),
                            self.Dose.get(),
                            self.NoOfTablets.get(),
                            self.Lot.get(),
                            self.IssueDate.get(),
                            self.ExpDate.get(),
                            self.DailyDose.get(),
                            self.StorageAdvice.get(),
                            self.NhsNumber.get(),
                            self.PatientName.get(),
                            self.DateOfBirth.get(),
                            self.Address.get()
                    ))

                    conn.commit()
                    self.fetch_data()          # to show data 
                    cursor.close()
                    conn.close()
                        
                    messagebox.showinfo("Success","Prescription data saved successfully")
                except Exception as e:
                        messagebox.showerror("Database Error",str(e))


    def fetch_data(self):
        conn = connect_db()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM prescriptions")
                rows = cursor.fetchall()
                if len(rows) != 0:
                    self.hospital_table.delete(*self.hospital_table.get_children())
                    for row in rows:
                        self.hospital_table.insert('', END, values=row)
                cursor.close()
                conn.close()
            except Exception as e:
                messagebox.showerror("Database Error", str(e))


    def get_cursor(self,event):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.PatientId.set(row[0])
        self.Nameoftablets.set(row[1])
        self.Reference.set(row[2])
        self.Dose.set(row[3])
        self.NoOfTablets.set(row[4])
        self.Lot.set(row[5])
        self.IssueDate.set(row[6])
        self.ExpDate.set(row[7])
        self.DailyDose.set(row[8])
        self.StorageAdvice.set(row[9])
        self.NhsNumber.set(row[10])
        self.PatientName.set(row[11])
        self.DateOfBirth.set(row[12])
        self.Address.set(row[13])


    def update_data(self):
        conn = connect_db()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("UPDATE prescriptions SET patient_id=%s, name_of_tablets=%s, dose=%s, no_of_tablets=%s, lot=%s, issue_date=%s, exp_date=%s, daily_dose=%s, storage_advice=%s, nhs_number=%s, patient_name=%s, date_of_birth=%s, address=%s WHERE reference=%s", (
                    self.PatientId.get(),   
                    self.Nameoftablets.get(),
                    self.Dose.get(),
                    self.NoOfTablets.get(),
                    self.Lot.get(),
                    self.IssueDate.get(),
                    self.ExpDate.get(),
                    self.DailyDose.get(),
                    self.StorageAdvice.get(),
                    self.NhsNumber.get(),
                    self.PatientName.get(),
                    self.DateOfBirth.get(),
                    self.Address.get(),
                    self.Reference.get()
                ))
                conn.commit()
                self.fetch_data()  # Refresh the table
                cursor.close()
                conn.close()
                messagebox.showinfo("Success", "Prescription data updated successfully")
            except Exception as e:
                messagebox.showerror("Database Error", str(e))


    def iprescription(self):
        self.textPresciption.insert(END,"Patient Name:\t\t\t"+self.PatientName.get()+"\n")
        self.textPresciption.insert(END,"Name of Tablets:\t\t\t"+self.Nameoftablets.get()+"\n")
        self.textPresciption.insert(END,"Reference No.:\t\t\t"+self.Reference.get()+"\n")
        self.textPresciption.insert(END,"Dose:\t\t\t"+self.Dose.get()+"\n")
        self.textPresciption.insert(END,"No of Tablets:\t\t\t"+self.NoOfTablets.get()+"\n")
        self.textPresciption.insert(END,"Lot:\t\t\t"+self.Lot.get()+"\n")
        self.textPresciption.insert(END,"Issue Date:\t\t\t"+self.IssueDate.get()+"\n")
        self.textPresciption.insert(END,"Exp Date:\t\t\t"+self.ExpDate.get()+"\n")
        self.textPresciption.insert(END,"Daily Dose:\t\t\t"+self.DailyDose.get()+"\n")
        self.textPresciption.insert(END,"Storage Advice:\t\t\t"+self.StorageAdvice.get()+"\n")
        self.textPresciption.insert(END,"NHS Number:\t\t\t"+self.NhsNumber.get()+"\n")
        self.textPresciption.insert(END,"Date of Birth:\t\t\t"+self.DateOfBirth.get()+"\n")
        self.textPresciption.insert(END,"Address:\t\t\t"+self.Address.get()+"\n")
        self.textPresciption.insert(END,"Possible Side Effects:\t\t\t"+self.PossibleSideEffects.get()+"\n")
        self.textPresciption.insert(END,"Blood Pressure:\t\t\t"+self.BloodPressure.get()+"\n")
        self.textPresciption.insert(END,"Medication:\t\t\t"+self.Medication.get()+"\n")


    def idelete(self):
        conn = connect_db()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM prescriptions WHERE reference=%s", (self.Reference.get(),))
                conn.commit()
                self.fetch_data()  # Refresh the table
                cursor.close()
                conn.close()
                messagebox.showinfo("Success", "Prescription data deleted successfully")
            except Exception as e:
                messagebox.showerror("Database Error", str(e))


    def clear_data(self):
        self.PatientId.set("")
        self.Nameoftablets.set("")
        self.Reference.set("")
        self.Dose.set("")
        self.NoOfTablets.set("")
        self.Lot.set("")
        self.IssueDate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.StorageAdvice.set("")
        self.NhsNumber.set("")
        self.PatientName.set("")
        self.DateOfBirth.set("")
        self.Address.set("")
        self.PossibleSideEffects.set("")
        self.FurtherInformation.set("")
        self.BloodPressure.set("")
        self.Medication.set("")
        self.textPresciption.delete("1.0", END)  # Clear the prescription text area


    def exit_app(self):
        exit=messagebox.askyesno("Hospital Management System","Do you want to exit?")
        if exit>0:
            self.root.destroy()
            return
        

root=ctk.CTk()
ob=Hospital(root)
root.mainloop()