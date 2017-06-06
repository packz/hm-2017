EESchema Schematic File Version 2
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
LIBS:switches
LIBS:talk-cache
EELAYER 25 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L C C1
U 1 1 5929308B
P 1650 2100
F 0 "C1" H 1675 2200 50  0000 L CNN
F 1 "C" H 1675 2000 50  0000 L CNN
F 2 "" H 1688 1950 50  0000 C CNN
F 3 "" H 1650 2100 50  0000 C CNN
	1    1650 2100
	1    0    0    -1  
$EndComp
$Comp
L CP1 C2
U 1 1 5929316E
P 1950 2100
F 0 "C2" H 1975 2200 50  0000 L CNN
F 1 "CP1" H 1975 2000 50  0000 L CNN
F 2 "" H 1950 2100 50  0000 C CNN
F 3 "" H 1950 2100 50  0000 C CNN
	1    1950 2100
	1    0    0    -1  
$EndComp
$Comp
L L L1
U 1 1 592931F5
P 2300 2100
F 0 "L1" V 2250 2100 50  0000 C CNN
F 1 "L" V 2375 2100 50  0000 C CNN
F 2 "" H 2300 2100 50  0000 C CNN
F 3 "" H 2300 2100 50  0000 C CNN
	1    2300 2100
	1    0    0    -1  
$EndComp
$Comp
L C C3
U 1 1 592D26A9
P 4200 2350
F 0 "C3" H 4225 2450 50  0000 L CNN
F 1 "C" H 4225 2250 50  0000 L CNN
F 2 "" H 4238 2200 50  0000 C CNN
F 3 "" H 4200 2350 50  0000 C CNN
	1    4200 2350
	1    0    0    -1  
$EndComp
$Comp
L L L2
U 1 1 592D273D
P 4600 2100
F 0 "L2" V 4550 2100 50  0000 C CNN
F 1 "L" V 4675 2100 50  0000 C CNN
F 2 "" H 4600 2100 50  0000 C CNN
F 3 "" H 4600 2100 50  0000 C CNN
	1    4600 2100
	0    1    1    0   
$EndComp
$Comp
L C C4
U 1 1 592D277D
P 5650 2200
F 0 "C4" H 5675 2300 50  0000 L CNN
F 1 "C" H 5675 2100 50  0000 L CNN
F 2 "" H 5688 2050 50  0000 C CNN
F 3 "" H 5650 2200 50  0000 C CNN
	1    5650 2200
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR3
U 1 1 592D2860
P 3550 2600
F 0 "#PWR3" H 3550 2350 50  0001 C CNN
F 1 "GND" H 3550 2450 50  0000 C CNN
F 2 "" H 3550 2600 50  0000 C CNN
F 3 "" H 3550 2600 50  0000 C CNN
	1    3550 2600
	1    0    0    -1  
$EndComp
$Comp
L SW_Push_SPDT SW1
U 1 1 592D28C7
P 5000 2100
F 0 "SW1" H 5000 2270 50  0000 C CNN
F 1 "SW_Push_SPDT" H 5000 2650 50  0000 C CNN
F 2 "" H 5000 2100 50  0000 C CNN
F 3 "" H 5000 2100 50  0000 C CNN
	1    5000 2100
	1    0    0    -1  
$EndComp
Text GLabel 3550 2100 0    60   Input ~ 0
VIN
Text GLabel 6000 1900 2    60   Input ~ 0
VOUT
$Comp
L R R1
U 1 1 592E8838
P 2900 4050
F 0 "R1" V 2980 4050 50  0000 C CNN
F 1 "R" V 2900 4050 50  0000 C CNN
F 2 "" V 2830 4050 50  0000 C CNN
F 3 "" H 2900 4050 50  0000 C CNN
	1    2900 4050
	1    0    0    -1  
$EndComp
$Comp
L C C5
U 1 1 592E88CF
P 2500 3800
F 0 "C5" H 2525 3900 50  0000 L CNN
F 1 "C" H 2525 3700 50  0000 L CNN
F 2 "" H 2538 3650 50  0000 C CNN
F 3 "" H 2500 3800 50  0000 C CNN
	1    2500 3800
	0    1    1    0   
$EndComp
$Comp
L GND #PWR1
U 1 1 592E8A38
P 2900 4300
F 0 "#PWR1" H 2900 4050 50  0001 C CNN
F 1 "GND" H 2900 4150 50  0000 C CNN
F 2 "" H 2900 4300 50  0000 C CNN
F 3 "" H 2900 4300 50  0000 C CNN
	1    2900 4300
	1    0    0    -1  
$EndComp
Text GLabel 3250 3800 2    60   Input ~ 0
VOUT
Text GLabel 2150 3800 0    60   Input ~ 0
VIN
$Comp
L MMBF170 Q3
U 1 1 592E93BE
P 6900 4000
F 0 "Q3" H 7100 4075 50  0000 L CNN
F 1 "MMBF170" H 7100 4000 50  0001 L CNN
F 2 "SOT-23" H 7100 3925 50  0000 L CIN
F 3 "" H 6900 4000 50  0000 L CNN
	1    6900 4000
	1    0    0    -1  
