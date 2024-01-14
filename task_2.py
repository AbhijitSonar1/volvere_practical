import speedtest
print("Please Wait It will Take Some time....")
speed_test = speedtest.Speedtest()
download_speed = speed_test.download() / 1024 / 1024
print("Your Download speed is", download_speed, "MB")
