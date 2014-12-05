import calendar
check_cal = calendar.Calendar(6)
sundays = 0
for i in xrange(1901,2001):
        for j in xrange(1,13):
                this_month = check_cal.monthdatescalendar(i,j)
                for week in this_month:
                        if week[0].day == 1:
                                sundays += 1

print sundays




