import common

def solve_multiple(coef_m):
    coef_m = clean_up(coef_m)
    B = make_B_matrix(coef_m)
    m = len(coef_m)
    x_count = len(coef_m[0]) - 1
    t_B = get_trapeze_matrix(B, m)
    x = get_x(t_B, m, x_count)
    return x


def make_B_matrix(coef_m):
    B = []
    for row_coef in coef_m:
        elements = row_coef[0:-1]
        c = row_coef[-1] * (-1)
        elements.append(c)
        B.append(elements)
    l = len(coef_m[0])
    I = common.make_I_matrix(l-1)
    for row in I:
        row.append(0)
        B.append(row)
    return B

def get_trapeze_matrix(B, m):
    # Идея
    # Зануляем все кроме последнего столбца в 1 строке
    # Делим и вычитаем из последнего столбца
    # Берем матрицу со второй строки-второго столбца
    # Зануляем все кроме последнего столбца в 1 строке
    # и тд для m строк
    k = 0
    while k < m:
        sub_B =  get_submatrix(B, k)
        sub_B = common.get_single_element_in_row(sub_B)
        sub_B = reorder_by_increase(sub_B)
        B = apply_submatrix(B, sub_B, k)
        if not bool(B[k][k]):
            raise Exception('Нет решения')
        coef = B[k][ -1]/B[k][k]
        rest = B[k][ -1] % B[k][k]
        if bool(rest):
            raise Exception('Нет решения в целых числах, ненулевой правый столбец')
        B = common.substract_colums(B, -1, k, coef);
        k = k + 1
    return B

def get_submatrix(B, i):
    result = []
    k = i
    while i < len(B):
        row = B[i][k:-1]
        result.append(row)
        i = i + 1
    return result

def reorder_by_increase(B):
    result = []
    col = common.get_max_nonzero_col(B)
    for row in B:
        r_row = []
        r_row.append(row[col])
        r_row = r_row + row[0:col] + row[col+1:]
        result.append(r_row)
    return result

def apply_submatrix(B, submatrix, k):
    result = []
    l = len(B)
    i = 0
    while i < l:
        if i < k:
            result.append(B[i])
        else:
            row = B[i][0:k] + submatrix[i - k] + [B[i][-1]]
            result.append(row)
        i = i + 1
    return result

def get_x(t_B, m, x_count):
    params_count = x_count - m

    result = []
    i = 0

    while i < x_count:
        result.append(get_x_i(t_B, i, m))
        i = i + 1
    return result

def get_x_i(t_B, i, m):
    result = []
    row = t_B[m + i][m:]
    result.append(row[-1])
    t_count = len(row) - 1
    j = 0
    while j < t_count:
        result.append(row[j])
        j = j + 1
    return result

def clean_up(coef_m):
    result = []

    # убрали нулевые
    for row in coef_m:
        if not common.is_zero(row):
            result.append(row)

    coef_m = result
    result = []

    # убрали линейно зависимые
    i = 1
    while i <= len(coef_m):
        row = coef_m[i-1]
        rest = coef_m[i:]

        # если нет линейно зависимых среди остальных векторов
        if not is_any_lin(rest, row):
            result.append(row)
        i = i + 1
    return result

def is_any_lin(matrix, row):
    for m_row in matrix:
        if common.is_lin(m_row, row):
            return True
    return False