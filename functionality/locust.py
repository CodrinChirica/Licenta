from django.http import HttpResponse
import requests
import subprocess


def locust():
    process = subprocess.call(["ls", "-l"])

    process = subprocess.Popen(
        "locust --host=http://localhost:5000 --no-web --clients=30 --hatch-rate=3 --num-request=30 --only-summary --logfile=locust_results.txt > locust_log.log", cwd="./licenta_gui", shell=True, stdout=subprocess.PIPE)

    process.wait()
    print(process.returncode)
    print("Make request")
    r = requests.post("http://localhost:8089/swarm",
                      data={'locust_count': 3, 'hatch_rate': 3})
    print(r.status_code, r.reason)

    time.sleep(10)  # 5 sec
    r = requests.get("http://localhost:8089/stop")
    return HttpResponse("Hello, world. You're at the polls index.")
