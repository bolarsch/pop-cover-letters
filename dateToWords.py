# datetime is used for date math uwu and for using computer clock to determine the actual date and time
import datetime

# sets var to MM/DD/YY
today_date = datetime.datetime.today().strftime('%m/%d/%y')
# converts a string into an array, delimited by / always remove brackets too!
# creates a list of the month, date, year
dateArray = [x for x in today_date.strip('[]').split('/')]



# returns a string indicating the month using m
def toMonth(m):

    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November',
              'December']
    return months[int(m) - 1]


# returns a string of an ordinal number (28th, for example)
def toOrdinal(num):
    if int(num) >= 10:
        x = num % 10 #retrieve the units digit simply by using the factorial
    if x == 1:
        date_suf = 'st'
    elif x == 2:
        date_suf = 'nd'
    elif x == 3:
        date_suf = 'rd'
    else:
        date_suf = 'th'
    return str(num) + date_suf


# returns the string (today's date) as: "December 28th, 2020"
def getStrDate ():
    return toMonth(dateArray[0]) + ' ' + toOrdinal(int(dateArray[1])) + ', 20' + dateArray[2]

