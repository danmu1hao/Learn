import torch
import torch.nn as nn

# 模型结构必须一致！
model = nn.Sequential(
    nn.Linear(1, 1),
    nn.Sigmoid()
)
model.load_state_dict(torch.load('simple_model.pth'))
model.eval()  # 设置为“推理模式”
with torch.no_grad():
    x_test = torch.tensor([[1.0]])  # 可以改成 1.0, 0.3, 0.8 等
    y_pred = model(x_test)
    print(f"输入 {x_test.item()} → 输出 {y_pred.item():.4f}")
