import os

fileName = str(input("File to be committed [* for all files]: "))
commitMessage = str(input("Message for the commit [Leave blank for null]: "))


try:
        if fileName == '*':
            os.system('git add *')
        else:
            os.system('git add "' + fileName + '"')

        os.system('git commit -m "' + commitMessage + '"')
        os.system('git push')
        print("File successfully committed and pushed to repo!")
except:
        print("Something went wrong!")
