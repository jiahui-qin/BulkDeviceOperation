import ftplib
import telnetlib
import time

class DeviceHost:
    ip = ""
    username = ""
    password = ""
    type = ""
    extraInfo = ""

    def __init__(self, ip, username, password, type):
        self.ip = ip
        self.username = username
        self.password = password
        self.type = type

    def getTelnetEcho(self, command):
        if self.type == "pcl":
            telnetClient = telnetlib.Telnet
            try:
                telnetClient = telnetlib.Telnet(self.ip)
                telnetClient.read_until(b'Username: ',timeout=10)
                telnetClient.write(self.username.encode('ascii') + b'\r')
                telnetClient.read_until(b'Password: ',timeout=10)
                telnetClient.write(self.password.encode('ascii') + b'\r')
                telnetClient.read_until(b'>',timeout=10)
                telnetClient.write(command.encode('ascii')+b'\r')
                time.sleep(2)
                command_result = telnetClient.read_very_eager().decode('ascii')
                telnetClient.write(b"exit\r")
                return command_result
            except:
                return(self.ip + ":"  + " telnet connect failed")
        else:
            return(self.ip + ": not support type " + self.type)

    def getSysTelnetEcho(self, command):
        if self.type == "pcl":
            telnetClient = telnetlib.Telnet
            try:
                telnetClient = telnetlib.Telnet(self.ip)
                telnetClient.read_until(b'Username: ',timeout=10)
                telnetClient.write(self.username.encode('ascii') + b'\r')
                telnetClient.read_until(b'Password: ',timeout=10)
                telnetClient.write(self.password.encode('ascii') + b'\r')
                telnetClient.read_until(b'>',timeout=10)
                telnetClient.write("en".encode('ascii') + b'\r')
                telnetClient.read_until(b'#',timeout=10)
                telnetClient.write("sy".encode('ascii') + b'\r')
                telnetClient.read_until(b'#',timeout=10)
                telnetClient.write(command.encode('ascii')+b'\r')
                time.sleep(2)
                command_result = telnetClient.read_very_eager().decode('ascii')
                telnetClient.write(b"exit\r")
                return command_result
            except:
                return(self.ip + ":"  + " telnet connect failed")
        else:
            return(self.ip  + ": not support type " + self.type)

    def getFtpFile(self, path):
        ftpClient = ftplib.FTP(host = self.ip, user = "root", passwd= "pcl")
        ftpClient.cwd(path)
        fileList = ftpClient.nlst()
        ftpClient.quit()
        return fileList

    def deleteFtpFile(self, filePath):
        try:
            ftpClient = ftplib.FTP(host = self.ip, user = "root", passwd= "pcl")
            ftpClient.delete(filePath)
            ftpClient.quit()
            return True
        except:
            return False

    def uploadFtpFile(self, localFile, remoteFilePath):
        filename = localFile.split('/')[-1]
        bufsize = 1024
        ftpClient = ftplib.FTP(host = self.ip, user = "root", passwd= "pcl")
        ftpClient.cwd(remoteFilePath)
        with open(localFile,'rb') as  f_up:
            ftpClient.storbinary('STOR '+  filename, f_up ,bufsize)
            ftpClient.set_debuglevel(0) #关闭调试模式
            ftpClient.quit #退出ftp
        return True

    def print(self):
        print(self.ip  + " with " + self.username + "/" + self.password + " and type is " + self.type)