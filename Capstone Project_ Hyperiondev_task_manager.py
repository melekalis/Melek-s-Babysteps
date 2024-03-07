# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========
import sys
import os
from datetime import datetime, date
import sys

DATETIME_STRING_FORMAT = "%Y-%m-%d"
    
def reg_user():
    '''Add a new user to the user.txt file'''
    new_username = ""
    while new_username == "":
        # - Request input of a new username
        new_username = input("New Username: ")
        # - Check if the username already exist in user.txt
        # Read in user_data
        with open("user.txt", 'r') as user_file:
            user_data = user_file.read().split("\n")
        # Convert user data to a dictionary
        global username_password
        username_password = {}
        for user in user_data:
            username, password = user.split(';')
            username_password[username] = password
        # Check if the username already exist in user.txt
        if new_username in username_password.keys():
            print("---Username is already exist. (This username is occupied. Please try another one)---")
            new_username = ""
            continue
        else:
            # - Request input of a new password
            new_password = input("New Password: ")
            # - Request input of password confirmation.
            confirm_password = input("Confirm Password: ")
        
            # - Check if the new password and confirmed password are the same.
            if new_password == confirm_password:
                # - If they are the same, add them to the user.txt file,
                print(f"---New user added---\n{"_"*80}")
                username_password[new_username] = new_password
                
                with open("user.txt", "a+") as out_file:
                    user_data = []
                    for k in username_password:
                        user_data.append(f"{k};{username_password[k]}")
                    out_file.write(f"\n{k};{username_password[k]}\n")
                get_user_choice()
            # - Otherwise you present a relevant message.
            else:
               print("---Passwords do no match---")
               new_username = ""
               continue

def add_task():
    '''Allow a user to add a new task to task.txt file
            Prompt a user for the following: 
             - A username of the person whom the task is assigned to,
             - A title of a task,
             - A description of the task and 
             - the due date of the task.'''
    task_username = ""
    while task_username == "":
        task_username = input("Name of person assigned to task: ")
        if task_username not in username_password.keys():
            print("---User does not exist. Please enter a valid username---")
            task_username = ""
            continue
        else:
            task_title = input("Title of Task: ")
            task_description = input("Description of Task: ")
            task_due_date = ""
            while task_due_date == "":
                try:
                    task_due_date = input("Due date of task (YYYY-MM-DD): ")
                    due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                    break
                except ValueError:
                    print("Invalid datetime format. Please use the format specified")
                    task_due_date = ""
                    continue

    # Then get the current date.
    curr_date = date.today()
    ''' Add the data to the file task.txt and
        Include 'No' to indicate if the task is complete.'''
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False,
        "task_id": f"T_{task_username[0:3]}{task_due_date}" }
    
    task_list.append(new_task)
    with open('tasks.txt', 'a+') as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No",
                 t['task_id']
                ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
        print(f"---Task successfully added----.\n{"_"*80}")
    get_user_choice()
    
def view_all():
    '''Reads the task from task.txt file and prints to the console in the 
    format of Output 2 presented in the task pdf (i.e. includes spacing and labelling)'''
    
    for t in task_list:
        disp_str = f"\nTask: \t\t\t {t['title']}\n"
        disp_str += f"Assigned to: \t\t {t['username']}\n"
        disp_str += f"Date Assigned: \t\t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t\t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \t {t['description']}\n"
        disp_str += f"Task ID: \t\t {t['task_id']}"
        print(disp_str)
        print(f"{"_"*80}")
    get_user_choice()

def view_mine():
    '''Reads the task from task.txt file and prints to the console in the 
    format of Output 2 presented in the task pdf (i.e. includes spacing and labelling)'''
    for t in task_list:
        if t['username'] == curr_user:
            disp_str = f"\nTask: \t\t\t {t['title']}\n"
            disp_str += f"Assigned to: \t\t {t['username']}\n"
            disp_str += f"Date Assigned: \t\t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t\t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \t {t['description']}\n"
            disp_str += f"Task ID: \t\t {t['task_id']}"
            print(disp_str)
            print(f"{"_"*80}")
    if len(disp_str) > 1:
        user_opt = ""
        print("""\t1. Edit your tasks
\t2. Return the main menu""")
        while user_opt == "":
            user_opt = input("Enter the number for action above: ")
            if user_opt == "1":
                edit_task()
            elif user_opt == "2":
                get_user_choice()
            else:
                print("---Invalid answer. Please try again.---\n")
                user_opt = ""
                continue

