# import numpy
# import Crypto
import os
import time
from hashlib import sha256


os.chdir("../")
path = os.getcwd()


def target_gen(difficulty=None):

    print("****Target Generation function**** \n\n")

    # for use in my time experiments. If there is an input difficulty, skip the user input bullshit
    if difficulty is None:
        difficulty = input("Input difficulty for target generation(integer): ")
        difficulty = int(difficulty)



    # creates target to display. The real target is a large integer, so I will save it rather than show it.
    target = ''
    for i in range(256):
        if i < difficulty:
            target += '0'
        else:
            target += '1'

    print(f"generated target: {target}")

    real_target = 2 ** (256 - difficulty)
    print(f"Bit target: {real_target}")
    # Write generated target to txt file in data/
    with open(f'{os.getcwd()}/data/target.txt', 'w') as f:
        f.write(str(real_target))


def solution_gen():
    """
    find solution to target given the message
    :param d: difficulty of solution necessary
    :return: solution. Will be an integer number that, combined with the message, has trailing zeroes of equal value to
    the target.
    """

    print("Solution generation function. Generates nonces until a solution satsifies the target.\n\n")

    max_nonce = 2 ** 32
    # Open the target file
    with open(f'{os.getcwd()}/data/target.txt', 'r') as f:
        target = f.read()

    # Open the message file, i.e. the Bearcat ID (mine will be m12865327)
    with open(f'{os.getcwd()}/data/input.txt', 'r') as f:
        message = f.read()

    target = int(target)
    # in this case, nonce is a potential solution. Nonce is simply iterating and getting larger as the loop goes
    for nonce in range(max_nonce):
        hash_result = sha256(bytes(str(message), 'utf-8')+bytes(str(nonce), 'utf-8')).hexdigest()
        # check if this is a valid result, below the target
        if int(hash_result, base=16) < target:
            print(f"Nonce that provided solution: {nonce}")
            print(f"Hash is {hash_result}")
            break

    with open(f'{os.getcwd()}/data/solution.txt', 'w') as f:
        f.write(str(nonce))


def verification():
    """
    verify the solution from solution_gen(). If solution is valid, print 1. If the solution does not satisfy the
    parameters, print 0
    :param d:difficulty
    :return: null
    """
    print("Verification function: Check if the solution satisfies the target\n\n")
    with open(f'{os.getcwd()}/data/target.txt', 'r') as f:
        target = f.read()
    with open(f'{os.getcwd()}/data/input.txt', 'r') as f:
        message = f.read()
    with open(f'{os.getcwd()}/data/solution.txt', 'r') as f:
        sol = f.read()

    target = int(target)

    # check if solution is valid, meaning hash(message||solution) < target
    if int(sol, base=16) < target:
        print("1")
        print("Solution meets target's requirements.")
    else:
        print("0")
        print("Solution does not meet target's requrements.")


def main():
    """
    Here's the main function. I will call the functions named after the assignment sections here in order.
    :return: null
    """

    # target_gen()
    # solution_gen()
    # verification()

    for i in range(16,25):
        target_gen(i)
        start = time.time()
        solution_gen()
        end = time.time()
        verification()
        total_time = end - start
        print(f"Elapsed time to find solution: {total_time} seconds")


if __name__ == "__main__":
    main()