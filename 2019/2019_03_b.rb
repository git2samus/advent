require 'set'

def plot_coord(steps)
  Enumerator.new { |enum|
    position, num_steps = [0, 0], 0
    steps.each { |step|
      direction, distance = step[0], step[1..].to_i

      breadcrumb = nil
      (1..distance).each { |delta|
        breadcrumb = position.clone

        case direction
        when "D"
          breadcrumb[1] -= delta
        when "U"
          breadcrumb[1] += delta
        when "L"
          breadcrumb[0] -= delta
        when "R"
          breadcrumb[0] += delta
        end
        num_steps += 1

        enum << [breadcrumb, num_steps]
      }

      position = breadcrumb
    }
  }
end

# transform step instructions into list of coordinates
wire1, wire2 = ARGF.each_line.map { |line|
  plot_coord(line.split(","))
}

# map coordinates to their distance keeping the shortest one for self-intersections
wire1_map = Hash.new
wire1.each { |coord, dist|
  wire1_map[coord] = dist unless wire1_map.has_key? coord
}

# look for intersections with wire1 and keep track of the shortest distance
min_intersection_coord, min_intersection_dist = nil, nil
wire2.each { |coord, dist|
  if wire1_map.has_key? coord
    sum_dist = dist + wire1_map[coord]
    if min_intersection_dist.nil? or sum_dist < min_intersection_dist
      min_intersection_coord, min_intersection_dist = coord, sum_dist
    end
  end
}

puts min_intersection_dist
