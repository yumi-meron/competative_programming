class Solution:
    def interpret(self, command: str) -> str:
        lst = []
        temp = []
        for i in command:
            temp .append(i)
            if i == 'G':
                temp = []
                lst.append('G')
            elif i == ')':
                if len(temp) == 2:
                    lst.append('o')
                    temp = []
                elif len(temp)==4:
                    lst.append('al')
                    temp = []
            else:
                continue
        return ''.join(lst)

        
        