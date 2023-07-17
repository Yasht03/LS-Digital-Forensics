def execute_brainfuck_file(filename):
    with open(filename, 'r') as file:
        code = file.read()

    
    tape = [0] * 30000
    pointer = 0

    
    loop_stack = []

   
    output = ""
    instruction_pointer = 0
    while instruction_pointer < len(code):
        instruction = code[instruction_pointer]

        if instruction == ">":
            pointer += 1
        elif instruction == "<":
            pointer -= 1
        elif instruction == "+":
            tape[pointer] = (tape[pointer] + 1) % 256
        elif instruction == "-":
            tape[pointer] = (tape[pointer] - 1) % 256
        elif instruction == ".":
            output += chr(tape[pointer])
        elif instruction == ",":
            
            pass
        elif instruction == "[":
            if tape[pointer] == 0:
                
                loop_depth = 1
                while loop_depth > 0:
                    instruction_pointer += 1
                    if code[instruction_pointer] == "[":
                        loop_depth += 1
                    elif code[instruction_pointer] == "]":
                        loop_depth -= 1
            else:
                loop_stack.append(instruction_pointer)
        elif instruction == "]":
            if tape[pointer] != 0:
                instruction_pointer = loop_stack[-1]
            else:
                loop_stack.pop()

        instruction_pointer += 1

    return output

filename = "brainfuck_code.bf"
output = execute_brainfuck_file(filename)
print(output)
