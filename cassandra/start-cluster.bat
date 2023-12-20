@echo off

set VERSION=4.0.7
set NODES=%1
set BRIDGE=br1

if "%NODES%"=="" (
    echo Usage: %0 ^<NUMBER OF NODES^>
    exit /b 1
)

for /L %%i in (1,1,%NODES%) do (
    echo Starting node %%i
    set "hostname=cass%%i"
    set "ip=192.168.112.%%i"

    rem Start container
    if %%i==1 (
        set "ports=-p 9160:9160 -p 9042:9042"
    ) else (
        set "ports="
    )
    for /f %%c in ('docker run -d --dns 192.168.56.114 -h %hostname  %ports -t cassandra:%VERSION% /usr/bin/start-cassandra') do set "cid=%%c"

    rem Add network interface
    timeout /t 1 /nobreak >nul
    pipework %BRIDGE% !cid! %ip%/24
)