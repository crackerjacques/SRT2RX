import re
import sys
import tkinter as tk
from tkinter import filedialog

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
            end_time = timecodes[1].replace(",", ".") if len(timecodes) > 1 else ""
            region_type = "Marker" if len(timecodes) == 1 else "Region"
            region_name = f"{region_type} {index+1}"
            comment = " ".join(entry_lines[2:])

            if end_time:
                output_file.write(f"{region_name}\t{start_time}\t{end_time}\t{comment}\n")
            else:
                output_file.write(f"{region_name}\t{start_time}\t{comment}\n")

def main():
    root = tk.Tk()
    root.withdraw()

    srt_filename = filedialog.askopenfilename(filetypes=[("SRT Files", "*.srt")])

    if srt_filename:
        output_filename = filedialog.asksaveasfilename(defaultextension=".txt")

        if output_filename:
            convert_srt_to_rx_region(srt_filename, output_filename)

    root.destroy()

if __name__ == "__main__":
    main()
