curl --header "Content-Type: application/json" \
     --request POST \
     --data '{"y":2022,"m":3,"d":5,"h":12,"averageTemp":"23.32"}' \
     http://127.0.0.1:8000/add_last_temp
