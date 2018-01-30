#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""STLM75: Digital temperature sensor and thermal watchdog"""

__author__     = "ChISL"
__copyright__  = "TBD"
__credits__    = ["ST Microelectronics"]
__license__    = "TBD"
__version__    = "Version 0.1"
__maintainer__ = "https://chisl.io"
__email__      = "info@chisl.io"
__status__     = "Test"

#
#   THIS FILE IS AUTOMATICALLY CREATED
#    D O     N O T     M O D I F Y  !
#

from STLM75_constants import *

# name:        STLM75
# description: Digital temperature sensor and thermal watchdog
# manuf:       ST Microelectronics
# version:     Version 0.1
# url:         http://www.st.com/resource/en/datasheet/stlm75.pdf
# date:        2018-01-30


# Derive from this class and implement read and write
class STLM75_Base:
	"""Digital temperature sensor and thermal watchdog"""
	# Register COMMAND
	# The command register retains pointer information between operations (see Table 5).
	#       Therefore, this register only needs to be updated once for consecutive READ operations
	#       from the same register. All bits in the command register default to '0' at power-up. 
	
	
	def setCOMMAND(self, val):
		"""Set register COMMAND"""
		self.write(REG.COMMAND, val, 8)
	
	def getCOMMAND(self):
		"""Get register COMMAND"""
		return self.read(REG.COMMAND, 8)
	
	# Bits reserved_0
	# The most significant bits (MSBs) of the command register must always be zero. Writing a '1'
	#           into any of these bits will cause the current operation to be terminated. 
	
	# Bits P
	# Register TEMP
	# The temperature register is a two-byte (16-bit) “Read only” register (see Table 7 on
	#       page 18). Digital temperatures from the T-to-D converter are stored in the temperature
	#       register in two’s complement format, and the contents of this register are updated each time
	#       the T-to-D conversion is finished.
	#       The user can read data from the temperature register at any time. When a T-to-D
	#       conversion is completed, the new data is loaded into a comparator buffer to evaluate fault
	#       conditions and will update the temperature register if a read cycle is not ongoing. If a READ
	#       is ongoing, the previous temperature will be read. Accessing the STLM75 continuously
	#       without waiting at least one conversion time between communications will prevent the
	#       device from updating the temperature register with a new temperature conversion result.
	#       Consequently, the STLM75 should not be accessed continuously with a wait time of less
	#       than tCONV (max).
	#       All unused bits following the digital temperature will be zero. The MSB position of the
	#       temperature register always contains the sign bit for the digital temperature, and Bit14
	#       contains the temperature MSB. All bits in the temperature register default to zero at powerup.
	#     
	
	
	def setTEMP(self, val):
		"""Set register TEMP"""
		self.write(REG.TEMP, val, 16)
	
	def getTEMP(self):
		"""Get register TEMP"""
		return self.read(REG.TEMP, 16)
	
	# Bits TD
	# Temperature data bits. 
	# Bits reserved_0
	# Register CONF
	# The configuration register is used to store the device settings such as device operation
	#       mode, OS operation mode, OS polarity, and OS fault queue.
	#       The configuration register allows the user to program various options such as thermostat
	#       fault tolerance, thermostat polarity, thermostat operating mode, and shutdown mode. The
	#       user has READ/WRITE access to all of the bits in the configuration register except the MSB
	#       (Bit7), which is reserved as a “Read only” bit (see Table 6). The entire register is volatile and
	#       thus powers-up in its default state only. 
	
	
	def setCONF(self, val):
		"""Set register CONF"""
		self.write(REG.CONF, val, 8)
	
	def getCONF(self):
		"""Get register CONF"""
		return self.read(REG.CONF, 8)
	
	# Bits reserved_0
	# must be set to '0'. Reserved 
	# Bits unused_1
	# must be set to '0'. 
	# Bits FT
	# fault tolerance1 bit 
	# Bits POL
	# output polarity. The OS is active-low ('0'). 
	# Bits M
	# Indicates operation mode; (see Comparator mode and Interrupt mode on page 13). 
	# Bits SD
	# Register T_OS
	# The TOS register is a two-byte (16-bit) READ/WRITE register that stores the userprogrammable
	#       upper trip-point temperature for the thermal alarm in two’s complement
	#       format (see Table 8 on page 19). This register defaults to 80 °C at power-up (i.e., 0101 0000
	#       0000 0000).
	#       The format of the TOS register is identical to that of the temperature register. The MSB
	#       position contains the sign bit for the digital temperature and Bit14 contains the temperature
	#       MSB.
	#       For 9-bit conversions, the trip-point temperature is defined by the 9 MSBs of the TOS
	#       register, and all remaining bits are “Don’t cares”. 
	
	
	def setT_OS(self, val):
		"""Set register T_OS"""
		self.write(REG.T_OS, val, 16)
	
	def getT_OS(self):
		"""Get register T_OS"""
		return self.read(REG.T_OS, 16)
	
	# Bits T_OS
	# Register T_HYS
	# THYS register is a two-byte (16-bit) READ/WRITE register that stores the userprogrammable
	#       lower trip-point temperature for the thermal alarm in two’s complement
	#       format (see Table 8). This register defaults to 75 °C at power-up (i.e., 0100 1011 0000
	#       0000).
	#       The format of this register is the same as that of the temperature register. The MSB position
	#       contains the sign bit for the digital temperature and bit14 contains the temperature MSB. 
	
	
	def setT_HYS(self, val):
		"""Set register T_HYS"""
		self.write(REG.T_HYS, val, 16)
	
	def getT_HYS(self):
		"""Get register T_HYS"""
		return self.read(REG.T_HYS, 16)
	
	# Bits SB
	# Two's complement sign bit. 
	# Bits SD
	# Temperature data. 
	# Bits reserved_0
