from PCLDeviceHandler import PclStartUpCheck
from DeviceHost import DeviceHost


## get device info
hosts = []
hosts.append(DeviceHost("172.10.10.1","830","admin","admin","pcl"))
hosts.append(DeviceHost("172.10.10.2","830","admin","admin","pcl"))
hosts.append(DeviceHost("172.10.30.3","830","admin","admin","pcl"))
hosts.append(DeviceHost("172.10.10.4","830","admin","admin","pcl"))
hosts.append(DeviceHost("172.10.50.5","830","admin","admin","pcl"))
hosts.append(DeviceHost("172.10.10.6","830","admin","admin","pcl"))
hosts.append(DeviceHost("172.10.10.7","830","admin","admin","pcl"))

for host in hosts:
    s = host.getSysTelnetEcho("reboot")
    print(s)