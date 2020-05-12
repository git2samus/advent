#!/usr/bin/env ruby

File.open(ARGV[0]) {|f|
  orientation = 'N'
  up, right = 0, 0

  f.read.split(', ').each {|step|
    turn, distance = step[0], Integer(step[1..-1])

    case
    when orientation == 'N'
      if turn == 'L'
        orientation = 'W'
        right -= distance
      else
        orientation = 'E'
        right += distance
      end
    when orientation == 'W'
      if turn == 'L'
        orientation = 'S'
        up -= distance
      else
        orientation = 'N'
        up += distance
      end
    when orientation == 'S'
      if turn == 'L'
        orientation = 'E'
        right += distance
      else
        orientation = 'W'
        right -= distance
      end
    when orientation == 'E'
      if turn == 'L'
        orientation = 'N'
        up += distance
      else
        orientation = 'S'
        up -= distance
      end
    end
  }

  puts up.abs + right.abs
}
