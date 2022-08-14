'''
Knapsack problem - from https://leetcode.com/discuss/interview-question/196253/barclays-coding-question-please-provide-solution (the sample answers on this page
are incorrect). 
'''
A = [(1, 53.38, 45), (2, 88.62, 98), (3, 78.48, 3), (4, 72.30, 76), (5, 30.18, 9), (6, 46.34, 48)]

B = [(1, 85.31, 29), (2, 14.55, 74), (3, 3.98, 16), (4, 26.24, 55), (5, 63.69, 52), (6, 76.25, 75), (7, 60.02, 74), \
    (8, 93.18, 35), (9, 89.95, 78)]


def get_adjoining_nums(list_of_ids, starting_index, num_items_per_combination) -> set:
    return set(list_of_ids[starting_index + 1: starting_index + num_items_per_combination - 1])


def get_ids(list_of_ids) -> list:
    '''
    Returns list of lists of combination of ids. None of the combinations is repetitive. A combination is
    considered repetitive if it contains the same elements as another combination, even if those elements are
    in a different order, eg AB and BA.
    '''
    num_items_per_combination = 1
    combinations = []
    while num_items_per_combination < len(list_of_ids) + 1:
        for starting_index in range(len(list_of_ids)):
            if num_items_per_combination == 1:
                temp = set()
                temp.add(list_of_ids[starting_index])
                combinations.append(temp)
                continue
            end_of_combination = starting_index + 1
            while num_items_per_combination == 2 and end_of_combination < len(list_of_ids):
                temp = set()
                temp.add(list_of_ids[starting_index])
                temp.add(list_of_ids[end_of_combination])
                combinations.append(temp)
                end_of_combination += 1
            if 2 < num_items_per_combination < len(list_of_ids) and starting_index + 3 < len(list_of_ids):
                for i in range(len(list_of_ids)):
                    temp = set()
                    temp.add(list_of_ids[starting_index])
                    temp.update(get_adjoining_nums(list_of_ids, starting_index, num_items_per_combination))
                    temp.add(list_of_ids[i])
                    combinations.append(temp)
        if num_items_per_combination == len(list_of_ids):
            temp = set()
            for j in range(len(list_of_ids)):
                temp.add(list_of_ids[j])
            combinations.append(temp)
        num_items_per_combination += 1
    return combinations


def solution(A):
    id_to_price = {}
    id_to_weight = {}
    ids = []
    for tuple in A:
        id_to_price[tuple[0]] = tuple[2]
        id_to_weight[tuple[0]] = tuple[1]
        ids.append(tuple[0])
    combinations = get_ids(ids)
    combination_id_to_cost = {}
    combination_id_to_combination = {}
    combination_id = 0
    if combinations:
        for combination in combinations:
            tot_weight = 0
            tot_cost = 0
            for num in combination:
                tot_weight += id_to_weight[num]
                tot_cost += id_to_price[num]
            if tot_weight <= 100:
                combination_id_to_cost[combination_id] = tot_cost
                combination_id_to_combination[combination_id] = combination
                combination_id += 1
    if len(combination_id_to_cost) == 0:
        return '-'
    else:
        return combination_id_to_combination[max(combination_id_to_cost, key=combination_id_to_cost.get)]

print(solution(A)) # returns {2}
print(solution(B)) # returns {2. 3. 6}
