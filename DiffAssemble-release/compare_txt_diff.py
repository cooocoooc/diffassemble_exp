import time
import re
import os
'''
compare the differences from different files
'''
# load data as set
def load_filenames(file_path):
    with open(file_path, 'r') as file:
        return set(line.strip() for line in file if line.strip().endswith('.jpg'))

# load data name from file
def load_filenames_from_folder(path):
    filenames = os.listdir(path)
    return set(filename for filename in filenames if filename.strip().endswith('.jpg'))

# compare the differences
def find_common_filenames(train_file, test_file):
    train_filenames = load_filenames(train_file)
    test_filenames = load_filenames(test_file)
    common = train_filenames.intersection(test_filenames)
    return common

# find common element of the set from other sets
def find_common_filenames_from_others(source_file,train_file,test_file):

    source_filenames = load_filenames_from_folder(source_file)
    
    train_filenames = load_filenames(train_file)
    test_filenames = load_filenames(test_file)
    
    comm_source_train = source_filenames.intersection(train_filenames)
    comm_source_test = source_filenames.intersection(test_filenames)
    
    return comm_source_train, comm_source_test
'''
find the start and end index from different files
'''
# load the file as list
def load_filenames_list(file_path):
    # Read the content of the file
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Use regex to find filenames like 123.jpg
    filenames = re.findall(r'\b\d+\.jpg\b', content)
    
    return filenames

# convert the names to the numbers
def load_list(train_file, test_file):
    # load list
    train_filenames = load_filenames_list(train_file)
    test_filenames = load_filenames_list(test_file) 
    
    # Extract numeric values from filenames
    train_numbers = [int(name[:-4]) for name in train_filenames if name.endswith(".jpg") and name[:-4].isdigit()]
    test_numbers = [int(name[:-4]) for name in test_filenames if name.endswith(".jpg") and name[:-4].isdigit()]
    
    return train_numbers, test_numbers

# find out the start and end index from isolated lists
def find_max_min_from_lists(train_list, test_list):

    # Start timing
    start_time = time.time()

    # Find min and max from each list and compare
    min1 = min(train_list)
    min2 = min(test_list)
    overall_min = min(min1, min2)

    max1 = max(train_list)
    max2 = max(test_list)
    overall_max = max(max1, max2)

    # End timing
    end_time = time.time()
    execution_time = end_time - start_time

    # Print results
    print("Execution time:", execution_time, "seconds")
    return overall_min, overall_max

# find out the start and end index with union list
def find_max_min_from_a_list(train_list, test_list):

    # Start timing
    start_time = time.time()

    # union the list
    # create a new list
    union_list = train_list + test_list
    
    # modify the original list
    # train_list.extend(test_list)
    
    # Find min and max
    overall_min = min(union_list)
    overall_max = max(union_list)

    # End timing
    end_time = time.time()
    execution_time = end_time - start_time

    # Print results
    print("Execution time:", execution_time, "seconds")
    return overall_min, overall_max
    
def rename_multiple_files(path):
    filenames = os.listdir(path)
    for filename in filenames:
        if filename.endswith('.jpg') and filename[:-4].isdigit():
            new_name = f"{int(filename[:-4])}.jpg"
            old_path = os.path.join(path, filename)
            new_path = os.path.join(path, new_name)
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_name}")

if __name__ == "__main__":
    train_path = "datasets/data_splits/CelebA-HQ_train.txt"
    test_path = "datasets/data_splits/CelebA-HQ_test.txt"
    
    imgs_path = "datasets/CelebAMask-HQ/CelebA-HQ-img"
    
    common_filenames = find_common_filenames(train_path, test_path)
    
    common_source_train, common_source_test = find_common_filenames_from_others(imgs_path, train_path, test_path)

    print(f"Number of common JPG files: {len(common_filenames)}")
    print("Sample of common filenames:")
    for filename in list(common_filenames)[:20]:  # Show first 20 matches
        print(filename)
    
    print(f"Number of common train JPG files: {len(common_source_train)}")
    print("Sample of common filenames:")
    for filename in list(common_source_train)[:20]:  # Show first 20 matches
        print(filename)
    
    print(f"Number of common test JPG files: {len(common_source_test)}")
    print("Sample of common filenames:")
    for filename in list(common_source_test)[:20]:  # Show first 20 matches
        print(filename)
        
    train_list, test_list = load_list(train_path, test_path)
    start_index, end_index = find_max_min_from_lists(train_list, test_list)
    print("start_id:", start_index)
    print("end_id:", end_index)
    
    start_index, end_index = find_max_min_from_a_list(train_list, test_list)
    print("start_id:", start_index)
    print("end_id:", end_index)
    
    rename_multiple_files(imgs_path)