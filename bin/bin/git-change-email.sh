#!/bin/sh
# Изменяет во всей истории проекта OLD_EMAIL на COORECT_EMAIL
# Осторожно! Если работу над проектом ведут несколько пользователей,
# то может поломаться вся история - номера commit-ом изменятся!

git filter-branch --env-filter '

OLD_EMAIL="podkorytov_pm@taximaxim.ru"
CORRECT_EMAIL="pod.pavel@gmail.com"

if [ "$GIT_COMMITTER_EMAIL" = "$OLD_EMAIL" ]
then
    export GIT_COMMITTER_EMAIL="$CORRECT_EMAIL"
fi
if [ "$GIT_AUTHOR_EMAIL" = "$OLD_EMAIL" ]
then
    export GIT_AUTHOR_EMAIL="$CORRECT_EMAIL"
fi
' --tag-name-filter cat -- --branches --tags
