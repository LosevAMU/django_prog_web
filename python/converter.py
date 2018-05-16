import csv

csvfile = open('test.csv')
fastspamreader = csv.reader(csvfile, delimiter=';')
line_count = 0
for row in fastspamreader:
        line_count += 1
csvfile.close()


csvfile = open('test.csv')
spamreader = csv.reader(csvfile, delimiter=';')

counter = -1

out_file = open('data_ini.json', 'w', encoding="utf-8")

out_file.write("%s\n" % "[")


for row in spamreader:
    counter += 1
    if counter == 0:
        continue

    out_file.write("%s\n" % "{")
    out_file.write("%s\n" % '"model": "snps.Post",')
    str_tmp = '"pk": ' + str(counter) + ','
    out_file.write("%s\n" % str_tmp)
    out_file.write("%s\n" % '"fields": {')
    out_file.write("%s\n" % '"author": 1,')
    str_tmp = '"PUBMEDID": ' + row[0] + ','
    out_file.write("%s\n" % str_tmp)
    str_tmp = '"published_date": "' + row[1] + '",'
    out_file.write("%s\n" % str_tmp)
    str_tmp = '"JOURNAL": "' + row[2] + '",'
    out_file.write("%s\n" % str_tmp)
    str_tmp = '"LINK": "' + row[3] + '",'
    out_file.write("%s\n" % str_tmp)
    str_tmp = '"STUDY": "' + row[4] + '",'
    out_file.write("%s\n" % str_tmp)
    str_tmp = '"DISEASE_TRAIT": "' + row[5] + '",'
    out_file.write("%s\n" % str_tmp)
    str_tmp = '"CHR_ID": "' + str(row[6]) + '",'
    out_file.write("%s\n" % str_tmp)

    str_tmp = '"CHR_POS": "' + str(row[7]) + '",'
    out_file.write("%s\n" % str_tmp)
    str_tmp = '"RSID_CURRENT": "' + str(row[8]) + '",'
    out_file.write("%s\n" % str_tmp)
    str_tmp = '"P_VALUE": "' + str(str(row[9]).replace(",", ".")) + '",'
    out_file.write("%s\n" % str_tmp)
    str_tmp = '"PVALUE_MLOG": "' + str(str(row[10]).replace(",", ".")) + '"'
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

