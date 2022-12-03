defmodule Utils do
  def get_input() do
    # get input data line by line and trim spaces/newlines
    get_input(System.argv) |> Stream.map(&String.trim/1)
  end

  defp get_input([head | _]) do
    # commandline argument is a filename, stream its contents
    File.stream!(head, [:utf8], :line)
  end

  defp get_input([]) do
    # no commandline arguments, stream standard input
    IO.stream()
  end


  def get_input_blocks() do
    # group input data as blocks separated by empty lines
    get_input() |> chunk_blocks()
  end

  defp chunk_blocks(input_stream) do
    chunk_fun = fn
      "", [] ->
        # skip multiple empty lines entirely
        {:cont, []}
      "", acc ->
        # skip empty line and produce reversed accumulator as chunk
        {:cont, Enum.reverse(acc), []}
      element, acc ->
        # prepend element into accumulator
        {:cont, [element | acc]}
    end

    after_fun = fn
      [] ->
        # nothing to produce
        {:cont, []}
      acc ->
        # produce last chunk
        {:cont, Enum.reverse(acc), []}
    end

    # group input stream into chunks
    input_stream |> Stream.chunk_while([], chunk_fun, after_fun)
  end


  def get_input_tokens() do
    # get input lines as list of space-separated tokens
    get_input() |> Stream.map(&String.split/1)
  end
end