def edit_task():
    '''After view mine function, allow the user to edit their own tasks. 
    After editing task components on task_list variable, finally replace all data in tasks with new data.'''
    edit_id= ""
    task_id_list = []
    for t in task_list:
        task_id_list += {t['task_id']}
    while edit_id == "":
        edit_id = input("Enter the Task ID to edit the task -OR- enter '-1' to return main menu: ")
        if edit_id == "-1":
            get_user_choice()
        elif edit_id not in task_id_list:
            print("---Invalid answer. Please try again.---")
            edit_id = ""
            continue
        else:
            for t in task_list:
                if edit_id == t['task_id']:
                    if t['username'] != curr_user and curr_user != "admin":
                        print("---You can edit only your own tasks.---")
                        edit_id = ""
                        break
                    else: 
                        user_act = ""
                        print("""\t1. Mark the task as 'completed'
\t2. Edit username
\t3. Edit due date""")
                        while user_act == "":
                            user_act = input("Enter the number for action above: ")
                            if user_act not in ["1","2","3"]:
                                print("---Invalid answer. Please try again.---")
                                user_act = ""
                                continue      
                            elif user_act == "1":
                                for t in task_list:
                                    if t['task_id'] == edit_id:
                                        t['completed'] = True
                                        with open('tasks.txt', 'w') as task_file:
                                            task_list_to_write = []
                                            for t in task_list:
                                                str_attrs = [
                                                    t['username'],
                                                    t['title'],
                                                    t['description'],
                                                    t['due_date'].strftime(DATETIME_STRING_FORMAT),
                                                    t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                                                    "Yes" if t['completed'] else "No",
                                                    t['task_id']
                                                    ]
                                                task_list_to_write.append(";".join(str_attrs))
                                            task_file.write("\n".join(task_list_to_write))
                                        print(f"---The task {edit_id} has been marked as completed!---\n{"_"*80}\n")
                                        edit_id = ""
                            elif user_act == "2":
                                task_username_list = []
                                for t in task_list:
                                    task_username_list += {t['username']}
                                for t in task_list:
                                    if t['task_id'] == edit_id and t['completed']:
                                        print(f"---The task {edit_id} has already been marked as completed. Completed task cannot be edited.---")
                                        edit_id = ""
                                    elif t['task_id'] == edit_id and not t['completed']:
                                        task_username = ""
                                        while task_username == "":
                                            task_username = input("Enter name of new person to whom the task will be assigned: ")
                                            if task_username not in task_username_list:
                                                print("---User does not exist. Please enter a valid username---")
                                                task_username = ""
                                                continue
                                            else:
                                                t['username'] = task_username
                                                with open('tasks.txt', 'w') as task_file:
                                                    task_list_to_write = []
                                                    for t in task_list:
                                                        str_attrs = [
                                                            t['username'],
                                                            t['title'],
                                                            t['description'],
                                                            t['due_date'].strftime(DATETIME_STRING_FORMAT),
                                                            t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                                                            "Yes" if t['completed'] else "No",
                                                            t['task_id']
                                                            ]
                                                        task_list_to_write.append(";".join(str_attrs))
                                                    task_file.write("\n".join(task_list_to_write))
                                                print(f"---The task {edit_id} has been assigned to {task_username}!---\n{"_"*80}\n")
                                                edit_id = ""
                            elif user_act == "3":
                                for t in task_list:
                                    if t['completed']:
                                        print(f"---The task {edit_id} has already been marked as completed. Completed task cannot be edited.---")
                                        edit_id = ""
                                    else:
                                        for t in task_list:
                                            if t['task_id'] == edit_id:
                                                task_due_date = ""
                                                while task_due_date == "":
                                                    try:
                                                        task_due_date = input("Enter new due date of task (YYYY-MM-DD): ")
                                                        due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                                                        t['due_date'] = due_date_time
                                                    except ValueError:
                                                        print(f"---Invalid datetime format. Please use the format specified---\n{"_"*80}")
                                                        task_due_date = ""
                                                        continue
                                                    else:
                                                        with open('tasks.txt', 'w') as task_file:
                                                            task_list_to_write = []
                                                            for t in task_list:
                                                                str_attrs = [
                                                                    t['username'],
                                                                    t['title'],
                                                                    t['description'],
                                                                    t['due_date'].strftime(DATETIME_STRING_FORMAT),
                                                                    t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                                                                    "Yes" if t['completed'] else "No",
                                                                    t['task_id']
                                                                    ]
                                                                task_list_to_write.append(";".join(str_attrs))
                                                            task_file.write("\n".join(task_list_to_write))
                                                        print(f"---The task {edit_id} due date has been changed as {task_due_date}!---\n{"_"*80}")
                                                        edit_id = ""
            get_user_choice()
            
