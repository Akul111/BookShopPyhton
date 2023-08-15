import bookSelect
from bookSearch import book_search
import databse
import bookReturn
from tkinter import *

root = Tk()
root.title("Library Management")

mainMenuFrame = Frame(root, bg="red")






checkoutButton = Button(mainMenuFrame, text="Checkout Book", padx=35, pady=35, command=lambda: checkoutFrame.tkraise())
returnButton = Button(mainMenuFrame, text="Return Book", padx=44, pady=35, command=lambda: returnBookFrame.tkraise())
selectButton = Button(mainMenuFrame, text="Books Recommendation", padx=8, pady=35, command=lambda: selectFrame.tkraise())

databse.console(root,"")

checkoutButton.pack(padx=275, pady=(50,10))
returnButton.pack(padx=275 )
selectButton.pack(padx=275, pady=(10,50))
mainMenuFrame.grid(row=0, column=0, sticky="nsew")










checkoutFrame = Frame(root)


returnButton = Button(checkoutFrame, text="Return Book", padx=44, pady=10, command=lambda: returnBookFrame.tkraise())
selectButton = Button(checkoutFrame, text="Books Recommendation", padx=8, pady=10, command=lambda: selectFrame.tkraise())

enterBookLabel = Label(checkoutFrame, text="Book Title:")
searchBar = Entry(checkoutFrame, bg="black")
searchButton = Button(checkoutFrame, text="Search", command=lambda: book_search(searchBar.get(),checkoutFrame,root))

try:
    databse.memberButton("",checkoutFrame,root)
except:
    pass

try:
    databse.createButton(checkoutFrame, [], root, 0)
except:
    pass

searchButton.grid(row=1,column=3, pady=100)
enterBookLabel.grid(row=1, column=0, pady=100)
searchBar.grid(row=1, column=2)
returnButton.grid(row=0, column=0)
selectButton.grid(row=0, column=1)
checkoutFrame.grid(row=0, column=0, sticky="nsew")







returnBookFrame = Frame(root)


checkoutButton = Button(returnBookFrame, text="Checkout Book", padx=35, pady=10, command=lambda: checkoutFrame.tkraise())
selectButton = Button(returnBookFrame, text="Books Recommendation", padx=8, pady=10, command=lambda: selectFrame.tkraise())

returnBar = Entry(returnBookFrame, bg="black")
returnBar.grid(row=3,column=2)
returnButton = Button(returnBookFrame, text="return",command=lambda: bookReturn.mainReturn(root, returnBar.get()))
returnButton.grid(row=3, column=3)

checkoutButton.grid(row=0, column=0)
selectButton.grid(row=0, column=1)
returnBookFrame.grid(row=0, column=0, sticky="nsew")






selectFrame = Frame(root)


checkoutButton = Button(selectFrame, text="Checkout Book", padx=35, pady=10, command=lambda: checkoutFrame.tkraise())
returnButton = Button(selectFrame, text="Return Book", padx=44, pady=10, command=lambda: returnBookFrame.tkraise())

generateButton = Button(selectFrame, text="Generate",width=15, command= bookSelect.creatingGraph)


selectFrame.grid(row=0, column=0, sticky="nsew")
checkoutButton.grid(row=0, column=0)
returnButton.grid(row=0, column=1)
generateButton.grid(row=1, column=0)

mainMenuFrame.tkraise()
root.resizable(False,False)
root.mainloop()





def menus():
    process = int(input("1) Would you like to checkout a book?\n2)Would you like to return a book?\n"
                        "3)Enter a new book purchase"))
    if process == 1:
        book_search()

    elif process == 2:
        bookReturn.mainReturn()

    elif process == 3:
        addingBooks()


def addingBooks():
    genre = input("Genre:")
    title = input("Title:")
    author = input("Author:")
    purchasePrice = input("Purchase price £:")
    purchaseDate = input("Purchase Date:")

    open_book_file = open("Book_Info.txt", "r")
    isEmpyt = open_book_file.readline()
    try:
        lastLine = open_book_file.readlines()[-1]
        lastLineStriped = lastLine.strip()
    except:
        isEmpyt = ""
    open_book_file.close()

    open_book_file = open("Book_Info.txt", "a")
    if isEmpyt == "":
        open_book_file.write("1-" + genre + "-" + title + "-" + author + "-" + purchasePrice + "-" + purchaseDate)
    else:
        last_line_list = lastLineStriped.split("-")
        book_id = int(last_line_list[0]) + 1
        open_book_file.write(
            str(book_id) + "-" + genre + "-" + title + "-" + author + "-" + purchasePrice + "-" + purchaseDate + "\n")
    menus()


#menus()
