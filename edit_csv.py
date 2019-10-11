input_filename = "input.csv"
output_filename = "output.csv"
target_idx = 2                #index num
target = 100
skip_header = True

input_file = open(input_filename, "r")  #r: read / w: write  rw: read & write
lines = input_file.readlines()                   #on memory
input_file.close()                      #unnecessary, free pointer.

output_file = open(output_filename, "w")

for i, line in enumerate(open(input_filename, "r")): 
  if i == 0 and skip_header:
    continue
  line = line.rstrip("\n")              #delete endline(\n)
  sp = line.split(",")                  #line: string, sp: list  , separated
  sp[target_idx] = str(target)          #replace 1 to 100
  processed_line = ",".join(sp)         #transform list to line
  output_file.write(processed_line + "\n")
print("done replacement.")
output_file.close()
