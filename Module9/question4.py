def sum_all_odds(list_of_ints):
    sum = 0
    for i in list_of_ints:
        if i % 2 != 0:
            sum += i
    return sum

list_of_ints = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sum_all_odds(list_of_ints))