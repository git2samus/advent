#!/usr/bin/env ruby

def run(intcode)
  memory = intcode.clone
  addr_pointer = 0

  read_addr = ->(param, mode=0) {
    case mode
    when 1
      param
    when 0
      memory[param]
    else
      raise "error"
    end
  }

  loop do
    instruction = memory[addr_pointer]

    opcode = instruction % 100
    modes = instruction % 1000 / 100, instruction % 10000 / 1000, instruction % 100000 / 10000

    #print Hash[memory.each_with_index.map { |a, i| [i, a] }]
    #puts
    #print [addr_pointer, opcode, modes]
    #puts

    case opcode
    when 1,2
      op = opcode == 1 ? :+ : :*

      params = memory[addr_pointer+1..addr_pointer+3]
      memory[params[2]] = read_addr.call(params[0], modes[0]).send(op, read_addr.call(params[1], modes[1]))

      addr_pointer += 4
    when 3
      param = memory[addr_pointer+1]

      print "input> "
      memory[param] = $stdin.gets.to_i

      addr_pointer += 2
    when 4
      param = memory[addr_pointer+1]

      puts read_addr.call(param, modes[0])

      addr_pointer += 2
    when 5,6
      cmp = opcode == 5 ? :!= : :==

      params = memory[addr_pointer+1..addr_pointer+2]
      if read_addr.call(params[0], modes[0]).send(cmp, 0)
        addr_pointer = read_addr.call(params[1], modes[1])
      else
        addr_pointer += 3
      end
    when 7,8
      cmp = opcode == 7 ? :< : :==

      params = memory[addr_pointer+1..addr_pointer+3]
      l_val = read_addr.call(params[0], modes[0])
      r_val = read_addr.call(params[1], modes[1])
      memory[params[2]] = l_val.send(cmp, r_val) ? 1 : 0

      addr_pointer += 4
    when 99
      return memory[0]
    else
      raise "error"
    end
  end
end

open(ARGV[0]) { |f|
  intcode = f.read.split(",").map { |num| num.to_i }
  run(intcode)
}
