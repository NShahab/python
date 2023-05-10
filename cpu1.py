import psutil
import time

while True:
    # Get current CPU usage
    cpu_usage = psutil.cpu_percent()

    # Get current memory usage
    memory_usage = psutil.virtual_memory().percent

    # Get current disk usage
    disk_usage = psutil.disk_usage('/').percent

    # Get current network usage
    network_usage = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv

    # Print the results
    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory_usage}%")
    print(f"Disk Usage: {disk_usage}%")
    print(f"Network Usage: {network_usage} bytes")

    # Wait for 5 seconds before getting the next set of data
    time.sleep(2)