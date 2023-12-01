#stream_input = Utils.get_raw_input |> Stream.map(&String.trim/1)

#top = Stream.take_while(stream_input, fn line -> line != "" end) |> Enum.to_list

#stream = File.stream!("05_sample.txt", [:utf8], :line)
#stream = IO.stream()
stream = 1..10

#top = Stream.take(stream, 3) |> Enum.to_list
#bottom = stream |> Enum.to_list
{top, bottom} = {Stream.take(stream, 3), stream}

IO.inspect(Enum.to_list(top), label: "top")
IO.inspect(Enum.to_list(bottom), label: "bottom")
