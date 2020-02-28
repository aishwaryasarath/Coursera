#!/usr/bin/env python3

def validate_user(username, minlen):
    assert type(username) == str, "username must be a string"
    if minlen < 1:
        raise ValueError("Minlen must be atleast 1")
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    return True

# python3
# from validation import validate_user
# validate_user("",-1)  -> ValueError
# validate_user("", 1)  ->False
# validate_user("myuser",1) ->True
# validate_user(88,1) ->TypeError
# validate_user([],1) ->"
# validate_user(["name"],1) ->Atrribute error
# validate_user([3],1) ->AssertionError: username must be a string

