import psutil
import time

# Define CPU usage threshold
CPU_USAGE_THRESHOLD = 80  # in percentage
CHECK_INTERVAL = 2        # in seconds

def monitor_cpu_usage():
    print("CPU usage Monitoring in progress... (Press Ctrl + C to stop)")
    
    try:
        while True:
            usage_cpu = psutil.cpu_percent(interval=1)
            if usage_cpu > CPU_USAGE_THRESHOLD:
                print(f"Alert! CPU usage now exceeds threshold: {usage_cpu}%")
            else:
                print(f"CPU usage is doing normal: {usage_cpu}%")
            time.sleep(CHECK_INTERVAL)
    except KeyboardInterrupt:
        print("\n Monitoring is stopped by user.")
    except Exception as e:
        print(f"An error occurred while monitoring CPU: {e}")

if __name__ == "__main__":
    monitor_cpu_usage()
