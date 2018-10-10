# python3


def max_pairwise_product(numbers):
    max_product = 0
    maxnum = max(numbers)
    numbers.remove(maxnum)
    n = len(numbers) 
    for first in range(n):
                
            max_product = max(max_product,
                              numbers[first] * maxnum)

    return max_product


if __name__ == '__main__':
    input_n = int(input())
    tmp = input();
    tmp = tmp.split();
    tmp=list(map(int,tmp)); #int(tmp)
    #input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(tmp));
     #  #max_pairwise_product(input_numbers))
