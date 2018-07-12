# data-traffic-monitoring
Monitor data traffic, and execute scripts when data traffic reaches the upper limit.

步骤：

1、执行 cat /proc/net/dev 命令，检查除了lo之外的另一块网卡是否名为eth0，如果不是，需要将check.py和liuliang.py中的eth0替换为新网卡名称（如：venet0）。如果替换后运行脚本提示'Please setup your netcard'，可以将两个脚本中新网卡名称的第一个字符删除（如venet0变为enet0）；

2、执行 python check.py，根据返回结果，修改liuliang.py中第23、24行recv和send后面方括号中的数值；

3、修改liuliang.py第4行的流量上限，单位Byte；

4、修改liuliang.py第43行的流量更新时间；

5、将liuliang.py第48行和第51行的井号（#）注释删除，执行 python liuliang.py，检查recvdata和senddata是否正常输出。如果输出正常，重新加上注释符号；

6、将 python liuliang.py 命令加入开机启动。
