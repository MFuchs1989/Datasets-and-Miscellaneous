import os
import random
import shutil



def Train_Validation_Test_Split(df1, df2, df3):
        '''
        Creates a folder containing three subfolders for the training, validation and testing part.
        These folders are randomly filled with the provided image data according to the specified proportions. 

        Args: 
                df1 (string): Name of the folder containing the original image data of the first category
                df2 (string): Name of the folder containing the original image data of the second category
                df3 (string): Name of the folder containing the original image data of the third category

        Returns:
                list_cats_training (int): List of randomly selected images for the training part of the first category
                list_dogs_training (int): List of randomly selected images for the training part of the second category
                list_wilds_training (int): List of randomly selected images for the training part of the third category
                list_cats_validation (int): List of randomly selected images for the validation part of the first category
                list_dogs_validation (int): List of randomly selected images for the validation part of the second category
                list_wilds_validation (int): List of randomly selected images for the validation part of the third category
                list_cats_test (int): List of randomly selected images for the test part of the first category
                list_dogs_test (int): List of randomly selected images for the test part of the second category
                list_wilds_test (int): List of randomly selected images for the test part of the third category
        '''

        # Determine the proportions of train, validation and test part
        train_part_proportion = 0.6
        validation_part_proportion = 0.2
        test_part_proportion = 0.2
        

        print('Final number of cat pictures:', len(os.listdir(df1)))
        print('Final number of dog pictures:', len(os.listdir(df2)))
        print('Final number of wild pictures:', len(os.listdir(df3)))
        print()
        print('-----------------------------------------------------------------')
        print()

        final_length_cats = len(os.listdir(df1))
        list_cats_full = list(range(1, final_length_cats+1))

        final_length_dogs = len(os.listdir(df2))
        list_dogs_full = list(range(1, final_length_dogs+1))

        final_length_wilds = len(os.listdir(df3))
        list_wilds_full = list(range(1, final_length_wilds+1))

        print('Start to determine test, validation and train part')
        list_cats_test = random.sample(list_cats_full, round(len(list_cats_full)*test_part_proportion))
        list_remaining_cat_images = [item for item in list_cats_full if item not in list_cats_test]

        list_dogs_test = random.sample(list_dogs_full, round(len(list_dogs_full)*test_part_proportion))
        list_remaining_dog_images = [item for item in list_dogs_full if item not in list_dogs_test]

        list_wilds_test = random.sample(list_wilds_full, round(len(list_wilds_full)*test_part_proportion))
        list_remaining_wild_images = [item for item in list_wilds_full if item not in list_wilds_test]

        list_cats_validation = random.sample(list_remaining_cat_images, 
                                        round(len(list_cats_full)*validation_part_proportion))


        list_dogs_validation = random.sample(list_remaining_dog_images, 
                                        round(len(list_dogs_full)*validation_part_proportion))


        list_wilds_validation = random.sample(list_remaining_wild_images, 
                                        round(len(list_wilds_full)*validation_part_proportion))                   


        list_cats_training = [item for item in list_remaining_cat_images if item not in list_cats_validation]
        list_dogs_training = [item for item in list_remaining_dog_images if item not in list_dogs_validation]
        list_wilds_training = [item for item in list_remaining_wild_images if item not in list_wilds_validation]
        print('Stop to determine test, validation and train part')
        print()
        print('Start to set folder structure')
        # Get root directory
        root_directory = os.getcwd()

        # Define original datasets direction
        original_dataset_dir_cats = os.path.join(root_directory, 'cats')
        original_dataset_dir_dogs = os.path.join(root_directory, 'dogs')
        original_dataset_dir_wilds = os.path.join(root_directory, 'wilds')

        # Define base direction 
        # This is the place where the image splitting 
        # (train, validation, test) should take place. 
        base_dir = os.path.join(root_directory, 'animals')
        os.mkdir(base_dir)


        # Define general train, validation and test direction
        train_dir = os.path.join(base_dir, 'train')
        os.mkdir(train_dir)

        validation_dir = os.path.join(base_dir, 'validation')
        os.mkdir(validation_dir)

        test_dir = os.path.join(base_dir, 'test')
        os.mkdir(test_dir)

        # Define train direction for cats
        train_cats_dir = os.path.join(train_dir, 'cats')
        os.mkdir(train_cats_dir)

        # Define train direction for dogs
        train_dogs_dir = os.path.join(train_dir, 'dogs')
        os.mkdir(train_dogs_dir)

        # Define train direction for wilds
        train_wilds_dir = os.path.join(train_dir, 'wilds')
        os.mkdir(train_wilds_dir)

        # Define validation direction for cats
        validation_cats_dir = os.path.join(validation_dir, 'cats')
        os.mkdir(validation_cats_dir)

        # Define validation direction for dogs
        validation_dogs_dir = os.path.join(validation_dir, 'dogs')
        os.mkdir(validation_dogs_dir)

        # Define validation direction for wilds
        validation_wilds_dir = os.path.join(validation_dir, 'wilds')
        os.mkdir(validation_wilds_dir)

        # Define test direction for cats
        test_cats_dir = os.path.join(test_dir, 'cats')
        os.mkdir(test_cats_dir)

        # Define test direction for dogs
        test_dogs_dir = os.path.join(test_dir, 'dogs')
        os.mkdir(test_dogs_dir)

        # Define test direction for wilds
        test_wilds_dir = os.path.join(test_dir, 'wilds')
        os.mkdir(test_wilds_dir)

        print('Stop to set folder structure')
        print()

        print('Start copying the determined images to the appropriate folders')
        fnames = ['cat{}.jpg'.format(i) for i in list_cats_training]
        for fname in fnames:
                src = os.path.join(original_dataset_dir_cats, fname)
                dst = os.path.join(train_cats_dir, fname)
                shutil.copyfile(src, dst)
        
        fnames = ['dog{}.jpg'.format(i) for i in list_dogs_training]
        for fname in fnames:
                src = os.path.join(original_dataset_dir_dogs, fname)
                dst = os.path.join(train_dogs_dir, fname)
                shutil.copyfile(src, dst)

        fnames = ['wild{}.jpg'.format(i) for i in list_wilds_training]
        for fname in fnames:
                src = os.path.join(original_dataset_dir_wilds, fname)
                dst = os.path.join(train_wilds_dir, fname)
                shutil.copyfile(src, dst)

        fnames = ['cat{}.jpg'.format(i) for i in list_cats_validation]
        for fname in fnames:
                src = os.path.join(original_dataset_dir_cats, fname)
                dst = os.path.join(validation_cats_dir, fname)
                shutil.copyfile(src, dst)

        fnames = ['dog{}.jpg'.format(i) for i in list_dogs_validation]
        for fname in fnames:
                src = os.path.join(original_dataset_dir_dogs, fname)
                dst = os.path.join(validation_dogs_dir, fname)
                shutil.copyfile(src, dst)

        fnames = ['wild{}.jpg'.format(i) for i in list_wilds_validation]
        for fname in fnames:
                src = os.path.join(original_dataset_dir_wilds, fname)
                dst = os.path.join(validation_wilds_dir, fname)
                shutil.copyfile(src, dst)

        fnames = ['cat{}.jpg'.format(i) for i in list_cats_test]
        for fname in fnames:
                src = os.path.join(original_dataset_dir_cats, fname)
                dst = os.path.join(test_cats_dir, fname)
                shutil.copyfile(src, dst)
        
        fnames = ['dog{}.jpg'.format(i) for i in list_dogs_test]
        for fname in fnames:
                src = os.path.join(original_dataset_dir_dogs, fname)
                dst = os.path.join(test_dogs_dir, fname)
                shutil.copyfile(src, dst)


        fnames = ['wild{}.jpg'.format(i) for i in list_wilds_test]
        for fname in fnames:
                src = os.path.join(original_dataset_dir_wilds, fname)
                dst = os.path.join(test_wilds_dir, fname)
                shutil.copyfile(src, dst)  


        print('Stop copying the determined images to the appropriate folders')
        print()
        print('-----------------------------------------------------------------')
        print()
        print('          The final data breakdown is as follows:')
        print()
        print('Total training cat images:', len(os.listdir(train_cats_dir)))
        print('Total training dog images:', len(os.listdir(train_dogs_dir)))
        print('Total training wild images:', len(os.listdir(train_wilds_dir)))
        print()
        print('Total validation cat images:', len(os.listdir(validation_cats_dir)))
        print('Total validation dog images:', len(os.listdir(validation_dogs_dir)))
        print('Total validation wild images:', len(os.listdir(validation_wilds_dir)))
        print()
        print('Total test cat images:', len(os.listdir(test_cats_dir)))
        print('Total test dog images:', len(os.listdir(test_dogs_dir)))
        print('Total test wild images:', len(os.listdir(test_wilds_dir)))

        return  list_cats_training, list_dogs_training, list_wilds_training, \
                list_cats_validation, list_dogs_validation, list_wilds_validation, \
                list_cats_test, list_dogs_test, list_wilds_test
