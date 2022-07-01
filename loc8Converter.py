#
# https://github.com/wukko/ubiart-loc8-converter
#
# UbiArt localisation file converter by https://github.com/wukko
# Tested on Just Dance 2015 - 2022 games on PC, Wii, Wii U, Nintendo Switch (NX).
# This script should work for Rayman Legends/Origins and other UbiArt games too.
#
# This script requires passing parameters when used standalone. 
#
# Usage:
# py loc8Converter.py <mode> <input> <output>
#
# Modes:
# -d --decompress     Decompresses the loc8 file as JSON
# -c --compress       Compresses the file back to loc8 from JSON
# -p --patch          Patches the output JSON file with values in input JSON file
# 
# Credit to me (https://github.com/wukko) is required when this script is used in other projects.

import json

def decompress(input, output):
    with open(input, "rb") as f:
        j = {}
        f.seek(8)
        i = 0
        amountOfStrings = int.from_bytes(f.read(4), "big")
        while i != amountOfStrings:
            id = int.from_bytes(f.read(4), "big")
            j[id] = f.read(int.from_bytes(f.read(4), "big")).decode("utf-8").replace("\x0A", "\n").replace('"', '\\"')
            i = i + 1
    with open(output, "w", encoding="utf-8") as f:
        json.dump(j, f, ensure_ascii=False, separators=(',', ':'))

def compress(input, output):
    with open(output, "wb") as f:
        j = json.load(open(input, "r", encoding="utf-8"))
        f.write(b'\x00\x00\x00\x01\x00\x00\x00\x00')
        f.write(len(j).to_bytes(4, "big"))
        for i in j:
            string = j[i].replace('\"', '"').replace("\n", "\x0A").encode("utf-8")
            f.write(int(i).to_bytes(4, "big"))
            f.write(len(string).to_bytes(4, "big"))
            f.write(string)
        f.write(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF')

def patch(input, output):
    patchjson = json.load(open(input, 'r', encoding="utf-8"))
    originaljson = json.load(open(output, 'r', encoding="utf-8"))
    for i in patchjson:
        originaljson[i] = patchjson[i]
    with open(output, "w", encoding="utf-8") as f:
        json.dump(originaljson, f, ensure_ascii=False, separators=(',', ':'))

if __name__ == "__main__":
    import sys

    if len(sys.argv) == 4:
        mode = sys.argv[1]
        inputFile = sys.argv[2]
        outputFile = sys.argv[3]

        if mode == "-d" or mode == "--decompress":
            decompress(inputFile, outputFile)

        if mode == "-c" or mode == "--compress":
            compress(inputFile, outputFile)

        if mode == "-p" or mode == "--patch":
            patch(inputFile, outputFile)
    else:
        print('')
        print("This script requires passing parameters when used standalone.")
        print('')
        print("Usage:")
        print("py loc8Converter.py <mode> <input> <output>")
        print('')
        print("Modes:")
        print("-d --decompress     Decompresses the loc8 file as JSON")
        print("-c --compress       Compresses the file back to loc8 from JSON")
        print("-p --patch          Patches the output JSON file with values in input JSON file")