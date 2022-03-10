curl --header "Content-Type: application/json" \
     --request POST \
     --data '{"y":2022,"m":3,"d":9,"h":22,"averageTemp":"22.29"}' \
     http://127.0.0.1:8000/add_temp
