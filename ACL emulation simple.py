from time import sleep
from tabulate import tabulate
import pandas as pd

# This program is meant for emulating Access Control System for the trainings purpose, not to be used for commercial
# activity.
class UserData:
    # Objectify data
    def __init__(self, user_name, emp_id, dept_name, line_manager, status, premise_access):
        self.user_name = user_name
        self.emp_id = emp_id
        self.dept_name = dept_name
        self.line_manager = line_manager
        self.status = status
        self.premise_access = premise_access

    # This function returns per user info based on employee id
    def user_info(self, emp_id):
        return "\nUser: " + self.user_name.title() + "\nEmployee Id: " + str(self.emp_id) + "\nDepartment: " + \
               self.dept_name.upper() + "\nLine Manager: " + self.line_manager.title() + "\nStatus: " + \
               self.status.title() + "\nPremise access:" + ",".join(self.premise_access)


def main():
    choice = [1, 2, 3, 4, 5]
    user_db = []
    empid_db = []
    premises_db = []
    dept_db = []
    linemgr_db = []
    status = ['Active', 'Inactive']
    while True:
        print("\nWelcome to ACL emulation.\n\n1.Enter new user\n2.Enter new premise\n3.Activate access\n4.Deactivate "
              "access\n5.Search employee")
        choose_option = int(input("\nSelect the above options: "))
        if choose_option == 1:
            user_name1 = input('Username:')
            emp_id1 = int(input('Employee id:'))
            if emp_id1 in empid_db:
                print("Duplicated employee id found!")
                sleep(2)
                continue
            dept_name1 = input('Department name:')
            line_manager1 = input('Line manager: ')
            status1 = input('Active/Inactive:')
            premise_access1 = []
            new_employee = UserData(user_name1.lower(), emp_id1, dept_name1.lower(), line_manager1.lower(),
                                    status1.lower(), premise_access1)
            user_db.append(new_employee)
            empid_db.append(emp_id1)
            print('A new user record has been created successfully!')
            print(new_employee.user_info(empid_db))
        elif choose_option == 2:
            new_room = input("Enter new room name:")
            if new_room not in premises_db:
                premises_db.append(new_room.lower())
        elif choose_option == 3:
            emp_id1 = int(input('Employee id to be activated:'))
            if emp_id1 not in empid_db:
                print("Employee id not found!")
                sleep(2)
                continue
            for x in user_db:
                if x.emp_id == emp_id1:
                    x.status = 'Active'
                    print("User {} has been activated.".format(x.user_name))
                    premise_access2 = input("Enter room name to provide access:")
                    while premise_access2 not in premises_db:
                        premise_access2 = input("Enter a valid room name to provide access:")
                    x.premise_access.append(premise_access2)
                    print("{} is provided access to {}.".format(emp_id1, premise_access2))
                else:
                    pass
        elif choose_option == 4:
            emp_id1 = int(input('Employee id to be deactivated:'))
            if emp_id1 not in empid_db:
                print("Employee id not found!")
                sleep(2)
                continue
            for x in user_db:
                if x.emp_id == emp_id1:
                    x.status = 'Inactive'
                    x.premise_access = []
                    print("User {} has been deactivated and revoked all accesses.".format(x.user_name))
                else:
                    pass
        elif choose_option == 5:
            temp_search_users = []
            temp_search_empid = []
            temp_search_dept = []
            temp_search_lnmgr = []
            temp_search_status = []
            temp_search_access = []
            search_something = input('Enter user name / employee id:')
            if len(user_db) == 0:
                print('\nNo user records available yet!')
            for x in user_db:
                if str(x.emp_id) == search_something or search_something.lower() in x.user_name:
                    temp_emp_id = x.emp_id
                    temp_search_users.append(x.user_name.title())
                    temp_search_empid.append(x.emp_id)
                    temp_search_dept.append(x.dept_name.upper())
                    temp_search_lnmgr.append(x.line_manager.title())
                    temp_search_status.append(x.status.title())
                    temp_search_access.append(",".join(x.premise_access))
                else:
                    pass
            if len(temp_search_users) == 0:
                print('User does not exist!')
            data = {'Users': temp_search_users, 'Employee id': temp_search_empid, 'Department': temp_search_dept,
                    'Line Manager': temp_search_lnmgr, 'Status': temp_search_status, "Accesses": temp_search_access}
            outputit = pd.DataFrame(data)
            print(tabulate(outputit, headers='keys', tablefmt='psql'))
        else:
            continue


main()
