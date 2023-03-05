import os

for i in range(1, 6):
    os.mkdir(f'./week{i}')
    for j in range(1, 6):
        os.mkdir(f'./week{i}/day{j}')
        os.mkdir(f'./week{i}/day{j}/lesson')
        os.mkdir(f'./week{i}/day{j}/homework')
