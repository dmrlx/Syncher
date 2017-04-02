import subprocess

# Генератор ping'a
def ping_cmd_generator(host, timer=1):
    ping_cmd = "ping " + str(host) + " -c 1 " + "-W " + str(timer)
    ping_cmd = ping_cmd.split()
    return ping_cmd

# pusher: Отправляет сформированные в модуле composer команды
# Возвращает "0" если всё хорошо и "1" если ошибка.
def pusher(cmd):
    push = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    push.wait()
    return push.poll()

if __name__ == "__main__":
    if pusher(ping_cmd_generator("192.168.56.103")) == 0: # Если пингуется
        pusher(ssh_connect_cmd_generator(params))