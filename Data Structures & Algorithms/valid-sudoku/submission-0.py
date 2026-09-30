class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row check
        for row in board:
            seen = []
            for number in row:
                if number.isdigit():
                    if number not in seen:
                        seen.append(number)
                    else:
                        return False

        # col def

        column = [[],[],[],[],[],[],[],[],[]]

        for row in board:
            for idx, number in enumerate(row):
                column[idx].append(number)

        # col check
        for col in column:
            seen = []
            for number in col:
                if number.isdigit():
                    if number not in seen:
                        seen.append(number)
                    else:
                        return False


        grid = [[],[],[],[],[],[],[],[],[]]

        for i in range(3):
            for row in board[i*3:(i+1)*3]:
                for j in range(3):
                    grid[j+(i*3)].append(row[j*3:(j+1)*3])
        # grid check
        for box in grid:
            seen = []
            for line in box:
                for number in line:
                    if number.isdigit():
                        if number not in seen:
                            seen.append(number)
                        else:
                            return False
        
        return True
