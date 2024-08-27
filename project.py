import csv
import sys
import tabulate
import random

def main():
    while True:
        main_tab = ["1. Set a Goal",
                    "2. Progress",
                    "3. Add to list",
                    "4. Chapter Completion",
                    "5. Goal Reset",
                    "6. Clear",
                    '7. Exit']
        try:
            print()
            print("how do you want to proceed?")
            for main_t in main_tab:
                print(main_t)
            print()
            answer = input("Choose your option: ")
            if int(answer) == 1:
                set_goal()

            elif int(answer) == 2:

                if number_of_lines("Goal.txt") == 0:
                    print("To proceed further, Please set a GOAL.")
                elif (number_of_lines("Records.csv") - 1) == 0:
                    print("To proceed further, Please set a Chapters.")
                else:
                    progress()

            elif int(answer) == 3:
                add()

            elif int(answer) == 4:
                delete()

            elif int(answer) == 5:
                clear("Goal.txt")
                print()
                print("GOAL HAS BEEN SUCCESSFULLY RESET")
                print()

            elif int(answer) == 6:
                clear("Goal.txt")
                clear("Records.csv")
                print()
                print("LIST HAS BEEN SUCCESSFULLY FORMATTED")
                print()

            elif int(answer) == 7:
                sys.exit("Adios Amigos!")

            else:
                print()
                print("⚠️ Option does not exist")
                print()

        except ValueError:

            print()
            print("⚠️","Please Input the corresponding number.")
            print()




def number_of_lines(file):
    n = 0
    with open(file, "r") as lines:
        for _ in lines:
            n += 1
    return n



def set_goal():
    print()
    print("Goal: Maximum number of chapters that can be added")
    print()
    while True:
        try:
            goal = int(input("Goal: "))
            if goal < (number_of_lines("Records.csv") - 1):
                print(f"Input a greater Integer than {number_of_lines("Records.csv")}")
                continue
            else:
                break
        except ValueError:
            print("Input an INTEGER")
            continue
    with open("Goal.txt",'w') as file:
        file.write(str(goal))



def goal():
    with open("Goal.txt","r") as line:
        for i in line:
            return int(i)


def add():
    if number_of_lines("Goal.txt") == 0:
        print()
        print("PLEASE SET A GOAL TO ADD CHAPTERS")
        print()
    else:
        n = 0
        with open("Records.csv","r") as file:
            for _ in file:
                n += 1
        file = open("Records.csv","a")
        writer = csv.DictWriter(file,fieldnames=["Sno","task"])

        if n == 0:
            writer.writeheader()
            n = 0
        else:
            n = n - 1

        while True:
            if n == goal():
                print("Maximum limit of chapters reached")
                break
            n += 1
            task = input("What's the Chapter? : ")
            if task == "":
                print("Invalid Input")
                break

            else:
                writer.writerow({"Sno":n,"task": task})
                print()
                print("TASK SUCCESSFULLY ADDED")
                print()

                ans1 = (input("Would you like to continue? (Y/N)")).casefold()

                if ans1 == "y":
                    continue
                elif ans1 == "n":
                    file.close()
                    break


def clear(file):
    x = open(file,"w")
    x.close



def delete():

    if (number_of_lines("Records.csv") - 1) == 0:
        print()
        print("Kindly Add Chapters to use this feature")
        print()
    else:
        temp = []
        temp2 = []
        Display = []
        #creates a list for displaying the chapters using tabulate
        with open("Records.csv","r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                Display.append({"Serial Number": row["Sno"],"Chapter": row["task"]})
        #creates list of the names of chapters in csv file
        for name in Display:
            temp.append(name["Chapter"])

        print(tabulate.tabulate(Display, headers= 'keys', tablefmt="double_grid"))

        #Asks for number of the chapter to be removed
        x = int(input("Which Chapter have you finished?: "))
        x = x - 1
        #Creates final list for putting back into csv file
        for index,value in enumerate(temp):
            if index != x:
                temp2.append(value)
        #Creates a fresh csv file with the removed chapter
        file = open("Records.csv","w")
        writer = csv.DictWriter(file,fieldnames=["Sno","task"])
        writer.writeheader()
        n = 0
        for word in temp2:
            n += 1
            writer.writerow({"Sno": n, "task": word})
        file.close()

        if (number_of_lines("Records.csv") - 1) == 0:
            clear("Goal.txt")
            print()
            print("CONGRATULATIONS, U HAVE SUCCESSFULLY COMPLETED ALL THE CHAPTERS! keep hustling champ ;)")
            print()
        else:
            print()
            print("CONGO! keep going Champ :) !!")



def progress():
    with open("Goal.txt","r") as g:
        for i in g:
            goal = i
    goal = int(goal)
    number = (number_of_lines("Records.csv")) - 1

    display = []

    with open("Records.csv","r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            display.append({"Serial Number": row["Sno"],"Chapter": row["task"]})

    print()
    print(tabulate.tabulate(display, headers="keys", tablefmt="heavy_grid"))
    print()

    #Maths
    div = number / goal
    percent = int(div * 100)
    percent = 100 - percent
    com = goal - number
    percentage = f"{percent}%"

    print(f"CHAPTERS COMPLETED: {com}")
    print()

    print(f"CHAPTERS REMAINING: {number}")
    print()

    print(f"PROGRESS: {percentage}")
    print()

    with open("quotes.txt","r") as line:
        temp = []
        for lines in line:
            temp.append(lines)
        numb = random.randint(0,2)
        print(temp[numb])




if __name__=="__main__":
    main()

