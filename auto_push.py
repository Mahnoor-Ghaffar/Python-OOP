# import os
# import time
# from datetime import datetime

# while True:
#     os.system("git add .")
#     os.system(f'git commit -m "Auto commit: {datetime.now()}"')
#     os.system("git push origin master")  # ya 'master' agar repo ka branch master ho
#     print("Code auto pushed! ✅")
#     time.sleep(300)  # wait 5 minutes




# Input every time (if running interactively)
import os
import time
from datetime import datetime

while True:
    commit_msg = input("\nEnter your commit message (or type 'exit' to stop): ")

    if commit_msg.lower() == 'exit':
        print("Stopped auto push loop.")
        break

    os.system("git add .")
    os.system(f'git commit -m "{commit_msg} - {datetime.now()}"')
    os.system("git push origin master")
    print("Code auto pushed! ✅")
    time.sleep(100)  # wait 5 minutes
