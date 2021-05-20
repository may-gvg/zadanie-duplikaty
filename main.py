


a_list = ['A', 'A', 'B', 'C']
a_tuple = ('A', 'A', 'B', 'C')
a_dict = {1: 'A', 2: 'A', 3: 'B', 4: 'C'}


def remove_duplicates(listy):
    if(str(type(listy)) == "<class 'list'>"):
        new_listy = []
        for i in listy:
            if i not in new_listy:
                new_listy.append(i)
        return new_listy
    if (str(type(listy)) == "<class 'dict'>"):
        new_dict = {}
        values = []
        for i in listy:
            if(listy[i] not in values):
                new_dict[i] = listy[i]
                values.append(listy[i])
        return(new_dict)
        pass
    if (str(type(listy)) == "<class 'tuple'>"):
        new_tuple = ()
        for i in listy:
            if i not in new_tuple:
                new_tuple = (*new_tuple, i)
        return new_tuple

print(remove_duplicates(a_list))
print(remove_duplicates(a_tuple))
print(remove_duplicates(a_dict))
