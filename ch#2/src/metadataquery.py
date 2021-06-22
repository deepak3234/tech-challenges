#!/usr/bin/env python3

from __future__ import print_function
import json

def find_values(id, json_repr):
    results = []

    def _decode_dict(a_dict):
        try:
            results.append(a_dict[id])
        except KeyError:
            pass
        return a_dict

    json.loads(json_repr, object_hook=_decode_dict) # Return value ignored.
    return results

with open('../ec2metadata.json', 'r') as file:
    json_repr = file.read() #Read JSON output from file

searchKey = input("Enter the searchkey: ")
print(find_values(searchKey, json_repr))
