import time
from urllib.request import urlopen
import json
import urllib

API_KEY = '2bc1db5de9395e00'
API_URL = 'http://api.page2images.com/restfullink'

API_CALL_STATUA_ERROR = 'error'
API_CALL_STATUA_PROCESSING = 'processing'
API_CALL_STATUA_FIHISHED = 'finished'


def getMobileScreenshot(search_url):
    # URL can be those formats: http://www.google.com
    # https://google.com google.com and www.google.com
    url = search_url

    # 0 - iPhone4, 1 - iPhone5, 2 - Android, 3 - WinPhone,
    # 4 - iPad, 5 - Android Pad, 6 - Desktop
    device = 0

    loop_flag = True
    TIMEOUT = 120  # timeout after 120 seconds

    start_time = time.time()
    timeout_flag = False

    while (loop_flag):
        # We need call the API until we get the screenshot or error message
        try:
            post_data = {
                "p2i_url": url,
                "p2i_key": API_KEY,
                "p2i_device": device,
                "p2i_screen": "2024x1000"
            }
            encoded = urllib.parse.urlencode(post_data)
            encoded = encoded.encode('utf-8')

            response = urlopen(API_URL, encoded).read()
            response = response.decode('utf-8')
            # print('response--------------------',response)
            json_data = json.loads(response)
            # print(json_data)
            if(json_data['status'] == API_CALL_STATUA_ERROR):
                # do something to handle error
                loop_flag = False
                print(' '.join([str(json_data['errno']), json_data['msg']]))
            elif(json_data['status'] == API_CALL_STATUA_FIHISHED):
                # do something with finished. For example, show this image
                # Or you can download the image from our server
                loop_flag = False
            else:  # API_CALL_STATUA_PROCESSING or Timeout
                if ((time.time() - start_time) > TIMEOUT):
                    loop_flag = False
                    # set the timeout flag. You can handle it later.
                    timeout_flag = True
                else:
                    time.sleep(3)  # This only work on windows.
            return json_data
        except ValueError as e:
            # Do whatever you think is right to handle the exception.
            loop_flag = False
            print('Caught exception: %s' % str(e))
            return None

    if (timeout_flag):
        # handle the timeout event here
        print("Error: Timeout after %d seconds." % TIMEOUT)
    return None
