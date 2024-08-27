# BI_TASK_MANAGER
BI_TASK_MANAGER is a small project that shows the PC resource usage as a classic task manager does, with the difference that the PC performance is shown on the PowerBI Dashboard in live.

In the project, the following technologies were used.
  
Python
  1. psutil
  2. sqlite3
PowerBI
  1. Custom ODBC connector (must be separately installed to connect to SQLLite3 version)
SQLLite3

In order to work, a Python script should be in the same directory as the other files. It must be run in the background, so it populates the PC performance stats on the local SQLLite3 server. A PowerBI dashboard will get the data from the connected local server.
