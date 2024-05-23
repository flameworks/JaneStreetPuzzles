import math
import json
import time

#### Restriction functions ####
def initialise_final_results(MASTER_NUM):
    final_results = {}
    for x in range(1, MASTER_NUM+1):
        final_results[x] = []
    return final_results

def derive_squares(MASTER_NUM):
    final_results = initialise_final_results(MASTER_NUM)
    for x in range(1,10**MASTER_NUM): 
        num = x ** 2
        digits = int(math.log10(num))+1
        if digits > MASTER_NUM: return final_results
        if digits not in final_results:
            final_results[digits] = []
        final_results[digits].append(num)
    
def power_seven(MASTER_NUM):
    final_results = initialise_final_results(MASTER_NUM)
    for x in range(1, MASTER_NUM): ###### POWER 7
        num = 7 ** x
        digits = int(math.log10(num))+1
        if digits > MASTER_NUM: return final_results
        final_results[digits].append(num)

def fibonacci(MASTER_NUM):
    final_results = initialise_final_results(MASTER_NUM)
    fib_seq = [0,1]
    final_results[1].append(0)
    final_results[1].append(1)
    while True:
        prev2 = fib_seq[-2]
        prev = fib_seq[-1]
        new_num = prev2 + prev
        digits = int(math.log10(new_num))+1
        if digits > MASTER_NUM: return final_results
        fib_seq.append(new_num)
        final_results[digits].append(new_num)
    
def palindrome(MASTER_NUM):
    final_results = initialise_final_results(MASTER_NUM)
    for num in range(10):
        final_results[1].append(num)
    for num in range(1,10**MASTER_NUM):
        for middle in list(range(10)) + ['']:
            new_num = int( str(num) + str(middle) + str(num)[::-1] )
            if new_num == 0: digits = 1
            else: digits = int(math.log10(new_num))+1
            if digits > MASTER_NUM: 
                with open('palindrome.json', 'w') as f:
                    json.dump(final_results, f)
                return final_results
            final_results[digits].append(new_num)

def palindrome_wrapper(MASTER_NUM):
    final_results = palindrome(MASTER_NUM)


    final_results_p1 = initialise_final_results(MASTER_NUM)
    final_results_23 = initialise_final_results(MASTER_NUM)
    final_results_m1 = initialise_final_results(MASTER_NUM)
    for digit, long_list in final_results.items():
        digit = int(digit)
        for num in long_list:
            p1 = num + 1
            digits_p1 = int(math.log10(p1))+1
            if digits_p1 <= MASTER_NUM:
                final_results_p1[digits_p1].append(p1)

            m1 = num - 1
            if m1 == 0: digits_m1 = 1
            elif m1 < 0: continue
            else: digits_m1 = int(math.log10(m1))+1
            if digits_m1 <= MASTER_NUM:
                final_results_m1[digits_m1].append(m1)

            if num % 23 == 0:
                if num == 0: digits_23 = 1
                else: digits_23 = int(math.log10(num))+1
                final_results_23[digits_23].append(num)

    with open('palindrome_p1.json', 'w') as f:
        json.dump(final_results_p1, f)
    with open('palindrome_23.json', 'w') as f:
        json.dump(final_results_23, f)
    with open('palindrome_m1.json', 'w') as f:
        json.dump(final_results_m1, f)
        
    return final_results_p1, final_results_23, final_results_m1

    # final_results + 1
    # multiuples of 23
    # final_results - 1

def get_primes(MASTER_NUM):
    final_results = initialise_final_results(MASTER_NUM)
    prime_list = [2]
    final_results[1].append(2)
    def is_prime(n, prime_list):
        for prime in prime_list:
            if n % prime == 0: return False
        return True
    last_range = int(math.sqrt(10**MASTER_NUM))+2 
    # print(last_range)
    for num in range(3, last_range):
        if is_prime(num, prime_list):
            prime_list.append(num)
            digits = int(math.log10(num))+1
            final_results[digits].append(num)
    return final_results

def prime_power(MASTER_NUM):
    with open('get_primes.json', 'r') as f:
        prime_results = json.load(f)
    final_results = initialise_final_results(MASTER_NUM)
    all_primes = []
    for digits, prime_list in prime_results.items():
        all_primes += prime_list
    for prime1 in all_primes:
        for prime2 in all_primes:
            num = prime1 ** prime2
            if num == 1331:
                print(prime1, prime2)
            digits = int(math.log10(num))+1
            if digits > MASTER_NUM: break
            final_results[digits].append(num)
    return final_results

def power_end_1(MASTER_NUM):
    final_results = initialise_final_results(MASTER_NUM)
    # product of digits ends with 1
    print('hihihi')
    for num in range(1, 10**MASTER_NUM, 2):
        list_num = list(str(num))
        if num % 1000000 == 0: print(num)
        if '2' in list_num: continue
        if '4' in list_num: continue
        if '5' in list_num: continue
        if '6' in list_num: continue
        if '8' in list_num: continue
        a = num

    return final_results

def mult37(MASTER_NUM):
    final_results = initialise_final_results(MASTER_NUM)
    for idx in range(1, 10**(MASTER_NUM-4), 2):
        num = idx*37
        digits = int(math.log10(num))+1
        if digits > MASTER_NUM: break
        final_results[digits].append(num)
    return final_results

def sum_digit7(MASTER_NUM):
    final_results = initialise_final_results(MASTER_NUM)
    # product of digits ends with 1
    for num in range(10**7, 10**(MASTER_NUM-3), 2):
        # split num into list of digits
        list_num = list(str(num))
        list_num = [int(x) for x in list_num]
        if sum(list_num) == 7:
            final_results[len(list_num)].append(num)
    return final_results

#### Main functions #####
def generate_jsons(MASTER_NUM):
    master_functions = {
                        # "derive_squares": derive_squares,
                        # "power_seven": power_seven,
                        # "fibonacci": fibonacci,
                        # "palindrome": palindrome,
                        # "palindrome_wrapper": palindrome_wrapper,
                        # "get_primes": get_primes,
                        # "prime_power": prime_power,
                        # "power_end_1": power_end_1,
                        # "mult37": mult37,
                        # "sum_digit7": sum_digit7,
                        }

    for label, func in master_functions.items():
        if func == "": continue
        result = func(MASTER_NUM)
        cnt = 0
        for x, a in result.items():
            cnt += len(a)
        print(cnt, label)
        if 'palindrome' in label: continue
        with open(label+'.json', 'w') as f:
            json.dump(result, f)

if __name__ == '__main__':
    MASTER_NUM = 11
    generate_jsons(MASTER_NUM)