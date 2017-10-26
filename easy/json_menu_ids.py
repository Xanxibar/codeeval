#!usr/bin/env python3
"""
JSON Menu IDs
Solution Author: Mild Z Ferdinand
Description: You have JSON string which describes a menu. Calculate the SUM of
 IDs of all "items" in the case a "label" exists for an item.
"""
import json
import sys


def main():
    with open(sys.argv[1], 'r') as text:
        for line in text:
            my_string = line.strip()
            if my_string == "":
                continue
            my_json = json.loads(my_string)
            my_list = my_json['menu']['items']
            acc = 0
            for items in my_list:
                if items is not None:
                    if 'label' in list(items.keys()):
                        acc += int(items['id'])
                else:
                    continue
            print(acc)


if __name__ == "__main__":
    main()