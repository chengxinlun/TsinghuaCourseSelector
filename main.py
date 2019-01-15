# Main execution point for course selector
# All information are transfered through config files
# All courses information are in ./course
# Account information in ./profile.conf
# All config files follow json format


# Import modules
import os
import json
import glob
import warnings
import cource_selector as csl


warnings.simplefilter("ignore")
# Read jsons from ./course
conf_list = glob.glob("course/*.conf")
# Load username and password
try:
    f = open("profile.conf")
except Exception as reason:
    print("profile.conf failed to open: " + str(reason))
    os._exit(0)
try:
    up = json.load(f)
except Exception as reason:
    print("profile.conf failed to load: " + str(reason))
    os._exit(0)
finally:
    f.close()
    print("Profile loaded. Correctness will NOT be checked")
# Load in each one and output invalid ones
course_list = []
for each in conf_list:
    try:
        f = open(each)
    except Exception as reason:
        print(each + " failed to open: " + str(reason))
        continue
    try:
        temp = json.load(f)
        course_list.append(temp)
    except Exception as reason:
        print(each + " failed to load: " + str(reason))
    finally:
        f.close()
# Construct all the classes for selection
# TO DO: asynchronize the process
for each in course_list:
    csl.XuanKe(each["sem"], each["cc"], each["cn"], each["cs"], up["user"],
               up["pswd"]).main_process()
