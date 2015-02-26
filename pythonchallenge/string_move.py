def find_index(char, list):
	if len(char) > 0:
		return list.index(char)
	else:
		return -1


def move_string_by_increment(input_string, list, increment):
    input_list = list(input_string)
    output_string = ''
	if len(input_list) > 0:
		for i in input_list:
			current_char = input_list[i]
			old_index = find_index(current_char, list)
			if old_index != -1:
				new_index = old_index + increment
				if new_index >= len(list):
					new_index -= len(list)
				new_char = list[new_index]
				output_string.join(new_char)
			else:
				output_string.join(current_char)
        return output_string

input_string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

increment = 1

print move_string_by_increment(input_string, list, increment)
