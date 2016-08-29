# BGB Pokemon Demo Generator
This progam is to help genenerate demo files for BGB (see bgb.html#demorec included with BGB)

Since BGB only accepts demo files through the command line. Here is the command MeGotsThis use to compile the demo file and run through bgb
```
taskkill /IM bgb.exe /F & cd C:\path\to\BGB && python C:\path\to\BGB-Pokemon-Input-Generator\input_generator.py && bgb -rom "C:\path\to\Pokemon Red.gb" -demoplay bgb-input.dem
```

The inputs generated are put filled at the exact input to be read. So you do need to account for additional lag frames (i.e sprites)

## Frame Counts
- Frames to buffer palette change: 76
- Stepping: 17
- Jumping a ledge: 40
- Press A in overworld: 2
- Boot to first input read for Pokemon RB: 491
- Fast manipulation to overworld: 903 (Red), 910 (Blue)
