import common


def solve_single(coef_v):
    result = []
    B = make_B_matrix(coef_v)
    c = coef_v[-1]
    B = common.get_single_element_in_row(B)
    d_i = common.get_max_nonzero_col(B)
    d = B[0][d_i]
    x_count = len(coef_v) - 1
    x_i = 0
    while x_i < x_count:
        x = get_x_i(B, c, d, x_i, d_i)
        result.append(x)
        x_i = x_i + 1

    rest = c % d
    if rest is not 0:
        raise Exception('Нет решения в целых числах')

    return result


def make_B_matrix(coef_v):
    return [coef_v[0:-1]] + common.make_I_matrix(len(coef_v) - 1)

def get_x_i(B, c, d, x_i, d_i):
    result = []
    row_i = x_i + 1
    base = (c/d) * B[row_i][d_i]
    result.append(base)
    l = len(B[row_i])
    i = 0
    while i < l:
        if i is not d_i:
            result.append(B[row_i][i])
        i = i + 1
    return result