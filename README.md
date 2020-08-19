# Hitcon-Agent
For gaming use, No commercial purpose

- Host Agent
    - POST /host/api/shellcode :[shellcode],[pid]\(optional\)
        - shellcode -> base64 encode
        - pid -> kill orignal pid
        - Return
            - success or not
            - pid
            - e.g success,58211

    - POST /host/api/status :[pid]
        - request with pid number
        - Return
            - process status
            - e.g running/sleeping/ or 'Process Dead'



### TODO
1. user binding ? -> socket.gethostname()
2. Does port need to be returned?
3. setrlimit testing

### Bug Fixed
- If user input is not valid , will crash the program
- Agent shutdown when client close connection.
- request with non-exist pid will crash the program
