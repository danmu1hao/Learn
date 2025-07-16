import torch
import torch.nn as nn
import torch.optim as optim

# 1. 模型：只要一个线性函数 y = wx + b
model = nn.Sequential(
    nn.Linear(1, 1),     # 输入1维，输出1维
    nn.Sigmoid()         # 把输出限制在 0 ~ 1 之间
)

# 2. 损失函数：均方误差
criterion = nn.MSELoss()
# 3. 优化器：随机梯度下降
optimizer = optim.SGD(model.parameters(), lr=0.1)

# 4. 训练数据
x_train = torch.tensor([[0.0], [1.0]])
y_train = torch.tensor([[0.0], [1.0]])

# 5. 训练循环
for epoch in range(100):
    output = model(x_train)
    loss = criterion(output, y_train)
    loss.backward()
    optimizer.step()
    optimizer.zero_grad()
    if epoch % 10 == 0:
        print(f"Epoch {epoch}: Loss={loss.item():.4f}")

# 6. 保存模型（保存权重参数）
torch.save(model.state_dict(), 'simple_model.pth')
print("✅ 模型已保存为 simple_model.pth")
