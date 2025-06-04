# Даны 2 кольцевых списка с фамилиями шахматистов 2-х команд. Произвести жеребьевку. 
# В первой команде выбирается каждый n-й игрок, а во второй — каждый k-й. 
# Для решения задачи использовать ООП.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = new_node
            new_node.next = self.head

    def remove(self, key):
        if self.head is None:
            return False

        curr = self.head
        prev = None
        while True:
            if curr.data == key:
                if curr == self.head:
                    tail = curr
                    while tail.next != self.head:
                        tail = tail.next
                    self.head = curr.next
                    tail.next = self.head
                else:
                    prev.next = curr.next
                return True
            prev = curr
            curr = curr.next
            if curr == self.head:
                break
        return False

    def find_at_step(self, step):
        if self.head is None:
            return None

        curr = self.head
        for _ in range(step - 1):
            curr = curr.next
        return curr.data

    def remove_at_step(self, step):
        if self.head is None:
            return None

        prev = None
        curr = self.head
        for _ in range(step - 1):
            prev = curr
            curr = curr.next

        if curr == self.head:
            tail = self.head
            while tail.next != self.head:
                tail = tail.next
            self.head = curr.next
            tail.next = self.head
        else:
            prev.next = curr.next

        return curr.data

    def is_empty(self):
        return self.head is None

    def __str__(self):
        if self.head is None:
            return "[]"
        result = [self.head.data]
        curr = self.head.next
        while curr != self.head:
            result.append(curr.data)
            curr = curr.next
        return " -> ".join(result)


class ChessDrawSystem:
    def __init__(self):
        self.team1 = CircularLinkedList()
        self.team2 = CircularLinkedList()

    def add_players(self, team_number, players):
        team = self.team1 if team_number == 1 else self.team2
        for player in players:
            team.append(player)

    def draw_pairs(self, n, k):
        results = []

        while not self.team1.is_empty() and not self.team2.is_empty():
            player1 = self.team1.remove_at_step(n)
            player2 = self.team2.remove_at_step(k)
            results.append((player1, player2))

        return results


if __name__ == "__main__":
    system = ChessDrawSystem()

    team1_names = ["Иванов", "Петров", "Сидоров", "Кузнецов", "Смирнов"]
    team2_names = ["Михайлов", "Федоров", "Алексеев", "Егоров", "Васильев"]

    system.add_players(1, team1_names)
    system.add_players(2, team2_names)

    print("Команда 1:", system.team1)
    print("Команда 2:", system.team2)

    n = 3
    k = 2

    print(f"\nНачинаем жеребьевку: команда 1 — шаг {n}, команда 2 — шаг {k}")

    pairs = system.draw_pairs(n, k)
    for i, (p1, p2) in enumerate(pairs, start=1):
        print(f"Пара {i}: {p1} vs {p2}")
