#!/usr/bin/env ruby

require 'socket'

host = Socket.gethostname
port = 915

s = TCPSocket.new host, port

s.puts('{ "artist" : "MIA", "song" : "Paper Planes"}')

begin 
  while line = s.gets   # Read lines from the socket
    puts line.chop      # And print with platform line terminator
  end
rescue
end
s.close               # Close the socket when done
