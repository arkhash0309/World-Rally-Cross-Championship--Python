import random

def ADD():
    global data
    data = []
    try:
        driver_name = input("Enter the name of the driver: ")
        driver_age = int(input("Please enter the age of the driver: "))
        driver_team = input("Please enter the team of the driver: ")
        car_model = input("Please enter the car model: ")
        championship_points = input("Enter the current championship points: ")
        driver_ID = input("Please enter the ID of the driver: ")
        while driver_ID in data:
            print("Record already entered, try again")
            driver_ID = input("Please enter the ID of the driver: ")
        data.append(driver_name + "-" + str(driver_age) + "-" + driver_team + "-" + car_model + "-" + championship_points + "-" + driver_ID + "\n")
        print("Record enter successful")
        confirm = input("Enter STF to enter the data to a text file: ")
        if confirm == "STF":
            STF()
        else:
            print("Record not saved!!")
    except:
        print("Please enter a valid information!!")



def DDD():                                    #local function to delete the details of driver
    name_to_delete = input("Please enter the name which has to be deleted: ")
    filecheck = "driver_details.txt"                    #checks if file is present in the memory
    try:
        data = []
        FileHandle = open(filecheck, "r")               #opens text file in readable mode
        data = FileHandle.readlines()
        FileHandle.close()
        delete_check = input("Please confirm the deletion(Y/N): ")
        if delete_check == "Y":
            filecheck2 = open(filecheck, "w")           #opens text file in writeable mode
            for line_num, line in enumerate(data):#selects the record to be deleted
                if name_to_delete not in line:          #deletes the record
                    filecheck2.write(line)
            filecheck2.close()          #closes the new file
            print("Deletion successful!")
        else:
            print("Record not found! Please try again!")
    except IOError:                                     #validation for existence of file
        print("The relevant file has not been found! Please try again!")


def UDD():
    name_to_update = input("Enter the name to be updated: ")
    filecheck = "driver_details.txt"                                        #checks if file is present in the memory
    try:
        data = []
        FileHandle = open(filecheck, "r")                                   #opens text file in read mode
        data = FileHandle.readlines()
        found = False
        for line_num, line in enumerate(data):
            if name_to_update in line:
                print(line)
                found = True
        if not found:
            print("The entered name cannot be traced.")
        update_check = input("Please confirm the updation(Y/N): ")
        if update_check == "Y":
            filecheck2 = open(filecheck, "w")             #opens file in writeable mode
            for line_num, line in enumerate(data):
                if name_to_update not in line:
                    filecheck2.write(line)
            filecheck2.close()                  #closes the text file
            ADD()
        FileHandle.close()
    except IOError:                 #validation for existence of text file
        print("The relevant file has not been found! Please try again!")


def VCT():
   driver_name = []
   driver_point = []
   driver_sorted_point = []
   driver_age = []
   driver_car = []
   driver_team = []
   filecheck = open("driver_details.txt", "r")            #opens the file in readable mode
   for data in filecheck.readlines():
      name = data[0: data.find("-")]
      team = data.split("-")[2]
      age = data.split("-")[1]
      model = data.split("-")[3]
      points = data.split("-")[4].rstrip("\n")
      driver_name.append(name)
      driver_point.append(points)
      driver_sorted_point.append(points)
      driver_age.append(age)
      driver_car.append(model)
      driver_team.append(team)
      driver_sorted_point.sort(reverse=True)
   print("{:<10}  {:<8}  {:<11}  {:<13}  {:<7}".format("NAME", "AGE", "POINTS", "CAR", "TEAM"))
   for n in range(0, len(driver_sorted_point)):
      marker = driver_point.index(driver_sorted_point[n])
      print("{:<10}  {:<10}  {:<8}  {:<12}  {:<7}".format(driver_name[marker], driver_age[marker], driver_point[marker], driver_car[marker], driver_team[marker]))
   filecheck.close()


