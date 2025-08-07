# Github Action
You can write individual tasks called actions and combine them to create a customworkflow
# Events
Run workflows when these events happen
push
pull request
issue (created, closed,..)
schedule (every 6pm)
external events

# VM (linux, window, macos) 
bootup to run job

Events --> Workflow --> Job --> Step --> Action/CMD
Virtual Environment --> Runners --> Github hosted runner 
                                --> Self hosted runner

### Runner
1. any machine with the github action runner appilication installed
2. a runner is responsible for running you jovs wheneveran event happens and display back the result
3. it can be hosted by github or you can host your own runner

### Notification
Github profile --> Setting --> Notification --> System --> Actions

### Logs
1. download logs form 3 dots in right corner
2. To get debug mode
setting --> secret --> New Secret
```
Name ACTIONS_RUNNER_DEBUG
value true

Name ACTIONS_STEP_DEBUG
value true
```

### ENcrypt file using gpg
gpg --symmetric --cipher-algo AES256 secret.txt

### Decrypt the file using gpg
gpg --quiet --batch --yes --decrypt --passphrase="$PASSPHRASE" --output $HOME/secret.txt secret.txt.gpg