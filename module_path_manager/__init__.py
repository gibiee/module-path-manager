import os
import sys
import glob

def get(current_file, target_file, depth):
    base_dir = os.path.dirname(current_file)
    for _ in range(depth+1):
        for path in glob.glob(os.path.join(base_dir, '*')):
            if not os.path.isdir(path):
                basename = os.path.basename(path)
                if basename == target_file:
                    return os.path.dirname(path)
        base_dir = os.path.dirname(base_dir)
    
    raise FileNotFoundError(f'{target_file} is not found in {base_dir} and its parent directories')

def set(current_file, target_file, depth, syspath=True, chdir=True):
    target_dir = get(current_file, target_file, depth)
    if syspath:
        sys.path.append(target_dir)
    if chdir:
        os.chdir(target_dir)
    return True