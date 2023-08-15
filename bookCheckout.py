from datetime import date
import databse
from tkinter import *



def reservation(log_record, root, memberID):
    try:
        if log_record != []:
            open_log_file_read = open("logfile.txt", "r")
            lines = open_log_file_read.readlines()
            open_log_file_write = open("logfile.txt", "w")
            for records in lines:
                if records.strip() != log_record.strip():
                    open_log_file_write.write(records)
                elif records.strip() == log_record.strip():
                    open_log_file_write.write(log_record.strip().replace("---", "--res-" + str(memberID) + "\n"))
                    databse.console(root, "Book has been reserved successfully")
        open_log_file_write.close()
        open_log_file_read.close()
    except:
        pass



def availablity(chosen_book_ID,memberID,root,checkoutFrame):

    available = True

    open_log_file = open("logfile.txt", "r+")
    for log_record in open_log_file:
        log_record_list = log_record.split("-")
        if log_record_list[0] == str(chosen_book_ID) and len(log_record_list[3]) == 0 and log_record_list[4] == "":
            databse.console(root,"This Book is currently on loan, would you like to reserve this book?")
            available= False
            databse.createButton(checkoutFrame,log_record,root,memberID)
            break
        elif log_record_list[0] == str(chosen_book_ID) and log_record_list[4]=="res":
            databse.console(root,"Sorry this book is out on loan and has already been reserved by someonelse please choose another copy of the book if availble or another book.")
            available = False
            break

        elif log_record_list[0] == str(chosen_book_ID) and len(log_record_list[3]) != 0:
            available = True
        elif log_record_list[0] == str(chosen_book_ID) and len(log_record_list[3]) == 0:
            available = False
    if available == True:
        open_log_file.write(str(chosen_book_ID)+"-"+str(memberID)+"-"+str(date.today()).replace("-","/")+"---\n")
        databse.console(root,"Book has been check out successfully")


    open_log_file.close()




def bookId_check(chosen_book_ID,memberID,root,checkoutFrame):

    try:
        integerMemberID = int(memberID)
    except:
        databse.console(root, "This is an invalid input")

    try:
        if integerMemberID >= 1000 and integerMemberID <= 9999 and chosen_book_ID != "":
            availablity(chosen_book_ID, integerMemberID, root,checkoutFrame)

        elif integerMemberID >= 1000 and integerMemberID <= 9999 and chosen_book_ID == "":
            databse.console(root, "Please select a book first")

        else:
            databse.console(root, "This is an invalid memberID please enter a valid memberID")
    except:
        pass


def authentication(memberID):
    if memberID >= 1000 and memberID <=9999 :
        return True
    else:
        return False






