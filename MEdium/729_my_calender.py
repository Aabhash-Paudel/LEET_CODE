class MyCalendar:
    def __init__(self):
        self.books_start = []
        self.books_end = []

    def book(self, start: int, end: int) -> bool:
        for i in range(len(self.books_start)):
            if start < self.books_end[i] and end > self.books_start[i]:
                return False
        
        self.books_start.append(start)
        self.books_end.append(end)
        return True

# Usage example:
# obj = MyCalendar()
# param_1 = obj.book(start, end)
