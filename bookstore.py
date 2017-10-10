#!/usr/bin/python
import argparse
import math


def num_books_in_budget(initial_price, discount, floor_price, budget):
    # set vars for processing
    current_price = initial_price
    balance = budget
    total_purchased = 0

    # loop until discount has reached floor price, updating total and current price variables
    while True:
        balance -= current_price
        total_purchased += 1

        current_price = current_price - discount

        if current_price <= floor_price:
            current_price = floor_price
            break

    # calculate number that can purchased at floor
    can_buy_at_floor = math.floor(balance / float(current_price))

    # update total and balance
    total_purchased += can_buy_at_floor
    balance -= can_buy_at_floor * current_price

    return int(total_purchased), balance

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find the total number of books that can be purchased '
                                                 'at the given discount parameters')
    parser.add_argument('initial_price', type=int, help='Initial price of the books')
    parser.add_argument('discount', type=int, help='Discount applied to each additional purchase')
    parser.add_argument('floor_price', type=int, help='The lowest discounted price available')
    parser.add_argument('budget', type=int, help='Find how many books can be purchased given this amount')
    args = parser.parse_args()

    books_purchased, remaining = num_books_in_budget(args.initial_price, args.discount, args.floor_price, args.budget)

    print('{} books purchased with ${:.2f} remaining'.format(books_purchased, remaining))
