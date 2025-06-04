# В рамках обеспечения безопасности на объекте требуется вести учет событий с возможностью быстрого доступа 
# к последним записям. Разработать программное обеспечение, предусматривающее структуру данных «Кольцевой буфер» 
# для хранения ограниченного количества записей о событиях. При заполнении буфера необходимо, 
# чтобы новые события замещали старые. Описать процесс инициализации буфера, методы добавления и извлечения записей, 
# а также управление памятью.


class Event:
    def __init__(self, event_id, description):
        self.event_id = event_id
        self.description = description

    def __str__(self):
        return f"{self.event_id}. {self.description}"


class RingBuffer:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.size = 0
        self.head = 0
        self.tail = 0

    def add(self, event):
        self.buffer[self.head] = event
        if self.size == self.capacity:
            self.tail = (self.tail + 1) % self.capacity
        else:
            self.size += 1
        self.head = (self.head + 1) % self.capacity

    def get_all(self):
        events = []
        for i in range(self.size):
            idx = (self.tail + i) % self.capacity
            events.append(self.buffer[idx])
        return events

    def clear_buffer(self):
        self.buffer = [None] * self.capacity
        self.size = 0
        self.head = 0
        self.tail = 0



buffer = RingBuffer(capacity=4)

event1 = Event(1, "Вход пользователя")
event2 = Event(2, "Неудачная попытка входа")
event3 = Event(3, "Доступ к закрытому файлу")
event4 = Event(4, "Выход пользователя")
buffer.add(event1)
buffer.add(event2)
buffer.add(event3)
buffer.add(event4)

for event in buffer.get_all():
    print(event)

event5 = Event(5, "Вход администратора")
event6 = Event(6, "Удаление файла")
buffer.add(event5)
buffer.add(event6)

print("")
for event in buffer.get_all():
    print(event)


