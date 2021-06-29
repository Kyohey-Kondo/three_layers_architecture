#!/bin/bash -e
SHELL_NAME='setuser.sh'
echo "[$SHELL_NAME] START"

# setup group
if getent group "$GROUP_ID" > /dev/null 2>&1; then
    echo "[$SHELL_NAME] GROUP_ID '$GROUP_ID' already exists."
else
    echo "[$SHELL_NAME] GROUP_ID '$GROUP_ID' does NOT exist. So execute [groupadd -g \$GROUP_ID \$GROUP_NAME]."
    groupadd -g $GROUP_ID $GROUP_NAME
fi

# setup user
if getent passwd "$USER_ID" > /dev/null 2>&1; then
    echo "[$SHELL_NAME] USER_ID '$USER_ID' already exists."
else
    echo "[$SHELL_NAME] USER_ID '$USER_ID' does NOT exist. So execute [useradd -m -s /bin/bash -u \$USER_ID -g \$GROUP_ID \$USER_NAME]."
    useradd -m -s /bin/bash -u $USER_ID -g $GROUP_ID $USER_NAME
fi

echo "[$SHELL_NAME] FINISH"
