import torch
import torch.nn as nn
import torch.nn.functional as F


class MNISTModel(nn.Module):

    def __init__(self):
        super(MNISTModel, self).__init__()

        self.conv1 = nn.Conv2d(1, 32, 2, stride=2, bias=True)
        self.conv2 = nn.Conv2d(32, 16, 8, stride=1,  bias=True)

        self.fc1 = nn.Linear(16*7*7, 64, True)
        self.fc2 = nn.Linear(64, 10, True)

    def forward(self, x):
        x = x.view((-1, 1, 28, 28))
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x)).view((-1, 16*7*7))
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return F.log_softmax(x, dim=1)
