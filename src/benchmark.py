import time
import statistics

def calculate_performance_metrics(tps_input, duration):
    total_transactions = int(tps_input * duration)
    latencies = []
    start_test_time = time.time()
    for i in range(total_transactions):
        t_sub = time.time()
        processing_delay = 0.01 + (tps_input / 15000)
        time.sleep(1 / tps_input)
        t_conf = time.time() + processing_delay
        latency_ms = (t_conf - t_sub) * 1000
        latencies.append(latency_ms)
    end_test_time = time.time()
    total_time = end_test_time - start_test_time
    actual_throughput = total_transactions / total_time
    results = {
        "min_latency": round(min(latencies), 2),
        "max_latency": round(max(latencies), 2),
        "avg_latency": round(statistics.mean(latencies), 2),
        "throughput": round(actual_throughput, 2),
        "total_transactions": total_transactions
    }
    return results

if __name__ == "__main__":
    test_results = calculate_performance_metrics(tps_input=500, duration=3)
    print(test_results)
