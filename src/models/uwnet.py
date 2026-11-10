import torch.nn as nn


class SonarFusionBlock(nn.Module):
    def __init__(self, channels):
        super().__init__()
        self.conv = nn.Conv2d(channels * 2, channels, 3, padding=1)
        self.gate = nn.Sequential(nn.Conv2d(channels * 2, channels, 1), nn.Sigmoid())

    def forward(self, image_feat, sonar_feat):
        fused = torch_cat(image_feat, sonar_feat)
        gate = self.gate(fused)
        return self.conv(fused) * gate


def torch_cat(a, b):
    import torch
    return torch.cat([a, b], dim=1)
