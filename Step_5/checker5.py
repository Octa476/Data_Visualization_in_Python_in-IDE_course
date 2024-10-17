import subprocess

cmd_sol = subprocess.run(["python3", "solution5.py"], capture_output=True)
stdout_sol = cmd_sol.stdout.decode()

cmd_task = subprocess.run(["python3", "task5.py"], capture_output=True)
stdout_task = cmd_task.stdout.decode()

CRED    = '\33[31m'
CGREEN  = '\33[32m'
if stdout_sol == stdout_task:
    print(CGREEN + 'Task passed!' + CGREEN)
else:
    print(CRED + 'Task failed!' + CRED)