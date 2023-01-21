

import sys


def decomment(line: str) -> str:
    """
    >>> decomment("foo // bar")
    "foo "
    >>> decomment("// foo bar")
    ""
    """
    return line[:x] if (x := line.find("//")) > -1 else line


def main():

    lines = [decomment(line).strip() for line in sys.stdin]
    lines = [line for line in lines if line]

    symbols = {f"R{i}":i for i in range(16)}
    symbols.update({"SCREEN": 16384, "KBD": 24576, "SP": 0, "LCL": 1, "ARG": 2,
                    "THIS": 3, "THAT": 4})

    # first pass
    i, instructions = 0, []
    for line in lines:
        if line[0] == "(" and line[-1] == ")":
            symbols[line[1:-1]] = i
        else:
            instructions.append(line)
            i += 1

    # second pass
    n = 16
    comps = {"0": "0101010", "1": "0111111", "-1": "0111010", "D": "0001100",
             "A": "0110000", "!D": "0001101", "!A": "0110001", "-D": "0001111",
             "-A": "0110011", "D+1": "0011111", "A+1": "0110111",
             "D-1": "0001110", "A-1": "0110010", "D+A": "0000010",
             "D-A": "0010011", "A-D": "0000111", "D&A": "0000000",
             "D|A": "0010101", "M": "1110000", "!M": "1110001", "-M": "1110011",
             "M+1": "1110111", "M-1": "1110010", "D+M": "1000010",
             "D-M": "1010011", "M-D": "1000111", "D&M": "1000000",
             "D|M": "1010101"}
    dests = {None: "000", "M": "001", "D": "010", "MD": "011", "A": "100",
             "AM": "101", "AD": "110", "AMD": "111"}
    jumps = {None: "000", "JGT": "001", "JEQ": "010", "JGE": "011", "JLT": "100",
             "JNE": "101", "JLE": "110", "JMP": "111"}
    for instruction in instructions:
        if instruction[0] == "@":
            symbol = instruction[1:]
            if symbol.isnumeric():
                address = int(symbol)
            elif (symbol := instruction[1:]) in symbols:
                address = symbols[symbol]
            else:
                address = n
                symbols[symbol] = address
                n += 1
            print(bin(address)[2:].zfill(16))
        else:
            if ";" in instruction:
                instruction, jump = instruction.split(";")
            else:
                jump = None
            if "=" in instruction:
                dest, comp = instruction.split("=")
            else:
                dest, comp = None, instruction
            print(f"111{comps[comp]}{dests[dest]}{jumps[jump]}")


if __name__ == "__main__":
    main()
