# weather app server

## tech info
using python, fastapi and mongodb

## get it working

1. run `pip install -r requirements.txt`
2. mongodb database named weather-app with following collections:
    - `temps` for storing the temperatures
    - `last_temp` for storing the last measured temperature
3. `.env` file, use `.env.example` as an example
4. run it inside `app` directory with `uvicorn main:app --reload`, omit `--reload` if it's in production

<br>

<div align="left">

[weather_app](https://github.com/MichalUSER/weather_app)
— [weather_app_client](https://github.com/MichalUSER/weather_app_client)
— [weather_app_cli](https://github.com/MichalUSER/weather_app_cli)

</div>
