import csv

csvfile = open('testPheno.csv')
fastspamreader = csv.reader(csvfile, delimiter=';')
line_count = 0
for row in fastspamreader:
        line_count += 1
csvfile.close()


csvfile = open('testPheno.csv')
spamreader = csv.reader(csvfile, delimiter=';')

counter = -1

out_file = open('data_Pheno.json', 'w', encoding="utf-8")

out_file.write("%s\n" % "[")


for row in spamreader:
    counter += 1
    if counter == 0:
        continue

    out_file.write("%s\n" % "{")
    out_file.write("%s\n" % '"model": "snps.SNP2Phenotype2Ref",')
    str_tmp = '"pk": ' + str(counter) + ','
    out_file.write("%s\n" % str_tmp)
    out_file.write("%s\n" % '"fields": {')

    str_tmp = '"Snp_id": ' + str(counter) + ','
    out_file.write("%s\n" % str_tmp)
    str_tmp = '"Disease_trait_id": ' + str(counter) + ','
    out_file.write("%s\n" % str_tmp)
    str_tmp = '"Reference_id": ' + str(counter) + ','
    out_file.write("%s\n" % str_tmp)


    str_tmp = '"pvalue": "' + str(str(row[0]).replace(",", ".")) + '",'
    out_file.write("%s\n" % str_tmp)
    str_tmp = '"neglog10pvalue": "' + str(str(row[1]).replace(",", ".")) + '"'
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

