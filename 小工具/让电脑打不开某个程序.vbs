dim qobj,pipe,good
do
    good="."
set qobj = getobject("winmgmts:\\"&good&"\root\cimv2")
set pipe= qobj.execquery("select * from win32_process where name='cloudmusic.exe'")
for each i in pipe
    i.terminate()
next
wscript.sleep(1000)
loop