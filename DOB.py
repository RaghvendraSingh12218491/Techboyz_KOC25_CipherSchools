print("Note that the format of date should be in -----> DD/MM/YYYY")
print("Please Enter your Date Of Birth")
DateOfBirth = input("Date of Birth:  ")
print("Please Enter Present Date")
PresentDate = input("Present Date:  ")
x = 365 * (int(PresentDate[6:10]) - int(DateOfBirth[6:10]))
y = 31 * (int(PresentDate[3:5]) - int(DateOfBirth[3:5])) - 4 * (int(PresentDate[3:5]) - int(DateOfBirth[3:5]))
z = int(PresentDate[0:2]) - int(DateOfBirth[0:2])+4

print("Total number of days you survived in the world are: ", str(x + y +z)+"days")