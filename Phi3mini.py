import torch
import os
import io
from io import BytesIO
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from textwrap import dedent

prepended_user_instruction_text = dedent("""
    You are creating a prompt for Stable Diffusion to generate a visually pleasing image.
    First step: understand the input and generate a text prompt for the input.
    Second step: respond in English with the prompt itself in clear and detailed phrases to vividly depict the scene and its composition, without using quotation marks. Ensure the prompt is under 200 tokens.
    """).strip()

class Phi3mini_4k_ModelLoader_Zho:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {

            }
        }

    RETURN_TYPES = ("PHI3", "TK")
    RETURN_NAMES = ("Phi3mini_4k", "tokenizer")
    FUNCTION = "load_model"
    CATEGORY = "🏖️Phi3mini"
  
    def load_model(self,):
        model = AutoModelForCausalLM.from_pretrained(
            "microsoft/Phi-3-mini-4k-instruct", 
            device_map="cuda", 
            torch_dtype="auto", 
            trust_remote_code=True, 
        )
        tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-3-mini-4k-instruct")
        return model, tokenizer


class Phi3mini_4k_Zho:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "model": ("PHI3",),
                "tokenizer": ("TK",),
                "prompt": ("STRING", {"default": "What is the meaning of life?", "multiline": True}),
                "prepended_user_instruction": ("STRING", {"default": prepended_user_instruction_text, "multiline": True}),
                "system_instruction": (["Disabled", "Enabled"],),
                "temperature": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 1.0, "step": 0.01}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "generate_content"

    CATEGORY = "🏖️Phi3mini"


    def generate_content(self, model, tokenizer, prompt, prepended_user_instruction, system_instruction, temperature):
        if system_instruction == "Enabled":
            system_instruction_txt = prepended_user_instruction
        else:
            prompt = prepended_user_instruction + prompt
            system_instruction_txt = ""
        
        messages = [
            {"role": "system", "content": system_instruction_txt},
            {"role": "user", "content": prompt},
        ]

        pipe = pipeline(
            "text-generation",
            model=model,
            tokenizer=tokenizer,
        )

        generation_args = {
            "max_new_tokens": 500,
            "return_full_text": False,
            "temperature": temperature,
            "do_sample": False,
        }

        output = pipe(messages, **generation_args)
        textoutput = output[0]['generated_text']

        return (textoutput,)


class Phi3mini_4k_Chat_Zho:
    def __init__(self):
        self.chat_history = []

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "model": ("PHI3",),
                "tokenizer": ("TK",),
                "prompt": ("STRING", {"default": "What is the meaning of life?", "multiline": True}),
                "prepended_user_instruction": ("STRING", {"default": prepended_user_instruction_text, "multiline": True}),
                "system_instruction": (["Disabled", "Enabled"],),
                "temperature": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 1.0, "step": 0.01}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "generate_content"

    CATEGORY = "🏖️Phi3mini"

    def phi_3(self, user_question, system_role):
        messages = [{"role": "system", "content": system_role},
                    {"role": "user", "content": user_question}]

        pipe = pipeline(
            "text-generation",
            model=self.model,  # Use self.model instead of model
            tokenizer=self.tokenizer,  # Use self.tokenizer instead of tokenizer
        )

        generation_args = {
            "max_new_tokens": 500,
            "return_full_text": False,
            "temperature": self.temperature,
            "do_sample": False,
        }

        output = pipe(messages, **generation_args)
        text_output = output[0]['generated_text']

        return text_output

    def generate_content(self, model, tokenizer, prompt, prepended_user_instruction, system_instruction, temperature):
        # Store model, tokenizer, and temperature as instance variables
        self.model = model
        self.tokenizer = tokenizer
        self.temperature = temperature

        if system_instruction == "Enabled":
            system_instruction_txt = prepended_user_instruction
            response = self.phi_3(prompt, system_instruction_txt)
        else:
            prompt = prepended_user_instruction + prompt
            system_instruction_txt = ""
            response = self.phi_3(prompt, system_instruction_txt)

        # Update chat history
        self.chat_history.append({"role": "user", "content": prompt})
        self.chat_history.append({"role": "system", "content": response})
        
        # Format and return chat history
        formatted_history = self.format_chat_history()
        return (formatted_history,)

    def format_chat_history(self):
        formatted_history = []
        for message in self.chat_history:
            formatted_message = f"{message['role']}: {message['content']}"
            formatted_history.append(formatted_message)
            formatted_history.append("-" * 40)  # Add a separator line
        return "\n".join(formatted_history)

        

NODE_CLASS_MAPPINGS = {
    "Phi3mini_4k_ModelLoader_Zho": Phi3mini_4k_ModelLoader_Zho,
    "Phi3mini_4k_Zho": Phi3mini_4k_Zho,
    "Phi3mini_4k_Chat_Zho": Phi3mini_4k_Chat_Zho,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Phi3mini_4k_ModelLoader_Zho": "🏖️Phi3mini 4k ModelLoader",
    "Phi3mini_4k_Zho": "🏖️Phi3mini 4k",
    "Phi3mini_4k_Chat_Zho": "🏖️Phi3mini 4k Chat",
}