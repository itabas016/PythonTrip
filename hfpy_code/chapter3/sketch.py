import os

os.getcwd()

if os.path.exists('../sketch.txt'):
    data = open('../sketch.txt')
    data.seek(0)

    for each_line in data:
        try:
            if not each_line.find(':') == -1:
                (role, line_spoken) = each_line.split(':', 1)
                print(role+' said: '+line_spoken)
        except:
            # print('throw exception handle read each line data.')
            pass
    data.close()
else:
    print('The data file is missing.')