#!/usr/bin/env python3

key_check = input("Please enter the key in the form x/y/z:\n")
key_new = key_check.replace('/','')
key_fin=list(key_new)
print(key_fin)
def nested(inp_dictt, nes_key):
    int_dict_val = inp_dictt
    for k in nes_key:
        int_dict_val = int_dict_val.get(k, None)
        if int_dict_val is None:
            return None
    return int_dict_val #Return input list

print (nested({"a":{"b":{"c":1}}},list(key_check.replace('/','')))) #Return required value, if present
print (nested({"a":{"e":{"c":1}}},list(key_check.replace('/',''))))
