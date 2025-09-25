board1 = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
bpard2 = [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # line check
        for line in board:
            if len([i for i in line if i != "."]) != len(set([i for i in line if i != "."])):
                return False
        
        # collum check
        for i in range(9):
            temp_list = []
            for line in board:
                temp_list.append(line[i])
            if len([i for i in temp_list if i != "."]) != len(set([i for i in temp_list if i != "."])):
                return False

        # squeare check
        for ix in range(0, 9, 3):
            for iy in range(0, 9, 3):
                temp_list = []
                for x in range(3):
                    for y in range(3):
                        temp_list.append(board[x + ix][y + iy])
                if len([i for i in temp_list if i != "."]) != len(set([i for i in temp_list if i != "."])):
                    return False  
        
        return True

s = Solution()
print(s.isValidSudoku(board1))