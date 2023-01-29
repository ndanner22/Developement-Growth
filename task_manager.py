#=====importing modules===========
from datetime import datetime
from datetime import date
# open file user.txt
file = open("user.txt", "r")

'''define a new function 'reg_user'. open file user.txt as appendable. Create two variables 'new_pass' as empty and 'new_pass1' with one character space so that they are not the same.
    Request user to enter a new password and save as 'new_pass'. Request user to confirm password and save entry as 'new_pass1'. If new_pass is equal to new_pass1,
    append new_user and new_pass to file users.txt. Else, have them continue until new_pass and new_pass1 do match'''

def reg_user():
    file1 = open("user.txt", "r")
    users1 = file1.readlines()
    # create a list named temp and set the first two items in list both equal to an empty space
    user_name = " "
    temp = [" "," "]
    # create empty list 'names'
    names = []
    # use a for loop to add the user names from user.txt into list names
    for user in users1:
            temp = user.strip()
            temp = temp.split(", ")
            names.append(temp[0])
    file1.close()
    # create a while loop that will continue to loop if user_name is in list names. If user_name is in list names, ask user to provide a user name and save as variable user_name and start list over.
    while True:
        user_name = input("Enter new user name (case sensitive): ")
        if user_name in names:
            print("This user name already exists, please try again.")
        # if user_name not in list name, break out of while loop
        else:
            break
    # if x not in names:
    file = open("user.txt","a")
    new_pass = ""
    new_pass1 = " "
    while new_pass != new_pass1:
        new_pass = input("Please enter new password - remember that this will be case sensitive: ")
        new_pass1 = input("Please confirm new password: ")
        if new_pass == new_pass1:
            file.write("\n" + user_name + ", " + new_pass)
            file.close()
            print()
            break
        else:
            print("Passwords do not match, try again.")
    return

# define function 'add_task' with no parameters
def add_task():
    # open file user.txt and file tasks.txt
    file = open("user.txt","r")
    file1 = open("tasks.txt", "a")
    # create variable 'new_name' and set to empty
    new_name = ""
    # create list 'temp' and set first index equal to a blank character space
    temp = [" "]
    # read the lines of user.txt into a list named user
    users = file.readlines()
    # using same structure as beginning of program, check to make sure user enters a valide user name from file user.txt
    while new_name != temp[0]:
        new_name = input("Enter valid user name for person assigned to this task: ")
        for user in users:
            temp = user.strip()
            temp = temp.split(", ")
            if temp[0] == new_name:
                break
    # after user name is confirmed as valid, request relevant information for tasks and save each piece of information to its own variable
    title = input("What is the title of the task: ")
    desc = input("What is description of the task: ")
    date = input("What is the due date of this task (using 07 Jan 2023 format) : ")
    current_date = input("What is the current date (using 07 Jan 2023 format): ")
    # append information to the file tasks.txt
    file1.write("\n" + new_name + ", " + title + ", " + desc + ", " + current_date + ", " + date + ", No")
    # close both files user.txt and tasks.txt
    file.close()
    file1.close()
    print()
    return

# define function 'view_all' with no parameters
def view_all():
    # open file tasks.txt as read only
    file = open("tasks.txt", "r")
    # read lines of tasks.txt into list named 'tasks'
    tasks = file.readlines()
    # create for loop that runs for each item in list tasks
    for task in tasks:
        # strip each line of tasks and split each line into a list.(split by commas)
        temp = task.strip()
        temp = temp.split(", ")
        print()
        # print out each new list in an easy to read format
        print("Task:                " + temp[1])
        print("Assigned to:         " + temp[0])
        print("Date assigned:       " + temp[3])
        print("Due Date:            " + temp[4])
        print("Task Complete:       " + temp[5])
        print("Task description:    \n" + "\t" + temp[2])
    # close file tasks.txt
    file.close()
    print()
    return

