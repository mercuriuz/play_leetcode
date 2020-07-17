class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [{} for _ in range(9)]
        cols = [{} for _ in range(9)] 
        boxes = [{} for _ in range(9)] 
        for i in range(9):
            for j in range(9):
                tmp = board[i][j]
                if not tmp.isdigit():
                    continue
                if rows[i].get(tmp) == 1:
                    return False
                else:
                    rows[i][tmp] = 1
                if cols[j].get(tmp) == 1:
                    return False
                else:
                    cols[j][tmp] = 1
                box = (i // 3) * 3 + (j // 3)
                if boxes[box].get(tmp) == 1:
                    return False
                else:
                    boxes[box][tmp] = 1
        return True