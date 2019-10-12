#!/usr/bin/python

import argparse


def find_max_profit(prices):
    smallest = prices[0]
    max_profit = prices[1] - smallest
    for i in range(1, len(prices) - 1):
        new_profit = prices[i] - smallest
        if new_profit > max_profit:
            max_profit = new_profit
        if prices[i] < smallest:
            smallest = prices[i]

    return max_profit


print(find_max_profit([1050, 270, 1540, 3800, 2]))

if __name__ == '__main__':
        # This is just some code to accept inputs from the command line
    description = 'Find max profit from prices.'

    parser = argparse.ArgumentParser(description=description)

    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')

    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock "
          "prices {prices}.".format(
              profit=find_max_profit(args.integers), prices=args.integers))
