class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        p1 = 0
        last = None
        for char in typed:
            if p1 < len(name) and char == name[p1]:
                p1+=1
                last = char
            elif char == last:
                continue
            else:
                return False

        return p1 == len((name))

             