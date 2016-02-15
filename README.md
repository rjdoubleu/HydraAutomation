# HydraAutomation
Trying to automate hydra dic attacks against web pages so that the user doesn't have to go into the DOM in order to find the variable names for ^USER^ ,^PASS^, the form method, and failure response.

Currently, the program is only suited for http-form-post attacks and I have been using DVWA as my lab for testing.

The program is a wrapper so it requires hydra and of course Python to be preinstalled.

Run the program on the command line 
> Python HydraAutomation.py URLOrIPAddress
