#!/usr/bin/env python
# coding: utf-8
#
 
import sys
import argparse
import math

def readfile(filename):
	dict = {};
	file = open(filename, 'r');
	for line in file:
		row = line.split('\t');
		id = int(row[0]);
		label = float(row[1]);
		if label > 5:
			print('Warning: %0.4f is out of range, the maximum value is 5. Skipping this input. ' % label);
			# label = 5;
			continue;
		if label < -5:
			print('Warning: %0.4f is out of range, the minimum value is -5. Skipping this input.' % label);
			# label = -5
			continue;
		if label != math.floor(label + 0.5):
			print('Warning: %0.4f is not an integer, will be converted to %d.' % (label, math.floor(label + 0.5)))
			label = math.floor(label + 0.5);
		if id in dict:
			print('duplicate tweet id: ' + str(id))
		else:
			dict[id] = label;
	file.close();
	return dict;

def cosine(dict1, dict2):
	keys1 = set(dict1.keys());
	keys2 = set(dict2.keys());
	keys_union = keys1 | keys2;
	keys_intersection = keys1 & keys2;
	# print('union len: ' + str(len(keys_union)) + '; intersection len: ' + str(len(keys_intersection)));
	print('Number of Gold entries:: %d\r\nNumber of Submitted entries:: %d' % (len(keys1), len(keys_intersection)));
	ratio = float(len(keys_intersection)) / len(keys1);
	sum_prod = 0;
	mod1 = 0;
	mod2 = 0;
	for id in keys_intersection:
		sum_prod += dict1[id] * dict2[id];
		mod1 += dict1[id] * dict1[id];
		mod2 += dict2[id] * dict2[id];
	mod1 = math.sqrt(mod1);
	mod2 = math.sqrt(mod2);
	cos = sum_prod / (mod1 * mod2);
	return (ratio, cos);


def main(file1, file2):
	dict1 = readfile(file1);
	dict2 = readfile(file2);
	(ratio, cos) = cosine(dict1, dict2);
	print('Cosine Similarity Score:: %0.4f\r\nPenalty:: %0.4f\r\nFinal Score:: %0.4f' % (cos, (1-ratio), cos*ratio));

if __name__ == '__main__':
	if (len(sys.argv) != 3):
		print('python cosine_eval.py <file1> <file2>');
	else:
		main(sys.argv[1], sys.argv[2]);