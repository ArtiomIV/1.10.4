from task_1_10_4 import Client

client_dict = [
    {
    "Firstname": "Иван",
    "Lastname": "Петров",
    "Balance": 50.0,
    "City": "Москва",
    "Status": "Наставник"
    },
    {
    "Firstname": "Артем",
    "Lastname": "Иванов",
    "Balance": 500.5,
    "City": "Милан",
    "Status": "Студент"
    },
    {
    "Firstname": "Лана", #P.S простите :)))
    "Lastname": "Роудс",
    "Balance": 5000.5,
    "City": "Чикаго",
    "Status": "Ветеринар" 
    }
]
class Guest(Client):
    def __init__(self, city = "Не указано", status = "Неуказано"):
        super().__init__(firstname = "Не указано", lastname = "Не указано", balance = "Не указано")
        self.city = city
        self.status = status
    
    def init_form_dict(self, even_dict):
        super().init_form_dict(even_dict)
        self.city = even_dict.get("City")
        self.status = even_dict.get("Status")

    def getInfo(self):
        return print(f"Полная информация о клиенте: {self.firstname} {self.lastname} \nБаланс: {self.balance} \nГород: {self.city} \nСтатус: {self.status}")

class CheckList():
    def __init__(self, guest = "Не указан", lastname = "Не указан"):
        self.guest = guest
        self.lastname = lastname
        self.guest_list = []

    
    def init_from_guest_dict(self, event_dict):
        self.guest = event_dict
        self.lastname = event_dict.get("Lastname")
        self.guest_list = []

    def addToList(self):
        self.guest_list.append(self.lastname)

    def guestCheckList(self):
        if self.lastname in self.guest_list:
            return print(f"Клиент {self.lastname} в списке")
        else:
            print(f"Клиент {self.lastname} не был приглашен")
            
        
    
for event in client_dict:
    client = CheckList()
    client.init_from_guest_dict(event)
    client.addToList()
    client.guestCheckList()
    client = Guest()
    client.init_form_dict(event)
    client.getInfo()




