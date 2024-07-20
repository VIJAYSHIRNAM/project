import torch
import torch.nn as nn
import torchvision.models as models
import torchvision.transforms as transforms
import torch.optim as optim
from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader


class ResNetModel(nn.Module):
    def __init__(self, num_classes):
        super(ResNetModel, self).__init__()
        self.resnet = models.resnet18(pretrained=True)  # You can choose different ResNet versions
        num_ftrs = self.resnet.fc.in_features
        self.resnet.fc = nn.Linear(num_ftrs, num_classes)

    def forward(self, x):
        return self.resnet(x)


class ReNetNNRunner:

    def __init__(self):
        self.model = ResNetModel()
        self.data_transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])  # ImageNet normalization
        ])
        self.criterion = nn.CrossEntropyLoss()
        self.optimizer = optim.Adam(self.model.parameters(), lr=0.001)
        self.num_epochs = 10
        self.train_dataset = self.train_loader = None

    def transform_data(self):
        self.train_dataset = ImageFolder('path_to_dataset/train', transform=self.data_transform)
        self.train_loader = DataLoader(self.train_dataset, batch_size=32, shuffle=True)

    def train_model(self):
        self.model.train()
        for epoch in range(self.num_epochs):
            running_loss = 0.0
            for inputs, labels in self.train_loader:
                self.optimizer.zero_grad()
                outputs = self.model(inputs)
                loss = self.criterion(outputs, labels)
                loss.backward()
                self.optimizer.step()
                running_loss += loss.item() * inputs.size(0)
            epoch_loss = running_loss / len(self.train_loader.dataset)
            print(f'Epoch [{epoch + 1}/{self.num_epochs}], Loss: {epoch_loss:.4f}')

    def save_model(self):
        # Save model
        torch.save(self.model.state_dict(), 'resnet_model.pth')

    def load_model(self):
        self.model.load_state_dict(torch.load('resnet_model.pth'))
        self.model.eval()

    def predict_image(self, image):
        self.model.eval()
        image_tensor = self.data_transform(image).unsqueeze(0)
        with torch.no_grad():
            outputs = self.model(image_tensor)
        _, predicted = torch.max(outputs, 1)
        return self.train_dataset.classes[predicted.item()]