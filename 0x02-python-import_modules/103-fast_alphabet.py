#!/usr/bin/python3
import builtins
builtins.print(*map(chr, range(ord('A'), ord('Z')+1)), sep='', end='\n')
