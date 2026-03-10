import speedtest

def run_speed_test():
    print("Starting Network Speed Test...")

    st = speedtest.Speedtest()

    print("Finding best server...")
    st.get_best_server()

    print("Testing download speed...")
    download = st.download()

    print("Testing upload speed...")
    upload = st.upload()

    ping = st.results.ping

    print(f"Ping: {ping} ms")
    print(f"Download: {round(download/1_000_000,2)} Mbps")
    print(f"Upload: {round(upload/1_000_000,2)} Mbps")

run_speed_test()