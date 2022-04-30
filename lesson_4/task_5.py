'''Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли. Например:
> python task_4_5.py USD
75.18, 2020-09-05'''
from task_4.utils import currency_rates

def main(argv):
    print(*currency_rates(argv))
    return 0

if __name__ == '__main__':
    import sys
    exit(main(sys.argv[1]))