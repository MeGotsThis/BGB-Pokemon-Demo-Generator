# BGB Pokemon Demo Generator
This progam is to help genenerate demo files for BGB (see bgb.html#demorec included with BGB)

Since BGB only accepts demo files through the command line. Here is the command MeGotsThis use to compile the demo file and run through bgb
```
taskkill /IM bgb.exe /F & cd C:\path\to\BGB && python C:\path\to\BGB-Pokemon-Input-Generator\input_generator.py && bgb -rom "C:\path\to\Pokemon Red.gb" -demoplay bgb-input.dem
```
