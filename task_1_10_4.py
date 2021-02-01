class Client:
    def __init__(self, firstname = "Не указан", lastname = "Не указан", balance = 0):
        self.firstname = firstname
        self.lastname = lastname
        self.balance = balance
        

    def init_form_dict(self, even_dict):
        self.firstname = even_dict.get("Firstname")
        self.lastname = even_dict.get("Lastname")
        if isinstance(even_dict.get("Balance"), float):
            self.balance = str(even_dict.get("Balance")) + " руб"
        else:
            return print("Значение баланса некорректное:", even_dict.get("Balance")) 

    def getInfo(self):
        return print(f"Клиент: {self.firstname} {self.lastname} \nБаланс: {self.balance}")

client_dict = [
    {
    "Firstname": "Иван",
    "Lastname": "Петров",
    "Balance": 50.0
    },
    {
    "Firstname": "Артем",
    "Lastname": "Иванов",
    "Balance": 500.5
    }
]

for event in client_dict:
    client = Client()
    client.init_form_dict(event)
    print(client.getInfo())