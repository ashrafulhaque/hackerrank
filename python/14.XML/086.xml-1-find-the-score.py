# Problem: https://www.hackerrank.com/challenges/xml-1-find-the-score/problem
# Programmer: Md. Ashraful Haque
# Date: 31.08.2024

import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    total_attrs = 0
    # Iterate through all child nodes and count the attributes in each node.
    for child in node.iter():
        total_attrs += len(child.attrib)
    # Get the number of attributes
    return total_attrs

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))