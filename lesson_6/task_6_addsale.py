import sys
import os

if len(sys.argv) == 2:
    if not os.path.exists('bakery.csv'):
        mode = 'w'
    else:
        mode = 'a'

    with open('bakery.csv', mode) as f:
        f.write(f'{sys.argv[1]}\n')

elif len(sys.argv) == 3:
    original_file = open('bakery.csv', 'r+')
    original_file.seek(7 * (int(sys.argv[2]) - 1))
    original_file.write(sys.argv[1])
    original_file.close()


