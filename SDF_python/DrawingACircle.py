import math, time

def circle(x: float, y: float) -> float:
  # since the range of x is -1..1, the circle's radius will be 40%,
  # meaning the circle's diameter is 40% of the screen
  radius = 0.4
  # calculate the distance from the center of the screen and subtract the
  # radius, so d will be < 0 inside the circle, 0 on the edge, and > 0 outside
  return math.sqrt(x**2 + y**2) - radius

def sample(x: float, y: float) -> str:
  # return a '#' if we're inside the circle, and ' ' otherwise
  if circle(x, y) <= 0:
    return '#'
  else:
    return ' '

while True:
  frame_chars = []
  for y in range(20):
    for x in range(80):
      # remap to -1..1 range (for x)...
      remapped_x = x / 80 * 2 - 1
      # ...and corrected for aspect ratio range (for y)
      remapped_y = (y / 20 * 2 - 1) * (2 * 20/80)
      frame_chars.append(sample(remapped_x, remapped_y))
    frame_chars.append('\n')
  print( ''.join(frame_chars))
  time.sleep(1/30)