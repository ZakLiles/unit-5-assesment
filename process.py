log_file = open("um-server-01.txt") #opens file for reading in text mode

#creates sales_reports() function taking in one file input
def sales_reports(log_file):
    for line in log_file: # iterates over every line in file
        line = line.rstrip() # removes whitespaces at end of each line
        day = line[0:3] # day is equal to first three characters of the line (Mon, Tue, Wed etc.)
        if day == "Mon": # check if day is tuesday
            print(line) # prints all lines from tuesdays
    log_file.seek(0)


sales_reports(log_file) # calls sales_reports function on log file

def ten_melons(log_file):
    for line in log_file:
        line = line.rstrip()
        line_arr = line.split(' ')
        quantity = int(line_arr[2])
        items = line_arr[3:-1]
        if any('melon' in ele for ele in items) and quantity >= 10:
            print(line)

ten_melons(log_file)