from PCLDeviceHandler import PclStartUpCheck
from DeviceHost import DeviceHost


## get device info
hosts = []
hosts.append(DeviceHost("172.10.10.21","admin","admin","pcl"))
hosts.append(DeviceHost("172.10.10.22","admin","admin","pcl"))
hosts.append(DeviceHost("172.10.10.23","admin","admin","pcl"))
hosts.append(DeviceHost("172.10.10.24","admin","admin","pcl"))
hosts.append(DeviceHost("172.10.10.25","admin","admin","pcl"))
hosts.append(DeviceHost("172.10.10.26","admin","admin","pcl"))

for host1 in hosts:

    telnetString = host1.getTelnetEcho("display startup")

    ## analysis device info
    host1Up = PclStartUpCheck(telnetString)
    host1Up.print()


    ## delete old file
    fileList = host1.getFtpFile("/mnt/flash2")
    host1Up.getDeleteFile(fileList)
    print("get need delete file is: " + host1Up.deleteFile)
    if host1Up.deleteFile != "null":
        host1.deleteFtpFile(host1Up.deleteFile)

    ## get upload file path
    host1Up.getUploadFilePath("/root/version")
    print("now want upload file: " +host1Up.newFile + " device startup file: " + host1Up.startUp)

    ## upload file
    uploadFlag = input("sure upload below file to device?")
    ##if uploadFlag == "yes":
    print("start upload file "  +host1Up.newFile + " to "  + host1.ip + "/mnt/flash2")
    host1.uploadFtpFile(host1Up.newFile, "/mnt/flash2")
    print("upload file success")
    ## set next startup file, reboot file
    newFile = host1Up.newFile.split("/")[-1]
    rebootFlag = input("set next startup flag to " + newFile + " and reboot device?")
        ##if rebootFlag == "yes":
    host1.getTelnetEcho("startup system-software " + newFile)
