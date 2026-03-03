# CLAUDE.md

本文档为 Claude Code (claude.ai/code) 在本项目中工作时提供指导。

## 项目概述

这是一个 Python 项目，用于集成搜客宝 API 平台，查询电商企业信息。API 文档存储在 `docs/` 目录中（已加入 gitignore）。

## 运行项目

```bash
# 使用虚拟环境运行
.venv\Scripts\python.exe auth.py

# 或激活虚拟环境后运行
python auth.py
```

## 依赖项

- `requests` - HTTP 客户端，用于 API 调用
- `python-dotenv` - 从 `.env` 文件加载环境变量

安装方式：
```bash
pip install requests python-dotenv
```

## 配置

API 凭证存储在 `.env` 文件中：
- `API_KEY` - API 访问密钥
- `API_SECRET` - 用于 HMAC-SHA1 签名的 API 密钥

## 代码结构

- `auth.py` - 主脚本，执行 API 鉴权并发起测试请求（按名称搜索企业）
- `.env` - 环境变量，包含 API 凭证（已加入 gitignore）
- `docs/` - API 文档（已加入 gitignore）

## 鉴权方式

API 使用 HMAC-SHA1 签名鉴权：
1. 获取当前时间戳（毫秒）
2. 使用 API_SECRET 作为密钥，时间戳作为消息，计算 HMAC-SHA1 签名
3. 对签名进行 Base64 编码
4. 在请求头中发送：`X-AK-KEY`、`X-AK-PIN`、`X-AK-TS`

## API 端点

参考 `README.MD` 中的文档链接：
- API 请求鉴权接口：https://apidoc.weiwenjia.com/docs/skb-open-dev/index-12026657.md
- 电商企业信息接口：https://apidoc.weiwenjia.com/docs/skb-open-dev/skb-open-dev-1h5te0thahi3g
- 历史电商企业信息接口：https://apidoc.weiwenjia.com/docs/skb-open-dev/skb-open-dev-1h5vo85efa673
