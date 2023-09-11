from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)


@app.route('/api', methods=['GET'])
def get_info():
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    current_day = datetime.datetime.utcnow().strftime('%A')
    utc_time = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    github_file_url = "https://github.com/hashkitti001/HNG9BackendTasks/blob/main/api.py"
    github_repo_url = "https://github.com/hashkitti001/HNG9BackendTasks"
    status_code = 200

    response = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": status_code
    }

    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
