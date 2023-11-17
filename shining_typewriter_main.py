
# The Shining v 0.0.1 
# study case 
import time

# techincal vars
intro = "*** Welcome to \"The Shining\" typewriter simulator ***"
version_number = "0.0.1" 
current_version = "*** The current version is " + version_number + " ***\n"

# main vars
message = "All work and no play makes Jack a dull boy. \n"

# body

print(intro) #вывод приветствия из technical_vars
time.sleep(2) # Эмуляция загрузки
print(current_version)
print("*" * 53)
time.sleep(2) # Эмуляция загрузки
print("*** loading ***")
time.sleep(3) # Эмуляция загрузки
input_count = int(input("Enter the number of text repeats. "))
print (message * input_count)