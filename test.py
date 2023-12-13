from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror
import sqlite3
import random


perekluchitel = False
db = sqlite3.connect('tablitca.db')
c = db.cursor()


def kz():
    root.title("Қауіпсіз пароль генераторы")
    tab_control.tab(0, text='      Пароль генераторы\t')
    tab_control.tab(1, text='        Пароль менеджері\t     ')
    tab_control.tab(2, text='            Параметрлер\t')
    btn['text'] = 'Құрастыру'
    parol.set('Шығару өрісі...')
    sandar['text'] = 'Сандарды қосу'
    arip['text'] = 'Үлкен әріптерді қосу'
    tablitca.heading("id", text="№", anchor=CENTER)
    tablitca.heading("name", text="Сайт/приложение аты", anchor=CENTER)
    tablitca.heading("login", text="Логин", anchor=CENTER)
    tablitca.heading("parol", text="Құпия сөз", anchor=CENTER)
    dobavit['text'] = 'Қосу'
    udalit['text'] = '  Жою   '
    sozdat['text'] = '  Қосу  '
    nazad['text'] = 'Артқа'
    label_name['text'] = 'Сайт/приложение аты'
    label_login['text'] = 'Логин'
    label_parol['text'] = 'Пароль'
    lg['text'] = 'Тілді таңдаңыз:'
    # lg_kz['text'] = ' Қазақша '
    # lg_ru['text'] = ' Орысша  '
    # lg_en['text'] = 'Ағылшынша'


def ru():
    root.title('Генератор безопасных паролей')
    tab_control.tab(0, text='\tГенератор\t')
    tab_control.tab(1, text='\tМенеджер паролей\t')
    tab_control.tab(2, text='\tНастройка\t')
    btn['text'] = '  Создать   '
    parol.set('Поле вывода...')
    sandar['text'] = 'Включить цифры'
    arip['text'] = 'Включить большие буквы'
    tablitca.heading("id", text="№", anchor=CENTER)
    tablitca.heading("name", text="Название сайта/приложение", anchor=CENTER)
    tablitca.heading("login", text="Логин", anchor=CENTER)
    tablitca.heading("parol", text="Пароль", anchor=CENTER)
    dobavit['text'] = 'Добавить'
    udalit['text'] = 'Удалить'
    sozdat['text'] = 'Создать'
    nazad['text'] = 'Назад'
    label_name['text'] = 'Название сайта/приложение'
    label_login['text'] = 'Логин'
    label_parol['text'] = 'Пароль'
    lg['text'] = 'Выберите язык:'
    # lg_kz['text'] = ' Казахский '
    # lg_ru['text'] = ' Русский  '
    # lg_en['text'] = 'Английский'


def en():
    root.title('Password Generator')
    tab_control.tab(0, text='\tGenerator\t')
    tab_control.tab(1, text='\tPassword Manager\t')
    tab_control.tab(2, text='\tSettings\t\t')
    btn['text'] = '  Generate  '
    parol.set('Output field...')
    sandar['text'] = 'Include numbers'
    arip['text'] = 'Include uppercase letters'
    tablitca.heading("id", text="№", anchor=CENTER)
    tablitca.heading("name", text="Website/Application Name", anchor=CENTER)
    tablitca.heading("login", text="Login", anchor=CENTER)
    tablitca.heading("parol", text="Password", anchor=CENTER)
    dobavit['text'] = 'Add'
    udalit['text'] = ' Delete '
    sozdat['text'] = ' Create '
    nazad['text'] = 'Back'
    label_name['text'] = 'Website/Application Name'
    label_login['text'] = 'Login'
    label_parol['text'] = 'Password'
    lg['text'] = 'Select language:'
    # lg_kz['text'] = ' Kazakh '
    # lg_ru['text'] = ' Russian '
    # lg_en['text'] = ' English '


