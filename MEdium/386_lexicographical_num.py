class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        list1 = []
        for i in range(1, n + 1):
            list1.append(i)
        list1.sort(key=str)
        return list1
