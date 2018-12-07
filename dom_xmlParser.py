#
# Simple DOM (Document Object Model) xml parser
#
#

# Import DOM xml libs
from xml.dom import minidom

# parser() function
def dom_xmlparser():
    print("DOM .xml parser - parser()")

    pattern_response = minidom.parse('/Users/demirdru/PycharmProjects/test_001/file_sources/pattern_response.xml')
    print("\n" "Parsing the pattern_response...")
    itemlist = pattern_response.getElementsByTagName("m")
    print(len(itemlist))
    print(itemlist[0].attributes['type'].value)
    print(itemlist[0].childNodes[0].nodeValue)

    vast_response = minidom.parse('/Users/demirdru/PycharmProjects/test_001/file_sources/vast_response.xml')
    print("\n" "Parsing the vast_response for <AdTitle>...")
    itemlist = vast_response.getElementsByTagName('AdTitle')
    print("Number of <AdTitle> in vast response is:" + str(len(itemlist)))
    for i in itemlist:
        print(i.childNodes[0].nodeValue)

    print("\n" "Parsing the vast_response for <Ad>...")
    itemlist = vast_response.getElementsByTagName('Ad')
    print("Number of <Ad> in vast response is:" + str(len(itemlist)))
    for i in itemlist:
        print("id = " + str(i.attributes['id'].value) + str("  ") + "sequence = " + str(i.attributes['sequence'].value))

# main() function
def main():
    print("DOM .xml parser - main()")

    dom_xmlparser()


# main() function
if __name__ == '__main__':
    main()