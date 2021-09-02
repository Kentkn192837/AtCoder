def sep_input():
  def sep_line(line):
    return line.rstrip().split('.')
  input_line = input()
  input_line = sep_line(input_line)
  return int(input_line[0]), int(input_line[1])
 
x, y = sep_input()
 
if 0 <= y and y <= 2:
  print('{}-'.format(x))
elif 3 <= y and y <= 6:
  print(x)
elif 7 <= y and y <= 9:
  print('{}+'.format(x))
