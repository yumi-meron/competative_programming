class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            row.reverse()
            for j in range(len(row)):
                if row[j] == 0:
                    row[j] = 1
                else:
                    row[j] = 0
                
                    
        return image
        