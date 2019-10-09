#!/usr/bin/python

import argparse


def find_max_profit(prices):
    prices.sort()
    maximum_profit = []
    count = 0
    for i in range(0, len(prices)):
        print(maximum_profit)
        count += 1
        maximum_profit.append(prices[i] - prices[count])

    return maximum_profit


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
