# How to solve a problem:
    # Figure out what the input and its type are
    # Set up a function
    # Figure out what the output and its type are
    # Gather Your Knowledge
    # Gathers Your Constraints (Not always necessary) 
    # Determine a Logical way to solve the problem
        #Write each step out English
        #Write each step out in Python-esse (sudo-code)
    # Invoke and Test Your Function

# “Water and Jug Problem” Challenge:
# Challenge: You have two jugs, one that can hold 3 liters and another that can hold 5 liters. Your goal is to measure exactly 4 liters of water. You have an unlimited supply of water, but no markings on the jugs.
# Coding/Real-Life Connection: This puzzle relates to problem-solving by manipulating available resources efficiently. In coding, it’s like optimizing algorithms to achieve specific outcomes. In real life, it mirrors creative resource management to reach desired goals.

# brainstorm
                    #   0                5
# fill up 5-j, pour into 3-j. with 5-j 2 liters in there.
                    #   3                2
# empty out 3-j, leaves you with 0 and 2
                    #   0                2
# pour the 2 liters from the 5-j into the 3-j. 3-j can take ONE MORE liter of water. Then fill up the 5-j.
                    #   2/3                5
# pour out of the 5-j into the 3-j. 3-j can only take ONE MORE liter so that leaves the 5-j with 4 liters of water.
                    #   3                4




# Problem Statement
# You are given a list of coin denominations (e.g., `[1, 5, 10]` for pennies, nickels, and dimes) and a target amount of money (e.g., `18` cents). Write a Python function to find the minimum number of coins needed to make up the target amount. If it's not possible to make the exact amount, return `-1`.

# min_coins([1, 2, 5], 11)  # Output: 3 (11 = 5 + 5 + 1)
# min_coins([2], 3)  # Output: -1 (No combination can sum to 3)

# we will need a function that will take in two arguments (coins, target)
# min coins => [pennies, nickels, dimes]
# reach target number, with least amount of coins => this likely means we need a coin counter
# if not possible, return -1 => probably if/else

# if we want least number of coins, we should try seeing if the biggest coin can go into the target number. if it can't move onto the next biggest coin.


example_coin = [1, 5, 10]
example_target = 18
# 10, 5, 1, 1, 1 = output 5


# [10, 5, 1]
# 10 > 18 ok - 1 coin
# 10 > 8 not ok
# 5 > 8 ok - 2 coin
# 5> 3 not ok
# 1 > 3 ok - 3 coin



def min_coins(coins_list, target_num):
    coin_counter = 0
    new_coin_list = sorted(coins_list, reverse = True)
    while target_num > 0:
        coin_used = False
        for coin in new_coin_list:
            if target_num >= coin:
                coin_counter += 1
                print(coin_counter, 'coin counter')
                print(f'{coin} coin used')
                target_num -= coin
                print(target_num, "target left")
                coin_used = True
                break
        if not coin_used:
            return '-1 (not possible)'
    if target_num == 0:
        return f'Target number reached. Number of coins used: {coin_counter}'

        
print(min_coins(example_coin,example_target))