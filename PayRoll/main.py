from tkinter import *
from tkinter import messagebox
import pymysql


class EmployeePayrollSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Payroll Management System")
        self.root.geometry("1600x900+0+0")
        self.root.config(bg="white")
        title = Label(self.root, text="Employee Payroll Management- System", font=(
            "times new roman", 30, "bold"), bg="#262626", fg="white", anchor="w", padx=10).place(x=0, y=0, relwidth=1)

     # --------------------------------Frame1--------------------------------

        # Frame 1 Variables----------------------------------------------------------

        self.var_emp_code = StringVar()
        self.var_designation = StringVar()
        self.var_name = StringVar()
        self.var_age = StringVar()
        self.var_gender = StringVar()
        self.var_email = StringVar()
        self.var_doj = StringVar()
        self.var_dob = StringVar()
        self.var_proof_id = StringVar()
        self.var_experience = StringVar()
        self.var_contact = StringVar()

        Frame1 = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        Frame1.place(x=10, y=70, width=900, height=680)

        title1 = Label(Frame1, text="Employee Details", font=(
            "times new roman", 20), bg="lightgray", padx=10).place(x=0, y=0, relwidth=1)

        lbl_code = Label(Frame1, text="Employee Code", font=(
            "times new roman", 20), bg="white").place(x=10, y=70)
        entry_code = Entry(Frame1, textvariable=self.var_emp_code, font=(
            "times new roman", 18), bg="#C2DFFF").place(x=200, y=75, width=300)
        btn_search = Button(Frame1, text="Search", font=(
            "times new roman", 18), bg="lightgray").place(x=550, y=65, width=120)

        # Row1----------------------------------------------------------------------

        lbl_designation = Label(Frame1, text="Designation", font=(
            "times new roman", 20), bg="white").place(x=10, y=140)
        entry_designation = Entry(Frame1, textvariable=self.var_designation, font=(
            "times new roman", 18), bg="#C2DFFF").place(x=180, y=145)
        lbl_doj = Label(Frame1, text="D.O.J", font=(
            "times new roman", 20), bg="white").place(x=450, y=140)
        entry_doj = Entry(Frame1, textvariable=self.var_doj, font=(
            "times new roman", 18), bg="#C2DFFF").place(x=600, y=145)

        # Row2----------------------------------------------------------------------

        lbl_name = Label(Frame1, text="Name", font=(
            "times new roman", 20), bg="white").place(x=10, y=210)
        entry_name = Entry(Frame1, textvariable=self.var_name, font=(
            "times new roman", 18), bg="#C2DFFF").place(x=180, y=215)
        lbl_dob = Label(Frame1, text="D.O.B", font=(
            "times new roman", 20), bg="white").place(x=450, y=210)
        entry_dob = Entry(Frame1, textvariable=self.var_dob, font=(
            "times new roman", 18), bg="#C2DFFF").place(x=600, y=215)

        # Row3----------------------------------------------------------------------

        lbl_age = Label(Frame1, text="Age", font=(
            "times new roman", 20), bg="white").place(x=10, y=280)
        entry_age = Entry(Frame1, textvariable=self.var_age, font=(
            "times new roman", 18), bg="#C2DFFF").place(x=180, y=285)
        lbl_experience = Label(Frame1, text="Experience", font=(
            "times new roman", 20), bg="white").place(x=450, y=280)
        entry_experience = Entry(Frame1, textvariable=self.var_experience, font=(
            "times new roman", 18), bg="#C2DFFF").place(x=600, y=285)

        # Row4----------------------------------------------------------------------

        lbl_gender = Label(Frame1, text="Gender", font=(
            "times new roman", 20), bg="white").place(x=10, y=350)
        entry_gender = Entry(Frame1, textvariable=self.var_gender, font=(
            "times new roman", 18), bg="#C2DFFF").place(x=180, y=355)
        lbl_proof_id = Label(Frame1, text="Proof ID", font=(
            "times new roman", 20), bg="white").place(x=450, y=350)
        entry_proof_id = Entry(Frame1, textvariable=self.var_proof_id, font=(
            "times new roman", 18), bg="#C2DFFF").place(x=600, y=350)

        # Row5----------------------------------------------------------------------

        lbl_email = Label(Frame1, text="Email", font=(
            "times new roman", 20), bg="white").place(x=10, y=420)
        entry_email = Entry(Frame1, textvariable=self.var_email, font=(
            "times new roman", 18), bg="#C2DFFF").place(x=180, y=425)
        lbl_contact = Label(Frame1, text="Contact", font=(
            "times new roman", 20), bg="white").place(x=450, y=420)
        entry_contact = Entry(Frame1, textvariable=self.var_contact, font=(
            "times new roman", 18), bg="#C2DFFF").place(x=600, y=425)

        # Row6----------------------------------------------------------------------

        lbl_address = Label(Frame1, text="Address", font=(
            "times new roman", 20), bg="white").place(x=10, y=490)
        self.entry_address = Text(Frame1, font=(
            "times new roman", 18), bg="#C2DFFF")
        self.entry_address.place(x=180, y=495, width=665, height=150)

     # --------------------------------Frame2--------------------------------

        # Frame 2 Variables----------------------------------------------------------

        self.var_month = StringVar()
        self.var_year = StringVar()
        self.var_basic_salary = StringVar()
        self.var_total_days = StringVar()
        self.var_absents = StringVar()
        self.var_medical = StringVar()
        self.var_PF = StringVar()
        self.var_convence = StringVar()
        self.var_net_sal = StringVar()

        Frame2 = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        Frame2.place(x=920, y=70, width=660, height=350)

        title2 = Label(Frame2, text="Employee Salary Details", font=(
            "times new roman", 20), bg="lightgray", padx=10).place(x=0, y=0, relwidth=1)

        # Row1----------------------------------------------------------------------

        lbl_month = Label(Frame2, text="Month", font=(
            "times new roman", 20), bg="white").place(x=10, y=70)
        entry_month = Entry(Frame2, textvariable=self.var_month, font=(
            "times new roman", 18), bg="#C2DFFF").place(x=100, y=75, width=100)
        lbl_year = Label(Frame2, text="Year", font=(
            "times new roman", 20), bg="white").place(x=240, y=70)
        entry_year = Entry(Frame2, textvariable=self.var_year, font=(
            "times new roman", 18), bg="#C2DFFF").place(x=310, y=75, width=100)
        lbl_salary = Label(Frame2, text="Salary", font=(
            "times new roman", 20), bg="white").place(x=440, y=70)
        entry_salary = Entry(Frame2, textvariable=self.var_basic_salary, font=(
            "times new roman", 18), bg="#C2DFFF").place(x=530, y=75, width=100)

        # Row2----------------------------------------------------------------------

        lbl_total_days = Label(Frame2, text="Total Days", font=(
            "times new roman", 20), bg="white").place(x=10, y=120)
        entry_total_days = Entry(Frame2, textvariable=self.var_total_days, font=(
            "times new roman", 18), bg="#C2DFFF").place(x=150, y=125, width=100)
        lbl_absents = Label(Frame2, text="Absents", font=(
            "times new roman", 20), bg="white").place(x=300, y=120)
        entry_absents = Entry(Frame2, textvariable=self.var_absents, font=(
            "times new roman", 18), bg="#C2DFFF").place(x=410, y=125, width=100)

        # Row3----------------------------------------------------------------------

        lbl_medical = Label(Frame2, text="Medical", font=(
            "times new roman", 20), bg="white").place(x=10, y=190)
        entry_medical = Entry(Frame2, textvariable=self.var_medical, font=(
            "times new roman", 18), bg="#C2DFFF").place(x=120, y=195, width=150)
        lbl_provident_funds = Label(Frame2, text="Provident Funds", font=(
            "times new roman", 20), bg="white").place(x=290, y=190)
        entry_provident_funds = Entry(Frame2, textvariable=self.var_PF, font=(
            "times new roman", 18), bg="#C2DFFF").place(x=490, y=195, width=150)

        # Row4----------------------------------------------------------------------

        lbl_convence = Label(Frame2, text="Convence", font=(
            "times new roman", 20), bg="white").place(x=10, y=240)
        entry_convence = Entry(Frame2, textvariable=self.var_convence, font=(
            "times new roman", 18), bg="#C2DFFF").place(x=140, y=245, width=150)
        lbl_net_salary = Label(Frame2, text="Net Salary", font=(
            "times new roman", 20), bg="white").place(x=310, y=240)
        entry_net_salary = Entry(Frame2, textvariable=self.var_net_sal, font=(
            "times new roman", 18), bg="#C2DFFF").place(x=450, y=245, width=150)

        btn_calculate = Button(Frame2, text="Calculate", font=(
            "times new roman", 18), bg="#C2DFFF").place(x=40, y=290)

        btn_save = Button(Frame2, command=self.database_entry, text="Save", font=(
            "times new roman", 18), bg="#52D017").place(x=450, y=290)

        btn_clear = Button(Frame2, text="Clear", font=(
            "times new roman", 18), bg="#E41B17").place(x=550, y=290)

     # --------------------------------Frame3--------------------------------

        Frame3 = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        Frame3.place(x=920, y=440, width=660, height=310)

        # Calculator Frame-------------------------------------------------------------

        self.number_txt = StringVar()
        self.number_operator = ''

        def btn_click(num):
            self.number_operator = self.number_operator + str(num)
            self.number_txt.set(self.number_operator)

        def result():
            res = str(eval(self.number_operator))
            self.number_txt.set(res)
            self.number_operator = ''

        def clr_Calculator():
            self.number_txt.set('')
            self.number_operator = ''

        Calculator_Frame = Frame(Frame3, bg="white", bd=2, relief=RIDGE)
        Calculator_Frame.place(x=2, y=2, width=247, height=300)

        entry_cal_input = Entry(
            Calculator_Frame, bg="#C2DFFF", textvariable=self.number_txt, font=("times new roman", 25, "bold"), justify=RIGHT).place(x=0, y=0, relwidth=1, height=50)

        # Row2----------------------------------------------------------------------

        cal_btn_7 = Button(Calculator_Frame, text="7", font=(
            "times new roman", 15, "bold"), command=lambda: btn_click(7)).place(x=0, y=50, width=60, height=60)
        cal_btn_8 = Button(Calculator_Frame, text="8", font=(
            "times new roman", 15, "bold"), command=lambda: btn_click(8)).place(x=61, y=50, width=60, height=60)
        cal_btn_9 = Button(Calculator_Frame, text="9", font=(
            "times new roman", 15, "bold"), command=lambda: btn_click(9)).place(x=122, y=50, width=60, height=60)
        cal_btn_div = Button(Calculator_Frame, text="/", font=(
            "times new roman", 15, "bold"), command=lambda: btn_click("/")).place(x=183, y=50, width=60, height=60)

        # Row3----------------------------------------------------------------------

        cal_btn_6 = Button(Calculator_Frame, text="6", font=(
            "times new roman", 15, "bold"), command=lambda: btn_click(6)).place(x=0, y=112, width=60, height=60)
        cal_btn_5 = Button(Calculator_Frame, text="5", font=(
            "times new roman", 15, "bold"), command=lambda: btn_click(5)).place(x=61, y=112, width=60, height=60)
        cal_btn_4 = Button(Calculator_Frame, text="4", font=(
            "times new roman", 15, "bold"), command=lambda: btn_click(4)).place(x=122, y=112, width=60, height=60)
        cal_btn_mul = Button(Calculator_Frame, text="*", font=(
            "times new roman", 15, "bold"), command=lambda: btn_click("*")).place(x=183, y=112, width=60, height=60)

        # Row4----------------------------------------------------------------------

        cal_btn_3 = Button(Calculator_Frame, text="3", font=(
            "times new roman", 15, "bold"), command=lambda: btn_click(3)).place(x=0, y=174, width=60, height=60)
        cal_btn_2 = Button(Calculator_Frame, text="2", font=(
            "times new roman", 15, "bold"), command=lambda: btn_click(2)).place(x=61, y=174, width=60, height=60)
        cal_btn_1 = Button(Calculator_Frame, text="2", font=(
            "times new roman", 15, "bold"), command=lambda: btn_click(1)).place(x=122, y=174, width=60, height=60)
        cal_btn_sub = Button(Calculator_Frame, text="-", font=(
            "times new roman", 15, "bold"), command=lambda: btn_click("-")).place(x=183, y=174, width=60, height=60)

        # Row1----------------------------------------------------------------------

        cal_btn_clr = Button(Calculator_Frame, text="C", font=(
            "times new roman", 15, "bold"), command=clr_Calculator).place(x=0, y=236, width=60, height=60)
        cal_btn_zero = Button(Calculator_Frame, text="0", font=(
            "times new roman", 15, "bold"), command=lambda: btn_click(0)).place(x=61, y=236, width=60, height=60)
        cal_btn_add = Button(Calculator_Frame, text="+", font=(
            "times new roman", 15, "bold"), command=lambda: btn_click("+")).place(x=122, y=236, width=60, height=60)
        cal_btn_equ = Button(Calculator_Frame, text="=", font=(
            "times new roman", 15, "bold"), command=result).place(x=183, y=236, width=60, height=60)

        # Salary Frame----------------------------------------------------------------------

        sal_Frame = Frame(Frame3, bg="white", bd=2, relief=RIDGE)
        sal_Frame.place(x=255, y=2, width=395, height=300)

        title3 = Label(sal_Frame, text="Salary Slip", font=(
            "times new roman", 18), bg="lightgray", padx=10).place(x=0, y=0, relwidth=1)

        sal_Frame1 = Frame(sal_Frame, bg="white", bd=2, relief=RIDGE)
        sal_Frame1.place(x=0, y=30, relwidth=1, height=230)

        sal_scollbar = Scrollbar(sal_Frame1, orient=VERTICAL)
        sal_scollbar.pack(fill=Y, side=RIGHT)

        self.salary_receipt_entry = Text(
            sal_Frame1, font=("times new roman", 15), bg="#C2DFFF", yscrollcommand=sal_scollbar.set)
        self.salary_receipt_entry.pack(fill=BOTH, expand=1)
        sal_scollbar.config(command=self.salary_receipt_entry.yview)

        btn_print = Button(sal_Frame, text="Print", font=(
            "times new roman", 18), bg="#52D017").place(x=280, y=262, height=30, width=100)

        self.database_connection()

    # All Functions------------------------------------------------------

    def database_entry(self):

        if self.var_emp_code.get() == "" or self.var_net_sal.get() == "" or self.var_proof_id.get() == "" or self.var_name.get() == "":
            messagebox.showerror("Error", "Employee details are required")
        else:

            try:
                con = pymysql.connect(host="localhost",
                                      user="root",
                                      password="",
                                      db="EmployeeSystem"
                                      )
                cur = con.cursor()

                cur.execute("select * from employee_salary where emp_id=%s",
                            (self.var_emp_code.get()))
                row = cur.fetchone()

                if row != None:
                    messagebox.showerror(
                        "Error", "Employee ID is already exist.")
                else:
                    cur.execute(
                        "insert into employee_salary values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (
                            self.var_emp_code.get(),
                            self.var_designation.get(),
                            self.var_name.get(),
                            self.var_age.get(),
                            self.var_gender.get(),
                            self.var_email.get(),
                            self.var_doj.get(),
                            self.var_dob.get(),
                            self.var_experience.get(),
                            self.var_proof_id.get(),
                            self.var_contact.get(),
                            self.entry_address.get('1.0', END),
                            self.var_month.get(),
                            self.var_year.get(),
                            self.var_basic_salary.get(),
                            self.var_total_days.get(),
                            self.var_absents.get(),
                            self.var_medical.get(),
                            self.var_PF.get(),
                            self.var_convence.get(),
                            self.var_net_sal.get(),
                            "receipt"
                        ))
                    con.commit()
                    con.close()
                    messagebox.showinfo(
                        "Success", "Record added Successfully.")

            except Exception as ex:
                messagebox.showerror("Error", f'Error due to: {str(ex)}')

    def database_connection(self):
        try:
            con = pymysql.connect(host="localhost",
                                  user="root",
                                  password="",
                                  db="EmployeeSystem"
                                  )
            cur = con.cursor()

            cur.execute("select * from employee_salary")
            rows = cur.fetchall()
            print(rows)

        except Exception as ex:
            messagebox.showerror("Error", f'Error due to: {str(ex)}')


root = Tk()
obj = EmployeePayrollSystem(root)
root.mainloop()
