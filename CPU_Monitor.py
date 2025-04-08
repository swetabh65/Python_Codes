import psutil
import time

# Define CPU usage threshold
CPU_USAGE_THRESHOLD = 80  # in percentage
CHECK_INTERVAL = 2        # in seconds

def monitor_cpu_usage():
    print("🔍 Monitoring CPU usage... (Press Ctrl+C to stop)")
    
    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            if cpu_usage > CPU_USAGE_THRESHOLD:
                print(f"⚠️  Alert! CPU usage exceeds threshold: {cpu_usage}%")
            else:
                print(f"✅ CPU usage is normal: {cpu_usage}%")
            time.sleep(CHECK_INTERVAL)
    except KeyboardInterrupt:
        print("\n🛑 Monitoring stopped by user.")
    except Exception as e:
        print(f"❌ An error occurred while monitoring CPU: {e}")

if __name__ == "__main__":
    monitor_cpu_usage()