# define function 'view_mine' with no parameters
def view_mine():
    # open file tasks.txt
    file = open("tasks.txt", "r")
    #file1 = open("tasks.txt", "w")
    # read lines of tasks.txt into list my_tasks
    my_tasks = file.readlines()
    # create int variables 'counter' and 'count' and set to 1
    count = 1
    counter = 1
    # create empty dictionary 'holder' and empty list 'holder1'
    holder = {}
    holder1 = []
    # run through each line of tasks
    for task in my_tasks:
        # strip line and save to variable temp
        temp = task.strip()
        # add current value of counter to temp and save to variable temp1
        temp1 = temp + ", " + str(counter)
        # split temp by a comma space
        temp = temp.split(", ")
        # if current user name matches the user name assigned to task, print out the details of current task in an easy to read format
        # if current value of index 0 in temp is equal to user_name, print out the below list, append temp1 to list holder1 and add 1 to the value of counter and count
        if temp[0] == user_name:
            print()
            print("Task number:         " + str(counter))
            print("Task:                " + temp[1])
            print("Assigned to:         " + temp[0])
            print("Date assigned:       " + temp[3])
            print("Due Date:            " + temp[4])
            print("Task Complete:       " + temp[5])
            print("Task description:    \n" + "\t" + temp[2])
            # add current value of count to holder as a key and current value of counter as the value
            holder[count] = counter
            holder1.append(temp1)
            counter += 1
            count += 1
        # else add one to variables counter
        else:
            counter +=1
    file.close()
    print()
    # create infinite while loop
    while(True):
        # request user to input which task they would like to view and save to task 1 - let them return to main menu if they select -1
        task1 = input("Which task would you like to select - select by task number or enter -1 to return to main menu: ")
        print()
        # if integer value of task is a value in dictionary 'holder'
        if int(task1) in holder.values():
            # create a for loop that runs through list holder
            for line in holder1:
                # for each item in holoder, split by a comma space and add to list temp
                temp = line.split(", ")
                # if task1 is equal to -1 break the while loop
                if task1 == "-1":
                    print()
                    break
                # else if temp at index 0 equals user_name and int value of task1 is in range between 1 and value of counter
                elif int(task1) == int(temp[6]):
                    print("Enter 1 if you would like to mark the task as complete")
                    print("Enter 2 if you would like to edit the task")
                    print()
                    # save user choice from above menu to variable 'choice'
                    choice = input("")
                    # create int variable counter1 and set equal to 1
                    counter1 = 1
                    # if choice is equal to 1 open tasks and read into variable 'my_tasks'
                    if choice == "1":
                        file = open("tasks.txt", "r")
                        my_tasks = file.readlines()
                        # create a for loop that runs through list my_tasks strip each item and split by a comma space and save to variable 'temp'
                        for task in my_tasks:
                            temp = task.strip()
                            temp = temp.split(", ")
                            # if counter1 is equal to value of task1 and counter 1 is equal to counter minus 1
                            if counter1 == int(task1) and counter1 == counter-1:
                                # change value of temp at index 5 to 'Yes'
                                temp[5] = "Yes"
                                # join list temp by a comma space
                                temp = ", ".join(temp)
                                # set my_tasks at index counter1-1 equal to temp 
                                my_tasks[counter1-1] = temp
                                file.close()         
                            # else if counter1 is equal to task1
                            elif counter1 == int(task1):
                                # change value of temp at index 5 to 'Yes' with a line break at the end
                                temp[5] = "Yes\n"
                                 # join list temp by a comma space
                                temp = ", ".join(temp)
                                 # set my_tasks at index counter1-1 equal to temp
                                my_tasks[counter1-1] = temp
                                file.close()
                                # add one to value of counter1
                            counter1 += 1
                    
                        file1 = open("tasks.txt","w")
                        # for loop through my_tasks and write each item to tasks.txt on a new line
                        for task in my_tasks:
                            file1.writelines(task)
                        file1.close()
                        print()
                    # if choice is equal to 2 read tasks.txt into variable my_tasks and create variable counter1 with a value of 1
                    if choice == "2":
                        print()
                        file = open("tasks.txt", "r")
                        my_tasks = file.readlines()
                        counter1 = 1
                        # for loop through my_tasks and strip each line and split by a comma space and save to variable 'temp'
                        for task in my_tasks:
                            temp = task.strip()
                            temp = temp.split(", ")
                            # if temp at index 5 equals 'Yes' and counter1 is equal to task1 - print that the task has already been completed
                            if temp[5] == "Yes" and counter1 == int(task1):
                                print("This task has already been compeleted")
                                break
                            # else if, temp at index 5 equals 'No' and counter1 equals task1 print the below menu
                            elif temp[5] == "No" and counter1 == int(task1):
                                print("Enter 1 if you would like to change the user name of this task")
                                print("Enter 2 if you would like to change the due date of this task")
                                print()
                                # save the user's choice as variable 'edit_choice'
                                edit_choice = input("")
                                print()
                                # if edit_choice is equal to 1 read lines of user.txt into variable users, set a new variable user_name1 equal to nothing and create a new list temp with the first two items as a blank character space
                                if edit_choice == "1":
                                    file = open("user.txt")   
                                    users = file.readlines()
                                    user_name1 = ""
                                    temp = [" "," "]
                                    # create a while loop that runs as along as user_name does not equal the first item saved in list temp. Ask user to provide a user name and save as variable user_name.
                                    while user_name1 != temp[0]:
                                        user_name1 = input("Enter new user name for task: ")
                                        print()
                                        #create a for loop that runs through each line of users. Strip each line and split each line by a comma space into a list named 'temp'.
                                        for user in users:
                                            temp = user.strip()
                                            temp = temp.split(", ")
                                            # if user_name1 is equal to the first item in list temp, break the loop
                                            if temp[0] == user_name1:
                                                break
                                        # if temp at index 0 does not euqal user_name1, print that and invalid user names was enter and start while loop over
                                        if temp[0] != user_name1:
                                            print("Invalid user name entered, please try again.")
                                            print()
                                    file.close()
                                    file = open("tasks.txt", "r")
                                    # read lines of tasks.txt into variable user_change and create variable 'counter2' with a value of 1                          
                                    user_change = file.readlines()
                                    counter2 = 1
                                    # for loop through user_change, strip each item and split by a comma space and save to variable temp
                                    for change in user_change:
                                        temp = change.strip()
                                        temp = temp.split(", ")
                                        # if counter2 equals task1 and counter2 equals counter - 1
                                        if counter2 == int(task1) and counter2 == counter-1:
                                            # set temp at index 0 equal to user_name1
                                            temp[0] = user_name1
                                            # join temp by a comma space
                                            temp = ", ".join(temp)
                                            # set user_change at index task1 minus one equal to temp
                                            user_change[int(task1)-1] = temp
                                            file.close()
                                        # else if, counter2 equals task1
                                        elif counter2 == int(task1):
                                             # set temp at index 0 equal to user_name1
                                            temp[0] = user_name1
                                            # set temp at index 5 equal to temp at index 5 plus a line break
                                            temp[5] = temp[5] + "\n"
                                            # join temp by a comma space
                                            temp = ", ".join(temp)
                                            # set user_change at index task1 -1 equal to temp
                                            user_change[int(task1)-1] = temp
                                            file.close()
                                        # add 1 to counter2
                                        counter2 += 1
                                    file1 = open("tasks.txt","w")
                                # loop through user_change and write each item to tasks.txt on a new line
                                    for i in user_change:
                                        file1.writelines(i)
                                    file1.close()
                                # else if choice equals 2, create variable new_date1 and ask for user to input a new due date in the correct date format
                                elif choice == "2":
                                    new_date1 = input("Please enter new due date in (using 07 Jan 2023 format): ")            
                                    print()
                                    # read lines of tasks.txt into variable 'date_change' and create variable counter3 with a value of 1
                                    file = open("tasks.txt", "r")                          
                                    date_change = file.readlines()
                                    counter3 = 1
                                    # loop through items in date_change, strip each item and split by a comma space and save to variable 'temp
                                    for change in date_change:
                                        temp = change.strip()
                                        temp = temp.split(", ")
                                        # if counter3 is equal to task1 and counter3 is equal to counter minus 1
                                        if counter3 == int(task1) and counter3 == counter-1:
                                            # set temp at index 4 equal to new_date1
                                            temp[4] = new_date1
                                            # join temp by a comma space
                                            temp = ", ".join(temp)
                                            # set date_change at index task1 minus 1 equal to temp
                                            date_change[int(task1)-1] = temp
                                            file.close()
                                        # else if counter3 is equal to task1
                                        elif counter3 == int(task1):
                                            # set temp at index 4 equal to new_date1
                                            temp[4] = new_date1
                                            # set temp at index 5 equal to temp at index 5 plus a line break
                                            temp[5] = temp[5] + "\n"
                                            # join temp by a comma space
                                            temp = ", ".join(temp)
                                            # set date_change at index task1-1 equal to temp
                                            date_change[int(task1)-1] = temp
                                            file.close()
                                        #  add 1 to counter3
                                        counter3 += 1
                                    file1 = open("tasks.txt","w")
                                    # loop through date_change and write each item to tasks.txt on a new line
                                    for i in date_change:
                                        file1.writelines(i)
                                    file1.close()
                            # add 1 to counter1
                            counter1 += 1  
                    # break
                    break
        # else, print that you have not entered a valid task number
        else:
            print("You have not entered a valid task number")
            print()
        # if task1 is equal to -1, break the loop
        if task1 == "-1":
            break    
    return
