class MinStack:

    def __init__(self):
        self.__mins = []
        self.__stack = []

    def push(self, val: int) -> None:
        self.__stack.append(val)
        if len(self.__mins) == 0 or val <= self.__mins[-1]:
            self.__mins.append(val)

    def pop(self) -> None:
        if self.__stack[-1] == self.__mins[-1]:
            self.__mins.pop()
        self.__stack.pop()

    def top(self) -> int:
        return self.__stack[-1]

    def getMin(self) -> int:

        return self.__mins[-1]
        
