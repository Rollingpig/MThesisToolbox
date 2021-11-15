import SALib.sample.morris
import SALib.analyze.morris
import SALib.plotting.morris
import pandas as pd


def generate_samples(problem, n):
    param_values = SALib.sample.morris.sample(problem, n)
    pd.DataFrame(param_values).to_csv('input.csv', index=False, header=problem['names'])


if __name__ == '__main__':
    # Define the model inputs
    problem = {
        'num_vars': 7,
        'names': ['avg_spd', 'std_spd', 'trl_shr', 'avg_int', 'grp_shr', 'str_cst', 'ctrl_par'],
        'bounds': [[1.25, 1.4], [0.15, 0.3], [0.4, 0.7], [1.3, 2.2], [0, 0.65], [10, 40], [0, 1]]
    }
    generate_samples(problem, 50)
