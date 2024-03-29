'''
    train meter/garage data
'''
from utils import *
from dataset import *

root = '2022/garage_dataset'
# root = '2022/meter_dataset'

dataset = ParkDataset(root, len_x=50, in_memory=True)[:20000]
train_set = dataset[:16000]
test_set = dataset[16000:]

scalar = dataset_scalar(train_set)
train_set.set_scalar(*scalar)
test_set.set_scalar(*scalar)

batch_size = 64
name = 'lstm_lnr'
n_epochs = 100
lr = 0.001

model = None
# model_dict = torch.load('runs\\garage\\2022-04-17-17-21-lnr_no_act\\model.pth')

train(train_set, test_set, model_path=model, name=name, epochs=n_epochs, lr=lr, batch_size=batch_size, test_batch_size=batch_size)