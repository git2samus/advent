#!/usr/bin/env ruby

def run(intcode)
  memory = intcode.clone
  addr_pointer = 0

  loop do
    case memory[addr_pointer]
    when 1
      op = :+
    when 2
      op = :*
    when 99
      return memory[0]
    else
      raise "error"
    end

    l_arg_pos, r_arg_pos, target_pos = memory[addr_pointer+1..addr_pointer+3]
    memory[target_pos] = memory[l_arg_pos].send(op, memory[r_arg_pos])
    addr_pointer += 4
  end
end

def guess_output(intcode, output)
  (0..99).each do |noun|
    (0..99).each do |verb|
      intcode[1..2] = noun, verb
      return noun, verb if run(intcode) == output
    end
  end
end

intcode = ARGF.read.split(",").map { |num| num.to_i }
noun, verb = guess_output(intcode, 19690720)
puts 100 * noun + verb
