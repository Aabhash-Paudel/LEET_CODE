class MyCalendarTwo:

    def __init__(self):
        self.singlebook=[]
        self.doublebook=[]

    def book(self, start: int, end: int) -> bool:
        for i,j in self.doublebook:
            if start <j and end >i:
                return False
        for i,j in self.singlebook:
            if start <j and end >i:
                self.doublebook.append((max(start,i),min(end,j)))
        self.singlebook.append((start,end))
        return True
            