def sim():
    driver_info_arr = []
    driver_info = open("driver_details.txt", "r")  # opening the text file in read mode
    for line in driver_info:  # checking each line in the text file
        form = line.strip("\n").split("-")  # separating all the driver details between '-' and forms a sub list
        driver_info_arr.append(form)  # the sub list is added to the main list
    driver_info.close()
    locations = ["Nyirad", "Holjes", "Montalegre", "Barcelona", "Riga", "Norway"]
    first_time = str(input("Is it the first race simulated? (Y/N)"))
    if first_time == "Y":
        date = input("Enter the race date as (2022/09/dd): ")
        file = open("Driver_race.txt", "w")  # opens text file in write mode
        file.write("Date: ")
        file.write(date + '\n')
        file.write("Location: ")
        file.write(random.choice(locations) + '\n')
        driver_name = []
        driver_posn = []
        driver_current_points = []
        file2 = open("driver_details.txt", "r")  # opens text file in readable mode
        for info in file2:
            name = info[0:info.find("-")]
            points = info.split("-")[4].rstrip("\n")
            driver_current_points.append(points)
            driver_name.append(name)
        driver_count = len(driver_name)
        file2.close()
        posn = random.sample(range(1, (driver_count + 1)), driver_count)
        driver_details_file = open("driver_details.txt", "r")
        lines = driver_details_file.readlines()
        for i in range(driver_count):
            file.write(str(posn[i]) + "th place is: " + (driver_name[i] + ' - '))
            tempLine = lines[i].split("-")
            data_arr = driver_details_file
            if posn[i] == 1:
                file.write("Renewed points: " + str((int(driver_current_points[i]) + 10)) + '\n')
                tempLine[4] = str(int(tempLine[4]) + 10)
            elif posn[i] == 2:
                file.write("Renewed points: " + str((int(driver_current_points[i]) + 7)) + '\n')
                tempLine[4] = str(int(tempLine[4]) + 7)
            elif posn[i] == 3:
                file.write("His points are: " + str((int(driver_current_points[i]) + 5)) + '\n')
                tempLine[4] = str(int(tempLine[4]) + 5)
            else:
                file.write("His points are: " + driver_current_points[i] + '\n')  # displays the points after updates
            seperator = "-"
            lines[i] = seperator.join(tempLine)
        driver_details_write = open("driver_details.txt", "w")
        driver_details_write.write("".join(lines))
        driver_details_write.close()
        file.write('\n')
        file.close()  # closes the text file
        print("The simulation is over! Details of race available on Driver_race.txt")
    else:
        date = input("Enter the race date as (yyyy/mm/dd): ")
        file = open("Driver_race.txt", "a")  # opens text file in write mode
        file.write("Date: ")
        file.write(date + '\n')
        file.write("Location: ")
        file.write(random.choice(locations) + '\n')
        driver_name = []
        driver_posn = []
        driver_current_points = []
        file2 = open("driver_details.txt", "r")  # opens text file in readable mode
        for info in file2:
            name = info[0:info.find("-")]
            points = info.split("-")[4].rstrip("\n")
            driver_current_points.append(points)
            driver_name.append(name)
        driver_count = len(driver_name)
        file2.close()
        posn = random.sample(range(1, (driver_count + 1)), driver_count)
        driver_details_file = open("driver_details.txt", "r")
        lines = driver_details_file.readlines()
        for i in range(driver_count):
            file.write(str(posn[i]) + "th place is: " + (driver_name[i] + ' - '))
            tempLine = lines[i].split("-")
            data_arr = driver_details_file
            if posn[i] == 1:
                file.write("His points are: " + str((int(driver_current_points[i]) + 10)) + '\n')
                tempLine[4] = str(int(tempLine[4]) + 10)
            elif posn[i] == 2:
                file.write("His points are: " + str((int(driver_current_points[i]) + 7)) + '\n')
                tempLine[4] = str(int(tempLine[4]) + 7)
            elif posn[i] == 3:
                file.write("His points are: " + str((int(driver_current_points[i]) + 5)) + '\n')
                tempLine[4] = str(int(tempLine[4]) + 5)
            else:
                file.write("His points are: " + driver_current_points[i] + '\n')  # displays the points after updates
            seperator = "-"
            lines[i] = seperator.join(tempLine)
        driver_details_write = open("driver_details.txt", "w")
        driver_details_write.write("".join(lines))
        driver_details_write.close()
        file.write('\n')
        file.close()  # closes the text file
        print("The simulation is over! Details of race available on Driver_race.txt")