def perekluchitel_function():
    global perekluchitel
    if perekluchitel:
        manager_window2.pack_forget()
        manager_window1.pack()
        setting.pack()
        tab_control.add(generator)
        tab_control.add(manager_window1)
        tab_control.add(setting)
        tablitca.pack()
        udalit.pack(side='left', ipadx=95)
        sozdat.pack(side='right', ipadx=95)
        perekluchitel = False
    else:
        manager_window1.pack_forget()
        tablitca.pack_forget()
        sozdat.pack_forget()
        udalit.pack_forget()
        manager_window2.pack(expand=1, fill='both')
        nazad.place(relx=0.001, rely=0.91, width=240)
        perekluchitel = True
    lg_when_open()


def dobavit_function():
    database = sqlite3.connect('tablitca.db')
    cursor = database.cursor()
    global perekluchitel
    tablitca.delete(*tablitca.get_children())
    name = enter_name.get()
    login = enter_login.get()
    paroll = enter_parol.get()
    if len(name) > 0 and len(login) > 0 and len(paroll) > 0:
        cursor.execute("INSERT INTO dannie VALUES (?, ?, ?)", (name, login, paroll))
        database.commit()
    else:
        showerror(title='Пустая поле ввода', message='Вы не ввели данные на все ячейки.\n'
                                                     'Если нечего вводить поставьте просто "-".\n'
                                                     'Пожалуйста повторите попытку.\n')
    enter_name.delete(0, 'end')
    enter_login.delete(0, 'end')
    enter_parol.delete(0, 'end')
    manager_window1.pack()
    tablitca.pack()
    sozdat.pack(side='right', ipadx=95)
    perekluchitel_function()
    cursor.execute("SELECT rowid, * FROM dannie")
    for element in cursor.fetchall():
        tablitca.insert("", END, values=element)
    lg_when_open()
    database.commit()
    database.close()
    perekluchitel = False


def generate_password():
    # Парольды курастыру
    k = dlina_v.get()
    if sandar_v.get() == 0 and arip_v.get() == 0:
        spisok = [chr(i) for i in range(97, 123)]
        parol.set(''.join(random.sample(spisok, k)))
    elif sandar_v.get() == 1 and arip_v.get() == 0:
        spisok = [chr(i) for i in range(97, 123)] + [str(i) for i in range(10)]
        parol.set(''.join(random.sample(spisok, k)))
    elif sandar_v.get() == 0 and arip_v.get() == 1:
        spisok = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(65, 90)]
        parol.set(''.join(random.sample(spisok, k)))
    elif sandar_v.get() == 1 and arip_v.get() == 1:
        spisok = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(65, 90)] + [str(i) for i in range(10)]
        parol.set(''.join(random.sample(spisok, k)))


def butin(n):
    # Болшек санды бутин санга айналдыру
    dlina_korsetu["text"] = dlina.get()
    float_value = float(n)
    int_value = round(float_value)
    dlina_korsetu["text"] = int_value


def copy_f():
    # Ctrl + C
    root.clipboard_clear()
    root.clipboard_append(parol.get())


def delete_function():
    database = sqlite3.connect('tablitca.db')
    cursor = database.cursor()
    for selected_items in tablitca.selection():
        cursor.execute("DELETE FROM dannie WHERE rowid = ?", (tablitca.set(selected_items, "#1"),))
    tablitca.delete(*tablitca.get_children())
    cursor.execute("SELECT rowid, * FROM dannie")
    for dannie in cursor.fetchall():
        tablitca.insert("", END, values=dannie)
    database.commit()
    database.close()


def lg_f(number):
    dbd = sqlite3.connect('language.db')
    cu = dbd.cursor()
    cu.execute("""DELETE FROM lg""")
    dbd.commit()
    cu.execute("""INSERT INTO lg VALUES(?)""", (number,))
    dbd.commit()
    dbd.close()
    if number == 1:
        kz()
    elif number == 2:
        ru()
    elif number == 3:
        en()


def lg_when_open():
    global language_value
    dbd = sqlite3.connect('language.db')
    cu = dbd.cursor()
    cu.execute("""SELECT * FROM lg""")
    for i in cu.fetchall():
        language_value = i[0]
        print(language_value)
    dbd.close()
    if language_value == 1:
        kz()
    elif language_value == 2:
        ru()
    elif language_value == 3:
        en()