def generate_reports():
    '''This code generates two txt files called task_overview.txt and user_overview.txt as output reports.  
    This menu option is available for only admin'''
    if curr_user != 'admin':
        print(f"---You are not allowed to open this section!---\n\n{"_"*80}")
        get_user_choice()
    else:
        # First part of the code is about task_overview report.
        today = datetime.today()
        total_task_num = 0
        completed_tasks = 0
        uncompleted_tasks = 0
        overdue_tasks = 0
        uncomp_overdue_tasks = 0
        
        # Read the last version of tasks.txt file.
        with open('tasks.txt', 'r') as task_file:
            task_data = task_file.read().split("\n")
            task_data = [t for t in task_data if t != ""]
                
        task_list = []
        for t_str in task_data:
            curr_t = {} 
            task_components = t_str.split(";")
            curr_t['username'] = task_components[0]
            curr_t['title'] = task_components[1]
            curr_t['description'] = task_components[2]
            curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
            curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
            curr_t['completed'] = True if task_components[5] == "Yes" else False
            curr_t['task_id'] = task_components[6]
            task_list.append(curr_t)
            
        # Count the task numbers according to final version of tasks.txt file and updated task_list variable. 
        for t in task_list:
            total_task_num += 1
        try:
            if total_task_num < 1:
                raise ZeroDivisionError
        except ZeroDivisionError:
            print(f"""---Task Overview Report cannot be generated because 
there isnot any task that has been generated and tracked using the Task_Manager.---\n{"_"*80}\n""")
            get_user_choice()
        else:
            for t in task_list:
                if t['completed']:
                    completed_tasks += 1
                else:
                    uncompleted_tasks += 1
            for t in task_list:
                if t['due_date'] < today:
                    overdue_tasks += 1
            for t in task_list:
                if not t['completed'] and t['due_date'] < today:
                    uncomp_overdue_tasks += 1  
            # After all for loops are completed, all count process for the variables are also completed.
            # At this point, task report content can be processed.
            task_report_str = f"\nTask Overview Report - {today} \n{"."*80}\n"
            task_report_str += f"Total number of tasks: \t {total_task_num}\n"
            task_report_str += f"Total number of completed tasks: \t {completed_tasks}\n"
            task_report_str += f"Total number of uncompleted tasks: \t {uncompleted_tasks}\n"
            task_report_str += f"The total number of tasks that haven’t been completed and are overdue: \t {uncomp_overdue_tasks}\n"
            task_report_str += f"The percentage of tasks that are incomplete: \t {round(((uncompleted_tasks/total_task_num)*100),2)}%\n"
            task_report_str += f"The percentage of tasks that are overdue \t {round(((overdue_tasks/total_task_num)*100),2)}%\n"
            task_report_str += f"{"_"*80}"

            with open("task_overview.txt", "w") as task_over_report:
                # Write the report content in task_overview.txt file
                task_over_report.write(task_report_str)
            # Write output action on the console for end-user.
            print(task_report_str)
            print(f"\n---The task overview report has been created as 'task_overview.txt'!")
            print(f"Please check the File Folder.---\n{"_"*80}\n{"_"*80}")
                
            # Second part of the code is about user_overview report.
            # Read in user_data
            with open("user.txt", 'r') as user_file:
                user_data = user_file.read().split("\n")  
            # Convert to a dictionary
            username_list = []
            total_user_num = 0
            for user in user_data:
                username, password = user.split(';')
                username_password[username] = password
                username_list.append(username)
                total_user_num += 1
            
            user_report_str = f"\nUser Overview Report - {today} \n{"."*80}\n"
            user_report_str += f"Total number of users: \t {total_user_num}\n"
            user_report_str += f"Total number of tasks: \t {total_task_num}\n"
            print(user_report_str)
            user_report_str_2 = ""
            for useri in username_list:
                user_report_str_2 += f"\n\t User: {useri}\n"
                user_tasks = 0
                for t in task_list:
                    if t['username'] == useri:
                        user_tasks += 1
                user_report_str_2 += f"\t\t Total number of {useri}'s tasks: {user_tasks}\n"
                user_report_str_2 += f"\t\t {round(((user_tasks/total_task_num)*100),2)}% of total tasks have been assigned to {useri}\n"
                if user_tasks < 1 :
                    user_report_str_2 += f"""---Other details for User Overview Report cannot be generated because 
there isnot any task that has been assigned to the user.---\n{"_"*80}\n"""
                    print(user_report_str_2)
                    continue
                else:
                    user_completed = 0
                    for t in task_list:
                        if t['username'] == useri and t['completed'] == True:
                            user_completed += 1
                    user_report_str_2 += f"\t\t {round(((user_completed/user_tasks)*100),2)}% of {useri}'s tasks have been completed.\n"
                    user_prog = 0
                    for t in task_list:
                        if t['username'] == useri and t['due_date'] <= today:
                            user_prog += 1
                    user_report_str_2 += f"\t\t {round(((user_prog/user_tasks)*100),2)}% of {useri}'s tasks must still be completed.\n"
                    user_uncomp_overdue = 0
                    for t in task_list:
                        if t['username'] == useri and t['due_date'] < today and t['completed'] == False:
                            user_uncomp_overdue += 1
                    user_report_str_2 += f"\t\t {round(((user_uncomp_overdue/user_tasks)*100),2)}% of {useri}'s tasks have not yet been completed and are overdue.\n"
                
            print(user_report_str_2)
            print(f"{"_"*80}\n")       
            with open("user_overview.txt", "w") as user_over_report:
                # Write the report content in task_overview.txt file
                user_over_report.write(user_report_str)
                user_over_report.write(user_report_str_2)
                # Write output action on the console for end-user.
            print(f"---The user overview report has been created as 'user_overview.txt'!")
            print(f"Please check the File Folder.---\n{"_"*80}")
            get_user_choice()
                  
