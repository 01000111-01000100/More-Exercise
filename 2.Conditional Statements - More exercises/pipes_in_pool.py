pool = int(input())
pipe_1 = int(input())
pipe_2 = int(input())
hours = float(input())

pipe_1 *= hours
pipe_2 *= hours
total_pipe = pipe_1 + pipe_2
total = (total_pipe / pool) * 100

pipe_1_brings = (pipe_1 / total_pipe) * 100
pipe_2_bring = (pipe_2 / total_pipe) * 100

if pool < total_pipe:
    sum = total_pipe - pool
    print(f'For {hours:.2f} hours the pool overflows with {sum:.2f} litres.')
else:
    print(f'The pool is {total:.2f}% full. Pipe 1: {pipe_1_brings:.2f}%. Pipe 2: {pipe_2_bring:.2f}%.')