# define a new function 'gen_report'
def gen_report():
    '''read lines of tasks.txt into variable 'stats'. create variables 'tot_count', 'y', 'n', 'over_due' and 'in_time' all equal to 0.
    create empty dictionaries 'user_total', 'user_comp', 'user_incomp', and 'user_overdue'.'''
    file = open("tasks.txt", "r")
    stats = file.readlines()
    tot_count = 0
    y = 0
    n = 0
    over_due = 0
    in_time = 0
    user_total = {}
    user_comp = {}
    user_incomp = {}
    user_overdue = {}
    # loop through stats, strip each item and split by a comma space and save to variable temp
    for line in stats:
        tot_count += 1
        temp = line.strip()
        temp = temp.split(", ")
        # if temp at index 0 not a key in dictionary user_total
        if temp[0] not in user_total.keys():
            # create key temp at index 0 with a value of one
            user_total[temp[0]] = 1
        # else add 1 to value of key temp at index 0
        else:
            user_total[temp[0]] += 1
        # if temp at index 0 not a key in user_comp at temp at index 5 is equal to 'Yes'
        if temp[0] not in user_comp.keys() and temp[5] == "Yes":
            # create key temp at index 0 with a value of one
            user_comp[temp[0]] = 1
        # elise if temp at index 0 is a key in user_comp and temp at index 5 is equal to 'Yes' add one to value of key temp at index 0
        elif temp[0] in user_comp.keys() and temp[5] == "Yes":
            user_comp[temp[0]] += 1
        # repeat the same process as previous if and elif statements for dictionary user_incomp
        if temp[0] not in user_incomp.keys() and temp[5] == "No":
            user_incomp[temp[0]] = 1
        elif temp[0] in user_incomp.keys() and temp[5] == "No":
            user_incomp[temp[0]] += 1 
        # if temp at index 5 is equal to 'No'
        if temp[5] == "No":
            # add 1 to variable n
            n += 1
            # create variable due_date with a value of temp at index 4
            due_date = temp[4]
            # create variable due_date1 and set equal due date (which has been converted into date time)
            due_date1 = datetime.strptime(due_date, '%d %b %Y').date()
            # if due_date1 is less than today's date (pulled from date time)
            if due_date1 < date.today():
                # add 1 to over_due
                over_due += 1
            # else, add 1 to in_time
            else:
                in_time += 1  
        # else, add 1 to y
        else:
            y += 1
        # if temp at index 0 not in user_overdue and temp at index 5 is equal 'No' and due_date1 is less than today's date
        if temp[0] not in user_overdue and temp[5] == "No" and due_date1 < date.today():
            # create key temp at index 0 in dicitionary user_overdue with a value of 1
            user_overdue[temp[0]] = 1
        # else if, temp at index 0 in user_overdue and temp at index 5 is equal to 'No' and due_date1 is less than today's date
        elif temp[0] in user_overdue and temp[5] == "No" and due_date1 < date.today():
            # add 1 to value of key temp at index 0 in user_overdue
            user_overdue[temp[0]] += 1
    file.close()
    # create variable 'per_incomplete' and set equal to n divided by (tot_count multiplied by 100)
    per_incomplete = (n / tot_count * 100)
    per_incomplete = round(per_incomplete, 2)
    # create variable 'per_overdue' and set equal to over_due divided by (tot_count multiplied by 100)
    per_overdue = (over_due / tot_count * 100)
    per_overdue = round(per_overdue, 2)
    file = open("task_overview.txt", "w")
    # write tot_count, y, n, over_due, per_incomplete, and per_overdue to file task_overview
    file.write(f"There are currently {tot_count} tasks in task manager.\n{y} have been completed.\n{n} are still not complete.\n{over_due} are currently overdue.\n{per_incomplete}% of tasks are not complete.\n{per_overdue}% of tasks are currently overdue.")
    file.close()
    file1 = open("user.txt", "r")
    # read lines of user.txt into variable 'user_num'
    user_num = file1.readlines()
    # create variable num_users and set equal to the length of user_num
    num_users = len(user_num)
    file1.close()
    file = open("user_overview.txt", "w")
    file.write(f"Total users:   {num_users}\nTotal Tasks: {tot_count}\n")
    # for each key in user_total, write the key and value into it's own line in file user_overview.txt
    for key, value in user_total.items():
        file.write(f"{key} currently is assigned {value}, or {int(value)/tot_count*100}% of the tasks.\n")
    # for each key in user_total, write the key and value into it's own line in file user_overview.txt
    for key, value in user_comp.items():
        file.write(f"{key} has completed {int(value)/(user_total.get(key))*100}% of their tasks.\n")
    # for each key in user_total, write the key and value into it's own line in file user_overview.txt
    for key, value in user_incomp.items():
        file.write(f"{key} still needs to complete {int(value)/(user_total.get(key))*100}% of their tasks.\n")
    # for each key in user_total, write the key and value into it's own line in file user_overview.txt
    for key, value in user_overdue.items():
        file.write(f"{key} is currently overdue on {int(value)/(user_incomp.get(key))*100} of their incomplete projects.\n")
    file.close()
    return
