import os
import datetime

#command = "df-h"
#command = "uptime"
#command = "date"


# def check_cpu(command): #defining a function
#     print(os.system(command))
# check_cpu("df -h") # calling a function

# def check_date(command):
#     return(os.system(command))     
# check_date("date")


# def check_RAM(command):
#     print(os.system(command))     
# check_RAM("free -h")


# def check_uptime(command):
#     print(os.system(command))     
# check_uptime("uptime")

# def run_command(command):
#     return os.system(command)

# run_command("df -h")
# run_command("date")
# run_command("free -h")


def show_date():
    return datetime.datetime.today()

today = show_date()
print(today)