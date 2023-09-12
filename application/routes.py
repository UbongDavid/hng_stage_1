from flask import request, make_response
from flask import current_app as app
from datetime import datetime


@app.route('/')
def index():
    slack_name = request.headers.get('slack_name')
    current_day = datetime.date.day
    utc_time = 5
    track = request.headers.get('track')
    #github_file_url = 5
    #github_repo_url = 'https://github.com/UbongDavid/hng_stage_1'
    #status_code = 200
    json_response = {
                    "slack_name": slack_name,
                    "current_day": current_day,
                    "utc_time": utc_time,
                    "track": track,
                    "github_file_url": "https://github.com/username/repo/blob/main/file_name.ext",
                    "github_repo_url": "https://github.com/username/repo",
                    "status_code": 200
                    }
    response = make_response(json_response, 200)
    return response

