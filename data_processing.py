def list_of_tuples_to_json(list_of_tuples):
    list_containing_list_of_zipped_tuples = []
    map_object_to_make_list = map(lambda x:dict(zip(('id','front','back'),x)),list_of_tuples)
    return list(map_object_to_make_list)