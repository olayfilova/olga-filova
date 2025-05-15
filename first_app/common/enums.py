from enum import StrEnum, auto


class WorkDayEnum(StrEnum):
    WORKING_DAY=auto()
    VACATION='vacation'
    SICK_DAY='sick_day'
    WEEKEND='weekend'
    UNPAID_DAY='unpaid_day'
    HOLIDAY='holiday'


for a in  WorkDayEnum:
    print(a)