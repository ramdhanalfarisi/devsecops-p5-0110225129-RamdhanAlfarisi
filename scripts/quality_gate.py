import json
import sys

def check_quality_gate(report_file):
    try:
        with open(report_file, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: File {report_file} tidak ditemukan.")
        sys.exit(1)

    results = data.get('results', [])
    high_count = sum(1 for item in results if item.get('issue_severity') == 'HIGH')
    medium_count = sum(1 for item in results if item.get('issue_severity') == 'MEDIUM')

    print(f"Hasil SAST Scan - High: {high_count}, Medium: {medium_count}")

    if high_count > 0 or medium_count > 0:
        print("[QUALITY GATE FAILED] Terdeteksi kerentanan tingkat HIGH/MEDIUM!")
        sys.exit(1)
    
    print("[QUALITY GATE PASSED] Kode aman dari kerentanan kritis.")
    sys.exit(0)

if __name__ == "__main__":
    check_quality_gate("bandit-report.json")