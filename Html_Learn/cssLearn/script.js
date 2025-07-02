// 平滑滚动到锚点
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// 按钮点击效果
document.querySelectorAll('.demo-button').forEach(button => {
    button.addEventListener('click', function() {
        this.style.transform = 'scale(0.95)';
        setTimeout(() => {
            this.style.transform = 'scale(1.05)';
        }, 150);
        
        // 显示提示信息
        showNotification('ボタンがクリックされました！', 'success');
    });
});

// 动画元素点击效果
document.querySelectorAll('.animated-element').forEach(element => {
    element.addEventListener('click', function() {
        this.style.animation = 'none';
        setTimeout(() => {
            this.style.animation = 'pulse 2s infinite';
        }, 10);
        
        showNotification('アニメーション効果が発動しました！', 'info');
    });
});

// 显示通知函数
function showNotification(message, type = 'info') {
    // 创建通知元素
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    
    // 添加样式
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 15px 25px;
        border-radius: 10px;
        color: white;
        font-weight: bold;
        z-index: 1000;
        transform: translateX(100%);
        transition: transform 0.3s ease;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    `;
    
    // 根据类型设置背景色
    switch(type) {
        case 'success':
            notification.style.background = 'linear-gradient(45deg, #4CAF50, #45a049)';
            break;
        case 'error':
            notification.style.background = 'linear-gradient(45deg, #f44336, #da190b)';
            break;
        case 'warning':
            notification.style.background = 'linear-gradient(45deg, #ff9800, #e68900)';
            break;
        default:
            notification.style.background = 'linear-gradient(45deg, #2196F3, #0b7dda)';
    }
    
    // 添加到页面
    document.body.appendChild(notification);
    
    // 显示动画
    setTimeout(() => {
        notification.style.transform = 'translateX(0)';
    }, 100);
    
    // 自动隐藏
    setTimeout(() => {
        notification.style.transform = 'translateX(100%)';
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 300);
    }, 3000);
}

// 页面加载完成后的初始化
document.addEventListener('DOMContentLoaded', function() {
    console.log('CSS学習プラットフォームが読み込まれました！');
    
    // 添加页面加载动画
    document.body.style.opacity = '0';
    document.body.style.transition = 'opacity 0.5s ease';
    
    setTimeout(() => {
        document.body.style.opacity = '1';
    }, 100);
    
    // 为每个部分添加进入动画
    const sections = document.querySelectorAll('.section');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    });
    
    sections.forEach(section => {
        section.style.opacity = '0';
        section.style.transform = 'translateY(30px)';
        section.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(section);
    });
});

// 添加键盘快捷键
document.addEventListener('keydown', function(e) {
    // Ctrl + 1-4 快速跳转到不同部分
    if (e.ctrlKey) {
        switch(e.key) {
            case '1':
                e.preventDefault();
                document.querySelector('#basics').scrollIntoView({behavior: 'smooth'});
                break;
            case '2':
                e.preventDefault();
                document.querySelector('#layout').scrollIntoView({behavior: 'smooth'});
                break;
            case '3':
                e.preventDefault();
                document.querySelector('#animations').scrollIntoView({behavior: 'smooth'});
                break;
            case '4':
                e.preventDefault();
                document.querySelector('#responsive').scrollIntoView({behavior: 'smooth'});
                break;
        }
    }
    
    // ESC键显示帮助信息
    if (e.key === 'Escape') {
        showNotification('ショートカット: Ctrl+1-4 セクション移動, ESC ヘルプ表示', 'info');
    }
}); 