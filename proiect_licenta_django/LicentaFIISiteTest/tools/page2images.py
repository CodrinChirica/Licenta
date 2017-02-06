#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib.request import urlopen
import json
import time
import urllib
# import urllib2

API_KEY = '2bc1db5de9395e00'
API_URL = 'http://api.page2images.com/restfullink'

# api call status
API_CALL_STATUA_ERROR = 'error'
API_CALL_STATUA_PROCESSING = 'processing'
API_CALL_STATUA_FIHISHED = 'finished'


def call_p2i():
    # URL can be those formats: http://www.google.com
    # https://google.com google.com and www.google.com
    url = "http://www.google.com"

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
                "p2i_device": device
            }
            encoded = urllib.parse.urlencode(post_data)
            encoded = encoded.encode('utf-8')

            json_data = json.loads(urlopen(API_URL, encoded).read())
            print(json_data)
            if(json_data['status'] == API_CALL_STATUA_ERROR):
                # do something to handle error
                loop_flag = False
                print(' '.join([str(json_data['errno']), json_data['msg']]))
            elif(json_data['status'] == API_CALL_STATUA_FIHISHED):
                # do something with finished. For example, show this image
                print(json_data['image_url'])
                # Or you can download the image from our server
                loop_flag = False
            else:  # API_CALL_STATUA_PROCESSING or Timeout
                if ((time.time() - start_time) > TIMEOUT):
                    loop_flag = False
                    # set the timeout flag. You can handle it later.
                    timeout_flag = True
                else:
                    time.sleep(3)  # This only work on windows.
        except ValueError as e:
            # Do whatever you think is right to handle the exception.
            loop_flag = False
            print('Caught exception: %s' % str(e))

    if (timeout_flag):
        # handle the timeout event here
        print("Error: Timeout after %d seconds." % TIMEOUT)

if __name__ == '__main__':
    call_p2i()
