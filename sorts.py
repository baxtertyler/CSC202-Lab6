import random
import time


def selection_sort(list):
    num_comp = 0
    for i in range(len(list)-1):
        smallest_i = i
        for j in range(i+1, len(list), 1):
            num_comp += 1
            if list[j] < list[smallest_i]:
                smallest_i = j
        temp = list[i]
        list[i] = list[smallest_i]
        list[smallest_i] = temp
    return num_comp


def insertion_sort(list):
    num_comp = 0
    for i in range(1, len(list), 1):
        for j in range(i, 0, -1):
            num_comp += 1
            if list[j] < list[j-1]:
                temp = list[j-1]
                list[j-1] = list[j]
                list[j] = temp
            else:
                break
    return num_comp


def main():
    # Code coverage NOT required for main
    # Give the random number generator a seed, so the same sequence of 
    # random numbers is generated at each run
    random.seed(1234)

    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 32000)
    start_time = time.time()
    comps = insertion_sort(randoms)
    stop_time = time.time()
    print(comps, stop_time - start_time)


if __name__ == '__main__':
    main()
