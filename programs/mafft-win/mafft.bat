@echo off

setlocal

if not "x%PROCESSOR_ARCHITECTURE%" == "xAMD64" goto _NotX64
set COMSPEC=%WINDIR%\SysWOW64\cmd.exe
%COMSPEC% /c %0 %*
goto EOF
:_NotX64

set ROOTDIR="%~d0%~p0\ms"
set PATH=/bin/:%PATH%
set MAFFT_BINARIES=/lib/mafft
set TMPDIR=%~d0%~p0/ms/tmp

%ROOTDIR%\bin\sh %ROOTDIR%\bin\mafft %*

:EOF
