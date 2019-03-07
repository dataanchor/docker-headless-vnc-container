inotifywait -m /logs/$POD_NAME -e create -e moved_to |
    while read path action file; do
       google-chrome $file &
    done