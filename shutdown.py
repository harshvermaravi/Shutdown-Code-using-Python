import os
shutdown = input("Dear, Er. Harsh Verma Do you wish to shutdown your computer ?(Yes/No):")
if shutdown == 'no':
    exit()
else:
    os.system("shutdown /s /t 1") 
