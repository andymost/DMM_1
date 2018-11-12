import sys

def make_I_matrix(size):
    I = []
    i = 0
    j = 0
    while i < size:
        row = []
        while j < size:
            if i == j:
                row.append(1)
            else:
                row.append(0)
            j = j + 1
        i=i+1
        j = 0
        I.append(row)
    return I

def substract_colums(B, i, j, coef):
    l = len(B)
    k = 0
    while k < l:
        B[k][i] = B[k][i] - (coef * B[k][j])
        k = k + 1
    return B

def get_min_nonzero_col(B):
    # сделать через boolean
    row = list(map(lambda x: abs(x) if x is not 0 else sys.maxsize, B[0]))
    return row.index(min(row))

def get_max_nonzero_col(B):
    # сделать через boolean
    row = list(map(lambda x: abs(x) if x is not 0 else -sys.maxsize, B[0]))
    return len(row) - row[::-1].index(max(row)) - 1

def is_single_elem(B):
    was_found = False
    for i in B[0]:
        if i is not 0:
            if was_found:
                return False
            was_found = True
    return True

def get_single_element_in_row(B):
    while not is_single_elem(B):
        i_min = get_min_nonzero_col(B)
        i_max = get_max_nonzero_col(B)
        coef = B[0][i_max] // B[0][i_min]
        B = substract_colums(B, i_max, i_min, coef)
    return B

def is_lin(v1, v2):
    SMALL_VAL = 1e-15;
    v1 = list(map(lambda x: x if x is not 0 else SMALL_VAL, v1))
    v2 = list(map(lambda x: x if x is not 0 else SMALL_VAL, v2))

    i = 0
    v1_clean = []
    v2_clean = []
    while i < len(v1):
        if v1[i] is not SMALL_VAL or v2[i] is not SMALL_VAL:
            v1_clean.append(v1[i])
            v2_clean.append(v2[i])
        i = i + 1

    coef = v1_clean[0]/v2_clean[0]
    i = 1
    while i < len(v1_clean):
        c_coef = v1_clean[i]/v2_clean[i]
        if c_coef != coef:
            return False
        i = i + 1
    return True

def is_zero(v):
    for e in v:
        if bool(e):
            return False
    return True