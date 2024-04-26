
![P3 Comfyui](https://github.com/ZHO-ZHO-ZHO/ComfyUI-Phi-3-mini/assets/140084057/08f9bffa-f925-4457-955d-98cb1181acd5)


<h1 align="center">Phi-3-mini in ComfyUI</h1>

![Dingtalk_20240426213526](https://github.com/ZHO-ZHO-ZHO/ComfyUI-Phi-3-mini/assets/140084057/bece1e48-4082-4900-a1f4-e0c2b6ec5934)


## 项目介绍 | Info

- 将微软 [Phi-3-mini-4k-instruct](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct) 模型引入到 ComfyUI 中，模型很小，速度很快，性能很强（媲美 GPT-3.5 和 Mixtral 8x7B）

- Phi-3-mini-4k-instruct 开源可商用（ MIT 许可），中文表现很不错，可用于 生成/补全提示词 或畅聊人生！

- 版本：V1.0 支持系统提示词，支持单/多轮对话双模式，支持中文输入自动并输出英文提示词



## 详细说明 | Features

- 节点:

   - 🏖️Phi3mini 4k ModelLoader：会自动下载模型（请保持网络畅通）
     
   - 🏖️Phi3mini 4k：支持系统指令设置（System Instruction）     

   - 🏖️Phi3mini 4k Chat：支持系统指令设置（System Instruction）+ 多轮对话
  

- 节点示例：

![Dingtalk_20240426225104](https://github.com/ZHO-ZHO-ZHO/ComfyUI-Phi-3-mini/assets/140084057/97ae75ed-65e3-405d-bace-2fd9a8663e28)


- 上下文多轮对话：

![Dingtalk_20240426224040](https://github.com/ZHO-ZHO-ZHO/ComfyUI-Phi-3-mini/assets/140084057/fc79b86f-9c1b-4263-bcb7-7d98ef63eee5)



## 参数说明 | Parameters

- model：接入模型
- tokenizer：分词器
- prompt：提示词
- system_instruction：系统指令
- temperature：随机性


## 安装 | Install

- 环境依赖要求：transformers>=4.40.0，手动升级：`pip uninstall -y transformers && pip install git+https://github.com/huggingface/transformers`

- 推荐使用管理器 ComfyUI Manager 安装（ON THE WAY）

- 手动安装：
    1. `cd custom_nodes`
    2. `https://github.com/ZHO-ZHO-ZHO/ComfyUI-Phi-3-mini.git`
    3. `cd custom_nodes/ComfyUI-Phi-3-mini`
    4. `pip install -r requirements.txt`
    5. 重启 ComfyUI

- 输出节点可配合像[ComfyUI-Gemini](https://github.com/ZHO-ZHO-ZHO/ComfyUI-Gemini)中 ✨DisplayText_Zho 一样的任何接受文本的节点


## 工作流 | Workflow

### V1.0 工作流

  [Phi-3-mini-4k + CosXL【Zho】](https://github.com/ZHO-ZHO-ZHO/ComfyUI-Phi-3-mini/blob/main/Phi-3-min%20Workflows/Phi-3-mini-4k%20%2B%20CosXL%E3%80%90Zho%E3%80%91.json)

  ![Dingtalk_20240426223015](https://github.com/ZHO-ZHO-ZHO/ComfyUI-Phi-3-mini/assets/140084057/ed87e255-2716-4de3-8659-654ef69dbbf1)

  [Phi-3-mini-4k Chat【Zho】](https://github.com/ZHO-ZHO-ZHO/ComfyUI-Phi-3-mini/blob/main/Phi-3-min%20Workflows/Phi-3-mini-4k%20Chat%E3%80%90Zho%E3%80%91.json)

  ![Dingtalk_20240426211605](https://github.com/ZHO-ZHO-ZHO/ComfyUI-Phi-3-mini/assets/140084057/e98252f6-39e3-4b6b-832b-c170dc2f7923)




## 更新日志 | Changelog

20240426

- V1.0： 支持系统提示词，支持单/多轮对话双模式，支持中文输入自动并输出英文提示词

- 创建项目


## Stars 

[![Star History Chart](https://api.star-history.com/svg?repos=ZHO-ZHO-ZHO/ComfyUI-Phi-3-mini&type=Timeline)](https://star-history.com/#ZHO-ZHO-ZHO/ComfyUI-Phi-3-mini&Timeline)


## 关于我 | About me

📬 **联系我**：
- 邮箱：zhozho3965@gmail.com
- QQ 群：839821928

🔗 **社交媒体**：
- 个人页：[-Zho-](https://jike.city/zho)
- Bilibili：[我的B站主页](https://space.bilibili.com/484366804)
- X（Twitter）：[我的Twitter](https://twitter.com/ZHOZHO672070)
- 小红书：[我的小红书主页](https://www.xiaohongshu.com/user/profile/63f11530000000001001e0c8?xhsshare=CopyLink&appuid=63f11530000000001001e0c8&apptime=1690528872)

💡 **支持我**：
- B站：[B站充电](https://space.bilibili.com/484366804)
- 爱发电：[为我充电](https://afdian.net/a/ZHOZHO)


## Credits

[Phi-3-mini-4k-instruct](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct)
