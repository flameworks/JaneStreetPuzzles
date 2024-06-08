from parameters import PARAMS, CONSTRAINTS, MASTER_NUM, WORD_CONSTANTS
from copy import deepcopy as dc
import json
import random

class specialgrid:
    def __init__(self):
        self.PARAMS = PARAMS
        self.MASTER_NUM = MASTER_NUM
        self.grid = [[-2 for _ in range(self.MASTER_NUM)] for _ in range(self.MASTER_NUM)]
        self.params_str = ''
        self.grid_str = ''
        self.possibilities = [[ list(range(-1,10)) for _ in range(self.MASTER_NUM)] for _ in range(self.MASTER_NUM)]
        self._initial_weed()

        with open('jsons/prime_power.json', 'r') as f:
            self.prime_power = json.load(f)
        with open('jsons/fibonacci.json', 'r') as f:
            self.fibonacci = json.load(f)
        
        self.weed_count = 0
        
        # -1 are blocks
        # -2 are empty
        # 0-9 are filled
    
    ####### Helpful methods #######
    def pprint(self, type=''):
        def _pprint(type="grid"):
            if type.lower() == "params": grid_to_print = self.PARAMS
            else: grid_to_print = self.grid
            headerStr = " "
            for i in range(self.MASTER_NUM):
                headerStr += " " * (4 - len(str(i)))
                headerStr += str(i)
            print(headerStr)
            for cnt in range(self.MASTER_NUM):
                row = grid_to_print[cnt]
                if cnt < 10: strr = f" {cnt}|"
                else: strr = str(cnt) + "|"
                for i in range(self.MASTER_NUM):
                    strr += " " * (1-len(str(row[i])))
                    if row[i] < -1: strr += "   "
                    elif row[i] == -1: strr += " . "
                    elif row[i] >= 10: strr += f" {row[i]}"
                    elif row[i] >= 0: strr += f" {row[i]} "
                    if i < self.MASTER_NUM-1: strr += "|"
                strr += "| " + str(cnt)
                if cnt < 10: strr += " "
                strr += "  " + WORD_CONSTANTS[cnt]
                print(strr)
            print(headerStr)

        print()
        if type != '':
            print("Params:")
            _pprint("params")
            print()
        print("Grid:")
        _pprint("grid")
        print()

    def get_neigh(self, i, j):
        neigh = []
        if i-1 >= 0: neigh.append((i-1, j))
        if j-1 >= 0: neigh.append((i, j-1))
        if i+1 < self.MASTER_NUM: neigh.append((i+1, j))
        if j+1 < self.MASTER_NUM: neigh.append((i, j+1))
        return neigh

    def get_all_valid_nums(self):
        all_nums = []
        for i in range(self.MASTER_NUM):
            temp_num = []
            for j in range(self.MASTER_NUM):
                if self.grid[i][j] == -1: 
                    if temp_num and -2 not in temp_num:
                        all_nums.append( (temp_num,i) )
                    temp_num = []
                else:
                    temp_num.append(self.grid[i][j])
            if temp_num and -2 not in temp_num:
                all_nums.append( (temp_num,i) )
        return all_nums

    def min_filled(self):
        count = 0
        for i in range(self.MASTER_NUM):
            for j in range(self.MASTER_NUM):
                if self.grid[i][j] >= -1:
                    count += 1
        return count

    def final_result(self):
        result = 0
        if not self.valid_check(): return -1
        if self.min_filled() != self.MASTER_NUM**2: return -1
        for num_arr, idx in self.get_all_valid_nums():
            num = int(''.join([str(x) for x in num_arr]))
            result += num
        return result
   
    def get_available_group(self):
        all_nums = []
        for row in self.PARAMS:
            all_nums += row
        all_nums = sorted(list(set(all_nums)))
        for idx in range(self.MASTER_NUM**2):
            if idx not in all_nums: return idx

    def get_entire_group(self, i, j):
        neigh_chain = set()
        curr_group_value = self.PARAMS[i][j]

        workspace = [ (i, j) ]
        while workspace:
            curr_i, curr_j = workspace.pop(0)
            if (curr_i, curr_j) in neigh_chain: continue
            else: neigh_chain.add((curr_i, curr_j))
            for neigh in self.get_neigh(curr_i, curr_j):
                if neigh in neigh_chain: continue
                n_i, n_j = neigh
                if self.PARAMS[n_i][n_j] == curr_group_value:
                    workspace.append(neigh)
        return list(neigh_chain)
    
    ######## Pruning methods methods #######
    def _initial_weed(self):
        # in row 8, self.possiblities can only contain -1, 1, 3, 7, 9, remove everything else
        for j in range(self.MASTER_NUM):
            for num in [0,2,4,5,6,8]:
                self.possibilities[8][j].remove(num)

        # in row 3, self.possiblities can only contain < 7 remove everything else
        for j in range(self.MASTER_NUM):
            for num in [8, 9]:
                self.possibilities[3][j].remove(num)

        # in all rows, index 1 and index -2 cannot be -1, and index 0 can't be 0
        for i in range(self.MASTER_NUM):
            self.possibilities[i][1].remove(-1)
            self.possibilities[i][-2].remove(-1)
            if 0 in self.possibilities[i][0]:
                self.possibilities[i][0].remove(0)
    
    def weed(self, outputBool=False):
        self.weed_count += 1
        actioned = False     
        # Work on Filled cells, remove possibilities from everywhere
        for i in range(self.MASTER_NUM):
            for j in range(self.MASTER_NUM):
                #### HANDLING IF CELL IS BLOCKED (-1) ###
                if self.grid[i][j] == -1:
                    # if -1, remove 0 from next cell's possibilities
                    if (j+1 <= self.MASTER_NUM-1):
                        if self.grid[i][j+1] == 0: 
                            if outputBool: print(f'False due to 0 after -1 for {i},{j}')
                            return False
                        if 0 in self.possibilities[i][j+1]: 
                            self.possibilities[i][j+1].remove(0)
                            actioned = True

                    # for any cells that are -1, remove -1 possibility from all its neighbours
                    for neigh in self.get_neigh(i, j):
                        n_i, n_j = neigh
                        if -1 in self.possibilities[n_i][n_j]:
                            self.possibilities[n_i][n_j].remove(-1)
                            actioned = True
                
                #### HANDLING IF CELL IS FILLED with 0-9 ###
                if self.grid[i][j] >= 0:
                    # check all neighbours, if same group, possibilities are either -1 or the number, remove everything else
                    # if different group, remove number from possibilities
                    to_remove = list(range(10))
                    to_remove.remove(self.grid[i][j]) # list from 0 to 9 exccept this num, and no -1
                    for neigh in self.get_neigh(i, j):
                        n_i, n_j = neigh
                        if self.PARAMS[n_i][n_j] == self.PARAMS[i][j]:
                            for num in to_remove:
                                if num in self.possibilities[n_i][n_j]:
                                    self.possibilities[n_i][n_j].remove(num)
                                    actioned = True
                        else:
                            if self.grid[i][j] in self.possibilities[n_i][n_j]:
                                self.possibilities[n_i][n_j].remove(self.grid[i][j])
                                actioned = True

                    ## Since current cell is filled, if previous cell is -1 or blank, next cell cannot be -1
                    if j-1 < 0 or (j-1>=0 and self.grid[i][j-1] == -1):
                        if j+1 >= self.MASTER_NUM: 
                            if outputBool: print(f'False due to -1 after filled for {i},{j}')
                            return False # previous cell is blocked, current cell is filled, next cell cannot be edge
                        if -1 in self.possibilities[i][j+1]: 
                            self.possibilities[i][j+1].remove(-1)
                            actioned = True

                
                #### HANDLING ANY non blank cell ###
                if self.grid[i][j] >= -1:
                    # Confirm if all filled cells are removed of possibilities, even if blocked 
                    if self.grid[i][j] in self.possibilities[i][j]:
                        if len(self.possibilities[i][j]) > 1:
                            self.possibilities[i][j] = [self.grid[i][j]]
                            actioned = True
                    else: 
                        if outputBool: print(f'False due to filled cell not in possibilities for {i},{j}, fc:{self.grid[i][j]}, poss:{self.possibilities[i][j]}')
                        return False
        
        if actioned:
            actioned = False
            # Reloop, now working on Blank cells 
            for i in range(self.MASTER_NUM):
                for j in range(self.MASTER_NUM):
                    #### HANDLING BLANK cell (-2) ###
                    # if a cell has only one possibility, fill it in
                    if self.grid[i][j] == -2:
                        if len(self.possibilities[i][j]) == 1:
                            self.grid[i][j] = self.possibilities[i][j][0] 
                            actioned = True            

        if actioned: return self.weed(outputBool) # Recursively weed till good
        # Since no action was taken
        return True

    def find_closest_cell(self):
        for i in range(self.MASTER_NUM):
            for j in range(self.MASTER_NUM):
                if self.grid[i][j] == -2:
                    return i, j, self.possibilities[i][j]
        return -1, -1, []

    ######## Valid check methods ########
    def direct_number_check(self, num_arr, row_num):
        if len(num_arr) <= 1: return False # Less than 2 digits
        if num_arr[0] == 0: return False # First digit is 0

        num = int(''.join([str(x) for x in num_arr]))
        digits = len(num_arr)
        if row_num == 0: # Square
            return num == int(num**0.5)**2
        elif row_num == 1: # 1 more than pallindrome
            return ( num-1 == int(str(num-1)[::-1]) )
        elif row_num == 2: # prime power p, USED REFERENCE
            return num in self.prime_power[str(digits)]
        elif row_num == 3: # sum digits 7
            return sum(num_arr) == 7
        elif row_num == 4: # fibonacci, USED REFERENCE
            return num in self.fibonacci[str(digits)]
        elif row_num == 5: # Square
            return num == int(num**0.5)**2
        elif row_num == 6: # multiple of 37
            return num % 37 == 0
        elif row_num == 7: # 23 palindrome
            return ( num == int(str(num)[::-1]) and num % 23 == 0 )
        elif row_num == 8: # product ends in 1
            product = 1
            for x in num_arr:
                product *= x
            return product % 10 == 1
        elif row_num == 9: # multiple of 88
            return num % 88 == 0
        elif row_num == 10: # 1 less than pallindrome
            return ( num+1 == int(str(num+1)[::-1]) )
        else:
            print('Invalid Row num')
            return False    

    def update_params_group(self): 
        # For every blocked cell, check neighbours. 
        # From each starting neighbour, get entire neighbour group and change their group number.
        # First starting neighbour can be ignored.
        for i in range(self.MASTER_NUM):
            for j in range(self.MASTER_NUM):
                if self.grid[i][j] == -1:
                    curr_group_num = self.PARAMS[i][j]
                    self.PARAMS[i][j] = -1
                    to_update_bool = False ### Don't need to update the 1st group
                    neigh_arr = self.get_neigh(i, j)
                    for n_x, n_y in neigh_arr:
                        if self.PARAMS[n_x][n_y] == curr_group_num:
                            if to_update_bool == False:
                                to_update_bool = True
                                continue
                            new_group_num = self.get_available_group()
                            for x, y in self.get_entire_group(n_x, n_y):
                                self.PARAMS[x][y] = new_group_num
        return

    def valid_check(self, outputBool=False, force_check=False):
        self.update_params_group() ## Update params on block
        self.weed(outputBool) ## Ensure weeded

        for num_arr, row_num in self.get_all_valid_nums():
            if not self.direct_number_check(num_arr, row_num): 
                if outputBool: print(f'False number on {num_arr}, row {row_num}')
                return False

        ## Check number groups
        for i in range(self.MASTER_NUM):
            for j in range(self.MASTER_NUM):
                if self.grid[i][j] >= 0:
                    for neigh in self.get_neigh(i, j):
                        n_i, n_j = neigh
                        if self.grid[n_i][n_j] >= 0:
                            if self.PARAMS[n_i][n_j] == self.PARAMS[i][j]:
                                if self.grid[n_i][n_j] != self.grid[i][j]:
                                    if outputBool: print(f'False due to number in group for {i},{j}')
                                    return False
                            else:
                                if self.grid[n_i][n_j] == self.grid[i][j]:
                                    if outputBool: print(f'False due to number in different group for {i},{j}')
                                    return False

        # check that blocks are not adjacent to each other
        for i in range(self.MASTER_NUM):
            for j in range(self.MASTER_NUM):
                if self.grid[i][j] == -1:
                    for neigh in self.get_neigh(i, j):
                        n_i, n_j = neigh
                        if self.grid[n_i][n_j] == -1:
                            if outputBool: print(f'False due to blocks adjacent for {i},{j}')
                            return False
        
        # check that possibilities are not empty
        for i in range(self.MASTER_NUM):
            for j in range(self.MASTER_NUM):
                if len(self.possibilities[i][j]) == 0: 
                    if self.grid[i][j] != -2:
                        if outputBool: print(f'False due to no possibilities for {i},{j} but filled previously')
                        return False
                        print('Weird Error where self.grid[i][j] != -2 but possibilities are empty')
                        print(self.grid[i][j], i, j, self.possibilities[i][j])
                        self.pprint('a')
                        1/0
                    if outputBool: print(f'False due to no possibilities for {i},{j}')
                    return False

        return self.weed(outputBool)

