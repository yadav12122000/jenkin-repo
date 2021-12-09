import subprocess
print("Hello jenkins")
print(subprocess.getoutput("date"))
print("cal is :")
print(subprocess.getoutput("cal 2021"))

