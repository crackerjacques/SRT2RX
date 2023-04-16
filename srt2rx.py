import re
import sys

def convert_srt_to_rx_region(srt_filename, output_filename):
    with open(srt_filename, "r", encoding="utf-8") as srt_file:
        srt_content = srt_file.read()

    srt_entries = re.split(r"\n\n", srt_content.strip())

    with open(output_filename, "w", encoding="utf-8") as output_file:
        output_file.write("Marker file version: 1\n")
        output_file.write("Time format: Time\n")

        for index, entry in enumerate(srt_entries):
            entry_lines = entry.split("\n")
            timecodes = entry_lines[1].split(" --> ")
            start_time = timecodes[0].replace(",", ".")
            end_time = timecodes[1].replace(",", ".")
            region_name = entry_lines[2]

            output_file.write(f"{region_name}\t{start_time}\t{end_time}\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python srt_to_rx_region.py <input_srt_file> <output_rx_region_file>")
        sys.exit(1)

    srt_filename = sys.argv[1]
    output_filename = sys.argv[2]

    convert_srt_to_rx_region(srt_filename, output_filename)