if __name__ == "__main__":

    gg = specialgrid()
    gg.grid[0] = [1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4]
    gg.grid[1] = [1, 3, 3, 3, 2, -1, 3, 4, 4, 4, -1]
    gg.grid[2] = [1, 3, 3, 1, -1, 7, 3, 4, 4, 4, 9]
    gg.grid[3] = [1, 3, 3, -1, 1, 0, 0, 4, 1, 1, -1]
    gg.grid[4] = [1, 3, -1, 1, 4, 4, -1, 4, 1, 8, 1]
    gg.grid[5] = [1, 4, 4, 4, -1, 4, 4, 4, 8, 8, 9]
    gg.grid[6] = [7, 4, 4, 4, 4, -1, 7, 4, 8, 8, 8]
    gg.grid[7] = [7, 7, 1, 4, 1, 7, 7, -1, 9, 8, 9]
    gg.grid[8] = [7, 7, 1, 1, 1, 7, 7, 9, 9, 9, 9]
    gg.grid[9] = [-1, 1, 1, 4, 4, -1, 7, 9, 9, 9, 2]
    gg.grid[10] = [4, 4, 4, 4, 4, 3, -1, 3, 9, 9, 2]

    gg.weed()

    gg.pprint('all')
    print(gg.valid_check(outputBool=True, force_check=True))
    print(f'Final Result: {gg.final_result():,}') 