# read lines from user.txt into a variable named 'users'
users = file.readlines()
# create a variable named 'user_name' and set equal to nothing
user_name = ""
# create a list named temp and set the first two items in list both equal to and empty space
temp = [" "," "]
#create a while loop that runs as along as user_name does not equal the first item saved in list temp. Ask user to provide a user name and save as variable user_name.
while user_name != temp[0]:
    user_name = input("Enter your user name (case sensitive): ")
    #create a for loop that runs through each line of users. Strip each line and split each line by a comma space into a list named 'temp'.
    for user in users:
        temp = user.strip()
        temp = temp.split(", ")
        # if user_name is equal to the first item in list temp, break the loop
        if temp[0] == user_name:
            break
    # if user_name is not equal to the first item in list temp, print out that an invalid user name was entered
    if temp[0] != user_name:
        print("Invalid user name entered, please try again.")

# create variable named 'password' and set equal to nothing
password = ""
#create a while loop that runs as along as password does not equal the second item saved in list temp. Ask user to provide a password and save as variable password.
while password != temp[1]:
    password = input ("Enter your password (case sensitive): ")
    #create a for loop that runs through each line of users. Strip each line and turn each line into its own list named 'temp' with each word being a item in list.
    for pass1 in users:
        temp = user.strip()
        temp = temp.split()
        # if password is equal to the second item in list temp, break the loop
        if temp[1] == password:
            break
    # if password is not equal to the second item in list temp, print out that an invalid user name was entered    
    if temp[1] != password:
        print("Invalid password entered, please try again.")
