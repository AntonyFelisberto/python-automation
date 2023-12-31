import psutil

print(psutil.cpu_count())
print(psutil.cpu_count(logical=False))
print(psutil.cpu_percent())
print(psutil.cpu_percent(interval=1))
print(psutil.cpu_times())
print(psutil.cpu_times().system)
print(psutil.cpu_stats())
print(psutil.cpu_freq())

print(psutil.virtual_memory())
print(psutil.swap_memory())

print(psutil.disk_usage("/"))
print(psutil.disk_usage("/").percent)
print(psutil.disk_partitions())