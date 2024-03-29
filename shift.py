import sys

if(len(sys.argv) != 3):
    print ("\nYou should put the file path of the srt file and then how many seconds you wanna shift it")
    print ("Example, if I wanna shift the Dune subtitles 12 seconds on the left:")
    print (r"shift.py C:\Users\Dune_subtitles.srt -12")
    exit()

srt_path = sys.argv[1]

def shift_string(string):
    argument = sys.argv[2]
    argument = int(argument)
    hours = int(string[0:2])  
    minutes = int(string[3:5])
    seconds = int(string[6:8])
    if argument < 0:    
        argument *= -1
        seconds -= argument
        if seconds < 0:
            seconds += 60
            minutes -= 1
            if minutes < 0:
                minutes += 60 
                hours -= 1
                if hours < 0:
                    hours = 0
    else:
        seconds += argument
        if seconds >= 60:
            seconds -= 60
            minutes += 1
            if minutes >= 60:
                minutes -= 60
                hours += 1

    if seconds == 0:
        string = string[:6] + "00" + string[8:]
    else:
        string = string[:6] + str(seconds).zfill(2) + string[8:]
    if minutes == 0:
        string = string[:3] + "00" + string[5:]
    else:
        string = string[:3] + str(minutes).zfill(2) + string[5:]
    if hours == 0:
        string = "00" + string[2:]
    else:
        string = str(hours).zfill(2) + string[2:]
        
    return string 

with open(srt_path, 'r') as file:
        content = file.read()

modified_content = ""

i = 0
while(i != len(content)):
    if content[i-1] == '\n' and content[i-2] == '\n':
        modified_content += content[i]
        modified_content += content[i+1]
        if content[i+2] == '\n':
            modified_content += content[i+2]
            i = i + 1
        elif content[i+3] == '\n':
            modified_content += content[i+2]
            modified_content += content[i+3]
            i = i + 2
        elif content[i+4] == '\n':
            modified_content += content[i+2]
            modified_content += content[i+3]
            modified_content += content[i+4]
            i = i + 3
        modified_content += shift_string(content[i+2:i+10])
        modified_content += content[i+10:i+19]
        modified_content += shift_string(content[i+19:i+27])
        i += 27
        continue
    else:
        modified_content += content[i]
    i = i + 1


with open(srt_path, 'w') as file:
        file.write(modified_content)
        