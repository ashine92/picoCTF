# Specialer

Cũng giống như challenge trước, ta đăng nhập vào SSH và nhập thử vài lệnh như sau:

```python
Specialer$ ls
-bash: ls: command not found
Specialer$ pwd
/home/ctf-player

```

Có thể thấy rằng ta có thể nhập lệnh `pwd` nhưng `ls` thì không, mình dùng `compgen -c` để kiểm tra những lệnh nào có thể sử dụng:

```python
Specialer$ compgen -c
if
then
else
elif
fi
case
esac
for
select
while
until
do
done
in
function
time
{
}
!
[[
]]
coproc
.
:
[
alias
bg
bind
break
builtin
caller
cd
command
compgen
complete
compopt
continue
declare
dirs
disown
echo
enable
eval
exec
exit
export
false
fc
fg
getopts
hash
help
history
jobs
kill
let
local
logout
mapfile
popd
printf
pushd
pwd
read
readarray
readonly
return
set
shift
shopt
source
suspend
test
times
trap
true
type
typeset
ulimit
umask
unalias
unset
wait
bash
```

Nhấn TAB 2 lần để nhìn theo chiều ngang:

```python
Specialer$
!          bind       compopt    elif       fc         if         printf     shift      true       while
./         break      continue   else       fg         in         pushd      shopt      type       {
:          builtin    coproc     enable     fi         jobs       pwd        source     typeset    }
[          caller     declare    esac       for        kill       read       suspend    ulimit
[[         case       dirs       eval       function   let        readarray  test       umask
]]         cd         disown     exec       getopts    local      readonly   then       unalias
alias      command    do         exit       hash       logout     return     time       unset
bash       compgen    done       export     help       mapfile    select     times      until
bg         complete   echo       false      history    popd       set        trap       wait
```

Mình nhập `cd` và nhấn TAB 2 lần, sẽ hiện ra những thư mục và files mà thư mục hiện tại đang có:

```python
Specialer$ cd
.hushlogin  .profile    abra/       ala/        sim/
```

Từ lệnh `compgen` , ta thấy không thể sử dụng lệnh `cat` hay `string` để đọc file, tuy nhiên ta có thể dùng được lệnh `echo`. Nội dung của một file có thể được đọc bằng cú pháp `echo "$(<filename)”`

Ta tiến hành đọc từng file:

```python
$ echo "$(<.hushlogin)"

Specialer$ echo "$(<.profile)"
export PS1='Specialer$ '

```

Tiếp tục đến thư mục `abra/`, ta nhập `echo abra` và nhấn TAB 2 lần để hiện thư mục con bên trong:

```python
Specialer$ echo abra/cada
cadabra.txt   cadaniel.txt

Specialer$ cd abra

Specialer$ echo "$(<cadabra.txt)"
Nothing up my sleeve!
Specialer$ echo "$(<cadaniel.txt)"
Yes, I did it! I really did it! I'm a true wizard!
```

Có thể thấy thư mục `abra/` chưa có thông tin gì, ta tiếp tục thử với thư mục `ala/` và `sim/` tương tự:

```python
Specialer$ cd ala/
Specialer$ echo "$(<kazam.txt)"
return 0 picoCTF{y0u_d0n7_4ppr3c1473_wh47_w3r3_d01ng_h3r3_a8567b6f}
```