def SRR():
    sim()
    further_sim = int(input("Enter the number of races you wish to further simulate: "))
    if further_sim == 0:
        print("Thank you!")
    else:
        for j in range(0, further_sim):
           sim()
        print("Thank you!")


def VRL():
    file = open("Driver_race.txt", "r")  #open the file
    race_dates = [] #list to get all the dates in file
    race_days = []   #list to get the days seperately
    Locations = []
    all_data = file.readlines()
    for x, y in enumerate(all_data):
        if "Date: " in y:
            race_dates.append(y)
    for j in range(len(race_dates)):
        days = race_dates[j].split("/")[2]
        race_days.append(days)
    max_dates = len(race_dates)
    j = max_dates - 1
    for b in range(max_dates - 1):
        for c in range(j):
            if race_days[c] > race_days[c+1]:
                grab = race_dates[c]
                race_dates[c] = race_dates[c+1]
                race_dates[c+1] = grab    #change the word temp everywhere
                grab = race_days[c]
                race_days[c] = race_days[c+1]
                race_days[c+1] = grab  #This is where the sorting is done
        j = j - 1

    for x, y in enumerate(all_data):
        if "Location: " in y:
            Locations.append(y.split(" ")[1])
    x = 0
    for item in race_dates:
        print("Date: " + (item.split(" ")[1]))
        print("Location: " + Locations[x])
        x+=1



def STF():
    first_time_check = input("Is it the first time saving to text file?(Y/N):")
    if first_time_check == "Y":
        FileHandle = open("driver_details.txt", "w")
        for i in range(len(data)):
            FileHandle.write(str(data[i]))
        FileHandle.close()
        print("Record successfully saved!")
    else:
        FileHandle = open("driver_details.txt", "a")
        for i in range(len(data)):
            FileHandle.write(str(data[i]))
        FileHandle.close()
        print("Record successfully saved!")

def RFF():
    choice = input("Do you wish to load driver details (enter D) or race details (enter R)?")
    if choice == "D":
        global driver_details_lists
        FileHandle = open("driver_details.txt", "r")
        driver_details_lists = FileHandle.readlines()
        FileHandle.close()
        data_load_confirm = input("Do you confirm to load data? (Y/N)")
        if data_load_confirm == "Y":
            print("Your data is loading!")
            print(driver_details_lists)
        else:
            print("Data loading cancelled!")
    elif choice == "R":
        global race_details_list
        FileHandle = open("Driver_race.txt", "r")
        race_details_list = FileHandle.readlines()
        FileHandle.close()
        data_load_confirm = input("Do you confirm to load data? (Y/N)")
        if data_load_confirm == "Y":
            print("Your data is loading!")
            print(race_details_list)
        else:
            print("Data loading cancelled")


def ESC():
    print("Thank you!")

                                                             
print("              DRIVER MENU               ")
print("........................................")
print("(1) TYPE ADD TO ADD DRIVER DETAILS     |")
print("(2) TYPE DDD TO DELETE DRIVER DETAILS  |")
print("(3) TYPE UDD TO UPDATE DRIVER DETAILS  |")
print("(4) TYPE VCT FOR STANDINGS TABLE       |")
print("(5) TYPE SRR FOR RANDOM RACE SIMULATION|")
print("(6) TYPE VRL TO VIEW RACE TABLE        |")
print("(7) TYPE STF TO SAVE CURRENT DATA      |")
print("(8) TYPE RFF TO LOAD DATA              |")
print("(9) TYPE ESC TO EXIT THE MENU          |")
choice = input("Please enter the option you want to proceed: ")# prompt to enter the desired function
while choice != "ESC":
    if choice == "ADD":
        ADD()
    elif choice == "DDD":
        DDD()
    elif choice == "UDD":
        UDD()
    elif choice == "VCT":
        VCT()
    elif choice == "SRR":
        SRR()
    elif choice == "VRL":
        VRL()
    elif choice == "STF":
        STF()
    elif choice == "RFF":
        RFF()
    else:
        print("Invalid input! Please try again!")
    choice = input("Please enter the option you want to proceed: ")
else:
    ESC()






     