$EndComp
$Comp
L Q_NPN_BCE Q1
U 1 1 592E941D
P 5950 4000
F 0 "Q1" H 6150 4050 50  0000 L CNN
F 1 "Q_NPN_BCE" H 6150 3950 50  0001 L CNN
F 2 "" H 6150 4100 50  0000 C CNN
F 3 "" H 5950 4000 50  0000 C CNN
	1    5950 4000
	1    0    0    -1  
$EndComp
$Comp
L Q_NJFET_DGS Q2
U 1 1 592E94E8
P 6450 4000
F 0 "Q2" H 6650 4050 50  0000 L CNN
F 1 "Q_NJFET_DGS" H 6650 3950 50  0001 L CNN
F 2 "" H 6650 4100 50  0000 C CNN
F 3 "" H 6450 4000 50  0000 C CNN
	1    6450 4000
	1    0    0    -1  
$EndComp
$Comp
L D D1
U 1 1 592EB9D8
P 5950 4600
F 0 "D1" H 5950 4700 50  0000 C CNN
F 1 "D" H 5950 4500 50  0001 C CNN
F 2 "" H 5950 4600 50  0000 C CNN
F 3 "" H 5950 4600 50  0000 C CNN
	1    5950 4600
	-1   0    0    1   
$EndComp
$Comp
L D_Schottky D2
U 1 1 592EBABF
P 6350 4600
F 0 "D2" H 6350 4700 50  0000 C CNN
F 1 "D_Schottky" H 6350 4500 50  0000 C CNN
F 2 "" H 6350 4600 50  0000 C CNN
F 3 "" H 6350 4600 50  0000 C CNN
	1    6350 4600
	-1   0    0    1   
$EndComp
$Comp
L D_Zener D3
U 1 1 592EBB30
P 6750 4600
F 0 "D3" H 6750 4700 50  0000 C CNN
F 1 "D_Zener" H 6750 4500 50  0000 C CNN
F 2 "" H 6750 4600 50  0000 C CNN
F 3 "" H 6750 4600 50  0000 C CNN
	1    6750 4600
	-1   0    0    1   
$EndComp
$Comp
L L L3
U 1 1 592EBC6F
P 3850 5100
F 0 "L3" V 3800 5100 50  0000 C CNN
F 1 "L" V 3925 5100 50  0001 C CNN
F 2 "" H 3850 5100 50  0000 C CNN
F 3 "" H 3850 5100 50  0000 C CNN
	1    3850 5100
	0    1    1    0   
$EndComp
$Comp
L SW_Push SW2
U 1 1 592EBD18
P 4300 5100
F 0 "SW2" H 4350 5200 50  0000 L CNN
F 1 "SW_Push" H 4300 5040 50  0001 C CNN
F 2 "" H 4300 5300 50  0000 C CNN
F 3 "" H 4300 5300 50  0000 C CNN
	1    4300 5100
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR4
U 1 1 592EBDBB
P 4700 5150
F 0 "#PWR4" H 4700 4900 50  0001 C CNN
F 1 "GND" H 4700 5000 50  0000 C CNN
F 2 "" H 4700 5150 50  0000 C CNN
F 3 "" H 4700 5150 50  0000 C CNN
	1    4700 5150
	1    0    0    -1  
$EndComp
$Comp
L VCC #PWR2
U 1 1 592EBDEA
P 3500 5000
F 0 "#PWR2" H 3500 4850 50  0001 C CNN
F 1 "VCC" H 3500 5150 50  0000 C CNN
F 2 "" H 3500 5000 50  0000 C CNN
F 3 "" H 3500 5000 50  0000 C CNN
	1    3500 5000
	1    0    0    -1  
$EndComp
$Comp
L D D4
U 1 1 592EC1D8
P 3850 4900
F 0 "D4" H 3850 5000 50  0000 C CNN
F 1 "D" H 3850 4800 50  0001 C CNN
F 2 "" H 3850 4900 50  0000 C CNN
F 3 "" H 3850 4900 50  0000 C CNN
	1    3850 4900
	1    0    0    -1  
$EndComp
$Comp
L D_Zener D?
U 1 1 592FD9A5
P 8600 2950
F 0 "D?" H 8600 3050 50  0000 C CNN
F 1 "D_Zener" H 8600 2850 50  0000 C CNN
F 2 "" H 8600 2950 50  0000 C CNN
F 3 "" H 8600 2950 50  0000 C CNN
	1    8600 2950
	0    1    1    0   
