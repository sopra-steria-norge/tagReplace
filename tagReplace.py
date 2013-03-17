
import os, sys, getopt

listF = ''
apF = ''
outDir='./'

helpStr="Usage: %s -l <listfile-csv> -a <apfile-xml> [-o <outDir>]" % os.path.basename(__file__)

try:
    opts, args = getopt.getopt(sys.argv[1:],"hl:a:o:",["listfile=","apfile=","outDir"])
except getopt.GetoptError:
    print helpStr
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
	    print helpStr
	    sys.exit()
    elif opt in ("-l", "--listfile"):
	    listF = arg
    elif opt in ("-a", "--apfile"):
	    apF = arg
    elif opt in ("-o", "--outDir"):
        tmp = arg.rstrip('\\')
        tmp = tmp.rstrip('/')
        outDir = outDir + tmp

if len(listF) == 0 or len(apF) == 0:
   print helpStr
   sys.exit(2)

if not os.path.isdir(outDir):
   print("Could not find directory %s" % outDir)
   sys.exit(2)

# Read CSV-file (";" separated) that contain the list 
# First line are the tag
f = open(listF, 'r')
(tag1,tag2) = f.readline().split(";")
tag2=tag2.rstrip("\n")
tag2=tag2.rstrip("\r")
print("Tag read     : %s;%s" % (tag1, tag2))

for line_fgruppe in f:
    (a1,a2) = line_fgruppe.split(';')
    a1=a1.rstrip("\n")
    a2=a2.rstrip("\n")
    a1=a1.rstrip("\r")
    a2=a2.rstrip("\r")
    if len(line_fgruppe) > 1:
        print("Handling line: %s;%s" % (a1, a2))
        # Open the template XML-file
        ap = open(apF, 'r')
        out = open(outDir + '/' + a1 +'-' + apF,'w')
        print("Creating file: %s" % out.name)
        for line_ap in ap:
            line_ap = line_ap.replace('%'+tag1+'%',a1)
            line_ap = line_ap.replace('%'+tag2+'%',a2)
            out.write(line_ap)
        out.close()
        ap.close()
f.close()
