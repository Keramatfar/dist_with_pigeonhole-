from math import factorial as fact

def num_of_select_r_from_n_with_atleast_one(n, r):
    return fact(n-1)/(fact(n-r)*fact(r))

num_of_select_r_from_n_with_atleast_one(10, 3)
