#imports
import psutil   # Module to diplay pc stats
import time
import sqlite3 

# db conn details, creates new db if does not exists!
conn = sqlite3.connect(r'\pc_performance.db')

cursor = conn.cursor()

# Creating table
cursor.execute('''CREATE TABLE IF NOT EXISTS PerformanceTable(
        ID INTEGER PRIMARY KEY,
        time TIMESTAMP,
        cpu_usage INTEGER DEFAULT 0,
        memory_usage INTEGER DEFAULT 0,
        cpu_interrupts INTEGER DEFAULT 0,
        cpu_calls INTEGER DEFAULT 0,
        memory_used INTEGER DEFAULT 0,
        memory_free INTEGER DEFAULT 0,
        bytes_sent INTEGER DEFAULT 0,
        bytes_received INTEGER DEFAULT 0,
        disk_usage INTEGER DEFAULT 0)'''
        )

while True:

    try:
        cpu_usage = psutil.cpu_percent()
        memory_usage = psutil.virtual_memory()[2]
        
        cpu_interrupts = psutil.cpu_stats()[1]
        cpu_calls = psutil.cpu_stats()[3]
        
        memory_used = psutil.virtual_memory()[3]
        memory_free = psutil.virtual_memory()[4]

        bytes_sent = psutil.net_io_counters()[0]
        bytes_received = psutil.net_io_counters()[1]

        disk_usage = psutil.disk_usage('/')[3]

        cursor.execute('''INSERT INTO PerformanceTable (time, cpu_usage, memory_usage, cpu_interrupts, cpu_calls, memory_used, memory_free, bytes_sent, bytes_received, disk_usage) VALUES(CURRENT_TIMESTAMP,?,?,?,?,?,?,?,?,?)''', 
            (str(cpu_usage),
            str(memory_usage),
            str(cpu_interrupts),
            str(cpu_calls),
            str(memory_used),
            str(memory_free),
            str(bytes_sent),
            str(bytes_received),
            str(disk_usage)))


        # Save (commit) the changes
        conn.commit()

        # Refresh every 5 seconds
        time.sleep(5)
    
    except:
        # Close the connection
        conn.close()
