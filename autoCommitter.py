import os

fileName = str(input("File(s) to be committed [* for all files]: "))
commitMessage = str(input("Message for the commit [Null = [Uploaded with autoCommit]]: "))

def commit():
    try:
            if fileName == '*':
                os.system('git add *')
            else:
                os.system('git add "' + fileName + '"')

            if commitMessage == "":
                os.system('git commit -m "[Uploaded with autoCommit]"')
            else:
                os.system('git commit -m "' + commitMessage + '"')

            os.system('git push')
            print("File(s) successfully committed and pushed to repo!")
    except:
            print("Something went wrong!")

if __name__ == '__main__':
        commit()
