from single import solve_single
from multiple import solve_multiple


def read_input():
    input_file = open('./input', 'r')
    first_row = input_file.readline()
    [n_str, m_str] = first_row.split(' ')
    n = int(n_str)
    m = int(m_str) + 1
    result = []
    for i in range(0, n):
        vec_str = input_file.readline()
        vec = list(map(int, vec_str.split(' ')))
        result.append(vec)
    input_file.close()
    return result

def solve(coef_m):
    dim = len(coef_m)
    if dim == 1:
        return solve_single(coef_m[0])
    else:
        return solve_multiple(coef_m)

def print_output(result):
    output_file = open('./output', 'w')
    t_count = len(result[0]) - 1
    output_file.write(str(t_count) + '\n')
    output_file.write('\n'.join(map(stringify_row ,result)))
    output_file.close()

def stringify_row(row):
    x = row.pop()
    vec = [x] + row
    return ' '.join(map(str, vec))

coef = read_input()
try:
    result = solve(coef)
except Exception as err:
    output_file = open('./output', 'w')
    output_file.flush()
    output_file.close()
    print(err.args[0])
    exit(1)
print_output(result)
