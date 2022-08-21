file=open('sp500.csv', 'r', encoding="ISO-8859-1")

def get_securities(file,sector):
    file=open('sp500.csv', 'r', encoding="ISO-8859-1")
    final=[]
    tuples=[]
    file.readline()
    for line in file:
        file_list=line.split(",")
        if (file_list[2]==sector):
            final=(file_list[1], file_list[3])
            tuples.append(final)
    return tuples
    
    
    


def print_sectors(file):
    file=open('sp500.csv', 'r', encoding="ISO-8859-1")
    selected=[]
    file.readline()
    for line in file:
        file_list=line.split(",")
        if (file_list[2] not in selected):
            selected.append(file_list[2])
    selected.sort()
    for new in selected:
        print(new)
        

def main(file_name):
    print("GICS Sectors in the S&P 500".center(50, '-'))
    print_sectors(file_name)

    print(50*'-')
    sector=input("Enter sector: ")

    sector_list=get_securities(file_name,sector)
    heading=str(len(sector_list))+ " S&P 500 Securities in " +sector
    print(heading.center(50,'-'))
    for i in range(len(sector_list)):
        security=str(sector_list[i][0]).ljust(35,'.')
        sub_industry=sector_list[i][1]
        print(str(i+1).ljust(2), security, sub_industry)

main(file)

#get_securities(file,"Energy")
