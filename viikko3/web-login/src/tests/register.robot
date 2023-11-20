*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page
Test Teardown  Reset Users

*** Test Cases ***
Register With Valid Username And Password
    Register  kalle  kalle123  kalle123
    Welcome Page Should Be Open

Register With Too Short Username And Valid Password
    Register  k  kalle123  kalle123
    Register Should Fail With Message  Username must be atleast 3 characters

Register With Valid Username And Invalid Password
    Register  kalle  kalle  kalle
    Register Should Fail With Message  Invalid password:

Register With Nonmatching Password And Password Confirmation
    Register  kalle  kalle123  kalle1234
    Register Should Fail With Message  Passwords do not match

Login After Successful Registration
    Register  kalle  kalle123  kalle123
    Go To Login Page
    Login  kalle  kalle123
    Main Page Should Be Open

Login After Failed Registration
    Register  k  kalle123  kalle123
    Go To Login Page
    Login  k  kalle123
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Text  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Text  password_confirmation  ${password}

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Reset Users
    Reset Application

Register
    [Arguments]  ${username}  ${password}  ${password_confirmation}
    Set Username  ${username}
    Set Password  ${password}
    Set Password Confirmation  ${password_confirmation}
    Click Button  Register

Login
    [Arguments]  ${username}  ${password}
    Set Username  ${username}
    Set Password  ${password}
    Click Button  Login