import csv

with open("highly_cited_2014.csv") as input, open("collegename.txt", "w") as college, open("college_Addr.txt", "w") as addr:
   reader = csv.DictReader(input, dialect="excel-tab")
   fieldnames = reader.fieldnames
   writer_college = csv.DictWriter(college, fieldnames, dialect="excel-tab")
   writer_addr = csv.DictWriter(addr, fieldnames, dialect="excel-tab")
   writer_college.writeheader()
   writer_addr.writeheader()
   for row in reader:
       print row["4"]
       '''if (row[4] == "Chemistry") :
          writer_college.writerow(row)
       else:
          writer_addr.writerow(row)'''