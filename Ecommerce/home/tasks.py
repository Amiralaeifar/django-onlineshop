from bucket import bucket 



def get_objects_task():
    result = bucket.get_objects()
    return result


def get_obj_list_task():
    result = bucket.get_object_list()
    return result



