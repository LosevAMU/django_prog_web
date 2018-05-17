import csv

csvfile = open('testDT.csv')
fastspamreader = csv.reader(csvfile, delimiter=';')
line_count = 0
for row in fastspamreader:
        line_count += 1
csvfile.close()


csvfile = open('testDT.csv')
spamreader = csv.reader(csvfile, delimiter=';')

counter = -1

out_file = open('data_DT.json', 'w', encoding="utf-8")

out_file.write("%s\n" % "[")


for row in spamreader:
    counter += 1
    if counter == 0:
        continue

    out_file.write("%s\n" % "{")
    out_file.write("%s\n" % '"model": "snps.Disease_trait",')
    str_tmp = '"pk": ' + str(counter) + ','
    out_file.write("%s\n" % str_tmp)
    out_file.write("%s\n" % '"fields": {')


    str_tmp = '"Name": "' + row[0] + '"'
    out_file.write("%s\n" % str_tmp)


    print(row)

    out_file.write("%s\n" % "}")
    if counter + 1 == line_count:
        out_file.write("%s\n" % "}")
    else:
        out_file.write("%s\n" % "},")

out_file.write("%s\n" % "]")
out_file.close()
csvfile.close()

