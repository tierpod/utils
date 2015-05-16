#!/bin/sh

read -p 'Are you sure??? ' answer

replace() {
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
}

case $answer in
  [Yy])
    echo 'Replace old email with current email'
	replace
	;;
  *)
    echo 'Exit'
	;;
esac

