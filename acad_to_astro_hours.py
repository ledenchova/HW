academic_hours = float(input("Please enter the number of academical hours: "))
hours = (academic_hours*40+academic_hours*15)//60
minutes = (academic_hours*40+academic_hours*15) % 60
print('{:.0f} academical hours are\
 {:.0f}:{:.0f} astronomical hours.'.format(academic_hours, hours, minutes))