# close file users.txt
file.close()
print()

# create a while loop that will continue to repeat unless force exited out of
while(True):
    # create if statement checking if current user name entered is 'admin'
    if user_name == "admin":
        # if yes, print out the below menu with options - r, a, va, vm, s, e)
        print("Select one of the following options:")
        print("r - Registering a user")
        print("a - Adding a task")
        print("va - View all tasks")
        print("vm - View my task")
        print("gr - Generate reports")
        print("s - View statistics")
        print("e - Exit")
        # save user input as variable 'menu'
        menu = input()
        # convert variable menu to all lowercase 
        menu = menu.lower()
        print()
        
        # create if statement checking if menu is equal to 'r'. Request user to input a new username and save to variable new_user. Run new_user through function reg_user

    # else, print out the below menu with option - a, va, vm, e
    else:
        print("Select one of the following options:")
        print("a - Adding a task")
        print("va - View all tasks")
        print("vm - view my task")
        print("e - Exit")
        # save user input as variable 'menu'
        menu = input()
        # convert variable menu to all lowercase
        menu = menu.lower()
        print()

    # if menu is equal to 'a', run function add_task
    if menu == "r" and user_name == "admin":
            reg_user()
        # else if menu is eual to 's'    
    elif menu == "s" and user_name == "admin":
        # try the below block of code that will open both files user_overview.txt and task_overview.txt and print contents on the user's screen
        try:
            file = open("user_overview.txt", "r")
            file1 = open("task_overview.txt", "r")
            user_overview = file.readlines()
            task_overview = file1.readlines()
            print("User Overview:")
            print()
            for line in user_overview:
                temp = line.strip()
                print(temp)
            print()
            print("Task Overview")
            print()
            for line in task_overview:
                temp = line.strip()
                print(temp)
            print()
            file.close()
            file1.close()
        # except if those two files cannot be found, run function gen_report first and then open both files and print contents onto the user's screen
        except:
            gen_report()
            file = open("user_overview.txt", "r")
            file1 = open("task_overview.txt", "r")
            user_overview = file.readlines()
            task_overview = file1.readlines()
            print("User Overview:")
            print()
            for line in user_overview:
                temp = line.strip()
                print(temp)
            print()
            print("Task Overview")
            print()
            for line in task_overview:
                temp = line.strip()
                print(temp)
            print()
            file.close()
            file1.close()
       
    elif menu == "gr" and user_name == "admin":
        gen_report()
       
    elif menu == 'a':
        add_task()
        
    # else if menu is equal to 'va' - run function view_all
    elif menu == 'va':
        view_all()
        
    # else if menu is equal to 'vm' - run function view_mine
    elif menu == 'vm':
        view_mine()
       
    # else if menu is equal to e
    elif menu == 'e':
        # print goodbye and exit the continuous while loop
        print('Goodbye!!!')
        exit()

    # if menu does not equal any of the valid options from above, tell user that they have entered a wrong choice and start loop over again
    else:
        print("You have made a wrong choice, Please Try again")