$EndComp
Text GLabel 8300 2700 0    60   Input ~ 0
VIN
Text GLabel 8950 2700 2    60   Input ~ 0
VOUT
$Comp
L GND #PWR?
U 1 1 592FDBC1
P 8600 3150
F 0 "#PWR?" H 8600 2900 50  0001 C CNN
F 1 "GND" H 8600 3000 50  0000 C CNN
F 2 "" H 8600 3150 50  0000 C CNN
F 3 "" H 8600 3150 50  0000 C CNN
	1    8600 3150
	1    0    0    -1  
$EndComp
$Comp
L Transformer_1P_1S T?
U 1 1 592FDE67
P 8600 2100
F 0 "T?" H 8600 2350 50  0000 C CNN
F 1 "Transformer_1P_1S" H 8600 1800 50  0000 C CNN
F 2 "" H 8600 2100 50  0000 C CNN
F 3 "" H 8600 2100 50  0000 C CNN
	1    8600 2100
	1    0    0    -1  
$EndComp
$Comp
L R R?
U 1 1 59355A32
P 8250 5100
F 0 "R?" V 8330 5100 50  0000 C CNN
F 1 "R" V 8250 5100 50  0000 C CNN
F 2 "" V 8180 5100 50  0000 C CNN
F 3 "" H 8250 5100 50  0000 C CNN
	1    8250 5100
	1    0    0    -1  
$EndComp
$Comp
L VCC #PWR?
U 1 1 59355C01
P 8250 4800
F 0 "#PWR?" H 8250 4650 50  0001 C CNN
F 1 "VCC" H 8250 4950 50  0000 C CNN
F 2 "" H 8250 4800 50  0000 C CNN
F 3 "" H 8250 4800 50  0000 C CNN
	1    8250 4800
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR?
U 1 1 59355C4B
P 8850 5600
F 0 "#PWR?" H 8850 5350 50  0001 C CNN
F 1 "GND" H 8850 5450 50  0000 C CNN
F 2 "" H 8850 5600 50  0000 C CNN
F 3 "" H 8850 5600 50  0000 C CNN
	1    8850 5600
	1    0    0    -1  
$EndComp
$Comp
L R R?
U 1 1 59355CAA
P 9650 4600
F 0 "R?" V 9730 4600 50  0000 C CNN
F 1 "R" V 9650 4600 50  0000 C CNN
F 2 "" V 9580 4600 50  0000 C CNN
F 3 "" H 9650 4600 50  0000 C CNN
	1    9650 4600
	1    0    0    -1  
$EndComp
$Comp
L SW_Push SW?
U 1 1 59356540
P 8550 5400
F 0 "SW?" H 8600 5500 50  0000 L CNN
F 1 "SW_Push" H 8550 5340 50  0000 C CNN
F 2 "" H 8550 5600 50  0000 C CNN
F 3 "" H 8550 5600 50  0000 C CNN
	1    8550 5400
	1    0    0    -1  
$EndComp
Text GLabel 8050 5400 0    60   Input ~ 0
PIN
Wire Wire Line
	5650 2600 5650 2350
Connection ~ 5650 2600
Wire Wire Line
	4200 2100 4200 2200
Connection ~ 4200 2100
Wire Wire Line
	4200 2500 4200 2600
Connection ~ 4200 2600
Wire Wire Line
	3550 2100 4450 2100
Wire Wire Line
	3550 2600 6050 2600
Wire Wire Line
	5200 2200 5200 2600
Connection ~ 5200 2600
Wire Wire Line
	5200 2000 5200 1900
Wire Wire Line
	5200 1900 6000 1900
Wire Wire Line
	5650 2050 5650 1900
Connection ~ 5650 1900
Wire Wire Line
	4750 2100 4800 2100
Wire Wire Line
	2150 3800 2350 3800
Wire Wire Line
	2650 3800 3250 3800
Wire Wire Line
	2900 3900 2900 3800
Connection ~ 2900 3800
Wire Wire Line
	2900 4200 2900 4300
Wire Wire Line
	3500 5000 3500 5100
Wire Wire Line
	3500 5100 3700 5100
Wire Wire Line
	4000 5100 4100 5100
Wire Wire Line
	4500 5100 4700 5100
Wire Wire Line
	4700 5100 4700 5150
Wire Wire Line
	3600 5100 3600 4900
Wire Wire Line
	3600 4900 3700 4900
Connection ~ 3600 5100
Wire Wire Line
	4000 4900 4050 4900
Wire Wire Line
	4050 4900 4050 5100
Connection ~ 4050 5100
Wire Wire Line
	8300 2700 8950 2700
Wire Wire Line
	8600 2800 8600 2700
Connection ~ 8600 2700
Wire Wire Line
	8600 3150 8600 3100
Wire Wire Line
	8250 4800 8250 4950
Wire Wire Line
	8850 5400 8850 5600
Wire Wire Line
	8350 5400 8050 5400
Wire Wire Line
	8750 5400 8850 5400
Wire Wire Line
	8250 5250 8250 5400
Connection ~ 8250 5400
$EndSCHEMATC
