# Problem: https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth/problem
# Programmer: Md. Ashraful Haque
# Date: 31.08.2024

import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    if (len( elem.findall(".//") ) > 0):
        lavel += 1
        if (lavel >= maxdepth):
            maxdepth = lavel + 1
        for child in elem:
            depth(child, lavel)


if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)