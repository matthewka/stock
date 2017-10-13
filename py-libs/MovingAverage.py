#!/usr/bin/python
# -*- coding: utf-8 -*-

class MovingAverage:
	
	
	def __init__(self, dataArray, moving):
		self.dataLen = len(dataArray)
		self.moving = moving
		if self.dataLen <= 0:
			raise Exception("Data length is less than 0")

		self.dataArray = dataArray

	def calculate(self, moving):
		index = 0
		ma = []
		while index + moving <= self.dataLen:
			start = index
			end = index + moving - 1
			datas = []
			
			for i in range(start, end, +1):
				datas.append(self.dataArray[i])
			
			ma.append(self.average(datas))
			index = index + 1

		return ma

	def average(self, datas):
		sum = 0
		lens= len(datas)
		for data in datas:
			sum = sum + data

		return (sum / lens)

	def get(self):
		self.ma = self.calculate(self.moving)
		return self.ma

	def getLen(self):
		return self.dataLen