def disp_stats():
    '''If the user is an admin they can display statistics about number of users and tasks.'''
    if curr_user == 'admin':
        num_users = len(username_password.keys())
        num_tasks = len(task_list)
    
        print("-----------------------------------")
        print(f"Number of users: \t\t {num_users}")
        print(f"Number of tasks: \t\t {num_tasks}")
        print("-----------------------------------")    
        print(f"\n{"_"*80}")
        get_user_choice()
        
    else:
        print(f"---You are not allowed to open this section!---\n\n{"_"*80}")
        get_user_choice()

def exit():
    clear_screen()
    print("\n---Exiting the Program. Goodbye!!!---\n")
    quit()
    
def clear_screen():
    '''Clear the console screen'''
    os.system("cls||clear")
    
#====Login Section====
logged_in = False

def get_user_choice():
    '''First, present the menu bar to the user. Then, ask user to select menu option.'''
    # presenting the menu to the user
    print("\tr - Registering a user")
    print("\ta - Adding a task")
    print("\tva - View all tasks")
    print("\tvm - View my task")
    print("\tgr - Generate reports")
    print("\tds - Display statistics")
    print("\te - Exit")
    menu = ""
    # getting user's input and
    # making sure that the user input is converted to lower case.
    while menu == "":
        try:
            menu = input("Please enter your choice: ").strip().lower()
            if not menu in ["r", "a", "va", "vm", "gr", "ds", "e"]:
                raise ValueError
        except ValueError:
            print("Invalid choice. Try again")
            menu == ""
            continue
        else:
            if menu == "r":
                reg_user()
            elif menu == "a":
                add_task()
            elif menu == "va":
                view_all()
            elif menu == "vm":
                view_mine()
            elif menu == "gr":
                generate_reports()
            elif menu == "ds":
                disp_stats()
            elif menu == "e":
                exit()

def log_in():
    '''This code runs at the begining of the program and reads usernames and password from the user.txt file to 
    allow a user to login.'''
    # If no user.txt file, write one with a default account
    if not os.path.exists("user.txt"):
        with open("user.txt", "w") as default_file:
            default_file.write("admin;password")
        
    # Read in user_data
    with open("user.txt", 'r') as user_file:
        user_data = user_file.read().split("\n")
        
    # Convert to a dictionary
    global username_password
    username_password = {}
    for user in user_data:
        username, password = user.split(';')
        username_password[username] = password
         
    global curr_user
    global logged_in
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("---User does not exist---")
        logged_in = False
    elif username_password[curr_user] != curr_pass:
        print("---Wrong password---")
        logged_in = False
    else:
        print("---Login Successful!---\n\n===Welcome to Taks Manager===")
        logged_in = True
        # Create tasks.txt if it doesn't exist
        if not os.path.exists("tasks.txt"):
            with open("tasks.txt", "w") as default_file:
                pass
        
        with open("tasks.txt", 'r') as task_file:
            task_data = task_file.read().split("\n")
            task_data = [t for t in task_data if t != ""]
            
        global task_list    
        task_list = []
        for t_str in task_data:
            curr_t = {} 
            # Split by semicolon and manually add each component
            task_components = t_str.split(";")
            curr_t['username'] = task_components[0]
            curr_t['title'] = task_components[1]
            curr_t['description'] = task_components[2]
            curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
            curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
            curr_t['completed'] = True if task_components[5] == "Yes" else False
            curr_t['task_id'] = task_components[6]
            task_list.append(curr_t)
        get_user_choice()
        
while not logged_in:
    print("===LOGIN TASK MANAGER===")
    log_in()