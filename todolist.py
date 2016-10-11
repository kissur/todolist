userinput = input("Enter an operation(add, list, mark, archive): ")

if userinput == "list":
    todolist = open("todolist.txt", "r")
    list = todolist.read()
    print(list)


if userinput == "add":
    newitem = input("Add an item: ")
    todolist = open("todolist.txt" , "a+")
    with open("todolist.txt") as a:
        b = a.readlines()
        if len(b) == 0:
            todolist.writelines ("1."+"[ ] " + (newitem) + "\n")
        else:
            todolist.writelines (str(len(b)+1)+"."+"[ ] " + (newitem) + "\n")


if userinput == "mark":
    print ("You saved the following todo items: ")
    with open("todolist.txt") as fobj:
            print (fobj.read())
            
    print ("Which one you want to mark as completed?" )
    line_int = int(input())
    with open("todolist.txt") as f:
        tasks = f.readlines()
     
    onetask = tasks [line_int-1]

    def mark(lenght):
        global onetask
        if onetask[lenght] == " ":
            a = onetask[:lenght-1]
            b = onetask[lenght+1:]
            onetask = (a+"X"+b)
            return onetask

    if len(tasks)>9:
        mark(4)
    else:
        mark(3)

    
    tasks[line_int-1] = onetask
    
    f = open("todolist.txt", "w")
    s = 1
    if len(tasks)>9:
        for i in tasks:
            lines = str(s) + "." + i[4:]
            f.write(lines)
            s += 1
        f.close()
        f = open("todolist.txt", "r")
        print (f.read())
    else:
        for i in tasks:
            lines = str(s) + "." + i[3:]
            f.write(lines)
            s += 1
        f.close()
        f = open("todolist.txt", "r")
        print (f.read())

if userinput == "archive":
    with open("todolist.txt","r+") as f:
        text_in_file = f.readlines()
        i=0
        print(text_in_file)
        while i < len(text_in_file):
            
            print(i,len(text_in_file))
            if "[X]" in text_in_file[i]:
                text_in_file.remove(text_in_file[i])
                i += 0
                continue
            else:
                i += 1
    with open ("todolist.txt","w") as f:
        s = 1
        for i in text_in_file:
            lines = str(s) + "." + i[2:]
            f.write(lines)
            s += 1    


        f.truncate()


            