#------------------------------------------------Беттерді құру----------------------------------------------------------


root = Tk()
root.geometry('480x270')
root.resizable(False, False)

root.iconbitmap(default="images/icon.ico")


tab_control = ttk.Notebook(root)                # Беттерді өзгертуге арналған
generator = ttk.Frame(tab_control)              # Бірнші бет
manager_window1 = ttk.Frame(tab_control)        # Екінші бет
setting = ttk.Frame(tab_control)                # Үшінші бет


#-------------------------------------------------Негізгі GUI-----------------------------------------------------------

style = ttk.Style()
style.theme_use("default")
style.configure("Treeview", background='silver', foreground='black', fieldbackground='silver')


manager_window1.place(relx=0.005, rely=0.005, relwidth=1, relheight=1)
manager_window2 = ttk.Frame(manager_window1)
setting.place(relx=0.005, rely=0.005, relwidth=1, relheight=1)


tab_control.add(generator, text='\tГенератор\t')                # Бірінші беттің аты
tab_control.add(manager_window1, text='\tМенеджер паролей\t')   # Екінші беттің аты
tab_control.add(setting, text='\tНастройка\t')                  # Үшінші беттің аты
tab_control.pack(expand=1, fill='both')                         # Меню орналасуы


# Бірінші беттің фоны
root.image = PhotoImage(file='images/fon_generator.png')
bg_logo = Label(generator, image=root.image)
bg_logo.grid(row=0, column=0)
copy_img = PhotoImage(file='images/copy_icon.png')


# Екінші беттің фоны
fon_sozdat_file = PhotoImage(file='images/fon_setting_manager.png')
fon_sozdat = Label(manager_window2, image=fon_sozdat_file)
fon_sozdat.place(anchor=CENTER)


# Үшінші беттің фоны
fon_setting_file = PhotoImage(file='images/fon_setting_manager.png')
fon_setting = Label(setting, image=fon_setting_file)
fon_setting.place(anchor=CENTER)


# Тілді таңдау батырмасының суреті
kz_img = PhotoImage(file='images/kazakhstan_icon.png')
ru_img = PhotoImage(file='images/russia_icon.png')
en_img = PhotoImage(file='images/usa_icon.png')


#--------------------------------------------------Бірінші бет----------------------------------------------------------

# Құрастыру батырмасы
btn = ttk.Button(generator, command=generate_password, cursor='hand2')
btn.place(relx=0.685, rely=0.6)


# Құрастырылған парольды көрестетін жол
parol = StringVar()
title = ttk.Label(generator, textvariable=parol, font=('Arial', 12), foreground='#000000', background='#C0C0C0')
title.place(width=275, height=27, relx=0.2, rely=0.25)


# Интерфейстегі багті тузеу ушін
bag_fix = ttk.Label(generator, text='\t')
bag_fix.place(relx=0.2, rely=0.35, height=17)


# Парольге цифрларды косу/қоспау батырмасы
sandar_v = IntVar()
sandar = ttk.Checkbutton(generator, variable=sandar_v, cursor='hand2')
sandar.place(relx=0.199, rely=0.6)


# Парольге үлкен әріптерді косу/қоспау батырмасы
arip_v = IntVar()
arip = ttk.Checkbutton(generator, variable=arip_v, cursor='hand2')
arip.place(relx=0.199, rely=0.485)


# Парольдың ұзындығын көрсету үшін
dlina_v = IntVar(value=8)
dlina_korsetu = ttk.Label(generator)
dlina_korsetu.place(relx=0.2, rely=0.35, height=15)


# Парольдың ұзындығын белгілеу ушін арналған батырма
dlina = ttk.Scale(generator, orient=HORIZONTAL, length=286, from_=8.0, to=24.0,
                  variable=dlina_v, command=butin, cursor='hand2')
dlina.place(relx=0.23, rely=0.35)


