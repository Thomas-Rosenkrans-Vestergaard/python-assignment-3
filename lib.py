import numpy as np

def numpy_read_csv(filename):
    return np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)

def by_key_eq(table, key, values):
    mask = table[:, key] == values[0]
    for x in range(1, len(values)):
        mask = mask | (table[:, key] == values[x])
    
    return table[mask]

def by_key_neq(table, key, values):
    mask = table[:, key] != values[0]
    for x in range(1, len(values)):
        mask = mask & (table[:, key] != values[x])
    
    return table[mask]

def by_year(table, *years):
    return by_key_eq(table, 0, years)

def by_neighbourhood(table, *codes):
    return by_key_eq(table, 1, codes)

def by_age(table, *ages):
    return by_key_eq(table, 2, ages)

def by_age_range(table, low, heigh):
    return table[(table[:, 2] >= low) & (table[:, 2] < heigh)] # exclusive

def by_country(table, *country_codes):
    return by_key_eq(table, 3, country_codes)

def by_country_not(table, *country_codes):
    return by_key_neq(table, 3, country_codes)

def sum_amount(table):
    return table[:, 4].sum()