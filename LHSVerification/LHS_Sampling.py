import pandas as pd
import numpy as np
from smt.sampling_methods import LHS


def generate_inputs(length, file_path, problem=None):
    if problem:
        x_limits = np.array(problem['bounds'])
        sampling = LHS(xlimits=x_limits)
        x = sampling(length)
        inputs = []
        for i in range(length):
            input = {}
            for j, item in enumerate(problem['names']):
                input[item] = x[i, j]
            for f in fix_value:
                if not(f in input.keys()):
                    input[f] = fix_value[f]
            inputs.append(input)
        pd.DataFrame(inputs).to_csv(file_path, index=False, header=inputs[0].keys())


if __name__ == '__main__':
    fix_value = {
        'avg_spd': 1.325,
        'std_spd': 0.225,
        'trl_shr': 0.55,
        'avg_int': 1.75,
        'grp_shr': 0.325,
        'str_cst': 25,
        'ctrl_par': 0.5,
    }
    # Define the model inputs
    # all inputs
    problem_unfixed = {
        'num_vars': 7,
        'names': ['avg_spd', 'std_spd', 'trl_shr', 'avg_int', 'grp_shr', 'str_cst', 'ctrl_par'],
        'bounds': [[1.25, 1.4], [0.15, 0.3], [0.4, 0.7], [1.3, 2.2], [0, 0.65], [10, 40], [0, 1]]
    }
    # fix negligible ones
    problem_fix_negligible = {
        'num_vars': 3,
        'names': ['avg_spd', 'avg_int', 'str_cst', ],
        'bounds': [[1.25, 1.4], [1.3, 2.2], [10, 40], ]
    }
    # fix influential ones
    problem_fix_influential = {
        'num_vars': 4,
        'names': ['avg_spd', 'std_spd', 'trl_shr', 'grp_shr'],
        'bounds': [[1.25, 1.4], [0.15, 0.3], [0.4, 0.7], [0, 0.65]]
    }

    generate_inputs(200, 'verification_data/LHS_fix_insensitive.csv', problem_fix_negligible)
    generate_inputs(200, 'verification_data/LHS_fix_sensitive.csv', problem_fix_influential)
    generate_inputs(200, 'verification_data/LHS_unfixed.csv', problem_unfixed)
