#-------------------------------------------------------------------------------
# Filename:   <name of file>
# Purpose:    Provide a system of tracking employee's work at home
#             and reporting          
# Author:     <Developer's name>
# Created:    <Date created>
# Version:    1.0    
# Notes:      <List any issues, to-do's, fixes, considerations etc>
#                         
#-------------------------------------------------------------------------------
# IMPORT PYTHON LIBRARIES

#-------------------------------------------------------------------------------
# GLOBAL VARIABLES (provide access to all methods in the program

#-------------------------------------------------------------------------------
# METHODS
#-------------------------------------------------------------------------------
# Method:   addWorkersHours() 
# Purpose:  Enter employee hours (for each day in a specified week)
#           and write to external file
# Inputs:   void
# Outputs:  void
#-------------------------------------------------------------------------------
def addWorkersHours():
    print("----------------------------")
    print("---  ADD EMPLOYEE HOURS  ---")
    print("----------------------------")

    #declare list of cdv strings for all employees
    employeesWork_WriteList = []
    # total hours worked for week for each employee
    totalHoursWorked = 0
    weekHoursLessThan30 = 0
    weekHoursMoreThan40 = 0
    weekHoursBetween37And39 = 0

    weekNbr = "Week"
    weekNbr = weekNbr + input ("Enter week # (1-52) -> ")

    for empNbr in range(1, 7):
        #for each employee, hours worked each day
        dayHours = []
        # reset totalHoursWorked for each employee
        totalHoursWorked = 0
        print("[Employee" + str(empNbr) + "]")
        empID = input("Enter Employee " + str(empNbr) + " ID:")
        empName = input("Enter Employee " + str(empNbr) + " Name:")

        #workStr (gets written to external drive)
        workStr = weekNbr + "," + empID + "," + empName + ","

        #loop for each day of the week to get hours worked
        dayList = ["Monday" , "Tuesday" , "Wednesday" , "Thursday" , "Friday" ]

        for day in dayList:
            hoursWorked = int(input("Enter hours worked for " + day + "->"))
            # get running total of each days hours to add to the total
            totalHoursWorked += hoursWorked
            dayHours.append(hoursWorked)
            if (day != "Friday"):
                workStr = workStr + str(hoursWorked) + ","
            else:
                workStr = workStr + str(hoursWorked)

        print(workStr)
        employeesWork_WriteList.append(workStr)

        # check on the total hours worked
        if totalHoursWorked < 30:
            weekHoursLessThan30 += 1
        elif totalHoursWorked > 40:
            weekHoursMoreThan40 += 1
        elif totalHoursWorked >= 37 and totalHoursWorked <= 39:
            weekHoursBetween37And39 += 1

        #for each employee display summary
        print("***************************")
        print("Summary for worker " + str(empID))
 
        for i in range(0, len(dayHours)): 
            if (dayHours[i] < 4):
                print ("Insufficient hours worked on " + dayList[i])
            elif (dayHours[i] >10):
                print("Too many hours worked on " + dayList[i])
        total_hrs = sum(dayHours) 
        print("Total hours worked for the week " + weekNbr + " : " + str(total_hrs) + " hours ")
        if(total_hrs < 20):
            print("Insufficient hours worked this week")
 
        if(total_hrs > 38):
            print("Too many hours worked this week")
    # end outer for loop (for each employee)

    # display for all employees (weekly hours report)
    if (weekHoursLessThan30 > 0):
        print("Number of employees who have worked less than 30 hours: " + str(weekHoursLessThan30))
    if (weekHoursMoreThan40 > 0):
        print ("Number of employees who have worked moren than 40 hours: " + str(weekHoursMoreThan40))
    if (weekHoursBetween37And39 > 0):
        print ("Number of employees worked between 37 and 39 hours per week: " + str(weekHoursBetween37And39))

    

    #write employeesWork_WriteList content to external file
    extFile = open("myData.csv", "a")
    # Loop through employeesWork_WriteList object and write each string to the
    for line in employeesWork_WriteList:
        extFile.write(line + "\n")
    extFile.close()
    

# end addWorkersHours() method
#-------------------------------------------------------------------------------
# Method:    getReport()
# Purpose:   Read external file of employee work-at-home data
#            and display
# Inputs:    void
# Outputs:   void
#-------------------------------------------------------------------------------
def getReport():
    print("----------------------------")
    print("---        REPORT        ---")
    print("----------------------------")
    
    #declare list of csv strings for all employees (for reading)
    employeesWork_ReadList = []

    #reading of the external file
    try:
        #open the file
        extFile = open("myData.csv", "r")
        #loop through each line in external file
        for line in extFile:
            #append line to employeesWork_Readlist
            if (len(line) > 0):
                employeesWork_ReadList.append(line.rstrip())
        #close extFile
        extFile.close()

        #reverse sort
        employeesWork_ReadList.reverse()

        numberrecords = int(input("Enter number of records to display :"))

        for i in range(0, numberrecords):
            print(employeesWork_ReadList[i])
            breakUpStr = employeesWork_ReadList[i].split(",")
            print(breakUpStr[0])
            print("ID: " + breakUpStr[1])
    except:
        print("NO_FILE_ERROR: There are no employee records to read - please use option 1 first!")

    

# end getReport() method
#-------------------------------------------------------------------------------
# Method:    main()
# Purpose:   Entry point to the program
# Inputs:    no input parameters
# Outputs:   no returns
#-------------------------------------------------------------------------------
def main():
    
    # DISPLAY PROGRAM TITLE
    print("-----------------------------------------------------------")
    print("---  DIAMOND REALITY:  EMPLOYEE WORK-FROM-HOME PROGRAM  ---")
    print("-----------------------------------------------------------")
    
    #---------------------------------------------------------------------------
    # 1. DECLARE VARIABLES
    #---------------------------------------------------------------------------
    # option is an integer which tracks the menu option made by the user
    option = 1

    #---------------------------------------------------------------------------
    # 2. INPUTS
    #---------------------------------------------------------------------------
    while (option != 3):
        print("Menu of options")
        print("1. Enter daily hours worked")
        print("2. Produce hours-worked report")
        print("3. Exit")
        print()
        
        # get option from user
        option = int(input("Enter your option 1|2|3 -> "))
        
        # check the option entered
        if (option == 1):
            # call method to add Workers hours
            addWorkersHours()
        elif (option == 2):
            # call method to get report
            getReport()
        else:
            # exit the program
            print("Thank you for using the program")
            break

    # end of main method

#-------------------------------------------------------------------------------
# call main() method
if __name__ == '__main__':
    main()
#-------------------------------------------------------------------------------
