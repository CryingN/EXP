import hashlib
import requests
import paramiko
from time import sleep
from concurrent.futures import ThreadPoolExecutor
import py_compile

urls = []

s = lambda time : sleep(time * 60)
with open("/home/root_cn/flag/tools/exp/trojan") as f:
    tj = f.read()

def changcheng(cookie, ip, flag):
    # cookie like "cha=llla;ckb=lllb"
    
    # set User-agent
    """
    url = f""
    headers = {
        "Cookie": cookie,
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"
    }
    """

    url = f""
    headers = {"Cookie": cookie}
    data = requests.get(url=url, headers=headers)
    return data

# api
def bugku(token, flag):
    url = f"https://ctf.bugku.com/pvp/submit.html?token={token}&flag={flag}"
    data = requests.get(url)
    return data


def awdscan(url_name):
    global urls
    urls = []
    try:
        with open(f"/home/root_cn/flag/tools/awdscan/{url_name}") as f:
            urls = f.readlines()
            return urls
    except:
        return None

def ak(function, urls = urls):
    with ThreadPoolExecutor() as executor:
        executor.map(function, urls)

def sha(crypto:str):
    crypto = crypto.encode()
    hash_object = hashlib.sha256()
    hash_object.update(crypto)
    return hash_object.hexdigest()

def pyc(file_name):
    py_compile.compile(file_name)


# 配置ssh相关
class SSH:
    def __init__(self, url, user, passwd):
        host, port = url.split(":")
        self.host = host
        self.port = int(port)
        self.user = user
        self.passwd = str(passwd)
        self.ssh = None

    def startup(self):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.host, self.port, self.user, self.passwd)
            t = paramiko.Transport((self.host, self.port))
            t.connect(username=self.user, password=self.passwd)
            self.ssh = ssh
            print("[+] Connect successfully")
            return True
        except BaseException as e:
            print("[-] Connect ERROR!! {}".format(e))
            return False

    def command_exec(self, command):
        try:
            std_in, std_out, std_err = self.ssh.exec_command(command)
            out = std_out.read()
            err = std_err.read()
            if out != b'':
                print(out.decode().rstrip("\n"))
                return out.decode().rstrip("\n")
            if err != b'':
                print(err.decode().rstrip("\n"))
        except BaseException as e:
            print("[-] Could not exec command! {}".format(e))
        return 0

    def change_passwd(self, new_passwd):
        try:
            command = "passwd %s" %(self.user)
            stdin, stdout, stderr = self.ssh.exec_command(command)
            # stdin.write(new_password + '\n' + new_password + '\n')
            stdin.write(self.passwd + '\n' + new_passwd + '\n' + new_passwd + '\n')
            out, err = stdout.read(), stderr.read()
            successful = 'password updated successfully'
            if successful in str(err):
                print(self.host + " successfully!")
                self.passwd = new_passwd
                self.ssh.close()
            else:
                print("[-] change {} passwd failed! {}".format(self.host, str(err)))
                self.ssh.close()
        except BaseException as e:
            print("[-] Could not exec command! {}".format(e))
        return 0




