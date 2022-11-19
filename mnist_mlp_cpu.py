def load_mnist(self,file_dir,is_images = 'True'):
    bin_file = open(file_dir,'rb')
    bin_data = bin_file.read()
    bin_file.close()
    if is_images:           #get the image data 
        fmt_header = '>iiii'
        magic,num_images,num_rows,num_cols = struct.unpack_from(fmt_header,bin_data,0)
    else:                   #get the label data
        fmt_header = '>ii'  
        magic,num_images = struct.unpack_from(fmt_header,bin_data,0)
        num_rows,num_cols = 1,1

    data_size = num_images * num_rows * num_cols 
    mat_data = struct.unpack_from('>' + str(data_size) + 'B',bin_file,struct.calcsize(fmt_header))
    mat_data = np.reshape(mat_data,[num_images,num_rows * num_cols])

    return mat_data

def load_data(self):
    train_images = self.load_mnist(os.path.join(MNIST_DIR,TRAIN_DATA),True)
    train_labels = self.load_mnist(os.path.join())
    test_images = 
    test_labels = 
    self.train_data = np.append(train_images,train_labels,axis=1)
    self.test_data = np.append(test_images,test_labels ,axis = 1)
