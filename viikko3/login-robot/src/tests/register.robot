*** Settings ***
Resource  resource.robot
Test Setup  Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kalle  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Input  new
    Input Credentials  kalle  kalle123
    Output Should Contain  Username already exists

Register With Too Short Username And Valid Password
    Input Credentials  k  kalle123
    Output Should Contain  Username must be atleast 3 characters

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  kalle2  kalle123
    Output Should Contain  Username must contain only letters a-z

Register With Valid Username And Too Short Password
    Input Credentials  kalle  kalle12
    Output Should Contain  Password must be atleast 8 characters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kalle  kalleaaa
    Output Should Contain  Password must contain atleast one special character or number

*** Keywords ***
Input New Command
    Input  new