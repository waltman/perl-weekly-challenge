from sys import argv
from time import localtime, mktime

def current_year():
    return localtime().tm_year

def is_leap(year):
    return 1 if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0) else 0

year = current_year() if len(argv) == 1 else int(argv[1])
leap = is_leap(year)
dim = [ [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] ]

for mon in range(12):
    # get dow for first of the month
    dom = 1
    time = mktime((year, mon+1, dom, 0, 0, 0, 0, 0, -1))
    dow = localtime(time).tm_wday

    # advance dow to Friday
    dom += (4 - dow) % 7

    # advance dom to last Friday
    while dim[leap][mon] - dom >= 7:
        dom += 7

    # print it
    print('{}/{:02d}/{}'.format(year, mon+1, dom))
