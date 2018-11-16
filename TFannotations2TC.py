import csv
import sys

tfInputFile = sys.argv[1]
tcOutputFile = sys.argv[2]
outputFile = open(str(tcOutputFile), "w")

with open(str(tfInputFile), mode='r') as csv_file:

    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    outputFile.write('path,annotations\n')
    
    for row in csv_reader:
            
        filename = str(row["filename"])
        className = str(row["class"]) 
        xmin = row["xmin"]
        xmax = row["xmax"]
        ymin = row["ymin"]
        ymax = row["ymax"]

        height = str(int(ymax) - int(ymin))
        width = str(int(xmax) - int(xmin))

        x = str(int(xmin) + int(width)/2)
        y = str(int(ymin) + int(height)/2)
        outputFile.write(filename+',[{"coordinates": {"height": '+height+', "width": '+width+', "x": '+x+', "y": '+y+'}, "label": "'+className+'"}]\n')
        line_count += 1

    print('Processed '+str(line_count)+' lines.')