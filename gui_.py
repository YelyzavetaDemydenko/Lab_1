from Lab_1 import House, Landlord, Tenant, Contract
from tkinter import *

class App():
    def __init__(self, root):
        self.root = root
        self.root.title("Програма аренди житла")
        self.root.geometry("720x400")
        self.list_of_landlords = []
        self.list_of_tenants = []
        self.all_elements = []

        self.menu()


    def menu(self):
        """" Меню """

        self.clean()

        text = Label(self.root, text= "Вкажіть, хто ви: орендодавець чи орендатор?")
        text.pack()
        text.update()

        btn1 = Button(root, text = "Орендодавець", width = 15, bg="#CFECEC", command= self.create_landlord)
        btn1.pack(pady=5)

        btn2 = Button(root, text = "Орендатор", width = 15, bg = "#D0F0C0", command= self.create_tenant)
        btn2.pack(pady=5)

        self.all_elements.extend([btn1, btn2, text])


    def create_landlord(self):
        """ Введення імені орендодавця """

        self.clean()

        text1 = Label(self.root, text= "Добрий день, орендодавцю!")
        text1.pack()

        text2 = Label(self.root, text= "Введіть ваше ім'я:")
        text2.pack()

        self.name_entry = Entry(self.root)
        self.name_entry.pack()

        btn = Button(self.root, text = "Зберегти", bg = "#90EE90", command = self.landlord_menu)
        btn.pack()

        self.all_elements.extend([text1, text2, btn, self.name_entry])


    def landlord_menu(self):
        """ Меню орендодавця """

        try:
            self.name = self.name_entry.get()
        except:
            pass

        self.clean()

        flag = 0
        for landlord in self.list_of_landlords:
            if landlord.name == self.name:
                flag = 1
                self.landlord = landlord
                break

        if not flag:
            self.landlord = Landlord(self.name)
            self.list_of_landlords.append(self.landlord)

        text1 = Label(self.root, text = f"Вітаю, {self.landlord.name}!")
        text1.pack()

        text2 = Label(self.root, text = "Оберіть дію:")
        text2.pack()

        btn1 = Button(self.root, text = "Змінити ім'я", command=self.landlord_name)
        btn2 = Button(self.root, text = "Переглянути список будинків", command=self.landlord_list_of_houses)
        btn3 = Button(self.root, text = "Додати будинок до списку", command=self.landlord_add_house)
        btn4 = Button(self.root, text = "Оформити бронювання будинку", command=self.landlord_add_contract)
        
        btn1.pack(pady = 10), btn2.pack(pady = 10), btn3.pack(pady = 10), btn4.pack(pady = 10)

        exit = Button(self.root, text = "Вихід", bg = "#FF9999", command=self.menu)
        exit.pack(side = "bottom", pady=10)

        self.all_elements.extend([text1, text2, btn1, btn2, btn3, btn4, exit])


    def landlord_name(self):
        """ Змінення імені орендодавця """

        self.clean()

        text = Label(self.root, text = "Введіть нове ім'я")
        text.pack()

        self.name_entry = Entry(self.root)
        self.name_entry.pack()

        btn = Button(self.root, text = "Зберегти", bg = "#90EE90", command=self.landlord_changing_name)
        btn.pack()

        self.all_elements.extend([self.name_entry, text, btn])

    def landlord_changing_name(self):
        """ Процес змінення імені орендодавця """

        self.landlord.name = self.name_entry.get()
        self.name = self.landlord.name

        for elem in self.all_elements:
            elem.destroy()
        self.all_elements = []

        text = Label(self.root, text = "Ім'я змінено!")
        text.pack()

        btn = Button(self.root, text = "Назад", command=self.landlord_menu)
        btn.pack()

        self.all_elements.extend([text, btn])
        

    def landlord_list_of_houses(self):
        """ Переглянути список житла, яким владіє орендодавець """

        self.clean()

        
        if self.landlord.list_of_houses:
            list_of_houses_ = []
            list_of_houses = self.landlord.list_of_houses
            
            for house in list_of_houses:
                if "Є в наявності" in str(house):
                    text = Label(self.root, text = str(house), fg = "#006400")
                else:
                    text = Label(self.root, text = str(house), fg = "#FA8072")
                text.pack()
                list_of_houses_.append(text)

            self.all_elements.extend(list_of_houses_)
        else:
            text = Label(self.root, text = "Поки що немає житлових приміщень")
            text.pack()
            self.all_elements.append(text)

        btn = Button(self.root, text = "Назад", command=self.landlord_menu)
        btn.pack()

        self.all_elements.append(btn)
        

    def landlord_add_house(self):
        """ Додати нове житло до списку """

        self.clean()

        text = Label(self.root, text = "Введіть ціну оренди:")
        text.pack()

        self.price = Entry(self.root)
        self.price.pack()


        btn = Button(self.root, text = "Зберегти", bg = "#90EE90", command= self.create_house)
        btn.pack()

        self.all_elements.extend([text, self.price, btn])


    def create_house(self):
        """ Процес створення та додавання житла """

        price = self.price.get()
        self.clean()

        self.landlord.list_of_houses.append(House(price))
        

        text = Label(self.root, text="Будинок додано!")
        text.pack()

        btn = Button(self.root, text = "Назад", command= self.landlord_menu)
        btn.pack()

        self.all_elements.extend([text, btn])



    def landlord_add_contract(self):
        """ Винаймання житла (створення контракту) """

        self.clean()

        text = Label(self.root, text = "Заповніть форму:")
        text.pack()

        text2 = Label(self.root, text = "Ваше ім'я:")
        text2.pack()

        self.landlord_name_ = Entry(self.root)
        self.landlord_name_.pack(pady= 10)

        text3 = Label(self.root, text = "Iм'я орендатора:")
        text3.pack()        

        self.tenant_name_ = Entry(self.root)
        self.tenant_name_.pack(pady= 10)

        text4 = Label(self.root, text = "Номер будинку:")
        text4.pack()    

        self.house_number = Entry(self.root)
        self.house_number.pack(pady= 10)

        text5 = Label(self.root, text = "Дата початку бронювання (DD.MM.YYYY):")
        text5.pack()  

        self.start_date = Entry(self.root)
        self.start_date.pack(pady= 10)        

        text6 = Label(self.root, text = "Кінець бронювання (DD.MM.YYYY):")
        text6.pack()  

        self.end_date = Entry(self.root)
        self.end_date.pack(pady= 10)     

        btn = Button(self.root, text = "Зберегти", bg = "#90EE90", command=self.creating_contract)
        btn.pack()

        btn2 = Button(self.root, text = "Назад", bg = "#FF9999",command=self.landlord_menu) 
        btn2.pack(pady=10)

        self.all_elements.extend([text, text2, text3, text4, text5, text6, self.landlord_name_, self.tenant_name_, self.house_number, self.end_date, self.start_date, btn, btn2])
        

    def creating_contract(self):
        """ Процес створення та додавання контракту """
        self.landlord_name_1 = self.landlord_name_.get()
        self.tenant_name_1 = self.tenant_name_.get()
        self.house_number_ = self.house_number.get()
        self.start_date_ = self.start_date.get()
        self.end_date_ = self.end_date.get()

        self.clean()

        for landlord in self.list_of_landlords:
            if landlord.name == self.landlord_name_1:
                landlord_ = landlord
                break
        
        for tenant in self.list_of_tenants:
            if tenant.name == self.tenant_name_1:
                tenant_ = tenant
                break

        contract = Contract(landlord_.list_of_houses[int(self.house_number_)-1], landlord_, tenant_, self.start_date_, self.end_date_)
        text = Label(self.root, text = "Договір оформлено")
        text.pack()

        text2 = Label(self.root, text = str(contract))
        text2.pack()

        btn = Button(self.root, text = "Назад", command=self.menu)
        btn.pack()

        self.all_elements.extend([text,text2, btn])

        



    def create_tenant(self):
        """ Введення імені орендатора """

        self.clean()

        text1 = Label(self.root, text = "Добрий день, орендаторе!")
        text1.pack()

        text2 = Label(self.root, text= "Введіть ваше ім'я:")
        text2.pack()

        self.name_entry = Entry(self.root)
        self.name_entry.pack()

        btn = Button(self.root, text = "Зберегти", bg = "#90EE90", command = self.tenant_menu)
        btn.pack()

        self.all_elements.append(text1)
        self.all_elements.append(text2)
        self.all_elements.append(btn)
        self.all_elements.append(self.name_entry)


    def tenant_menu(self):
        """ Меню орендатора """

        try:
            self.name = self.name_entry.get()
        except:
            pass

        self.clean()

        flag = 0
        for tenant in self.list_of_tenants:
            if tenant.name == self.name:
                flag = 1
                self.tenant = tenant        
                break

        if not flag:
            self.tenant = Tenant(self.name)
            self.list_of_tenants.append(self.tenant)

        text1 = Label(self.root, text = f"Вітаю, {self.tenant.name}!")
        text1.pack()

        text2 = Label(self.root, text = "Оберіть дію:")
        text2.pack()

        btn1 = Button(self.root, text = "Змінити ім'я", command=self.tenant_name)
        btn2 = Button(self.root, text = "Переглянути список будинків", command=self.choose_landlord)
        btn3 = Button(self.root, text = "Забронювати будинок", command=self.tenant_add_contract)
        btn1.pack(pady = 10), btn2.pack(pady = 10), btn3.pack(pady = 10)

        exit = Button(self.root, text = "Вихід", bg = "#FF9999", command=self.menu)
        exit.pack(side = "bottom", pady=10)

        self.all_elements.extend([text1, text2, btn1, btn2, btn3, exit])

    def tenant_name(self):
        """ Змінення імені орендатора """

        self.clean()

        text = Label(self.root, text = "Введіть нове ім'я")
        text.pack()

        self.name_entry = Entry(self.root)
        self.name_entry.pack()

        btn = Button(self.root, text = "Зберегти", bg = '#90EE90', command=self.tenant_changing_name)
        btn.pack()

        self.all_elements.extend([self.name_entry, text, btn])

    def tenant_changing_name(self):
        """ Процес змінення імені орендодавця """

        self.tenant.name = self.name_entry.get()
        self.name = self.tenant.name

        self.clean()

        text = Label(self.root, text = "Ім'я змінено!")
        text.pack()

        btn = Button(self.root, text = "Назад", command=self.tenant_menu)
        btn.pack()

        self.all_elements.extend([text, btn])

    def choose_landlord(self):
        """ Обрати орендодавця """

        self.clean()

        if self.list_of_landlords:
            text = Label(self.root, text = "Оберіть одного з орендодавців:")
            text.pack()
            self.all_elements.append(text)
            self.list_of_chk = []
            self.list_of_var = []
            for landlord in self.list_of_landlords:
                var = IntVar()
                chk = Checkbutton(self.root, text = landlord.name, variable= var)
                chk.pack()
                self.list_of_chk.append(chk)
                self.list_of_var.append(var)

            self.all_elements.extend(self.list_of_chk)

            btn = Button(self.root, text = "Зберегти", bg = "#90EE90", command= self.show_list_of_houses)
            btn.pack()
            self.all_elements.append(btn)

        else:
            text2 = Label(self.root, text = "На жаль, ще немає орендодавців")
            text2.pack()
            btn = Button(self.root, text = "Назад", command=self.tenant_menu)
            btn.pack()

            self.all_elements.extend([btn, text2])


    def show_list_of_houses(self):       
        """ Визначаємо орендодавця та показуємо список """

        self.clean()

        n = 0
        for var in self.list_of_var:
            if var.get():
                break
            n +=1

        landlord = self.list_of_landlords[n]

        if landlord.list_of_houses:
            list_of_houses_ = []
            list_of_houses = landlord.list_of_houses
            
            for house in list_of_houses:
                if "Є в наявності" in str(house):
                    text = Label(self.root, text = str(house),fg = "#006400")
                else:
                    text = Label(self.root, text = str(house), fg = "#FA8072")
                text.pack()
                list_of_houses_.append(text)

            self.all_elements.extend(list_of_houses_)
        else:
            text = Label(self.root, text = "Поки що немає житлових приміщень")
            text.pack()
            self.all_elements.append(text)

        btn = Button(self.root, text = "Назад", command=self.tenant_menu)
        btn.pack()

        self.all_elements.extend([text, btn])


    def tenant_add_contract(self):
        """ Бронювання житла """

        self.clean()

        text = Label(self.root, text = "Заповніть форму:")
        text.pack()

        text2 = Label(self.root, text = "Ваше ім'я:")
        text2.pack()

        self.tenant_name_ = Entry(self.root)
        self.tenant_name_.pack(pady= 10)

        text3 = Label(self.root, text = "Iм'я орендодавця:")
        text3.pack()        

        self.landlord_name_ = Entry(self.root)
        self.landlord_name_.pack(pady= 10)

        text4 = Label(self.root, text = "Номер будинку:")
        text4.pack()    

        self.house_number = Entry(self.root)
        self.house_number.pack(pady= 10)

        text5 = Label(self.root, text = "Дата початку бронювання (DD.MM.YYYY):")
        text5.pack()  

        self.start_date = Entry(self.root)
        self.start_date.pack(pady= 10)        

        text6 = Label(self.root, text = "Кінець бронювання (DD.MM.YYYY):")
        text6.pack()  

        self.end_date = Entry(self.root)
        self.end_date.pack(pady= 10)     

        btn = Button(self.root, text = "Зберегти", bg = '#90EE90', command=self.creating_contract)
        btn.pack()

        btn2 = Button(self.root, text = "Назад", bg = "#FF9999",command=self.tenant_menu) 
        btn2.pack(pady=10)

        self.all_elements.extend([text, text2, text3, text4, text5, text6, self.landlord_name_, self.tenant_name_, self.house_number, self.end_date, self.start_date, btn, btn2])

    def clean(self):
        for elem in self.all_elements:
            elem.destroy()
        self.all_elements = []

root = Tk()
app = App(root)
root.mainloop()