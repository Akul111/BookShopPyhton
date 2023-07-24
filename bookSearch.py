#Student ID ->
#F213667

import databse
from tkinter import *

def availablity(available,record_list,bookOptions):

    if available == True:

        bookOptions.append(record_list[0] + "| " + record_list[1] + " | " + record_list[2] + " | " + record_list[3] + " | Available")
        return bookOptions

       # print(record_list[0], "|", record_list[1], "|", record_list[2],  "|", record_list[3], "| Available")
    elif available == False:
        bookOptions.append(record_list[0] + "| " + record_list[1] + " | " + record_list[2] + " | " + record_list[3] + " | Not Available")
        return bookOptions
        #print(record_list[0], "|", record_list[1], "|", record_list[2], "|", record_list[3], "| Not Available")


def inFile(bookid):
    open_log_file = open("logfile.txt", "r")
    available2 = False
    for log_record in open_log_file:
        log_record_list = log_record.split("-")
        if bookid !=log_record_list[0]:
            available2 = True
        else:
            available2 = False
            return available2

    return available2


def dropDownMenu(checkoutFrame, dropDownBarList,root):
    selected = StringVar()
    selected.set(dropDownBarList[0])


    drop = OptionMenu(checkoutFrame, selected, *dropDownBarList)
    drop.grid(row=3, column=0, columnspan=3,)


    confirmButton = Button(checkoutFrame, text="confirm",
                           command=lambda: (databse.memberButton(selected.get().split("|")[0],checkoutFrame,root)))
    confirmButton.grid(row=3, column=3)


def book_search(search_criteria, checkoutFrame,root):

    match = False
    dropDownBarList = []

    lower_search_criteria = search_criteria.lower()
    open_book_file = open("Book_Info.txt", "r")
    for book_record in open_book_file:
        record_list = book_record.split("-")
        title = record_list[2].lower()

        try:
            for i in range(0, len(title)):
                if lower_search_criteria[i] == title[i]:
                    match = True

                else:
                    match = False

                if match == True and i == len(lower_search_criteria) - 1:
                    open_log_file = open("logfile.txt", "r")
                    reversedFileArray = reversed(open_log_file.readlines())

                    for log_record in reversedFileArray:
                        available = True
                        log_record_list = log_record.split("-")
                        if inFile(record_list[0]):
                            dropDownBarList = availablity(available, record_list, dropDownBarList)
                            break
                        elif log_record_list[0] == record_list[0]:
                            if len(log_record_list[3]) == 0 or log_record_list[4] == "res":
                                available= False
                                dropDownBarList = availablity(available, record_list, dropDownBarList)
                                break

                            elif len(log_record_list[3]) != 0 or log_record_list[4] == "":
                                dropDownBarList = availablity(available, record_list, dropDownBarList)
                                break







        except IndexError:
            pass

    dropDownMenu(checkoutFrame, dropDownBarList,root)

    open_book_file.close()
    open_log_file.close()
    #bookCheckout.main_checkout()