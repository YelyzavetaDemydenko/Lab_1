import threading

class House():
    """Клас житлове приміщення"""

    num = 0
    def __init__(self, price, availability = True):
        House.num += 1

        self.__num = House.num
        self.__price = price
        self.__availability = availability
        
        self.lock = threading.Lock()

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    @property
    def number(self):
        return self.__num

    @number.setter
    def number(self, num):
        self.__num = num

    @property
    def availability(self):
        return self.__availability

    @availability.setter
    def availability(self, availability):
        self.__availability = availability

    def __str__(self):
        availability_str = "Є в наявності." if self.availability else "Немає в наявності."
        return f"Житло №{self.number}. Ціна: {self.price}. {availability_str}"

class Tenant():
    """Клас орендатор"""

    def __init__(self, name, rental_house = None):
        self.__name = name
        self.__rental_house = rental_house

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name    

    @property
    def rental_house(self):
        return self.__rental_house

    @rental_house.setter
    def rental_house(self, house):
        self.__rental_house = house

    def __str__(self):
        string = f"Ім'я орендатора: {self.name}"
        if self.rental_house:
            string += f"\nОрендовано житло №{self.rental_house.number}."
        else:
            string += "\nНе орендує житло."
        return string

class Landlord():
    """Клас орендодавець"""

    def __init__(self, name, list_of_houses = []):
        self.__name = name
        self.__list_of_houses = list_of_houses

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name    

    @property
    def list_of_houses(self):
        return self.__list_of_houses

    def add_available_house(self, house):
        self.list_of_houses.append(house)

    def add_contract(self, house, landlord, tenant, start_date, end_date):
        house.lock.acquire()
        if house.availability:
            Contract(house, landlord, tenant, start_date, end_date)
        else:
            print("Ми не можемо оформити контракт.")
        house.lock.release()

    def __str__(self):
        string = f"Ім'я орендодавця: {self.name}"

        if self.list_of_houses:
            string += "\nСписок житлових приміщень:\n№ Ціна  Наявність"
            for house in self.list_of_houses:
                availability_str = "Є в наявності." if house.availability else "Немає в наявності."
                string += f"\n{house.number} {house.price} {availability_str}"
        return string


class Contract():
    """Клас договір оренди"""
    list_of_contracts = []
    def __init__(self, house, landlord, tenant, start_date, end_date):
        self.__house_number = house.number
        self.__house_price = house.price
        self.__landlord = landlord
        self.__tenant = tenant
        self.__start_date = start_date
        self.__end_date = end_date
        self.list_of_contracts.append(self)

        house.availability = False
        tenant.rental_house = house

    @property
    def house_number(self):
        return self.__house_number
            
    @property
    def house_price(self):
        return self.__house_price
    
    @property
    def landlord(self):
        return self.__landlord
    
    @property
    def tenant(self):
        return self.__tenant
    
    @property
    def start_date(self):
        return self.__start_date
    
    @property
    def end_date(self):
        return self.__end_date


    def __str__(self):
        return (
            f"Договір оренди житлового приміщення №{self.house_number}"
            f"\nЦіна оренди в місяць: {self.house_price}"
            f"\nОрендодавець: {self.landlord.name}"
            f"\nОрендатор: {self.tenant.name}"
            f"\nТермін оренди: з {self.start_date} до {self.end_date}"
            )

if __name__ == "__main__":
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

    print()
    print(Contract.list_of_contracts[0])
    print(Contract.list_of_contracts[0].house_price)