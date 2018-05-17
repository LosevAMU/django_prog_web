import csv

csvfile = open('testSNP.csv')
fastspamreader = csv.reader(csvfile, delimiter=';')
line_count = 0
for row in fastspamreader:
        line_count += 1
csvfile.close()


csvfile = open('testSNP.csv')
spamreader = csv.reader(csvfile, delimiter=';')

counter = -1

out_file = open('data_SNP.json', 'w', encoding="utf-8")

out_file.write("%s\n" % "[")


for row in spamreader:
    counter += 1
    if counter == 0:
        continue

    out_file.write("%s\n" % "{")
    out_file.write("%s\n" % '"model": "snps.SNP",')
    str_tmp = '"pk": ' + str(counter) + ','
    out_file.write("%s\n" % str_tmp)
    out_file.write("%s\n" % '"fields": {')

    str_tmp = '"Chrom": "' + str(row[0]) + '",'
    out_file.write("%s\n" % str_tmp)
    str_tmp = '"Chrom_pos": "' + str(row[1]) + '",'
    out_file.write("%s\n" % str_tmp)
    str_tmp = '"Rsid": "' + str(row[2]) + '"'
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

