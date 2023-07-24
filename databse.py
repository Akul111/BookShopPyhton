#Student ID -> F213667

from tkinter import *
import bookCheckout


def console(root,toInsert):
    outputBox = Text(root, bg="black",width=110,height=10)
    outputBox.grid(row=1,column=0)

    if toInsert != "":
        outputBox.insert(0.0,toInsert)

def memberButton(chosen_book_ID,checkoutFrame,root):
    enterMemberId = Label(checkoutFrame, text="Member ID:")
    memberidBar = Entry(checkoutFrame, bg="black")
    memberidButton = Button(checkoutFrame, text="checkout",
                            command=lambda: bookCheckout.bookId_check(chosen_book_ID,memberidBar.get(), root,checkoutFrame))

    memberidButton.grid(row=4, column=1)
    memberidBar.grid(row=2, column=2)
    enterMemberId.grid(row=2, column=0)

def createButton(checkoutFrame, log_record, root, memberID):
    memberidButton = Button(checkoutFrame, text="reserve", command=lambda: bookCheckout.reservation(log_record, root, memberID))
    memberidButton.grid(row=4, column=2)
