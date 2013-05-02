__author__ = 'arobres'


import getopt
import os
import sys



def usage():
    print
    print "Usage: python execute.py [command]"
    print
    print "\t--test"


    print

try:
    optlist, args = getopt.getopt(sys.argv[1:],
                                  "h",
                                  ["test"])
except getopt.GetoptError:
    # print help information and exit:
    print "Invalid command found in %s" % sys.argv
    usage()
    sys.exit(2)


def execute_test(xunit_file):

    os.system('lettuce google_maps/' + " --with-xunit --xunit-file=" + xunit_file)
    #os.system('lettuce component/api-rest/create-topic/ --with-xunit --xunit-file=create_topic_result.xml')
    #lettuce.Runner(os.path.abspath(path), verbosity=4, enable_xunit=True, xunit_filename=xunit_file).run()


def test_geocodification():

    print("Running geocodification Tests")

    print("Geocodification Tests")
    execute_test("geocodification-tests.xml")
    print


if len(optlist) == 0:
    usage()
    sys.exit(1)

# Check for help requests, which cause all other
# options to be ignored.
for option in optlist:
    if option[0] in ("--help", "-h"):
        usage()
        sys.exit(1)


# Parse the arguments, in order
for option in optlist:
    if option[0] in "--test":
        test_geocodification()
        os.system(' relish push "Toni/geocodification" path ./google_maps/features/')



