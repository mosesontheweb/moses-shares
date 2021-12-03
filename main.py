import sys
import re


def parse_str(num):
    """
    Parse a string that is expected to contain a number.
    :param num: str. the number in string.
    :return: float or int. Parsed num.
    """
    if not isinstance(num, str): # optional - check type
        raise TypeError('num should be a str. Got {}.'.format(type(num)))
    if re.compile('^\s*\d+\s*$').search(num):
        return int(num)
    if re.compile('^\s*(\d*\.\d+)|(\d+\.\d*)\s*$').search(num):
        return float(num)
    raise ValueError('num is not a number. Got {}.'.format(num)) # optional


def sum_all(values: list) -> int:
    summary = 0
    for val in values:
        _v = parse_str(val)
        summary += _v
    return summary

if len(sys.argv) < 3:
    usage = '''Usage: python main.py num num [num ...]

    <num> can be either float or integer
    minimum amount of arguments is two
    '''
    print(usage)
    sys.exit(1)

summary = sum_all(sys.argv[1:])

print(f"Die Summe ist: {summary}")
