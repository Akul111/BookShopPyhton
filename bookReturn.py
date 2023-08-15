from datetime import date
import databse

def mainReturn(root, returnID):
    open_log_file = open("logfile.txt", "r+")
    for log_record in open_log_file:
        log_record_list = log_record.split("-")

        if log_record_list[0] == returnID and log_record_list[4] =="":

            open_log_file_read = open("logfile.txt", "r")
            lines = open_log_file_read.readlines()
            open_log_file_write = open("logfile.txt", "w")
            for records in lines:
                if records.strip() != log_record.strip():
                    open_log_file_write.write(records)
                elif records.strip() == log_record.strip():
                    open_log_file_write.write(log_record.replace("---", "-" +str(date.today()).replace("-","/")+ "--\n"))
            open_log_file_write.close()
            open_log_file_read.close()

        elif log_record_list[0] == returnID and log_record_list[4]=="res":

            open_log_file_read = open("logfile.txt", "r")
            lines = open_log_file_read.readlines()
            open_log_file_write = open("logfile.txt", "w")
            for records in lines:
                if records.strip() != log_record.strip():
                    open_log_file_write.write(records)
                elif records.strip() == log_record.strip():
                    open_log_file_write.write(log_record.replace("--res-"+log_record_list[5], "-" + str(date.today()).replace("-", "/") + "--\n")) #.readlines puts it in an array add the reserved book at end of array
                    lines.append(returnID+"-"+log_record_list[5].strip()+"-"+str(date.today()).replace("-","/")+"---\n")
            open_log_file_write.close()
            open_log_file_read.close()
            break
    try:
        int(returnID)
        databse.console(root, "returned book")
    except:
        databse.console(root, "please enter a bookID")
    open_log_file.close()
