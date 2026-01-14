class Solution:
    def separateSquares(self, squares: list[list[int]])-> float:
        total_area = sum(l*l for _, _, l in squares)
        half_area = total_area / 2
        low = min(y for _, y, _ in squares)
        high = max(y + l for _, y, l in squares)
        
        def bottom_area(mid):
            area = 0
            for _, y, l in squares:
                if mid <= y:
                    continue
                elif mid >= y + l:
                    area += l*l
                else:
                    area += l * (mid - y)
            return area
        
        for i in range(100):
            mid = (low + high) / 2
            if bottom_area(mid) < half_area:
                low = mid
            else:
                high = mid
        return low


squares = ([[333,54,87],[87,7,1]])
print(Solution().separateSquares(squares))  

# This is leetcode problem 3453. Separate Squares