# Парольды копия жасау үшін арналған батырма
copy = Button(generator, image=copy_img, command=copy_f, cursor='hand2', compound=TOP)
copy.place(relx=0.78, rely=0.25, width=25, height=24)


#--------------------------------------------------Екінші бет-----------------------------------------------------------

# Таблицаны құру (manager_window1)
columns = ("id", "name", "login", "parol")
tablitca = ttk.Treeview(manager_window1, columns=columns, show="headings", height=9)
tablitca.pack(fill=BOTH, expand=1)


# Ұзыныдығын белгілеу (manager_window1)
tablitca.column("#1", width=30, anchor=CENTER)
tablitca.column("#2", width=170, anchor=CENTER)
tablitca.column("#3", width=140, anchor=CENTER)
tablitca.column("#4", width=140, anchor=CENTER)


# Енгізу жолдарын ортаға қарай жылжыту (manager_window2)
label_name = ttk.Label(manager_window2, text='', background='silver')
label_name.pack(padx=10, pady=13)


# Сайт/приложение атын енгізу жолы (manager_window2)
label_name = ttk.Label(manager_window2, background='silver')
label_name.pack(padx=10, pady=1)
enter_name = ttk.Entry(manager_window2)
enter_name.pack(padx=10, pady=1, ipadx=80)


# Логин енгізу жолы (manager_window2)
label_login = ttk.Label(manager_window2, text='Логин', background='silver')
label_login.pack(padx=10, pady=1)
enter_login = ttk.Entry(manager_window2)
enter_login.pack(padx=10, pady=1, ipadx=80)


# Пароль енгізу жолы (manager_window2)
label_parol = ttk.Label(manager_window2, text='Пароль', background='silver')
label_parol.pack(padx=10, pady=1)
enter_parol = ttk.Entry(manager_window2)
enter_parol.pack(padx=10, pady=1, ipadx=80)


# Жаңасын жасау батырмасы (кестеге жаңа элементтер қосу, келесі бетке аустырады)
sozdat = Button(manager_window1, command=perekluchitel_function, background='lightgrey', cursor='hand2')
sozdat.pack(side='right', ipadx=95)


# Жою батырмасы (кестедегі элементтерді жою)
udalit = Button(manager_window1, command=delete_function, background='lightgrey', cursor='hand2')
udalit.pack(side='left', ipadx=95)


# Қосу батырмасы (элементтерді енгізіп болғаннан кейін басуға)
dobavit = Button(manager_window2, command=dobavit_function, background='lightgrey', cursor='hand2')
dobavit.place(relx=0.5, rely=0.91, width=240)


# Артқа қайту батырмасы (екінші беттен бірінші бетке қайту)
nazad = Button(manager_window2, command=perekluchitel_function, background='lightgrey', cursor='hand2')
nazad.pack(side='left', ipadx=95)


#---------------------------------------------------Үшінші бет----------------------------------------------------------

lg = Label(setting, bg='silver')
lg.place(relx=0.2, rely=0.2)


# Тілді қазақшаға аустыру батырмасы
lg_kz = Button(setting, image=kz_img, background='silver', command=lambda: lg_f(1), cursor='hand2')
lg_kz.place(relx=0.45, rely=0.2)


# Тілді орысшаға аустыру батырмасы
lg_ru = Button(setting, image=ru_img, background='silver', command=lambda: lg_f(2), cursor='hand2')
lg_ru.place(relx=0.57, rely=0.2)


# Тілді ағылшыншаға аустыру батырмасы
lg_en = Button(setting, image=en_img, background='silver', command=lambda: lg_f(3), cursor='hand2')
lg_en.place(relx=0.69, rely=0.2)


#------------------------------------------------------Соңы-------------------------------------------------------------

# Базадағы мәліметтерді кестеге енгізу (manager_window1)
c.execute("SELECT rowid, * FROM dannie")
for person in c.fetchall():
    tablitca.insert("", END, values=person)


# Тілді орнату
lg_when_open()

db.commit()
db.close()
root.mainloop()


#-----------------------------------------------------------------------------------------------------------------------