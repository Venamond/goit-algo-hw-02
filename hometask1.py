import queue
import datetime
import itertools
import random
import os
import sys, time

# List of first names
first_names = [
    "Олександр", "Андрій", "Михайло", "Іван", "Дмитро",
    "Олег", "Володимир", "Сергій", "Юрій", "Тарас",
    "Марія", "Олена", "Ірина", "Наталія", "Світлана",
    "Галина", "Катерина", "Анна", "Людмила", "Вікторія"
]
# List of last names
last_names = [
    "Шевченко", "Бондаренко", "Ткаченко", "Коваленко", "Мельник",
    "Ковальчук", "Кравченко", "Олійник", "Поліщук", "Мороз",
    "Козак", "Романюк", "Петренко", "Гриценко", "Яковенко",
    "Савченко", "Білоус", "Гаврилюк", "Захарченко", "Дмитрук"
]
# Generate a random phone number
def generate_phone():
    return "+380" + "".join(str(random.randint(0, 9)) for _ in range(9))

request_types = ["Консультація", "Скарга", "Запит", "Пропозиція"]

queue = queue.Queue()

class Client:
    def __init__(self, first_name, last_name, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

class Request:
    _id_counter = itertools.count(1)
    def __init__(self, client: Client, type: str):
        self.client = client
        self.type = type
        self.date = datetime.datetime.now()
        self.id = next(Request._id_counter) # Unique ID for each request

# Function to generate a new client request
def generate_request():
    client = Client(
        first_name=random.choice(first_names),
        last_name=random.choice(last_names),
        phone_number=generate_phone()
    )
    request = Request(client, random.choice(request_types))
    queue.put(request)

def process_request():
    print(f"\033[91mЗаявок в черзі: {queue.qsize()}\033[0m")
    if not queue.empty():
        request = queue.get()
        print(40 * '-')
        print(f"{request.date.strftime('%d.%m.%Y %H:%M:%S')} Отримано заявку:")
        print(f"\033[94mНомер заявки:\033[0m {request.id}")
        print(f"\033[94mТип заявки:\033[0m {request.type}")
        print(f"\033[94mКлієнт:\033[0m {request.client.first_name} {request.client.last_name}, Телефон: {request.client.phone_number}\n")
        stages = ["[•    ]", "[••   ]", "[•••  ]", "[•••• ]", "[•••••]"]  # 5  steps
        for s in stages:
            sys.stdout.write("\033[93m\r" + s + " Обробка заявки\033[0m")
            sys.stdout.flush()
            time.sleep(random.uniform(0.1, 0.8))
        print("\033[92m\r[Готово] Обробка заявки завершена\033[0m\n")
        return
    print('⏳ Черга пуста, очікуємо...')
    return

os.system("clear")

print("\033[92mЗапуск системи обробки заявок клієнтів:\033[0m\n")
# generate initial requests, for stop processing press Ctrl+C
try:
    while True:
        # Generate new requests
        for _ in range(random.randint(1, 3)):
            generate_request()
        # Process existing requests
        for _ in range(random.randint(1, 5)):
            process_request()
except KeyboardInterrupt:
    print("\n❌\033[91mСистема обробки заявок зупинена користувачем.\033[0m")