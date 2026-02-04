# Takes threshold values (CPU, disk, memory) from user input
#Also fetches system metrics using a Python library (example: psutil)
#Compares metrics against thresholds
#Prints the result to the terminal

import psutil

def health_check_fun():
    cpu_thresheold = int (input("Enter the cpu threshould: "))
    disk_thresheold = int (input("Enter the disk threshold: "))
    mem_threshoeld = int (input("Enter the memory threshoeld: "))

    cpu_curr = psutil.cpu_percent(interval=1)
    disk_curr = psutil.disk_usage('/').percent
    mem_curr = psutil.virtual_memory().percent

    print("cpu current %: ",cpu_curr)
    print("disk usage%: ",disk_curr)
    print("memory current %: ",mem_curr)

    if cpu_curr >= cpu_thresheold:
        print("cpu reaches threshold")

    if disk_curr >= disk_thresheold:
        print("disk threshould reached ")

    if mem_curr >= mem_threshoeld:
        print("memory threshould reached")

# function calling 
health_check_fun()


