import os
from collections import defaultdict

def generate_asset_report(folder_path):
    file_count = 0
    file_types = defaultdict(int)

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_count += 1
            _, ext = os.path.splitext(file)
            file_types[ext] += 1

    report_path = os.path.join(folder_path, "asset_report.txt")

    with open(report_path, "w") as report:
        report.write("Asset Report\n")
        report.write("====================\n")
        report.write(f"Total Files: {file_count}\n\n")
        report.write("File Types:\n")

        for ext, count in file_types.items():
            report.write(f"{ext}: {count}\n")

    print("Report generated.")
    print(f"Total Files: {file_count}")
    print("File Types:")
    for ext, count in file_types.items():
        print(f"{ext}: {count}")


if __name__ == "__main__":
    folder = input("Enter folder path to scan: ")
    generate_asset_report(folder)
