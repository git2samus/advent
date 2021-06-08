#!/usr/bin/env ruby

def run(intcode)
  pos = 0

  loop do
    case intcode[pos]
    when 1
      op = :+
    when 2
      op = :*
    when 99
      return intcode
    else
      raise "error"
    end

    l_arg_pos, r_arg_pos, target_pos = intcode[pos+1..pos+3]
    intcode[target_pos] = intcode[l_arg_pos].send(op, intcode[r_arg_pos])
    pos += 4
  end
end

intcode = ARGF.read.split(",").map { |num| num.to_i }
intcode[1] = 12
intcode[2] = 2
puts run(intcode)[0]
