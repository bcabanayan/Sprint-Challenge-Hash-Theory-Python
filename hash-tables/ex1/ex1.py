#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    found = False
    for i in range(0, length):
        comp = limit - weights[i]
        comp_index = hash_table_retrieve(ht, comp)
        if comp_index is not None:
            found = True
            if comp_index > i:
                return [comp_index, i]
            else:
                return [i, comp_index]
        else:
            hash_table_insert(ht, weights[i], i)
    if not found:
        return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

