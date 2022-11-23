import numpy
import Crypto
import os
import hashlib

os.chdir("../")
path = os.getcwd()


def target_gen():
    # yuh
    # take user input for target generation. Then do stuff
    difficulty = input("Input difficulty for target generation(integer): ")
    difficulty = int(difficulty)
    target = ''
    for i in range(256):
        if i < difficulty:
            target += '0'
        else:
            target += '1'

    print(f"generated target: {target}")
    print(f"Target length: {len(target)}")

    # Write generated target to txt file in data/
    with open(f'{os.getcwd()}/data/target.txt', 'w') as f:
        f.write(target)


def solution_gen():
    """
    find solution to target given the message as well
    :return:
    """
    with open(f'{os.getcwd()}/data/target.txt', 'r') as f:
        target = f.read()


    with open(f'{os.getcwd()}/data/input.txt', 'r') as f:
        message = f.read()

    # so, with target and message, make some kind of for loop that tries to find a hash between them
    # that has target's number of leading zeros? i'm so confused...

    # take message and concatenate it with SOLUTION, and if the hash of this has the same number of leading zeros as
    # the target, then return 1. If that's wrong, idk. It sounds wrong



    m = hashlib.sha256()
    m.update(bytes(message))


def verification():
    pass


def main():
    """
    Here's the main function. I will call the functions named after the assignment sections here in order.
    :return: null
    """
    target_gen()
    solution_gen()


if __name__ == "__main__":
    main()