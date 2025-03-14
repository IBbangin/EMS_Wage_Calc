class Pay_slip:
    """a simple class to represent the pay for a week"""
    def __init__(self,  regular_hours: float, overtime_hours: float, regular_pay: float, overtime_pay: float,):
        # assign information provided to the new Payslip (an instance of the class)
        self.regular_hours = regular_hours
        self.overtime_hours = overtime_hours
        self.regular_pay = regular_pay
        self.overtime_pay = overtime_pay

    def __str__(self):  # how to print a Pay_slip
        return ( # just returns a string so caller can decide to print or save to file
            f"\tRegular hours: {self.regular_hours:.2f}\n"
            f"\tOvertime hours: {self.overtime_hours:.2f}\n"
            f"\tRegular pay: £{self.regular_pay:.2f}\n"
            f"\tOvertime pay: £{self.overtime_pay:.2f}"
        )


def extract_hours_worked(hours_entered: str) -> list[float]:
    """returns a list of hours worked for each day worked of the week"""
    try:  # in case some goes wrong converting
        return [float(hours) for hours in hours_entered.split(",")]
    except ValueError:  # something went wrong with converting a string to a float
        raise ValueError("Expected hours worked with commas between hours for each day ")  # shout about it


print("\n\nWelcome to the COCO EMS pay calculator!\n")

# need to establish hourly pay rate
while True:  # input validation loop
    try:
        wage = float(input("How much do you make per hour? "))
        if wage < 0 or wage > 100:
            raise ValueError()
        break  # leave input validation loop as have valid submission
    except ValueError:
        print("Expected an hourly wage between £0 and £100. Please try again.")
print()

OVERTIME_RATE = float(1.5)  # what to multiple wage by to get overtime pay
STANDARD_SHIFT_HOURS = float(12)

NUM_WEEKS = 2  # how many weeks to calculate pay for
weeks = []  # to store hours worked by day for each week
weeks_pay = []  # to store payslips for each week

valid = True  # assume for now valid data will be provided

# loop for each week in period to be calculated
for week_num in range(1, NUM_WEEKS + 1):
    hours_entered = input(f"Enter hours worked in week {week_num} (comma separated, just return for none): ")
    if hours_entered:  # an empty string is considered False byy Python
        try:  # in case of invalid data
            hours_worked = extract_hours_worked(hours_entered)
            if len(hours_worked) > 7:
                raise ValueError("Too many days of hours worked entered for a week" )
        except ValueError as err_msg:
            print(err_msg)
            valid = False  # this will stop us producing payslips later
            break  # leave loop, no point checking any more weeks
    else:  # if no hours entered, perhaps on leave
        hours_worked = [0]  # so set hours to 0, allows lists below to be correctly populated
    weeks.append(hours_worked)

# if we had good data, can calculate hours, ot hours, and pay for each week
if valid:  # only do this if we have valid data
    for week in weeks:  # loop through data for each week
        # calculate total regular and overtime hours for week
        ot_hours = 0  # accumulate overtime hours for week
        regular_hours = 0  # accumulate regular hours for week
        for hours in week:  # loop through hours for current week
            if hours > STANDARD_SHIFT_HOURS:
                ot_hours += hours - STANDARD_SHIFT_HOURS  # accumulate overtime hours for week
                regular_hours += STANDARD_SHIFT_HOURS  # accumulate regular hours for week
            else:
                regular_hours += hours  # accumulate regular hours for week

        # calculate pay for week
        regular_pay = regular_hours * wage
        ot_pay = ot_hours * OVERTIME_RATE * wage
        weeks_pay.append(Pay_slip(regular_hours, ot_hours, regular_pay, ot_pay))

    # print payslips
    for week_num, week in enumerate(weeks_pay, start=1):
        print(
            f"\nPayslip for week {week_num}:\n"
            f"-------------------------------------\n"
            f"{week}"
        )

else:
    print("Data invalid, no pay calculated")