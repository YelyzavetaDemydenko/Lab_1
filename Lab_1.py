import threading

class House():
    """Клас житлове приміщення"""

    number = 0
    def __init__(self, price, availability = True):
        House.number += 1

        self.__number = House.number
        self.__price = price
        self.__availability = availability
        
        self.lock = threading.Lock()

    def get_price(self):
        return self.__price

    def get_number(self):
        return self.__number

    def get_availability(self):
        return self.__availability

    def set_price(self, price):
        self.__price = price

    def set_number(self, number):
        self.__number = number

    def set_availability(self, availability):
        self.__availability = availability

    def __str__(self):
        availability_str = "Є в наявності." if self.get_availability() else "Немає в наявності."
        return f"Житло №{self.get_number()}. Ціна: {self.get_price()}. {availability_str}"

class Tenant():
    """Клас орендатор"""

    def __init__(self, name, rental_house = None):
        self.__name = name
        self.__rental_house = rental_house

    def get_name(self):
        return self.__name

    def get_rental_house(self):
        return self.__rental_house

    def set_name(self, name):
        self.__name = name

    def set_rental_house(self, house):
        self.__rental_house = house

    def __str__(self):
        string = f"Ім'я орендатора: {self.get_name()}"
        if self.get_rental_house():
            string += f"\nОрендовано житло №{self.get_rental_house().get_number()}."
        else:
            string += "\nНе орендує житло."
        return string

class Landlord():
    """Клас орендодавець"""

    def __init__(self, name, list_of_houses = []):
        self.__name = name
        self.__list_of_houses = list_of_houses

    def get_name(self):
        return self.__name

    def get_list_of_houses(self):
        return self.__list_of_houses

    def set_name(self, name):
        self.__name = name

    def add_available_house(self, house):
        self.get_list_of_houses().append(house)

    def add_contract(self, house, landlord, tenant, start_date, end_date):
        house.lock.acquire()
        if house.get_availability():
            Contract(house, landlord, tenant, start_date, end_date)
        else:
            print("Ми не можемо оформити контракт.")
        house.lock.release()

    def __str__(self):
        string = f"Ім'я орендодавця: {self.get_name()}"

        if self.get_list_of_houses():
            string += "\nСписок житлових приміщень:\n№ Ціна  Наявність"
            for house in self.get_list_of_houses():
                availability_str = "Є в наявності." if house.get_availability() else "Немає в наявності."
                string += f"\n{house.get_number()} {house.get_price()} {availability_str}"
        return string


class Contract():
    """Клас договір оренди"""
    
    def __init__(self, house, landlord, tenant, start_date, end_date):
        self.house_numder = house.get_number()
        self.house_price = house.get_price()
        self.landlord = landlord
        self.tenant = tenant
        self.start_date = start_date
        self.end_date = end_date

        house.set_availability(False)
        tenant.set_rental_house(house)

    def __str__(self):
        return (
            f"Договір оренди житлового приміщення №{self.house_numder}"
            f"\nЦіна оренди в місяць: {self.house_price}"
            f"\nОрендодавець: {self.landlord.get_name()}"
            f"\nОрендатор: {self.tenant.get_name()}"
            f"\nТермін оренди: з {self.start_date} до {self.end_date}"
            )


landlord_Steve = Landlord("Steve")
landlord_John = Landlord("John")
tenant_Nick = Tenant("Nick")
tenant_Fred = Tenant("Fred")
print(landlord_Steve)
print(landlord_John)
print(tenant_Nick)
print(tenant_Fred)
print()

house_1 = House(15000)
house_2 = House(25000)
landlord_Steve.add_available_house(house_1)
landlord_Steve.add_available_house(house_2)
print(landlord_Steve)
print(tenant_Nick)
print()


t1 = threading.Thread(target = landlord_Steve.add_contract(house_1, landlord_Steve, tenant_Nick, "21.12.2024", "21.05.2025"))
t2 = threading.Thread(target = landlord_Steve.add_contract(house_1, landlord_Steve, tenant_Fred, "23.12.2024", "13.05.2025"))

t1.start()
t2.start()

t1.join()
t2.join()

print()
print(landlord_Steve)
print(tenant_Nick)
print(tenant_Fred)

print(house_1)
print(house_2)