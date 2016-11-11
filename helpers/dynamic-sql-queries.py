# helper for constructing range query strings from a range of column values
def range_query(start, end, value_list, column_name):
	start_index = value_list.index(start)
	end_index = value_list.index(end)
	selected_values = value_list[start_index:end_index + 1]
	query_string = ""
	for value in selected_values:
		query_string = (query_string + column_name + " = '" + value + "' OR ")
	query_string = query_string[:-4]
	return query_string
