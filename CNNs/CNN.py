import itertools
import torch
from torch.nn import Module, Conv2d, Linear, MaxPool2d, ReLU, MSELoss
from torch import flatten
from torch.optim import Adam
from torch.utils.data import DataLoader, random_split, TensorDataset
import matplotlib.pyplot as plt
import time
import numpy as np

class Generate():
    def __init__():
        pass
    
    def Model(df, device, Train_split, param_grid):
        # Generate all combinations of hyperparameters
        param_combinations = list(itertools.product(param_grid['lr'], 
                                                    param_grid['batch_size'], 
                                                    param_grid['conv1_out_channels'], 
                                                    param_grid['conv2_out_channels'],
                                                    param_grid['epcoch']))

        best_val_loss = float('inf')
        TRAIN_SPLIT = Train_split
        VAL_SPLIT = 1 - TRAIN_SPLIT

        counter = 1
        for params in param_combinations:
            lr, batch_size, conv1_out_channels, conv2_out_channels, epcoch = params
            EPOCHS = epcoch
            print(f"Testing combination: lr={lr}, batch_size={batch_size}, conv1_out_channels={conv1_out_channels}, conv2_out_channels={conv2_out_channels}, epcoch={epcoch}")
            
            # Rebuild your model with the new hyperparameters
            class LeNetTabular(Module):
                def __init__(self, numChannels):
                    super(LeNetTabular, self).__init__()
                    self.conv1 = Conv2d(in_channels=numChannels, out_channels=conv1_out_channels, kernel_size=(1, 2))
                    self.relu1 = ReLU()
                    self.maxpool1 = MaxPool2d(kernel_size=(2, 2), stride=(1, 1))
                    self.conv2 = Conv2d(in_channels=conv1_out_channels, out_channels=conv2_out_channels, kernel_size=(1, 2))
                    self.relu2 = ReLU()
                    self.maxpool2 = MaxPool2d(kernel_size=(2, 2), stride=(1, 1))
                    #self.conv3 = Conv2d(in_channels=conv1_out_channels, out_channels=conv2_out_channels, kernel_size=(1, 2))
                    #self.relu3 = ReLU()
                    #self.maxpool3 = MaxPool2d(kernel_size=(2, 2), stride=(1, 1))
                    self.fc1 = Linear(in_features=conv2_out_channels * 1 * 11, out_features=50)
                    self.relu4 = ReLU()
                    self.fc2 = Linear(in_features=50, out_features=1)  # Predicting "Profit"

                def forward(self, x):
                    x = self.conv1(x)
                    x = self.relu1(x)
                    x = self.maxpool1(x)
                    x = self.conv2(x)
                    x = self.relu2(x)
                    #x = self.maxpool3(x)
                    #x = self.conv3(x)
                    #x = self.relu3(x)
                    x = self.maxpool2(x)
                    x = flatten(x, 1)
                    x = self.fc1(x)
                    x = self.relu4(x)
                    x = torch.tanh(self.fc2(x))
                    return x

            # Initialize the model, loss function, optimizer
            model = LeNetTabular(numChannels=1).to(device)
            opt = Adam(model.parameters(), lr=lr)
            lossFn = MSELoss()

            # Packet the data
            Packets = []
            packet_size = 20

            for i in range(packet_size, len(df)+1):
                snapshot = df.iloc[i-3:i].values
                Packets.append(snapshot)

            # Convert to tensor and reshape
            packets_tensor = torch.tensor(Packets).float()
            packets_tensor = packets_tensor.unsqueeze(1)

            target_tensor = torch.tensor(df['Profit'].values).float()
            target_tensor = target_tensor[:packets_tensor.shape[0]]

            # Create the TensorDataset and split into training/validation
            dataset = TensorDataset(packets_tensor, target_tensor)
            numTrainSamples = int(len(dataset) * TRAIN_SPLIT)
            numValSamples = len(dataset) - numTrainSamples
            trainData, valData = random_split(dataset, [numTrainSamples, numValSamples])

            # Re-create DataLoaders with the new batch size
            trainDataLoader = DataLoader(trainData, shuffle=True, batch_size=batch_size)
            valDataLoader = DataLoader(valData, batch_size=batch_size)

            # Training Loop (simplified)
            for e in range(EPOCHS):
                model.train()
                totalTrainLoss = 0
                totalValLoss = 0

                # Training loop
                for (x, y) in trainDataLoader:
                    (x, y) = (x.to(device), y.to(device))
                    pred = model(x)
                    loss = lossFn(pred.squeeze(), y)
                    opt.zero_grad()
                    loss.backward()
                    opt.step()
                    totalTrainLoss += loss.item()

                # Validation loop
                model.eval()
                with torch.no_grad():
                    for (x, y) in valDataLoader:
                        (x, y) = (x.to(device), y.to(device))
                        pred = model(x)
                        valLoss = lossFn(pred.squeeze(), y)
                        totalValLoss += valLoss.item()

                # Calculate the average losses for the epoch
                avgValLoss = totalValLoss / len(valDataLoader)
                
            # Check if current parameters result in a lower validation loss
            print("Avg Val Loss:", avgValLoss)
            if avgValLoss < best_val_loss:
                best_val_loss = avgValLoss
                best_params = params
                best_model = model
            counter += 1

        print(f"Best parameters: {best_params} with validation loss {best_val_loss:.4f}")
        return best_model