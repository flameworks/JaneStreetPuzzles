import math

def get_blockages(MASTER_NUM):
    global_grids = [ [0], [1] ]
    finalised = []
    while global_grids:
        temp_grid = global_grids.pop(0)
        if len(temp_grid) == MASTER_NUM:
            finalised.append(tuple(temp_grid))
            continue
    
        if not( 1 in temp_grid[-2:] or len(temp_grid) == 1 ):
            global_grids.append( temp_grid+[1] )
        global_grids.append( temp_grid+[0] )

    final_ans = []
    for block in finalised:
        if block[-2] == 1: continue
        final_ans.append(block)
    return final_ans

def get_latest_req(grouping_formula, blocked_grid):
    if len(grouping_formula) != len(blocked_grid): return []
    incrementor = 0
    new_formula = []
    for i in range(len(grouping_formula)):
        blocked_bool = blocked_grid[i] == 1
        if blocked_bool:
            incrementor += 1
            new_formula.append(-1)
        else:
            new_formula.append(grouping_formula[i]+incrementor)
    return new_formula

def split_list(lst):
    result = []
    temp = []
    for x in lst:
        if x == -1:
            result.append(temp)
            temp = []
        else:
            temp.append(x)
    result.append(temp)
    while [] in result:
        result.remove([])
    return result

def compare_req(num, requirement):
    if len(requirement) == 1: return True
    num_arr = [int(x) for x in list(str(num))]
    if len(num_arr) != len(requirement):
        print('why?')
        print(num, requirement)
        return 1/0

    prev_group = requirement[0]
    prev_num = num_arr[0]
    for idx in range(1, len(requirement)):
        curr_group = requirement[idx]
        curr_num = num_arr[idx]
        if prev_group == curr_group:
            if prev_num != curr_num: return False
        else:
            if prev_num == curr_num: return False
        prev_group = curr_group
        prev_num = curr_num
    return True
    
def joiner(new_req, blockage_results):
    final_arr = []
    countdown = 0
    blk_idx = 0
    for num in new_req:
        if num == -1: 
            if countdown != 0:
                print('critical error')
                1/0
            final_arr.append(-1)
        else:
            if countdown != 0:
                countdown -= 1
            else:   
                final_arr.append(blockage_results[blk_idx])
                D = blockage_results[blk_idx][0]
                if D == 0: countdown = 0
                else: countdown = int(math.log10(D))+1 -1
                blk_idx += 1
    return final_arr

def get_possibilities(fractioned_req, constraint_function):
    blockage_results = []
    for req in fractioned_req:
        sample_nums = []
        L = len(req) 
        flag = False
        for num in constraint_function[str(L)]:
            if compare_req(num, req):
                flag = True
                sample_nums.append(num)
        if not flag: return []
        blockage_results.append(sample_nums)
    return blockage_results
