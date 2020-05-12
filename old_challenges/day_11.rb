#!/usr/bin/env ruby
require 'set'

ELEVATOR = "_"

def parse_floors(file, elevator_floor=0)
  # process text input and create floor structure and elevator as arrays
  floors = []

  file.each_line do |line|
    matches = line.scan(/(\w+(?:-compatible microchip| generator))/)
    floors << matches.flatten
  end

  # elevator starts at the bottom
  floors[elevator_floor] << ELEVATOR

  floors
end

def hash_floors(floors)
  # generate a unique output on each floors configuration
  floors.map {|floor|
    floor.sort.join('|')
  }.join('/')
end

def valid_state?(floors)
  # determine if the given floors configuration does not destroy chips
  floors.all? do |floor|
    chips, generators = floor.select {|item|
      item != ELEVATOR
    }.partition {|item|
      item.end_with? "microchip"
    }

    if generators.empty?
      true
    else
      chips.all? do |chip|
        element = chip.split("-")[0]

        generators.any? do |generator|
          generator.include? element
        end
      end
    end
  end
end

def _generate_next_states(floors, seen_hashes)
  # given a floors configuration, generate all possible valid moves
  floors.each_with_index do |floor, index|
    if floor.includes?(ELEVATOR)
      elevator_floor = index
      break
    end
  end

  new_states = []

  [1, -1].each do |direction|
    target_floor = elevator_floor + direction
    next if target_floor < 0 or target_floor >= floors.length

    (0...floors[elevator_floor].length-1).each do |index|
      next_state = floors.clone

      next_state[target_floor] << next_state[elevator_floor].delete(ELEVATOR)
      next_state[target_floor] << next_state[elevator_floor].delete_at(index)

      new_states << next_state if valid_state?(next_state) and not seen_hashes.include?(hash_state(next_state))

      (index+1...floors[elevator_floor].length-1).each do |subindex|
        next_state2 = next_state.clone

        next_state2[target_floor] << next_state2[elevator_floor].delete_at(subindex)

        new_states << next_state2 if valid_state?(next_state2) and not seen_hashes.include?(hash_state(next_state2))
      end
    end
  end
end

def generate_next_states(possible_states, seen_hashes)
  # transform the list of possible floors configurations into the list of valid next moves on each
  new_states = possible_states.map {|floors|
    _generate_next_states(floors, seen_hashes)
  }

  flat_new_states = []
  new_states.each do |floors|
    flat_new_states << floors
  end

  flat_new_states
end

def endgame?(floors)
  # determine if the given floors configuration is a solution to the game
  not floors[(0...-1)].any? {|floor|
    not floor.any? {|item|
      item.includes?("microchip")
    }
  }
end


# begin script #

initial_floors = parse_floors(File.open(ARGV[0]))
seen_hashes = Set.new([hash_floors(initial_floors)])

possible_states = [initial_floors]
steps = 0

unless possible_states.any? {|floors| endgame?(floors) } do
  possible_states = generate_next_states(possible_states, seen_hashes)
  seen_hashes.add(possible_states.map {|floors| hash_floors(floors)})
  steps += 1
end

puts steps
