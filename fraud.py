input_one = ["Alice;START", 
                    "Bob;START", 
                    "Bob;1", 
                    "Carson;START", 
                    "Alice;15", 
                    "Carson;6", 
                    "David;START", 
                    "David;24", 
                    "Evil;START", 
                    "Evil;24",
                    "Evil;START", 
                    "Evil;18"]

input_two = ["Tom;START", 
                "Jeremy;START", 
                "Dana;START", 
                "Jeremy;4", 
                "Dana;2",
                "James;START", 
                "Leah;START", 
                "James;5", 
                "Nick;START", 
                "Tom;1", 
                "Nick;6", 
                "Leah;3"]

input_three = ["Nick;START",
                "Jeremy;START",
                "Leah;START",
                "Nick;10",
                "Jeremy;START",
                "Jeremy;START",
                "Leah;15",
                "Jeremy;8,14,9"]

def processInvoice(data_structures, more_details):
    ans, details, seen = data_structures
    employee, highest_invoice, line = more_details
    if details[0] == 'START':
        seen[employee] = line, highest_invoice
    else:
        for invoice in details:
            if int(invoice) < seen[employee][1]:
                ans.append("{};{};{}".format(line,employee, 'SUSPICIOUS_BATCH' if len(details) > 1 else  'SHORTENED_JOB'))
                break
            else:
                highest_invoice = int(invoice) if highest_invoice <  int(invoice) else highest_invoice
    return highest_invoice 

def detectFraud(array):
    seen = {}
    ans = []
    highest_invoice = 0
    for line in range(0, len(array)):
        event = array[line].split(';')
        employee = event[0]
        details = event[1].split(',')
        if employee not in seen:
            seen[employee] = line, highest_invoice
        else:
            highest_invoice = processInvoice((ans,details,seen), (employee,highest_invoice,line))
    return ans

print(detectFraud(input_one))
print(detectFraud(input_two))
print(detectFraud(input_three))




