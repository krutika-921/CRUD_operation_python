from tkinter import*
from tkinter.messagebox import*
from tkinter.scrolledtext import*
from sqlite3 import*

def f1():
	add_window.deiconify()
	main_window.withdraw()
def f2():
	main_window.deiconify()
	add_window.withdraw()
def f3():
	view_window.deiconify()
	main_window.withdraw()

	vw_st_data.delete(1.0,END)
	info=""
	con=None
	try:
		con=connect("emp.db")
		cursor=con.cursor()
		sql="select*from employee"
		cursor.execute(sql)
		data=cursor.fetchall()
		for d in data:
			info= info + "id:"+ str(d[0]) +    "/name:"   + str(d[1]) + "	/salary:	"   + str(d[2]) + "\n"
		vw_st_data.insert(INSERT, info)
	except Exception as e:
		showerror("failure", e)
		con.rollback()
	finally:
		if con is not None:
			con.close()

def f4():
	main_window.deiconify()
	view_window.withdraw()
def f5():
	con=None
	try:
		con=connect("emp.db")
		cursor=con.cursor()
		sql="insert into employee values('%d','%s','%f')"
		id=int(aw_ent_id.get())
		name=aw_ent_name.get()
		salary=float(aw_ent_salary.get())

		cursor.execute(sql%(id,name,salary))
		con.commit()
		
		showinfo("success", "record added")
		aw_ent_id.delete(0,END)
		aw_ent_name.delete(0,END)
		aw_ent_salary.delete(0,END)
	except Exception as e:
		showerror("failure", e)
		con.rollback()
	finally:
		if con is not None:
			con.close()

def f6():
	update_window.deiconify()
	main_window.withdraw()
def f7():
	main_window.deiconify()
	update_window.withdraw()
def f8():
	con=None
	try:
		con=connect("emp.db")
		cursor=con.cursor()
		sql="update employee set name='%s', salary= '%f' where id= '%d'"
		id= int(uw_ent_id.get())
		name= uw_ent_name.get()
		salary= float(uw_ent_salary.get())

		cursor.execute(sql%(name,salary,id))
		if cursor.rowcount == 1:
			con.commit()
			print("record updated")
		else:
			print("record does not exist")
		showinfo("success", "record updated")
		uw_ent_id.delete(0,END)
		uw_ent_name.delete(0,END)
		uw_ent_salary.delete(0,END)
	except Exception as e:
		showerror("failure", e)
		con.rollback()
	finally:
		if con is not None:
			con.close()
def f9():
	delete_window.deiconify()
	main_window.withdraw()
def f10():
	main_window.deiconify()
	delete_window.withdraw()
def f11():
	con=None
	try:
		con=connect("emp.db")
		cursor=con.cursor()
		sql="delete from employee where id= '%d'"
		id= int(dw_ent_id.get())

		cursor.execute(sql%(id))
		if cursor.rowcount == 1:
			con.commit()
			print("record deleted")
		else:
			print("record does not exist")
		showinfo("success", "record deleted")
		dw_ent_id.delete(0,END)
	
	except Exception as e:
		showerror("failure", e)
		con.rollback()
	finally:
		if con is not None:
			con.close()	
	

main_window = Tk()
main_window.title("E.M.S")
main_window.geometry("500x500")

f = ("Aria", 20, "bold")
mw_lbl_emp = Label(main_window, text="EMPLOYEE  DETAILS:", width= 25, font= f)
mw_lbl_emp.pack(pady=5)

mw_btn_add = Button(main_window, text="Add", font= f, width= 10, bd= 4, command= f1)
mw_btn_add.pack(pady=5)

mw_btn_view = Button(main_window, text="View", font= f, width= 10, bd= 4, command= f3)
mw_btn_view.pack(pady=5)

mw_btn_update = Button(main_window, text="Update", font= f, width= 10, bd= 4, command =f6)
mw_btn_update.pack(pady=5)

mw_btn_delete = Button(main_window, text="Delete", font= f, width= 10, bd= 4, command=f9)
mw_btn_delete.pack(pady=5)



   # ADD WINDOW
add_window = Toplevel(main_window)
add_window.geometry("500x500")
add_window.title("Add Emp")

aw_lbl_id = Label(add_window, text="enter id", font=f)
aw_lbl_id.pack(pady=5)
aw_ent_id = Entry(add_window, font=f, bd=4)
aw_ent_id.pack(pady=5)

aw_lbl_name = Label(add_window, text="enter name", font=f)
aw_lbl_name.pack(pady=5)
aw_ent_name = Entry(add_window, font=f, bd=4)
aw_ent_name.pack(pady=5)

aw_lbl_salary = Label(add_window, text="enter salary", font=f)
aw_lbl_salary.pack(pady=5)
aw_ent_salary = Entry(add_window, font=f, bd=4)
aw_ent_salary.pack(pady=5)

aw_btn_save = Button(add_window, text="save", width=10, font=f, command=f5)
aw_btn_save.pack(pady=5)
aw_btn_back = Button(add_window, text="back", width=10, font=f, command=f2)
aw_btn_back.pack(pady=5)
add_window.withdraw()

#VIEW window
view_window = Toplevel(main_window)
view_window.geometry("500x500")
view_window.title("View window")

vw_st_data = ScrolledText(view_window, width=30, height=10, font=f)
vw_st_data.pack(pady=5)
vw_btn_back = Button(view_window, text="back", width=10, font=f, command=f4)
vw_btn_back.pack(pady=5)

view_window.withdraw()


#update window
update_window = Toplevel(main_window)
update_window.geometry("500x500")
update_window.title("update window")

uw_lbl_id = Label(update_window, text="enter id", font=f)
uw_lbl_id.pack(pady=5)
uw_ent_id = Entry(update_window, font=f, bd=4)
uw_ent_id.pack(pady=5)

uw_lbl_name = Label(update_window, text="enter name", font=f)
uw_lbl_name.pack(pady=5)
uw_ent_name = Entry(update_window, font=f, bd=4)
uw_ent_name.pack(pady=5)

uw_lbl_salary = Label(update_window, text="enter salary", font=f)
uw_lbl_salary.pack(pady=5)
uw_ent_salary = Entry(update_window, font=f, bd=4)
uw_ent_salary.pack(pady=5)

uw_btn_save = Button(update_window, text="save", width=10, font=f, command =f8)
uw_btn_save.pack(pady=5)
uw_btn_back = Button(update_window, text="back", width=10, font=f, command =f7)
uw_btn_back.pack(pady=5)

update_window.withdraw()

#delete window
delete_window = Toplevel(main_window)
delete_window.geometry("500x500")
delete_window.title("delete window")

dw_lbl_id = Label(delete_window, text="enter id", font=f)
dw_lbl_id.pack(pady=5)
dw_ent_id = Entry(delete_window, font=f, bd=4)
dw_ent_id.pack(pady=5)
dw_btn_save = Button(delete_window, text="save", width=10, font=f, command =f11)
dw_btn_save.pack(pady=5)
dw_btn_back = Button(delete_window, text="back", width=10, font=f, command =f10)
dw_btn_back.pack(pady=5)




delete_window.withdraw()


main_window.mainloop()

