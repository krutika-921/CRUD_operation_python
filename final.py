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
		con=connect("kk.db")
		cursor=con.cursor()
		sql="select*from student"
		cursor.execute(sql)
		data=cursor.fetchall()
		for d in data:
			info= info + "id:" + str(d[0]) + "name" + str(d[1]) + "salary" + str(d[2]) + "\n"
		vw_st_data.insert(INSERT, info)
	except Exception as e:
		showerror("failure", e)
	finally:
		if con is not None:
			con.close()

def f4():
	main_window.deiconify()
	view_window.withdraw()
def f5():
	con=None
	try:
		con=connect("KK.db")
		cursor=con.cursor()
		sql="insert into student values('%d','%s','%f')"
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


main_window = Tk()
main_window.title("E.M.S")
main_window.geometry("500x500")

f = ("Aria", 20, "bold")
mw_btn_add = Button(main_window, text="Add", font= f, width= 10, bd= 4, command= f1)
mw_btn_add.pack(pady=5)

mw_btn_view = Button(main_window, text="View", font= f, width= 10, bd= 4, command= f3)
mw_btn_view.pack(pady=5)

mw_btn_update = Button(main_window, text="Update", font= f, width= 10, bd= 4)
mw_btn_update.pack(pady=5)

mw_btn_delete = Button(main_window, text="Delete", font= f, width= 10, bd= 4)
mw_btn_delete.pack(pady=5)

mw_btn_charts = Button(main_window, text="Charts", font= f, width= 10, bd= 4)
mw_btn_charts.pack(pady=5)

mw_lbl_qotd = Label(main_window, text="QOTD:", font= f)
mw_lbl_qotd.pack(pady=5)

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

uw_btn_save = Button(update_window, text="save", width=10, font=f)
uw_btn_save.pack(pady=5)
uw_btn_back = Button(update_window, text="back", width=10, font=f)
uw_btn_back.pack(pady=5)



#delete window
delete_window = Toplevel(main_window)
delete_window.geometry("500x500")
delete_window.title("delete window")



main_window.mainloop()

