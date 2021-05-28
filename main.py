class AuthSystem:
    def __init__(self, user_name):
        self.user_name = user_name
        self.role = self.get_role()
        self.access = self.get_access()

    def get_access(self):
        if not collect_user_name:
            access_list = "Read \n Write \n Delete \n"
        if self.role == "Admin":
            access_list = "Read \n Write \n Delete \n"
        else:
            access_list = "Read \n Write"
        return access_list

    def get_role(self):
        if not collect_user_name:
            role = "Admin"
        else:
            role = input("Enter your role, \n Admin \n User \n")
        return role


collect_user_name = {}


def get_user():
    value = int(input("press 1 to for login as another user \n Press 2 for create user \n  "
                      "press 3 for edit role \n press 4 to exit \n \n"))
    obj_list = []
    try:
        if value == 1 or value == 2 or value == 3 or value ==4:
            if value == 2:
                new_name = input("Enter your name \n")
                obj2 = AuthSystem(new_name)
                print("Hi, {} you are a {} and you have access to {}".format(obj2.user_name, obj2.role, obj2.access))
                obj_list.append(obj2)
                collect_user_name[new_name] = obj2
            elif value == 1:
                login_name = input("Enter your name \n")
                if login_name in collect_user_name:
                    print(collect_user_name[login_name])
                else:
                    print("This user is not registered \n \n")
            elif value == 3:
                get_name_to_edit = input("Enter your name \n")
                if get_name_to_edit in collect_user_name:
                    print(collect_user_name[get_name_to_edit])
                    obj3 = AuthSystem(get_name_to_edit)
                    print("Hi, {} you are a {} and you have access to {}".format(obj3.user_name, obj3.role, obj3.access))

            elif value == 4:
                return
            else:
                raise Exception

        get_user()

    except Exception as e:
        print("Enter no only as 1,2,3,4", e)


print("Hi! Welcome to Telnet, You are the first user in our System. Please register as Admin to initiate the system")
Name = input("Enter your name \n")
obj1 = AuthSystem(Name)
print("Hi, {} you are a {} and you have access to {}".format(obj1.user_name, obj1.role, obj1.access))
collect_user_name[Name] = obj1
get_user()
